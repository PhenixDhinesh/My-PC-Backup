package shop;
import java.util.*;

public class Admin {
	final String pass="HELLO";
	Scanner in=new Scanner(System.in);
	Admin(){
		System.out.println("Enter the Admin Password : ");
		String temp =in.next();
		if(temp.equals(pass)) {
			Items item=new Items();
			item.newitem("Cookey",30,1);
		}else {
			System.out.println("Your Admin Password is wrong");
		}
	}
}
