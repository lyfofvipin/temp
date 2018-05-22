#include<stdio.h>
void main()
{
	FILE *p;
	int q;
        p=fopen("/home/vipin/hello.txt","r");
        q=ftell(p);
	printf("\n\n%d\n\n",q);
	fseek(p,9,SEEK_SET);
	q=ftell(p);
	printf("\n\n%d\n\n",q);
	fseek(p,-4,SEEK_CUR);
	q=ftell(p);
	printf("\n\n%d\n\n",q);
	fseek(p,0,SEEK_END);
	q=ftell(p);
	printf("\n\n%d\n\n",q);
	fseek(p,-33,SEEK_END);
	q=ftell(p);
	printf("\n\n%d\n\n",q);
}
