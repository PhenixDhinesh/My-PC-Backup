import java.io.*;
import java.util.*;

public class Anagrams {

    public static void main(String[] args) {
        int i,j,flag=0;
        Scanner in=new Scanner(System.in);
        String a=in.nextLine();
        String b=in.nextLine();
        if(a.length()!=b.length()){
            System.out.println("Not Anagrams");
        }else if(a.equalsIgnoreCase(b))System.out.println("Anagrams");
        else{
            for(i=0;i<a.length();i++){
                Character temp=Character.toUpperCase(a.charAt(i));
                int a_counter=0;
                int b_counter=0;
                for(j=0;j<a.length();j++){
                    if(Character.toUpperCase(a.charAt(j))==temp)a_counter+=1;
                    if(Character.toUpperCase(b.charAt(j))==temp)b_counter+=1;
                }
                if(a_counter!=b_counter){
                    flag=1;
                    break;
                }
            }
            System.out.println(flag==0 ? "Anagrams" : "Not Anagrams");
        }
    }
}