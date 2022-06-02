#include <stdio.h>

int main()
{
    int n,i,j;
    scanf("%d",&n);
    for(i=0;i<n;i++){
            for(j=(-n)+1;j<n;j++){
                if(j<0 && i>=(-j)){
                    printf("%d",-j);
                }else if(j>=0 && i>=j){
                    printf("%d",j);
                }else{
                    printf(" ");
                }
            }printf("\n");
    }
    for(i=n-2;i>=0;i--){
            for(j=(-n)+1;j<n;j++){
                if(j<0 && i>=(-j)){
                    printf("%d",-j);
                }else if(j>=0 && i>=j){
                    printf("%d",j);
                }else{
                    printf(" ");
                }
            }printf("\n");
    }

    return 0;
}
