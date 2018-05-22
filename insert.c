#include<stdio.h>
void main()
{
   int i;
   int a[10]={10,9,8,7,6,5,4,3,2,1};
   void insert(int []);
   insert(a);
	for(i=0;i<top;i++)
	printf("%d\t",a[i]);
}
void insert (int a[])
{
  int i,j,val;
	for(i=1;i<t;i++)
{
  for(j=i-1,val=a[i];j>=0&&a[j]>val;j--)
{
        a[j+1]=a[j];
}
	a[j+1]=val;
}
}
