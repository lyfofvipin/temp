#include<stdio.h>
void main()
{
  int a[10],i,b,l,s,e;
    s=e=l=0;

	printf("enter the serch element\n");
	scanf("%d",&b);

   for (i=0;i<10;i++)
     {
       printf("enter a number \n");
	     scanf("%d",&a[i]);


	     if(a[i]==b)
		e++;

	     if(a[i]<b)
		s++;

	     if(a[i]>b)
		 l++;
     }
    printf("large number is %d small number is %d and equal are %d",l,s,e);
     }
