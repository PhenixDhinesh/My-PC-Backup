#include <stdio.h>
const int max=1000;

int main() {
    int a[max],s,sum=0,j;
    scanf("%d",&s);
    for(int i=0;i<s;i++){
        scanf("%d",&j);
        sum+=j;
    }
    printf("%d",sum);
    return 0;
}