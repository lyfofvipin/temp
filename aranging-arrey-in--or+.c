#include<stdio.h>
void main()
{
  int a[5],i,temp,j;
   for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&a[i]);
     }
     for (j=0,i = 0; i < 5; i++)
		{
		if(a[i]<0)
				{
					temp=a[j];
					a[j]=a[i];
					a[i]=temp;
					j++;
				}
		}
	 for (i = 0; i < 5; i++)
		 printf("%d \t",a[i]);
}
