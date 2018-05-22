#include<stdio.h>
void main()
{
    int a[10]={10,9,8,7,6,5,4,3,2,1},n;
	n=10;
    void shell (int [],int);
	shell(a,n);
    for(n=0;n<10;n++)
    printf(" %d ",a[n]);
}
void shell(int a[],int n)
{
   int gap,i,j,temp,swap=0;
   for(gap=n/2;gap>0;gap=gap/2)
		{
			while(swap=0)
			{
		  	for(i=0;swap==0;i++)
				{
                                         swap=1;
					if(a[i]>a[gap+i])
						{
						   swap=0;
                                                   temp=a[i];
						   a[i]=a[gap+i];
						   a[gap+i]=temp;
						}
				}
			}
		}


}
