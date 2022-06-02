import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        try{
            String s=Integer.toString(n);
            System.out.println("Good job");
        }
        catch (Exception e){
            System.out.println("Wrong answer");
        }
    }
}
