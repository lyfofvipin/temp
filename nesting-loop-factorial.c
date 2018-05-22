#include<stdio.h>
void main()
{
int a,i,j,f=1;
for(i=1;i<=3;i++)
{
printf("enter a number \n");
scanf("%d",&a);

for(j=1;j<=a;j++)
f=f*j;

	printf("%d \n",f);

}
}
