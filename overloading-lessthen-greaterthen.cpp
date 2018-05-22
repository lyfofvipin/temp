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
   friend istream & operator >> (istream &z , relactional &x)
   {
     cout <<  "Please enter num and dan :: \n " ;
     z >> x.num >> x.den;
     return z;
   }
   friend ostream & operator << (ostream &z , relactional &x)
   {
     z << x.num << "/" << x.den << endl;
     return z;
   }
   friend relactional add   ( relactional , relactional );
   friend relactional min   ( relactional , relactional );
   friend relactional multi ( relactional , relactional );
   friend relactional div   ( relactional , relactional );
};
relactional add ( relactional a , relactional b)
{
           relactional z;
           z.num = a.num*b.den + b.num * a.den;
           z.den = a.den*b.den;
           return z;
}
relactional min ( relactional a , relactional b)
{
           relactional z;
           z.num = a.num*b.den - b.num * a.den;
           z.den = a.den*b.den;
           return z;
}
relactional multi ( relactional a , relactional b)
{
           relactional z;
           z.num = a.num*b.num;
           z.den = a.den*b.den;
           return z;
}
relactional div ( relactional a , relactional b)
{
           relactional z;
           z.num = a.num * b.den;
           z.den = b.num * a.den;
           return z;
}
main()
{
   relactional a(34,65),b(12,32),c;
   cin >> a;
   cout << a;
   cin >> b;
   cout << b;
   c = add(a,b);
   cout << c;
   c = min(a,b);
   cout << c;
   c = multi(a,b);
   cout << c;
   c = div(a,b);
   cout << c;

}