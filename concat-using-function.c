#include<stdio.h>
#include<string.h>
void main()
{
	char a[20],b[20];
	void strca(char[],char[]);
         printf("enter your first string \n");
           gets(a);
	 printf("enter your secand string \n");
	gets(b);
	strca(a,b);
	puts(a);
}
void strca(char a[],char b[])
{

	int i,j;

             for(i=0;a[i]!=NULL;i++);
	                i=i-1;

	for(j=0;b[j]!=NULL;j++)
		{
			a[i+j+1]=b[j];
		}
             a[i+j+1]=NULL;
}
