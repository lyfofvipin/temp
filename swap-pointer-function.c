#include<stdio.h>
void main()
{
       int a,b;
	void swapa (int*,int*);
     printf("enter two number \n");
	scanf("%d%d",&a,&b);
        swapa (&a,&b);
	printf("%d\n%d",a,b);
}
void swapa (int *p,int *q)
{
	 int temp;
	temp=*p;
	*p=*q;
	*q=temp;
}
