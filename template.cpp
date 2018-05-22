#include <iostream>
using namespace std;
template <class tem>
void qswap ( tem &a , tem &b)
{
   tem temp;
   temp = a;
   a = b;
   b = temp;
}
template <class tim>
tim sum ( tim x , tim y )
{   tim temp;
	temp = x+y;
	return temp;
}
class relaction
{
   int num,den;
   public :
   relaction( int a = 0,int b = 1)
   {
   	 num = a;
   	 den = b;
   }
   friend istream & operator >> (istream &a , relaction &z)
   {
        cout << " Please enter num and den  :: ";
        a >> z.num >> z.den;
        return a;
   }
   friend ostream & operator << (ostream &a , relaction &z)
   {
   	  a << z.num << "/" << z.den << endl;
   }
   friend relaction operator + (relaction x , relaction y)
   {
   	  relaction z;
   	  z.num = x.num * y.den + y.num*z.den;
   	  z.den = x.den * x.num;
   	  return z;
   }
};
main()
{
	int x = 3,y = 7 , f ;
	float a = 9.89 ,b = 98.7 , fu;
	relaction p(12,24),q(434,54) , fuc ;
	cout << "Before calling \n ";
	cout << x << "  " << y << endl;
	cout << a << "  " << b << endl;
	cout << p << q;
	qswap(x,y);
	qswap(a,b);
	qswap(p,q);
	cout << " \n After calling \n";
	cout << x << "  " << y << endl;
	cout << a << "  " << b << endl;
	cout << p << q;
	cout << " \n\n\n   sum function  \n\n\n ";
	f = sum(x,y);
	fu = sum(a,b);
	fuc = sum(p,q);
	cout << " \n After calling \n";
	cout << f << endl; 
	cout << fu << endl;
	cout <<fuc;
}