#include<stdio.h>
void main()
{
	FILE *y,*x;
	char l;
        x=fopen("/home/vipin/foobar.txt","r");
	y=fopen("/home/vipin/hello.txt","w");
        while(1)
		{
			l=fgetc(x);
			if(l==EOF)
				break;
			else
 fputc(l,y);
		}
	fclose(x);
	fclose(y);
}
