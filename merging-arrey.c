#include<stdio.h>
void main()
{
  int a[5],i,b[5],c[10];
   for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&a[i]);
     }
    for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&b[i]);
     }

	for (i = 0; i < 5; i++)
     {
       c[i]=a[i];
       c[i+5]=b[i];
     }
	for (i = 0; i <10 ; i++)
	  {
	    printf("%d \t",c[i]);
	  }
}
