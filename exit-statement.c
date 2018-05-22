#include<stdio.h>
#include<stdlib.h>
void main()
{
	  int a,i,sum;

	for (i=1,sum=0;i<=10;i++)
	  {
         printf("enter a positeve number \n");
         scanf("%d",&a);
	   if(a<0)
	exit(0);
           else
            sum=sum+a;
	  }
	printf("%d",sum);
}	         
