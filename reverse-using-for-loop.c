#include<stdio.h>
void main()
{
   int a,i;
   printf("enter a number\n");
   scanf("%d",&a);
   for(i=0;a>0;a=a/10)
   {
    i=i*10+a%10;
   }
   printf("%d",i);
}
