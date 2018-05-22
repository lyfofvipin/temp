import java.util.Scanner;
public class relactional
{   
    int num,den;
    Scanner reading = new Scanner(System.in);
    public relactional()
    {
        num = 0 ;
        den = 1 ;
    }
    public relactional( int x , int y)
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
        void munt( relactional a,relactional b )
        {
            num = a.num*b.num;
            den = a.den*b.den;
        }
    public static void main( String [] args )
    {
        relactional a = new relactional();
        relactional b = new relactional();
        relactional c = new relactional();
        a.input();
        b.input();
        c.munt(a,b);
        c.output();
    }
}