#include<stdio.h>
void main()
{
   FILE *x;
	char a;
	x=fopen("/home/vipin/hello.txt","r");
	while(1)
		{
			a=fgetc(x);
			if(a==EOF)
				break;
			else
				printf("%c\t",a);
		}
	fclose(x);
}
