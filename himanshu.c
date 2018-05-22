#include<stdio.h>
void main()
{
    char x;
    scanf("%c",&x);
    x >= 'a' && x <= 'z' ? printf("YES") : printf("NO");
}