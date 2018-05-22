#include<iostream>

#include<fstream>

using namespace std;

main()

{
	
       ofstream A("/home/vipin/hello.txt");
       char v;

	cout << "writing ddata : :  \n";
while(1)
{
    cout << "enter a word ::  ";
	cin >> v;
    if(cin.eof())
      break;
    A.put(v);
}
    A.close();

}