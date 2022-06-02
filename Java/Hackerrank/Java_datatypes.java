import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        for(int k=0;k<n;k++){
            try{
                long i=in.nextLong();
                if(i>=-128 && i<=127){
                    System.out.print(i+" can be fitted in:\n* byte\n* short\n* int\n* long");
                }else if(i>=-32768 && i<=32767){
                    System.out.print(i+" can be fitted in:\n* short\n* int\n* long");
                }else if(i>=-2147483648 && i<=2147483647){
                    System.out.print(i+" can be fitted in:\n* int\n* long");
                }else{
                    System.out.print(i+" can be fitted in:\n* long");
                }System.out.println();
            }
            catch(Exception e){
                System.out.println(in.next()+" can't be fitted anywhere.");
            }
        }
    }
}
