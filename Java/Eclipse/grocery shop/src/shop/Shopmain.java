package shop;
import java.util.*;

public class Shopmain {
	
	static String name;
	String getname() {
		return name;
	}
	public static void main(String[] args) {
		Shopmain m=new Shopmain();
		System.out.println("Hello Everyone\nWelcome DSK Shop");
		Scanner in=new Scanner(System.in);
		int templog;
		do {
			System.out.println("1.Admin\n2.Login\n3.Sign up\n4.Guest user\n5.Exit\n");
			templog=in.nextInt();
			User user=new User();
			if(templog==1) {
				Admin ad=new Admin();
			}if(templog==2) {
				user.ini();
				if(user.getdetails()) {
					Shopmain main=new Shopmain();
					name=user.getName();
					System.out.println("Welcome back "+name+"!!");
					Buy buy=new Buy();
					buy.ini();
				}else {
					System.out.println("Register As new user or Use as Guest User");
				}		
			}
			if(templog==3) {
				if(user.newuser()) {
					name=user.getName();
					System.out.println("you Have Successfully Registerd "+name+"!!");
					Buy buy=new Buy();
					buy.ini();
				}else {
					System.out.println("User is Already Exists, go through login page");
				}
			}
			if(templog==4) {
				Buy buy=new Buy();
				buy.setGuest(true);
				buy.ini();
			}
		}while(templog!=5);
	}

}
