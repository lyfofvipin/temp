import java.awt.*;
import java.applet.*;
public class inputinapp extends Applet
{
		TextField t1, t2;
		public void init()
        {
                t1 = new TextField(10);
                t2 = new TextField(10);

                add(t1);
                add(t2);

                t1.setText("0");
                t2.setText("0");
        }
        public void paint(Graphics g)
        {
                int a=0,b=0,c=0;
                String str1,str2,str;

                g.drawString("Enter the number in each box",10,50);

                        str1=t1.getText();
                        a=Integer.parseInt(str1);

                        str2=t2.getText();
                        b=Integer.parseInt(str2);
                c=a+b;

                str=String.valueOf(c);

                g.drawString("Sum is",10,15);
                g.drawString(str,100,75);
        }
}
