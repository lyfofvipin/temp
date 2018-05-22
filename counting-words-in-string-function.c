#include<stdio.h>
void main()
{
   char a[20];
   int count ( char a[]),i;
       printf("enter your string \n");
      gets(a);
      i=count(a);
      printf("the number of words in the string is %d",i);
}
int count(char a[])
{
    int i,j;
    for(i=0,j=1;a[i]!=NULL;i++)
    {
        if(a[i]==' ')
              j++;
    }

    return j;
}

