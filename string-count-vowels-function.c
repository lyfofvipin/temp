#include<stdio.h>
#include<string.h>
void main()
{
	int v;
	char a[20];
	int strcp(char[]);
         printf("enter your first string \n");
	 scanf("%[^\n]",a);
	v=strcp(a);
	printf("number of voules in string is %d \n",v);

}
int strcp(char a[])
{

	int i,l,v;
	l=strlen(a);
        for(v=i=0;i<=l;i++)
		{
             if( a[i]=='a'||a[i]=='i'||a[i]=='e'||a[i]=='o'||a[i]=='u')
		  v++;
		}
             return v;
}
