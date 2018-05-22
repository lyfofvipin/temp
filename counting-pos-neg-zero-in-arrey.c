#include<stdio.h>
void main()
{
  int a[5],z,p,n,i;
	z=p=n=0;
   for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&a[i]);

	     if(a[i]>0)
		p++;
	     if(a[i]<0)
		n--;
	     if(a[i]==0)
		 z++;
     }
    printf("positive number is %d negtive number is %d and zeros are %d",p,n,z);
}
