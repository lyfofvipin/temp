#include<stdio.h>
typedef union
{
 int a;
	char b[20];
}test;
void input(test *p)
{
	printf("enter a number and naame");
	scanf("%d%s",&(*p).a,&p->b);
}
void output(test *p)
{
	printf("%d\n\n%s",p->a,(*p).b);
}
void main()
{
   test a;
	input(&a);
	output(&a);
}
