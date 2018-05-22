#include<stdio.h>
void main()
{
	int a,p,se,s;
	printf("enter your number \n");
	scanf("%d",&a);
	for(p=0,se=1,s=0;a>=1;a--)
		{
                       printf("%d\n",p);
		       s=p+se;
                       p=se;
		       se=s;
		}
}
