#include<stdio.h>
void main()
{
    float x,n,i,sum = 0;
    printf("Enter value of X :");
    scanf("%f",&x);
    printf("Enter value of N :");
    scanf("%f",&n);
    for ( i = 1 ; i <= (int)n ; i++ )
    {  
        sum = sum + 1/(x+i);
    }
    printf("%f",sum);
}