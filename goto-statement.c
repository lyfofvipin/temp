#include<stdio.h>
void main()
{
	int i=0;
gotol:
	printf("%d \n",i);
	i++;
	if(i<=10)
		goto gotol;
}
