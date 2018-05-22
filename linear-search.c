#include<stdio.h>
void main()
{
  int a[5],i,b,c;
  int serch (int [],int);

   for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&a[i]);
     }
	printf("enter a number u want to search \n");
	scanf("%d",&b);

	c = serch (a,b);

	if(c==1)
		printf("element is prsent in array \n");
        else
		printf("element is not prsent in array \n");
  }
int serch (int a[],int b)
{
    int i;

 for (i = 0; i < 5; i++)
		{
			if(b==a[i])
		return 1;
			else
				return 0;
		}
}
