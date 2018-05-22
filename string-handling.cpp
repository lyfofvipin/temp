#include<iostream>
#include <string.h>
using namespace std;
class stri
{
	char *s;
public:
	stri()
	{
		s = new char[0];
		s[0] = 0;
	}
	stri( char a[])
	{
		s = new char[ strlen(a) + 1];
		strcpy(s,a);
	}
	stri ( stri &a)
	{
		s = new char[ strlen(a.s) + 1];
		strcpy(s,a.s);
	}
	~stri()
	{
		delete [] s;
	}
	stri operator + ( stri a )
    {
    	s = strcat(s,a.s);
    	return *this ;
    }
    stri operator = ( stri a )
    {
    	strcpy(s,a.s);
    	return *this;
    }
    bool operator < ( stri a )
    {   
        int x;
    	x = strcmp(s,a.s);
    	if ( x < 0 )
    	  return true;
    	else
    	  return false;
    }
    bool operator > ( stri a )
    {   
        int x;
    	x = strcmp(s,a.s);
    	if ( x > 0 )
    	   return true;
    	else
    	   return false;
    }
    bool operator == ( stri a )
    {   
        int x;
    	x = strcmp(s,a.s);
    	if ( x == 0 )
    	   return true;
    	else
    	   return false;
    }
    bool operator != ( stri a )
    {   
        int x;
    	x = strcmp(s,a.s);
    	if ( x != 0 )
    	  return true;
    	else
    	  return false;
    }
	void input()
	{   
		cout << "Enter how many latters u have ";
		int n;
		cin >> n;
		s = new char [n+1];
		cout << " \n Enter a strin :: " ;
		cin >> s;
	}
	void output()
	{
		cout << s <<"\n";
	}
    
};
main()
{
	stri str,str1;
	str.input();
	str1.input();
	if( str < str1 )
	   cout << " \n STR is less then STR1 ";

	if( str > str1 )
	   cout << " \n STR is > then STR1 ";

	if( str == str1 )
	   cout << " \n STR is == then STR1 ";

	if( str != str1 )
	   cout << " \n STR is != then STR1 ";
}