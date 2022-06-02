import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Main
{
    static void isvalid(String k){
        if(Pattern.matches("^[a-zA-Z][\\w]{7,29}",k)){
            System.out.println("Valid");
        }else System.out.println("Invalid");
    }
    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int size =Integer.parseInt(in.nextLine());
        for(int i=0;i<size;i++){
            isvalid(in.nextLine());
        }
    }
}
