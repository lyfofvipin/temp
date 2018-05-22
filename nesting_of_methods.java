import java.util.Scanner;
class realact
{   
    int num,den;
    Scanner reading = new Scanner(System.in);
    public realact()
    {
        num = 0 ;
        den = 1 ;
    }
    public realact( int x , int y)
    {   
        if ( y == 0 )
        {
            System.out.println("Enter Correct data.");
            System.exit(0);
        }
        num = x ;
        den = y ;
    }
        void inputnum()
        {
            System.out.println("Enter value of num. :: ");
            num = reading.nextInt();
        }
        void inputden()
        {   
            inputnum();
            System.out.println("Enter value of den. :: ");
            den = reading.nextInt();
        }
        void input()
        {
            inputden();
        }
        void output()
        {
            System.out.println( num + "/" + den );
        }
        void munt( realact a,realact b )
        {
            num = a.num*b.num;
            den = a.den*b.den;
        }
}
public class nesting_of_methods extends realact
{
    int real,img;
    Scanner reading = new Scanner(System.in);
    public nesting_of_methods()
    {
        real = 0 ; img = 0;
    }
    public nesting_of_methods( int x , int y )
    {
        real = x ; img = y;
    }
    void output()
        {
            System.out.println( real + "+" + "i" + img );
            super.output();
        }
    void inputreal()
        {
            super.input();
            System.out.println("Enter value of Real :: ");
            real = reading.nextInt();
        }
    void inputimg()
    {
            inputreal();
            System.out.println("Enter value of Img. :: ");
            img = reading.nextInt();
    }
    void input()
    {
        inputimg();
    }
    public static void main( String [] args )
    {
        nesting_of_methods obj2 = new nesting_of_methods();
        obj2.input();
        obj2.output();
    }
}