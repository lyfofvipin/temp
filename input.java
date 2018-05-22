import java.util.*;
public class input
{
    public static void main(String[] args) 
    {
        Scanner reading = new Scanner(System.in);
     System.out.println("Enter name : ");
       String nam = reading.next();
     System.out.println("Enter your class : ");
       int clas = reading.nextInt();
     System.out.println("Enter your roll : ");
       int roll = reading.nextInt();
     System.out.println("Enter your persantage : ");
       double marks = reading.nextDouble();
     System.out.println("name = "+nam+"  class ="+clas+"  roll-no = "+roll+"  marks = "+marks);
    }
}