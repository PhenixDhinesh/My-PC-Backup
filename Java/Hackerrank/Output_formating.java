import java.io.*;
import java.util.*;


public class Output_formating
{
	public static void main(String[] args) {
	  int k;
	  String[] aa;
		Scanner i=new Scanner(System.in);
		String a=i.nextLine();
		String b=i.nextLine();
		String c=i.nextLine();
		i.close();
		System.out.println("================================");
		aa=a.split(" ");
		System.out.print(aa[0]);
		for(k=0;k<(15-aa[0].length());k++){
		    System.out.print(" ");
		}for(k=0;k<(3-aa[1].length());k++){
		    System.out.print(0);
		}
		System.out.print(aa[1]);
		System.out.print("\n");

		aa=b.split(" ");
		System.out.print(aa[0]);
		for(k=0;k<(15-aa[0].length());k++){
		    System.out.print(" ");
		}for (k=0;k<(3-aa[1].length());k++){
		    System.out.print(0);
		}
		System.out.print(aa[1]);
		System.out.print("\n");

		aa=c.split(" ");
		System.out.print(aa[0]);
		for(k=0;k<(15-aa[0].length());k++){
		    System.out.print(" ");
		}for(k=0;k<(3-aa[1].length());k++){
		    System.out.print(0);
		}
		System.out.print(aa[1]);
		System.out.print("\n");
		System.out.println("================================");
	}
}
