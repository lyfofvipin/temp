#include<stdio.h>
void main()
{
	int i,a,b,c,max;
	printf("enter three number \n");
	scanf("%d \n %d \n %d",&a,&b,&c);
	for(i=2,max=0;i<=a||i<=b||i<=c;i++)
		{
	      if(a%i==0 && b%i==0 && c%i==0)
		   max=i;
		}
	printf("%d", max);
}
