#include<stdio.h>
void main()
{
	int a,b,c,d,i,max,lcm;
	printf("enter 4 number\n");
	scanf("%d\n%d\n%d\n%d",&a,&b,&c,&d);
	max=a*b*c*d;
	for(i=1;i<=max;i++)
		{
			if(i%a==0 && i%b==0 && i%c==0 && i%d==0)
				{	lcm=i;
					break;
				}

		}
printf("lcm is \n %d",lcm);
}
