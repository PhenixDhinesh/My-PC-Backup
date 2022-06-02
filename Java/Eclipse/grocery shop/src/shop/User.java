package shop;
import java.util.*;

public class User {
	Scanner in=new Scanner(System.in);
	private static LinkedHashMap<String,User> map=new LinkedHashMap<>();
	private String name,pass;
	private boolean vipuser=false;
	private int credits=0;
	void ini() {
		newuser("Hai","Hai");
	}
	String getName() {
		return this.name;
	}
	boolean getdetails(){
		System.out.println("Enter Your Name : ");
		name=in.nextLine();
		if(map.containsKey(name)) {
			System.out.println("Enter The Password : ");
			pass=in.nextLine();
			if(map.get(name).pass.equals(pass)) {
				return true;
			}else{
				System.out.println("Your Password is Wrong");
				return false;
			}
		}System.out.println("Your Name is not Registered");
		return false;
	}
	boolean newuser() {
		System.out.println("Enter your Name");
		name=in.nextLine();
		if(map.containsKey(name)) {
			return false;
		}
		System.out.println("Enter your password");
		pass=in.nextLine();
		newuser(name,pass);
		return true;
	}
	void newuser(String na,String pa) {
		User temp=new User();
		temp.pass=pa;
		map.put(na,temp);
	}
	boolean checkvip() {
		Shopmain shop=new Shopmain();
		String name=shop.getname();
		if(map.get(name).vipuser)
		    return true;
		return false;
	}
	int getcredit() {
		Shopmain shop=new Shopmain();
		String name=shop.getname();
		return map.get(name).credits;
	}
}
