import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Main {
    static boolean isip(String i){
        boolean o=Pattern.matches("\\d{1,3}.\\d{1,3}.\\d{1,3}.\\d{1,3}",i);
        if(o) for(String p : i.split("\\.")) if(Integer.parseInt(p)>255) return false;
        return o;
    }

    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        while(in.hasNextLine()){
            System.out.println(isip(in.nextLine()));
        }
    }
}