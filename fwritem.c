#include<stdio.h>
void main()
{
	FILE *p,*q;
        char a[20];
	p=fopen("/home/vipin/hello.txt","a");
	q=fopen("/home/vipin/foobar.txt","r");
  if(fgets(a,20,q)>0)
		{
               fputs(a,p);
		}
	fclose(p);
	fclose(q);
}
