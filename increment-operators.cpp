#include <iostream>
using namespace  std;
class relactional
{
	int num,den;
public:
	relactional( int x = 0 ,int y = 1)
	{
       num = x;
       den = y;
	}
    relactional operator ++ ()
    {
       num = num + den ;
       den = den;
       relactional z(num,den);
       return z;
    }
    relactional operator ++ ( int )
    {
       relactional z(num,den);
       num = num + den ;
       den = den;
       return z;
    }
    relactional operator -- ()
    {
       num = num - den ;
       den = den;
       relactional z(num,den);
       return z;
    }
    relactional operator -- ( int )
    {
       relactional z(num,den);
       num = num - den ;
       den = den;
       return z;
    }
    void output()
    {
    	cout << num <<"/"<<den<<endl;
    }
};
main()
{
	relactional A(2,3),p;
	p = ++A;
	p.output();
	A.output();
	p = A++;
	p.output();
	A.output();
	p = --A;
	p.output();
	A.output();
	p = A--;
	p.output();
	A.output();
}