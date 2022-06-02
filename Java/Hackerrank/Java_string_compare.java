import java.io.*;
import java.util.*;

public class Java_string_compare {

    public static void main(String[] args) {
        String a;
        List<String> aa=new ArrayList<>();
        int b,i;
        Scanner in=new Scanner(System.in);
        a=in.nextLine();
        b=in.nextInt();
        for(i=0;i<=a.length()-b;i++){
            aa.add(a.substring(i,i+b));
        }Collections.sort(aa);
        System.out.println(aa.get(0)+"\n"+aa.get(aa.size()-1));
    }
}
