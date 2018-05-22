#include<stdio.h>
#define sz 5
void rev (int *a)
{    int temp,i,j;
	for(i=0,j=sz-1;i<j;i++,j--)
		{
			temp=*(a+i);
                        *(a+i)=*(a+j);
			*(a+j)=temp;
		}
}
void main()
{
 int a[sz]={5,10,15,20,25},i;
	void rev (int *);
	for(i=0;i<sz;i++)
		printf("%d\t",a[i]);
        	rev(a);
	for(i=0;i<sz;i++)
		printf("%d\t",a[i]);
}
