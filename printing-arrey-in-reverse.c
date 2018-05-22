#include<stdio.h>
void main()
{
  int a[5],i;
  char x;
	printf("enter first arrey \n");
   for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&a[i]);
     }

	for (i=4;i>=0;i--)
        printf("%d \n",a[i]);

}
