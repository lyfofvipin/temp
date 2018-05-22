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
   void input()
{
    cout << "Pleas enter num and den :: ";
    cin  >> num >> den ;
}
   relactional sort( relactional);
   friend relactional operator + ( relactional , relactional );
   friend relactional operator - ( relactional , relactional );
   friend relactional operator * ( relactional , relactional );
   friend relactional operator / ( relactional , relactional );
};
relactional operator + ( relactional a , relactional b)
{
           relactional z;
           z.num = a.num*b.den + b.num * a.den;
           z.den = a.den*b.den;
           return z;
}
relactional operator - ( relactional a , relactional b)
{
           relactional z;
           z.num = a.num*b.den - b.num * a.den;
           z.den = a.den*b.den;
           return z;
}
relactional operator * ( relactional a , relactional b)
{
           relactional z;
           z.num = a.num*b.num;
           z.den = a.den*b.den;
           return z;
}
relactional operator / ( relactional a , relactional b)
{
           relactional z;
           z.num = a.num * b.den;
           z.den = b.num * a.den;
           return z;
}
main()
{
   relactional a(34,65),b(12,32),c;
   a.output();
   b.output();
   c = 25+a;
   c.output();
   c = a-b;
   c.output();
   c = a*b;
   c.output();
   c = a/b;
   c.output();

}