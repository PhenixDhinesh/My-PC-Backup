#include <stdio.h>

int main()
{
    int a[]={-1,-2,-3,-4},n=4,max=a[0],sum;
    for(int i=0;i<n;i++){
        sum=0;
        for(int j=i;j<n;j++)sum+=a[j];
        if(sum>max)max=sum;
    }
    printf("%d",max);
    return 0;
}
