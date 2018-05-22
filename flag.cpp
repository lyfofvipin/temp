#include<iostream>
#include<iomanip>
using namespace std;
main()
{
	bool z;
	int x = 75;
	float r = 89;
	cout.precision(4);
	cout << r << endl;
	cout << "Calling before activating  ::: " <<  z << endl;
	cout.setf(ios::boolalpha);
	cout << "Calling after activating  ::: " <<  z << endl ;
	cout.flags(ios::oct);
	cout << "Calling before activating show base ::: " <<  x << endl ;
	cout.flags(ios::showbase | ios::dec);
	cout << "Calling after activating show base ::: " <<  x << endl ;
	cout.setf(ios::showpos);
	cout << x << endl;
	cout.setf(ios::showpoint);
	cout << r << endl;
	cout.setf(ios::left);
	cout << setw(12) << x << endl;
	cout << setfill('-') << setw(12) << x << endl;
}