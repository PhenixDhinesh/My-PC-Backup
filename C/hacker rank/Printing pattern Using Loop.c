#include <stdio.h>
const int max=100;

int main()
{
    int s,ss,arr[max],a[max][max];
    scanf("%d",&s);
    ss=(s*2)-1;
    for(int i=0;i<s;i++){
        arr[i]=i+1;
    }
    for(int i=s-1;i>=0;i--){
        for(int j=s-1;j>=0;j--){
            if(arr[i]<=j){
                a[i][j]=j+1;
            }else{
                a[i][j]=i+1;
            }
        }
    }
    for(int i=s-1;i>=0;i--){
        for(int j=s-1;j>=0;j--){
            printf("%d ",a[i][j]);
        }for(int k=1;k<s;k++){
            printf("%d ",a[i][k]);
        }
        printf("\n");
    }
    for(int i=1;i<s;i++){
        for(int j=s-1;j>=0;j--){
            printf("%d ",a[i][j]);
        }for(int k=1;k<s;k++){
            printf("%d ",a[i][k]);
        }
        printf("\n");
 }
    return 0;
}
