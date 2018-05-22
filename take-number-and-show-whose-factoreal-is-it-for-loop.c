#include<stdio.h>
void main()
{
	int n,i,j;
	printf("enter a number");
	scanf("%d",&n);
        j=1;
	for(i=1;i<=n;i++)
{
	j=j*i;
	if(j==n)
		{
			n=-1;
		break;
		}
}
	if(n==-1)
		printf("%d",i);
	else
		printf("invalid number\n");
}
