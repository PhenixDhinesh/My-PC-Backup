import java.util.*;

public class Practice_05_05_2022{
  public static void main(String[] args){
    int i,j,k,size;
    Scanner in=new Scanner(System.in);
    size=in.nextInt();
    in.close();
    System.out.println("===========================");
    // Top of the piramid (Filled)

    for(i=0;i<size;i++,System.out.println()){
      for(j=(-size)+1;j<size;j++){
        if(j<0 && i>=(-j) || j>=0 && i>=j){
          System.out.print(Math.abs(j));
        }else{
          System.out.print(" ");
        }
      }
    }System.out.println("===========================");
    // Bottom of the piramid(Filled)

    for(i=size-1;i>=0;i--,System.out.println()){
      for(j=(-size)+1;j<size;j++){
        if(j<0 && i>=(-j) || j>=0 && i>=j){
          System.out.print(Math.abs(j));
        }else{
          System.out.print(" ");
        }
      }
    }System.out.println("===========================");
    // Full piramid(Filled)

    for(i=0;i<size;i++,System.out.println()){
      for(j=(-size)+1;j<size;j++){
        if(j<0 && i>=(-j) || j>=0 && i>=j){
          System.out.print(Math.abs(j));
        }else{
          System.out.print(" ");
        }
      }
    }
    for(i=size-2;i>=0;i--,System.out.println()){
      for(j=(-size)+1;j<size;j++){
        if(j<0 && i>=(-j) || j>=0 && i>=j){
          System.out.print(Math.abs(j));
        }else{
          System.out.print(" ");
        }
      }
    }System.out.println("===========================");
    // Top of piramid(Not Filled)

    for(i=0;i<size;i++,System.out.println()){
      for(j=(-size)+1;j<size;j++){
        if(i==size-1 || j<0 && i==(-j) || j>=0 && i==j){
          System.out.print(Math.abs(j));
        }else{
          System.out.print(" ");
        }
      }
    }System.out.println("===========================");
    // Bottom of the piramid(Not Filled)

    for(i=size-1;i>=0;i--,System.out.println()){
      for(j=(-size)+1;j<size;j++){
        if(i==size-1 || j<0 && i==(-j) || j>=0 && i==j){
          System.out.print(Math.abs(j));
        }else{
          System.out.print(" ");
        }
      }
    }System.out.println("===========================");
    // Full piramid(Not Filled)

    for(i=0;i<size;i++,System.out.println()){
      for(j=(-size)+1;j<size;j++){
        if(j<0 && i==(-j) || j>=0 && i==j){
          System.out.print(Math.abs(j));
        }else{
          System.out.print(" ");
        }
      }
    }
    for(i=size-2;i>=0;i--,System.out.println()){
      for(j=(-size)+1;j<size;j++){
        if(i==size-1 || j<0 && i==(-j) || j>=0 && i==j){
          System.out.print(Math.abs(j));
        }else{
          System.out.print(" ");
        }
      }
    }System.out.println("===========================");
    // ABCD methods
    k=65;
    for(i=0;i<size;i++,System.out.println()){
      for(j=0;j<size;j++){
        if(j<=i){System.out.print((char)(k+i));}
      }
    }System.out.println("===========================");
    k=65;
    for(i=0;i<size;i++,System.out.println()){
      for(j=0;j<size;j++){
        if(j<=i){System.out.print((char)(k+j));}
      }
    }System.out.println("===========================");
    k=65;
    int temp=0;
    for(i=0;i<size;i++,System.out.println()){
      for(j=0;j<size;j++){
        if(j<=i){
          System.out.print((char)(k+temp++));
        }
      }
    }
  }
}
