#include<stdio.h>
struct emp
{
        int age,sailry;
	char name[20];
};
void main()
{
	struct emp x;
	printf("enter name and age and sailry");
	scanf("%s%d%d",&x.name,&x.age,&x.sailry);
	printf("%d\t%d\t%s",x.age,x.sailry,x.name);
} 
