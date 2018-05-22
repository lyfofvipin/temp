#include<stdio.h>
void main()
{
	int a[5]={5,10,15,20,25},*p;
        p=a;
	for(;p<a+5;p++)
	printf("%d \t",*p);
}
