#include<stdio.h>
void main()
{
	int a,b,*x,*y;
	a=5;
	b=56;
	x=&a;
	y=&b;
	*x=*x+*y;
	printf("%d \n",*x);
}
