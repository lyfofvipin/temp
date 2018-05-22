#include<stdio.h>
#include<string.h>
void main()
{
	char a[20],b[20];
        printf("enter first string \n");
	scanf("%[^\n]",a);
	printf("enter secand string \n");
        scanf("%s",b);
	strcat(a,b);
	puts(a);
}
