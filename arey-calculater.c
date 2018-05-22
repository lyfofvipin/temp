#include<stdio.h>
void main()
{
  int a[5],b[5],i;
  char x;
	printf("enter first array \n");
   for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&a[i]);
     }
	printf("enter secand array \n");
	for (i = 0; i < 5; i++)
     {
       printf("enter a number \n");
	     scanf("%d",&b[i]);
     }


     	printf("select a opperaction \n");
                   fflush(stdin);
               scanf("%c",&x);

	switch(x)
		{
		case '+':
		{
			for (i = 0; i < 5; i++)
                        printf("%d \n",a[i]+b[i]);

			break;
		}
		case '-':
		{
			for (i = 0; i < 5; i++)
                        printf("%d \n",a[i]-b[i]);

			break;
		}
		case '*':
			{
			for (i = 0; i < 5; i++)
                        printf("%d \n",a[i]*b[i]);

				break;
		}
		case '/' :
			{
			for (i = 0; i < 5; i++)
                        printf("%d \n",a[i]/b[i]);

				break;
		}
		default:
			printf("invalid slection \n");
		}



}
