#include<stdio.h>
void main()
{
	int i,n,pow=1;
	printf("enter a number \n");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		{
                  pow=pow*n;
		}
	printf("%d",pow);
}
