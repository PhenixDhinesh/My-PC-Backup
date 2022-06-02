import java.io.*;
import java.util.*;

public class Java_substring {

    public static void main(String[] args) {
        String a;
        int b,c;
        Scanner in=new Scanner(System.in);
        a=in.nextLine();
        b=in.nextInt();
        c=in.nextInt();
        System.out.println(a.substring(b,c));
    }
}
