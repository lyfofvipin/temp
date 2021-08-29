# Setup postgresql
yum install postgresql postgresql-server postgresql-contrib
postgresql-setup initdb
systemctl start postgresql
systemctl enable postgresql
# Open SQL interpriter and setup the DB tables
sudo su - postgres -c "psql"
CREATE DATABASE reportportal;
CREATE USER rpdbuser WITH ENCRYPTED PASSWORD 'rpdbuser123*';
GRANT ALL PRIVILEGES ON DATABASE reportportal TO rpdbuser;
ALTER USER rpdbuser WITH SUPERUSER;
# Edit the file for auth...
vi /var/lib/pgsql/data/pg_hba.conf
replace 
# "local" is for Unix domain socket connections only
local   all             all                                     md5
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
systemctl restart postgresql
psql -U rpdbuser -d reportportal -c "CREATE EXTENSION pgcrypto;"
# Done for the phase 1 


# Phase2 started
yum install -y https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.9.4/rabbitmq-server-3.9.4-1.el8.noarch.rpm https://github.com/rabbitmq/erlang-rpm/releases/download/v24.0.5/erlang-24.0.5-1.el8.x86_64.rpm
rabbitmq-plugins enable rabbitmq_management
chown -R rabbitmq:rabbitmq /var/lib/rabbitmq/
rm -rf /var/log/rabbitmq/*
systemctl start rabbitmq-server
systemctl enable rabbitmq-server
rabbitmqctl add_user admin rpdbuser123*
rabbitmqctl set_user_tags admin administrator
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"
rabbitmqctl add_user rpdbuser rpdbuser123*
rabbitmqctl set_user_tags rpdbuser administrator
rabbitmqctl set_permissions -p / rpdbuser ".*" ".*" ".*"
rabbitmqctl add_vhost analyzer
rabbitmqctl set_permissions -p analyzer rpdbuser ".*" ".*" ".*"
systemctl stop firewalld.service
systemctl disable firewalld.service
# To verify the same do `curl localhost:15672`
# Done for the phase 2 

# Phase 3 started
rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
echo '''
[elasticsearch]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
''' > /etc/yum.repos.d/elasticsearch.repo

dnf -y install elasticsearch java wget chkconfig
systemctl start elasticsearch
systemctl enable elasticsearch
curl -X GET "localhost:9200/"
# Done for the phase 3


# Phase 4 started
mkdir /opt/traefik && chown $USER:$USER /opt/traefik && cd /opt/traefik
wget -c -N -O traefik https://github.com/traefik/traefik/releases/download/v1.7.29/traefik_linux-amd64 && chmod +x traefik
curl -LO https://raw.githubusercontent.com/reportportal/linux-installation/master/data/traefik.toml
./traefik --configFile=traefik.toml 2>&1 &
# Done for the phase 4


# Phase 5 started
yum install python3 python3-devel gcc unzip -y

MAVEN_REPO="https://repo1.maven.org/maven2/com/epam/reportportal"
API_VERSION="5.3.5"
UAT_VERSION="5.3.5"
MIGRATIONS_VERSION="5.3.5"
UI_VERSION="5.3.5"
SERVICE_INDEX_VERSION="5.0.10"
SERVICE_ANALYZER="5.3.5"
SERVICE_API_JAVA_OPTS="-Xms1024m -Xmx2048m"
SERVICE_UAT_JAVA_OPTS="-Xms512m -Xmx512m"
RP_POSTGRES_USER=rpdbuser
RP_POSTGRES_PASSWORD='rpdbuser123*'
RP_RABBITMQ_USER=rpdbuser
RP_RABBITMQ_PASSWORD='rpdbuser123*'

mkdir /opt/reportportal/ && \
chown -R $USER:$USER /opt/reportportal/ && \
cd /opt/reportportal/

curl -LO https://github.com/reportportal/service-auto-analyzer/archive/refs/tags/${SERVICE_ANALYZER}.zip && \
unzip ${SERVICE_ANALYZER}.zip && \
cd /opt/reportportal/service-auto-analyzer-${SERVICE_ANALYZER}

# Create a virtual environment with any name (for example /vrpanalyzer)
python3.7 -m venv /vrpanalyzer
source /vrpanalyzer/bin/activate
pip install -r requirements.txt
# Install stopwords package from the nltk library
/vrpanalyzer/bin/python3 -m nltk.downloader -d /usr/share/nltk_data stopwords
# Changes for ini file
vi app.ini
virtualenv = vrpanalyzer
# Changes for Python file
vi app.py
"amqpUrl":           os.getenv("AMQP_URL", "amqp://rpdbuser:rpdbuser123*@localhost:5672").strip("/").strip("\\"),
"binaryStoreType":   os.getenv("ANALYZER_BINARYSTORE_TYPE", "filesystem"),
"filesystemDefaultPath": os.getenv("FILESYSTEM_DEFAULT_PATH", "rpstorage").strip()
# Done for the phase 5


# Phase 6 started
dnf install java-latest-openjdk java-latest-openjdk-devel -y
alternatives --config java

cd /opt/reportportal/ && \
wget -c -N -O migrations.zip https://github.com/reportportal/migrations/archive/${MIGRATIONS_VERSION}.zip && unzip migrations.zip && mv migrations-${MIGRATIONS_VERSION} migrations && rm -f migrations.zip
PGPASSWORD=$RP_POSTGRES_PASSWORD psql -U $RP_POSTGRES_USER -d reportportal -a -f migrations/migrations/0_extensions.up.sql -f migrations/migrations/1_initialize_schema.up.sql -f migrations/migrations/2_initialize_quartz_schema.up.sql -f migrations/migrations/3_default_data.up.sql -f migrations/migrations/4_size_limitations.up.sql -f migrations/migrations/5_test_case_id_type.up.sql -f migrations/migrations/6_retries_handling.up.sql -f migrations/migrations/7_auth_integration.up.sql -f migrations/migrations/8_sender_case_enabled_field.up.sql -f migrations/migrations/9_analyzer_params.up.sql -f migrations/migrations/10_attachment_size.up.sql -f migrations/migrations/11_password_encoding.up.sql -f migrations/migrations/12_remove_ticket_duplicates.up.sql -f migrations/migrations/13_add_allocated_storage_per_project.up.sql -f migrations/migrations/14_test_case_id_size_increase.up.sql -f migrations/migrations/15_statistics_decreasing.up.sql -f migrations/migrations/16_remove_unused_indexes.up.sql -f migrations/migrations/17_status_enum_extension.up.sql -f migrations/migrations/18_job_attributes.up.sql -f migrations/migrations/19_retries_handling_extension.up.sql -f migrations/migrations/20_deep_merge_statistics_handling.up.sql -f migrations/migrations/21_deep_merge_retries_fix.up.sql -f migrations/migrations/22_deep_merge_nested_steps_fix.up.sql -f migrations/migrations/23_rerun_item_statistics_fix.up.sql -f migrations/migrations/24_widget_views_cleanup.up.sql -f migrations/migrations/25_deep_merge_nested_steps_path_fix.up.sql 2>&1 &

cd /opt/reportportal/ && \
wget -c -N -O service-index https://github.com/reportportal/service-index/releases/download/$SERVICE_INDEX_VERSION/service-index_linux_amd64
chmod +x service-index && \
RP_SERVER_PORT=9000 LB_URL=http://localhost:8081 ./service-index 2>&1 &

cd /opt/reportportal/ && \
curl -L $MAVEN_REPO/service-api/$API_VERSION/service-api-$API_VERSION-exec.jar -o service-api.jar
sudo RP_AMQP_HOST=localhost RP_AMQP_APIUSER=$RP_RABBITMQ_USER RP_AMQP_APIPASS=$RP_RABBITMQ_PASSWORD RP_AMQP_USER=$RP_RABBITMQ_USER RP_AMQP_PASS=$RP_RABBITMQ_PASSWORD RP_DB_USER=$RP_POSTGRES_USER RP_DB_PASS=$RP_POSTGRES_PASSWORD RP_DB_HOST=localhost java $SERVICE_API_JAVA_OPTS -jar service-api.jar 2>&1 &

cd /opt/reportportal/ && \
curl -L $MAVEN_REPO/service-authorization/$UAT_VERSION/service-authorization-$UAT_VERSION-exec.jar -o service-uat.jar
RP_DB_HOST=localhost RP_DB_USER=$RP_POSTGRES_USER RP_DB_PASS=$RP_POSTGRES_PASSWORD java $SERVICE_UAT_JAVA_OPTS -jar service-uat.jar 2>&1 &

mkdir -p /opt/reportportal/ui && cd /opt/reportportal/
curl -L https://github.com/reportportal/service-ui/releases/download/$UI_VERSION/service-ui_linux_amd64 -o service-ui && \
mv service-ui ui/ && \
chmod -R +x ui/* && \
curl -LO https://github.com/reportportal/service-ui/releases/download/5.3.5/ui.tar.gz && \
mkdir public && \
tar -zxvf ui.tar.gz -C public && rm -f ui.tar.gz
cd ui/ && RP_STATICS_PATH=../public RP_SERVER_PORT=3000 ./service-ui 2>&1 &
# default cred to login user:`superadmin`, password: `erebus`
# Done for the phase 6

