import java.io.*;
import java.util.*;

public class If_else {

    public static void main(String[] args) {
        Scanner i=new Scanner(System.in);
        int i1=i.nextInt();
        i.close();
        
        if(i1%2!=0 || i1%2==0 && i1>6 && i1<21){
            System.out.print("Weird");
        }else{
            System.out.print("Not Weird");
        }
    }
}