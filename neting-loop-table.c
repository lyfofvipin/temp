#include<stdio.h>
void main()
{
	int a,b,i,j;
	printf("enter your both number \n");
	scanf("%d \n %d",&a,&b);
	for (a++;a<b;a++)
	  {
              for (j = 1; j <=10 ; j++)
                {
                  printf("%d  ",a*j);
                }
	  }
}
