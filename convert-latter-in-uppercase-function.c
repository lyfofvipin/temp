#include<stdio.h>
void main()
{
    char a;
    int b;
     int upper (char);
	printf("enter a latter \n");
	scanf("%c",&a);
	b = upper (a);
	if(b==1)
	  printf("you allready enterd a capital later %c \n",a);
	 else
		 printf("small number is %c and capital is %c",a,b);
}
int upper (char a)
{
	int b;
	if(a>=65 && a<=90)
	    b=1;
	else
		b=a-32;

	return b;
}
