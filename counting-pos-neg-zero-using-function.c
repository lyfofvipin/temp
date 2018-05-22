#include<stdio.h>
#define sz 5
void count (int *a,int*b)
{
	 int  p;
	for(p=0;p<sz;p++)
		{
			if(*(a+p)>0)
			   *(b+0)=*(b+0)+1;
			else if(*(a+p)<0)
				*(b+1)=*(b+1)+1;
			else
				*(b+2)=*(b+2)+1;
		}
}
void main()
{
	int a[sz],b[3]={0},i;
	for(i=0;i<sz;i++)
		{
			printf("enter a number" );
			scanf("%d",&a[i]);
		}
	count(a,b);
	for(i=0;i<3;i++)
	printf("%d\n",b[i]);
}
