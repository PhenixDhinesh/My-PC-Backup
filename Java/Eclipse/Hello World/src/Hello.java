import java.util.*;

public class Hello {

	public static void main(String[] args) {
		System.out.println("How are you");
		ArrayList li=new ArrayList();
		HashMap map=new HashMap();
		map.put("hi",1000);
		map.put(12,"hai");
		li.add("Hi");
		li.add(100);
		li.add(true);
		li.add('c');
		System.out.println(li+"\n"+map);
	}

}
