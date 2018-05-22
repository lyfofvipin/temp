#include<stdio.h>
void main()
{
    char a[20];
    void rev(char[]);
    puts("enter your string");
    gets(a);
    rev(a);
    puts(a);
}
void rev(char a[])
{
    int i,j,temp;

    for(i=0;a[i]!=NULL;i++);
    i=i-1;

    for(j=0;j<=i/2;j++,i--)
    {
       temp=a[j];
        a[j]=a[i-j];
        a[i]=temp;
    }
}
