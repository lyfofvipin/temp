#include<stdio.h>
void main()
{
	float har,da,b,sal,con,i,basic,bo;
	printf("enter your sale \n");
	scanf("%f",&basic);
	if(basic>=100000)
		{
			i= basic*10/100;
			bo=500;
		}
	else
		{
			i=basic*5/100;
			bo=200;
		}
		b=3000;
	har=20*b/100;
	con=500;
	da=110*b/100;
 sal=da+b+har+con+i+bo;
	printf("%f",sal);
}
