#include<stdio.h>
void main()
{
	int i,j,n;
	printf("enter a number \n");
	scanf("%d",&n);
	for(i=n;i>=1;i--)
		{

			for(j=i;j<n;j++)
			   printf(" ");


			for(j=i;j>=1;j--)
		           printf("%d",j);

			for(j=2;j<=i;j++)
                           printf("%d",j);

			printf("\n");
		}
}
