#include<stdio.h>
void main()
{
	FILE *p;
	char a[100],b[100],c[100];
	p=fopen("/home/vipin/foobar.txt","r");
        fscanf(p,"%s%s%s",a,b,c);
	printf("\n\n%s\n\n%s\n\n%s\n\n",a,b,c);
	fclose(p);
}
