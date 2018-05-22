#include<stdio.h>
#include<string.h>
void main()
{
	int l;
	char a[20],b[20];
        printf("enter first string \n");
	gets(a);
	printf("enter secand string \n");
	scanf("%s",b);

	l=strcmp(a,b);
	if(l>0)
		printf("a is large");
	else if(l<0)
		printf("b is large");
	else
		printf("both are equal");
}
