#include <stdio.h>

int main() {

  int n, i,n1=0,n2=1,temp;
  printf("Enter a positive integer more than 1: ");
  scanf("%d", &n);
  printf("%d,%d,",n1,n2);
  for(i=3;i<=n;i++){
      temp=n1+n2;
      printf("%d,",temp);
      n1=n2;
      n2=temp;
  }
  return 0;
}