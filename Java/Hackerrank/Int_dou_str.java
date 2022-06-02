import java.io.*;
import java.util.*;

public class Int_dou_str {

    public static void main(String[] args) {
        Scanner i=new Scanner(System.in);
        int a=i.nextInt();
        double b=i.nextDouble();
        i.nextLine();
        String c=i.nextLine();
        i.close();
        
        System.out.print("String: "+c+"\n"+"Double: "+b+"\n"+"Int: "+a);
    }
}