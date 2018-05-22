#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream A;
    A.open("/home/vipin/hello.txt");
    char v;
    while( !A.eof() )
    {
      A.get(v);
      cout << v;
    }
    A.close();
}