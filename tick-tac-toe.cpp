#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<cstdlib>
#define sz  20
#define sk  60
using namespace std;

int A[sz][sk];

int f[10];

void BOARD_ine()
{
   for( int j = 0 ; j < 10 ; j++ )
       f[j] = ' ';
   for ( int j = 0 ; j < sk ; j++)
       A[6][j] = '-';
   for ( int j = 0 ; j < sk ; j++)
       A[13][j] = '-';
   for ( int j = 0 ; j < sz ; j++)
       A[j][21] = '|';
   for ( int j = 0 ; j < sz ; j++)
       A[j][42] = '|';

}

void DISPLAY()
{
       A[2][8] = f[0],A[2][30] = f[1],A[2][48] = f[2];
       A[10][8] = f[3],A[10][30] = f[4],A[10][48] = f[5];
       A[18][8] = f[6],A[18][30] = f[7],A[18][48] = f[8];
   for( int j = 0 ; j < sz ; j++ )
   {
     cout << endl;
     for( int k = 0 ; k < sk ; k++ )
        printf("%c",A[j][k]);
   }
}
bool notin ()
{
    for( int j = 0 ; j <= 8 ; j++ )
    {
        if ( f[j] == ' ' )
            return false;
    }
        return true;
}
void logic( int a)
{
    int pos;
	if (a % 2 == 0)
    {
		cout << " \n ::::::  PLAYER 2   ::::::   ";
		cout << "\nPlease Enter the posiction from ' 1 - 9 ' :: ";
		cin >> pos;
		pos--;
		f[pos] = 'X';
    }
	else
    {
		cout << " \n ::::::  PLAYER 1   ::::::   ";
		cout << " \nPlease Enter the posiction from ' 1 - 9 ' :: ";
		cin >> pos;
		pos--;
		f[pos] = 'O';
    }
    cout << f;
}
void won()
{
	if ( f[0] == 'X' && f[1] == 'X' && f[2] == 'X' || f[3] == 'X' && f[4] == 'X' && f[5] == 'X' ||f[6] == 'X' && f[7] == 'X' && f[8] == 'X'||f[0] == 'X' && f[4] == 'X' && f[8] == 'X' ||f[2] == 'X' && f[4] == 'X' && f[6] == 'X' || f[0] == 'X' && f[3] == 'X' && f[6] == 'X' ||f[1] == 'X' && f[4] == 'X' && f[7] == 'X' ||f[2] == 'X' && f[5] == 'X' && f[8] == 'X' )
		{
           cout<< "The game is over  :: \n\n    PLAYER 2 IS WINNER ";
		   DISPLAY();
		   exit(0);
		}
	else if ( f[0] == 'O' && f[1] == 'O' && f[2] == 'O' || f[3] == 'O' && f[4] == 'O' && f[5] == 'O' ||f[6] == 'O' && f[7] == 'O' && f[8] == 'O'||f[0] == 'O' && f[4] == 'O' && f[8] == 'O' ||f[2] == 'O' && f[4] == 'O' && f[6] == 'O' || f[0] == 'O' && f[3] == 'O' && f[6] == 'O' ||f[1] == 'O' && f[4] == 'O' && f[7] == 'O' ||f[2] == 'O' && f[5] == 'O' && f[8] == 'O' )
		{
		    cout<< "The game is over  :: \n\n    PLAYER 1 IS WINNER ";
		   DISPLAY();
		   exit(0);
		}
	else if (notin())
	    cout << "\n\n\n :::::::::::::  THE MATCH IS DROW  ::::::::::::::::: \n\n\n" ;
}

main()
{
  cout << "\n\n\nTHE SIMPLE RULE OF GAME PLAYER 1 HAS SYMBOL   ' O  ' AND\n\n PLAYER 2 HAS    SYMBOL    'X' " ;
  cout << "\n\n\nCHOSE THE POSICTION IN THE BORD :) \n\n\n" ;
  cout << "Let us Begen our game :====) \n\n\n\n";
  BOARD_ine();
  for( int j = 0 ; j < 10 ; j++ )
  {
	DISPLAY();
	logic(j);
	system("cls");
	won();
  }
}
