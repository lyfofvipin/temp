#include<stdio.h>
void main()
{
	int i,j,n;
	printf("enter a number \n");
	scanf("%d",&n);
	for(i=n;i>=1;i--)
		{
			for (j=n;j>i;j--)
			  printf(" ");

			for(j=1;j<=2*i-1;j++)
				printf("*");

			printf("\n");
		}
}
