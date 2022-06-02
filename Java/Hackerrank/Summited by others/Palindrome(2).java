import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String a=sc.next();
 
        StringBuilder input1 = new StringBuilder();
        input1.append(a);
        String b=input1.reverse().toString();
        if(a.equals(b)) System.out.println("Yes");
        else System.out.println("No");
    }
}