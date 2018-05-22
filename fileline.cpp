#include <iostream>
#include <fstream>
using namespace std;
main()
{
	ifstream A("/home/vipin/hello.txt");
	char v[100];
	while(A)
	{
	A.getline(v,15);
	cout << v << " ";
	}
	A.close();
}