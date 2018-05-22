#include <iostream>
using namespace std;
main()
{
   int *p;
    p = new int[10];
    p[3] = 90;
    cout  << p[3];
   delete [] p ;
}