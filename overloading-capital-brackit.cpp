#include<iostream>
using namespace std;
class relaction
{
   int i[5];
public:
	relaction()
	{
	     i[0] = 0,i[1] = 1,i[2] = 2,i[3] = 3,i[4] = 4;
	}
	int & operator [] (int a)
	{
        return i[a];
	}
};
main()
{
    relaction A;
    cout << A[4];
    A[4] = 90;
    cout << A[4];
}