#include<stdio.h>
void main()
{
	float a,r,p;
	void area(float *,float *,float);
	printf("enter radeus of your circle \n");
             scanf("%f",&r);
	area(&a,&p,r);
	printf(" area is %f \n and perameter is %f \n ",a,p);
}
void area (float *a,float *p,float r)
{
      *a=r*r*3.14;
	*p=2*r*3.14;
}
