import java.io.*;
import java.util.*;

public class Java_loops_ll
{
    static int[] str_int(String[] i){
        int j;
        int[] temp=new int[i.length];
        for(j=0;j<i.length;j++){
	           temp[j] =Integer.parseInt(i[j]);
	    }return temp;
    }
	public static void main(String[] args) {
	    int i,size,j;String temp;
	    Scanner in=new Scanner(System.in);
	    size=in.nextInt();
	    int[][] li=new int[size][];
	    in.nextLine();
	    for(i=0;i<size;i++){
	        temp=in.nextLine();
	        String[] tempstr=new String[(temp.length()/2)+1];
	        tempstr=temp.split(" ");
	        li[i]=str_int(tempstr);
	    }
	    
	    
	    
	    for(i=0;i<li.length;i++){
	        int te=li[i][0]+li[i][1];
	        System.out.print(te);
	        for(int ii=1;ii<li[i][2];ii++){
	            te+=(Math.pow(2,ii)*li[i][1]);
	            System.out.print(" "+te);
		    }System.out.println();
	    }
	}
}
