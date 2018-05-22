#include<stdio.h>
#include<string.h>
void main()
{
	char a[20],b[20];
        printf("enter 3 string \n");
	scanf("%[^\n]",a);

	strcpy(b,a);
	puts(b);
}
