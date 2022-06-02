import java.io.*;
import java.util.*;

public class Java_string {

    public static void main(String[] args) {
        String a,b,c;
        Scanner in=new Scanner(System.in);
        a=in.next();
        b=in.next();
        System.out.println((a+b).length());
        String result = (a.compareTo(b)>0) ? "Yes":"No";
        System.out.println(result);
        c=a.substring(0,1).toUpperCase()+a.substring(1)+" "+b.substring(0,1).toUpperCase()+b.substring(1);
        System.out.println(c);
    }
}
