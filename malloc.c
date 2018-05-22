#include <stdio.h>
#include <stdlib.h>
void main()
{
	int *p,n;
	p = (int *)malloc(sizeof(int));
	*p = 45;
	printf("%d\n",*p);
	free(p);
}