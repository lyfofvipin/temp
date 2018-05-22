#include<stdio.h>
void main()
{
    char a[20],b[20];
    void rev(char [],char[]);
    puts("enter your string");
    gets(a);
       rev(a,b);
    puts(a);
    puts(b);
}
void rev(char a[],char b[])
{
    int i,j;

    for(i=0;a[i]!=NULL;i++);
   i=i-1;

    for(j=0;j<=i;j++)
    {
        b[j]=a[i-j];
    }
    b[j]=NULL;
}
