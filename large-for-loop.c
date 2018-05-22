#include<stdio.h>
void main()
{
	int i,a,max;
	printf("enter a number\n");
        scanf("%d",&a);
	max=a;
	for(i=1;i<=4;i++)
		{
	printf("enter a number\n");
        scanf("%d",&a);
			if(a>max)
				max=a;
		}
	printf("%d",max);

}
