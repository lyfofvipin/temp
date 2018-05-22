class myex extends Exception
{  
    myex(String s)
    {  
         super(s);  
    }  
}  
public class Exepsion 
{       
      public static void main(String args[]){
        try
        {
                if ( 34 > 18 )
                    throw new myex("fuck off");
                else
                    System.out.println("welcome to vote");
        }
        catch(Exception m)
        {
            System.out.println("Exception occured: "+m);
        }
  
        System.out.println("rest of the code...");

}
}