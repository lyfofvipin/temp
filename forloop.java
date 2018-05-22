public class forloop
{
    public static void main(String[] args) 
    {
        int i;
        for( i = 1 ; i <= 30 ; i++ )
        {
            if( i % 3 == 0 )
                System.out.print( i + "\n");
        }
        System.out.print("\n\n\n");
        i = 1;
        while( i <= 50 )
        {
            if( i % 5 == 0 )
                System.out.print( i + "\n");
            i++;
        }
        System.out.print("\n\n\n");
        i = 1;
        do
        { 
            if ( i % 6 == 0 )
            System.out.print( i + "\n");
            i++;
        }while( i <= 60 );
    }
}