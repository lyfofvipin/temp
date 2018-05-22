#include<iostream>
using namespace std;
class relactional
{
   int num,den;
public:
   relactional(int x = 0,int y = 1)
   {
      num = x;
      den = y;
   }
   void output()
   {
   	cout << num << "/" << den << endl;
   }
   operator float()
   {
   	  return float(num)/den;
   }
};
class complex
{
   int real,img;
public:
   complex(int x = 0,int y = 0)
   {
   	   real = x;
   	   img = y;
   }
   operator relactional()
   {
   	 return relactional(real,img);
   }
   void output()
   {
   	 cout << real << "+i" << img << endl;
   }
};
void user_to_user()
{
	 complex A(12,98);
	 relactional a;
	 a = relactional(A);
	 a.output();
}
void user_to_inbuild()
{
	relactional A(43,56);
	float a;
	a = A;
	cout << endl << a << endl << endl ;
	a = float(A);
	cout << endl << a << endl << endl ;
}
void inbuild_to_user()
{
    int a = 90;
    relactional A;
    A = a;
    a = 98;
    A.output();
    A = relactional(a);
    A.output();
}
void inbuild_to_inbuild()
{
	int a = 23 , b = 3;
	float c;
	c = a/b;
    cout << "Value before casting :"<< c;
    c = float(a)/b;
    cout << endl << "Value after casting :"<< c << endl;
}
main()
{
    user_to_user();
}