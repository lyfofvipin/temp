#include<stdio.h>
void main()
{
	 FILE *x;
           char a;
          x=fopen("/home/vipin/hello.txt","a");
	while(1)
		{
			a=getchar();
			if(a==EOF)
				break;
			else
				fputc(a,x);
		}
  fclose(x);
}
