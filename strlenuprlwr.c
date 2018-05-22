#include<stdio.h>
#include<string.h>
void main()
{
	int l;
	char a[20],lwr[20],upr[20];
        printf("enter first string \n");
	scanf("%[^\n]",a);
	l=strlen(a);
	printf("lenght of the string is %d \n",l);
	 strupr( a );
	strcpy(upr,a);
	puts(upr);
	strlwr (a) ;
	strcpy(lwr,a);
	puts(lwr);
}
