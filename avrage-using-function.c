#include<stdio.h>
void main()
{
 int a,b,c,d;
	float x;
	float avg (int,int,int,int);
      printf("enter four number \n");
	scanf("%d%d%d%d",&a,&b,&c,&d);
	x= avg (a,b,c,d);
	printf("%d \n",x);

}
float avg (int a,int b,int c,int d)
{
	float x;
	x= a+b+c+d;
	x=x/4;
	return x;
}
