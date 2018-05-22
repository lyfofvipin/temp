#include<stdio.h>
void main()
{
	int i,n,temp=0;
               printf("enter a number \n");
	scanf("%d",&n);

	    for (i=2;i<n-1;i++)
	      {
                 if ( n%i==0 )
	           {
		          temp=1;
			   break;
		   }
	  }

	if(temp==1||n==1)
        printf("non prime\n");
	else
        printf("prime\n");
}
