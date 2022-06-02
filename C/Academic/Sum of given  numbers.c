#include <stdio.h>

int main()
{
    int n,t,i;
    printf("Enter the value of n:");
    scanf("%d",&n);
    t=0;
    for(i=0;i<n;i++){
        int k;
        scanf("%d",&k);
        t=t+k;
    }
    printf("Sum of All numbers given is :%d",t);
    return 0;
}
