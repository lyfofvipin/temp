#include<stdio.h>
void main()
{
  int a[5],i;
  void shorting (int []);
   for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&a[i]);
     }
	shorting(a);
       for (i = 0; i < 5; i++)
       printf("%d \t",a[i]);
}
void shorting (int a[])
{
	int i,temp,j;
      for (j = 0; j < 5; j++)
		{
	for (i = 0; i < 4; i++)
		{
			if(a[i]>a[i+1])
				{
					temp=a[i];
					a[i]=a[i+1];
					a[i+1]=temp;
				}
		}

		}

}
