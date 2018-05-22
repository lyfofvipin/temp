#include <iostream>
using namespace std;
class relaction
{
   int num[100];
   int den[100];
   static int y;
public:
 void  operator () (int x,int q)
   {
       num[y] = x;
       den[y] = q;
       y++;
       
   }
   void  operator () (int x,int q ,int p)
   {
       num[p] = x;
       den[p] = q;
       y = p+1;
     
   }
 void operator [] (int x)
   {
      cout << num[x] << "/" << den[x]<<endl;
   }
};
int relaction::y;
main()
{
   relaction A,B;
   A(90,13);
   A[0];
   A(45,67,56);
   A[56];
   A(57,57);
   A[57];
  }