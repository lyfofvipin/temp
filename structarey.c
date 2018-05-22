#include<stdio.h>
struct emp
{
	int age,sailry;
	char a[10];
}b[5];
void main()
{

	int i;
	for(i=0;i<5;i++)
	{
	printf("enter name age and sailry\n");
        scanf("%s%d%d",&b[i].a,&b[i].age,&b[i].sailry);
	}
	for(i=0;i<5;i++)
        printf("%s\t%d\t%d\n",b[i].a,b[i].age,b[i].sailry);
 }
