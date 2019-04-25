#include<stdio.h>
#include<string.h>
#define sz 50
int main()
{
    char a[] = "My name is vipin";
    char *p;
    char * ReverseWords(char []);
    p = ReverseWords(a);
    puts(p);
    return 0;
}

char * ReverseWords( char a[])
{
    int i,j;
    char b[sz];
    char *p;
    for( i = strlen(a)-1, p = b ; i >= 0 ; i-- )
    {
        if( a[i] == ' ' )
        {
            for( j = i+1 ; a[j] != 0 && a[j] != ' ' ; j++, p++)
            {
                *p = a[j];
            }
            *p = ' ';
            p++;
        }
    }
    for( i = 0 ; a[i] != ' '; i++, p++ )
        *p = a[i];
    p = 0;

    strcpy(a,b);
    return a;
}