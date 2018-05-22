import java.util.Scanner;
class relactiona
{   
    int num,den;
    Scanner reading = new Scanner(System.in);
    public relactiona()
    {
        num = 0 ;
        den = 1 ;
    }
    public relactiona( int x , int y)
    {
        if ( y == 0 )
        {
            System.out.println("Enter Correct data.");
            System.exit(0);
        }
        num = x ;
        den = y ;
    }
        void input()
        {
            System.out.println("Enter value of num. :: ");
            num = reading.nextInt();
            System.out.println("Enter value of den. :: ");
            den = reading.nextInt();
        }
        void output()
        {
            System.out.println( num + "/" + den );
        }
        void munt( relactiona a,relactiona b )
        {
            num = a.num*b.num;
            den = a.den*b.den;
        }
}
public class complex extends relactiona
{
    int real,img;
    Scanner reading = new Scanner(System.in);
    public complex()
    {
        real = 0 ; img = 0;
    }
    public complex( int x , int y )
    {
        real = x ; img = y;
    }
    void output()
        {
            System.out.println( real + "+" + "i" + img );
            super.output();
        }
    void input()
        {
            super.input();
            System.out.println("Enter value of Real :: ");
            real = reading.nextInt();
            System.out.println("Enter value of Img. :: ");
            img = reading.nextInt();
        }
    public static void main( String [] args )
    {
        complex obj2 = new complex();
        obj2.input();
        obj2.output();
    }
}