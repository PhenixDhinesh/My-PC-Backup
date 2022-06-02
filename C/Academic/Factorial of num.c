#include <stdio.h>

int main()
{
    int n,t,i;
    printf("Enter the Value to be factorialized:");
    scanf("%d",&n);
    t=1;
    for(i=1;i<=n;i++){
        t=t*i;
    }
    printf("Factorial of number given is :%d",t);
    return 0;
}
