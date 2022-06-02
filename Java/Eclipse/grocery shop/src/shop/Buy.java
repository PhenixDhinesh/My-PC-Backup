package shop;
import java.util.*;

public class Buy {
	private LinkedHashMap<Integer,Integer> listofitems=new LinkedHashMap<>();
	Scanner in=new Scanner(System.in);
	final int vipusercredit=100;
	private Items item=new Items();
	private int product,quantity;boolean guest=false;
	private LinkedHashMap<Integer,Items> totallist=item.getMap();
	void ini(){
		item.ini();
		item.display();
		System.out.println("Enter the product No and Quatity to buy. Like This  \"1(candy) 5(Quantity)\" ");
		System.out.println("Get 5% discount on Purches more than 20,000");
		System.out.println("click any Key to start buying");
		if(in.hasNextLine())getitems();
	}
	void setGuest(boolean i) {
		this.guest=i;
	}
	void getitems() {
		System.out.println("Enter 0 to stop Buying\n");
		while(true){
			product=in.nextInt();
			if(product==0)break;
			quantity=in.nextInt();
			in.nextLine();
			if(quantity==0) {
				continue;
			}
			listofitems.put(product,quantity);
		}
		System.out.println("\n1.Continue buying\n2.Start Billing");
		int temp=in.nextInt();
		if(temp==1) {
			getitems();
		}else bill();
	}
	void bill() {
		int totalprice=0,totalquantity=0,counter=1;
		User user=new User();
		if(user.checkvip()) {
			System.out.println("Your are a VIP user");
		}else {
			System.out.println("Get "+(vipusercredit-user.getcredit())+" more credits to become VIP user");
		}
		System.out.println("------------------------------------------------------");
		System.out.printf("%1s%11s%11s%10s\n","No.","Product","Quantity","Price");
		System.out.println("------------------------------------------------------");
		for(Integer i:listofitems.keySet()) {
			System.out.printf("%1s%13s%9s%11s\n",counter,totallist.get(i).pname,listofitems.get(i),(totallist.get(i).pprice)*listofitems.get(i));
			totalprice+=(totallist.get(i).pprice)*listofitems.get(i);
			totalquantity+=listofitems.get(i);
			counter++;
		}
		System.out.println("------------------------------------------------------");
		System.out.printf("%1s%18s%11s\n","Total",totalquantity,totalprice);
		System.out.println("------------------------------------------------------");
		System.out.println("\nHave a nice and safe journey, Lets Meet again!!!\n:)");
	}
}
