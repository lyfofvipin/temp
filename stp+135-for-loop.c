#include<stdio.h>
void main()
{
	int i,j,n;
	printf("enter a number \n");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		{
			for(j=1;j<=2*i-1;j++)
				{
				if(i%2!=0)
				printf("*");
			else
				printf("+");
		}

			printf("\n");
		}
}
