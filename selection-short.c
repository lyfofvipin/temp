#include<stdio.h>
void main()
{
  int a[5],temp,i,j,l;
   for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&a[i]);
     }

    for(i=0;i<4;i++)
		{
	     l=i;
    for(j=i+1;j<5;j++)
		{
                  if(a[l]>a[j])
	               l=j;
		}

		temp=a[i];
		a[i]=a[l];
	        a[l]=temp;
   }
	for (i = 0; i < 5; i++)
         printf("%d \t",a[i]);

}
