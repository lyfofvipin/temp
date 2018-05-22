#include<stdio.h>
void main()

{
	void abr(char []);
	char a[20];
	puts("enter your string \n");
	gets(a);
        abr(a);
	puts(a);
}
void abr (char a[20])
{
   int i,x;
	for(i=0;a[i]!=NULL;i++)
		{
		if(a[i]=='a'||a[i]=='i'||a[i]=='e'||a[i]=='o'||a[i]=='u')
				{
					for(x=i;a[x]!=NULL;x++)
						a[x]=a[x+1];

					i--;
				}
		       	}
}
