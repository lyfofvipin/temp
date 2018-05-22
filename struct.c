#include<stdio.h>
struct vipin
{
    int a ;
    char b[10] ;
};
void main()
{
    struct vipin object;
    struct vipin object2;
    printf("Enter Your name ::");
    scanf("%s",&object.b);
    printf("Enter a your age :");
    scanf("%d",&object.a);
    printf("\n%s",object.b);
    printf("\n%d",object.a);
    object2 = object;
    printf("\n%s",object2.b);
    printf("\n%d\n",object2.a);
}