#include <iostream>
using namespace std;
main()
{
   int *p;
    p = new int;
    *p = 90;
    cout  << *p;
   delete p;
}