#include<stdio.h>
void main()
{
	int i,j,temp=0;

	for (i=1;i<=50; i++)
	  {

	    for (j=2;j<i;j++)
	      {
                 if ( i%j==0 )
     	          temp=1;

	  }

	if(temp==0||i!=1)
       printf("%d \n",i);
}
}
