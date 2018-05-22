#include<iostream>
#include <stdlib.h>
using namespace std;
class matrix
{
   int **M,raw,col;
public:
   matrix(int x = 0 , int y = 0 )
   { 
   	raw = x,col = y;
    M = new int*[raw];
   	for (int i = 0; i < raw; i++)
   	   M[i]	= new int [col];
   }
  
   matrix operator + ( matrix z)
   {
   	  matrix A(raw,col);
   	  if ( raw != z.raw || col != z.col )
   	     {
   	     	cout << "\n\n\n\n :::ENTER SAME SIZE OF MATRIX:::\n\n\n\n";
   	     	exit(0);
   	     }

   	  for (int i = 0; i < raw; i++)
      {  
      	for (int j = 0; j < col; j++)
      		A.M[i][j] = M[i][j] + z.M[i][j];
      }
      return A;
   }

   matrix operator - ( matrix z)
   {
   	  matrix A(raw,col);
   	  if ( raw != z.raw || col != z.col )
   	     {
   	     	cout << "\n\n\n\n :::ENTER SAME SIZE OF MATRIX:::\n\n\n\n";
   	     	exit(0);
   	     }

   	  for (int i = 0; i < raw; ++i)
      {  
      	for (int j = 0; j < col; ++j)
      		A.M[i][j] = M[i][j] - z.M[i][j];
      }
      return A;
   }

   matrix operator * ( matrix z)
   {
   	  matrix A(raw,z.col);
   	  if ( raw != z.col )
   	     {
   	     	cout << "ENTER correact order OF MATRIX ";
   	     	exit(0);
   	     }
   	  for (int i = 0; i < raw; ++i)
      {  
      	for (int j = 0; j < z.col; ++j)
      	{   
      		A.M[i][j] = 0;
      		for (int k = 0; k < raw ; ++k)
      		{
      		    A.M[i][j] = A.M[i][j] + M[i][k] * z.M[k][j];
      		}
      		
      	}
      }
      return A;
   }



   void input()
   {
      for (int i = 0; i < raw; ++i)
      {  
      	cout << " \n ENTER "<< i << " RAW :: \n";
      	for (int j = 0; j < col; ++j)
      		cin >> M[i][j];
      }
   }
   void output()
   {
   	  cout << "\n";
      for (int i = 0; i < raw; ++i)
      {  
      	cout << "\n";
      	for (int j = 0; j < col; ++j)
      		cout << M[i][j] << "\t" ;
      }
   }
};
int main()
{
	matrix x(3,3),y(3,3);
    x.input();
    x.output();
    y.input();
    y.output();
    y = x*y;
    y.output();
}