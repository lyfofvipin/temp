#include<stdio.h>
#define sz 5
void sum(int *a,int *p,int *n)
{
	int i;
	for(*p=*n=i=0;i<sz;i++)
		{
	if(*(a+i)>0)
	 *p=*p+*(a+i);
	else
	*n=*n+*(a+i);
		}
}
void main()
{
	int a[sz],p,n,i;
	void sum (int*,int*,int*);
	for(i=0;i<5;i++)
		{
	printf("enter a number\n");
	scanf("%d",&a[i]);
		}
	sum (a,&p,&n);
	printf(" positive= %d \n negtive= %d ",p,n);
}
