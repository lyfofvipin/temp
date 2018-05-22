#include<stdio.h>
void main()
{
    int i,j,x;
    char a[20];
    puts("enter a string \n");
    gets(a);
  for(i=0;a[i]!=NULL;i++);

  for(i--;i>=0;i--)

  {
      for(j=0;j<=i;j++)
      printf("%c",a[j]);

	printf("\n");
  }
}
