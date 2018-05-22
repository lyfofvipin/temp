#include<stdio.h>
void main()
{
	int c,s,r,n;
        void fun (int,int*,int*,int*);
	printf("entre your number \n");
	scanf("%d",&n);
	fun(n,&s,&r,&c);
	printf("the sum is %d revers is %d count is %d",s,r,c);
}
void fun (int n,int *s,int *r,int *c)
{
	int i;
	*s=*r=*c=0;

	for (;n>0;n=n/10)
	  {
		 *s=*s+n%10;
	         *r=*r*10+n%10;
		 *c=*c+1;
	  }
}
