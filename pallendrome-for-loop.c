#include<stdio.h>
void main()
{
	int i,a,b;
	printf("enter your number \n");
	scanf("%d",&a);
	b=a;
	for(i=0;a>0;a=a/10)
		{
			i=i*10+a%10;
		}
	if(b==i)

	printf("%d\n",i);

	else
		printf("no");
}
