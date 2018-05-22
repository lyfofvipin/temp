#include<stdio.h>
void main()
{
  FILE *p;
  char a[20];
     p=fopen("/home/vipin/hello.txt","r");
	if(fgets(a,20,p)>0)
	 printf("\n\n%s\n\n",a);

     fclose(p);
}
