#include<stdio.h>
void main()
{
	int i,a;
	float avg;
	char d;
	i=0,avg=0;
	do
		{
			printf("enter a number\n");
			scanf("%d",&a);
			avg=avg+a;
			i++;
			printf("do you want to run it again");
			fflush(stdin);
			scanf("%c",&d);
		}while(d=='y');

	printf("%f",avg/i);
}
