#include<stdio.h>
void main()
{
  FILE *x;
	char p;
	int v=0;
   x=fopen("/home/vipin/foobar.txt","r");
	while(1)
		{
			p=getc(x);
			if(p==EOF)
				break;
			if(p==' '||p=='\n')
				v++;
		}
	printf("\n\nno of words are %d\n\n",v);
}
