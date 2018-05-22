#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream A;
    A.open("/home/vipin/hello.txt");
    char v[100];
    while( !A.eof() )
    {
      A >> v;
      cout << v << " ";
    }
    A.close();
}