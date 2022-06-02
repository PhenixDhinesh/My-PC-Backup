#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void calculate_the_maximum(int n, int k) {
// here
    int a=0,o=0,x=0;
  for(int i=1;i<n;i++){
      for(int j=i+1;j<=n;j++){
          int k1,k2,k3;
          k1=i&j;
          k2=i|j;
          k3=i^j;
          if(k1<k && k1>a){a=k1;}
          if(k2<k && k2>o){o=k2;} 
          if(k3<k && k3>x){x=k3;}          
      }
  }
  printf("%d\n%d\n%d",a,o,x);
// here
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}