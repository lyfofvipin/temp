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
   relactional sort  (      relactional          );
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
   a.output();
   b.output();
   c = add(a,b);
   c.output();
   c = min(a,b);
   c.output();
   c = multi(a,b);
   c.output();
   c = div(a,b);
   c.output();

}