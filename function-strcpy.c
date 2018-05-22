#include<stdio.h>
#include<string.h>
void main()
{
	char a[20],b[20];
	void strcp(char[],char[]);
         printf("enter your first string \n");
     gets(a);
	 strcp(a,b);
	 puts(b);
}
void strcp(char a[],char b[])
{

	int i;
             for(i=0;a[i]!=NULL;i++)
		{
			b[i]=a[i];
		}
             b[i]=NULL;
}
