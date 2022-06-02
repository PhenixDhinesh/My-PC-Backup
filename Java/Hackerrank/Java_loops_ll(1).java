import java.io.*;
import java.util.*;

public class Java_loops_ll(1)
{
    public static void main(String[] args) {
        int q,a,b,n,j,i,temp;
        Scanner in=new Scanner(System.in);
        q=in.nextInt();
        for(j=0;j<q;j++){
            a=in.nextInt();b=in.nextInt();n=in.nextInt();
            temp=a+b;
            System.out.print(temp);
            for(i=1;i<n;i++){
                temp+=(Math.pow(2,i)*b);
                System.out.print(" "+temp);
            }System.out.println();
       }
    }
}
