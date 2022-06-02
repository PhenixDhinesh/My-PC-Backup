#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
    char a[1000];
    int n,i,j;
    scanf("%[^\n]s",a);
    n=strlen(a);
    for(i=1;i<=n;i++){
        for(j=0;j<n;j++){
            if(j==i-1 || j==n-i){
                printf("%c",a[j]);
            }else{printf(" ");}
        }printf("\n");
    }
    
    return 0;
}
