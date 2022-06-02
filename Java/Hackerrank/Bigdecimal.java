import java.util.*;

public class Main
{
	public static void main(String[] args) {
		HashMap<Integer,HashMap<String,Float>> o=new HashMap<>();
		ArrayList<Float> p=new ArrayList<Float>();
		Scanner in=new Scanner(System.in);
		int size=Integer.parseInt(in.nextLine());
		for(int i=0;i<size;i++){
		    String temp=in.nextLine();
		    HashMap<String,Float> temp_hash=new HashMap<String,Float>();
		    temp_hash.put(temp,Float.parseFloat(temp));
		    o.put(i,temp_hash);
		    p.add(Float.parseFloat(temp));
		}Collections.sort(p,Collections.reverseOrder());
		for(float i:p){
		    for(int k:o.keySet()){
		        int flag=0;
		        for(String j : o.get(k).keySet()){
		            if(o.get(k).get(j)==i){
		                System.out.println(j);
		                o.remove(k);
		                flag=1;
		            }
		        }if(flag==1) break;
		    }
		}
	}
}
