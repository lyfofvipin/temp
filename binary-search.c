#include<stdio.h>
void main()
{
  int a[5],i,b,c;
  int serch (int [],int,int);

   for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&a[i]);
     }
	printf("enter a number u want to search \n");
	scanf("%d",&b);
           i=i-1;
	c = serch (a,b,i);

	if(c==1)
		printf("element is prsent in array \n");
        else
		printf("element is not prsent in array \n");
  }
int serch(int a[],int b,int h)
{
    int i,m,l;
	l=0;
	for(;l<=h;)
		{
			m=(l+h)/2;

			if(m==b)
			  return 1;
			else if(b>m)
			  l=m+1;
			else if(b<m)
			  h=m-1;
		}
	return 0;
 }
