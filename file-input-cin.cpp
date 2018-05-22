#include<iostream>
#include<fstream>
using namespace std;
main()
{
    ofstream A("/home/vipin/hello.txt");
    char s[10],chois;
    do
    {
    cout << "\nEnter your name : :";
    cin >> s;
    A << s << "\n";
    cout << "YOU HAVE SOME MORE NAMES :: ";
    cin >> chois;
    }while(chois == 'y');
    A.close();
}