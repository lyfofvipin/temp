#include<stdio.h>
void main()
{
	  int a,i,sum;

	for (i=1,sum=0;i<=10;i++)
	  {
         printf("enter a number \n");
         scanf("%d",&a);
	   if(a<0)
           {
	   i--;
              continue;
            }
           else
            sum=sum+a;
	  }
	printf("%d",sum);
}	         
