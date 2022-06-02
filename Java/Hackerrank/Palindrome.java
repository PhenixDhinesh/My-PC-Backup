import java.io.*;
import java.util.*;

public class palindrome {
    public static void main(String[] args) {
        int i,flag=0;
        Scanner in = new Scanner(System.in);
        String a=in.nextLine();
        for(i=0;i<a.length();i++){
            if(a.charAt(i)!=a.charAt(a.length()-i-1)){
                flag=1;
                break;
            }
        }System.out.println(flag==1 ? "No" : "Yes");
    }
}