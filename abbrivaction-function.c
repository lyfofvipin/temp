#include<stdio.h>
void main()

{
	void abr(char);
	char a[20];
	puts("enter your string \n");
	gets(a);
        abr(a);
}
void abr (char a[20])
{
   int i,x;
              for(i=x=0;a[i]!=NULL;i++)
		{
			if(a[i]==' ')
				{
		        		printf("%c.",a[x]);
					x=x+1;
				}
		}
	for(;a[x]!=NULL;x++)
		printf("%c",a[x]);
}
