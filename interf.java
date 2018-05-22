interface interfa
{
   void print();
}
public class interf implements interfa
{
   public void print()
    {
        System.out.print("It's interface \n");
    }
public static void main(String[] args) 
{
    interf v = new interf();
    v.print();
}
}