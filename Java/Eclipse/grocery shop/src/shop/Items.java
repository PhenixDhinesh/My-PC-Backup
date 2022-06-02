package shop;
import java.util.*;
public class Items {
	Scanner in=new Scanner(System.in);
	private static LinkedHashMap<Integer,Items> map=new LinkedHashMap<>();
	protected String pname;
	protected int pprice;
	protected int credits;
	
	void ini() {
		if(map.size()!=0)return;
		newitem("candy",10,1);
		newitem("cake",100,5);
	    newitem("Icecream",50,2);
	}
	void newitem(String name,int price,int credit) {
		Items temp=new Items();
		temp.pname=name;
		temp.pprice=price;
		temp.credits=credit;
		map.put(map.size()+1, temp);
	}
	void display() {
		System.out.println("------------------------------------------------------");
		System.out.printf("%1s%12s%10s%10s\n","No.","Product","Price","Credit");
		System.out.println("------------------------------------------------------");
		for(Integer i:map.keySet()) {
			System.out.printf("%1s%13s%10s%10s\n",i,map.get(i).pname,map.get(i).pprice,map.get(i).credits);
		}System.out.println("------------------------------------------------------");
	}
	LinkedHashMap<Integer,Items> getMap(){
		return map;
	}
}
