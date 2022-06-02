import java.io.*;
import java.util.*;

public class Java_string_token {
    public static void main(String[] args) {
        int count=0;
        Scanner sc=new Scanner(System.in);
        String A=sc.nextLine();
        String[] a=A.split("[^a-zA-Z]");
        for(String i:a)if(i.length()>0)count+=1;
        System.out.println(count);
        for(String i:a)if(i.length()>0)System.out.println(i);
    }
}
