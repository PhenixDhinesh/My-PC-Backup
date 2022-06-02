#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int find_nth_term(int n, int a, int b, int c) {
// here
    int sum=a+b+c;
    if(n>0){
        n-=n;
        find_nth_term(n,b,c,sum);
    }
    return sum;
// here
}


int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}