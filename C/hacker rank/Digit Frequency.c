#include <stdio.h>
#include <string.h>
const int max=1000;

int main()
{
    int ans[11]={0,0,0,0,0,0,0,0,0,0},tes[11]={0,1,2,3,4,5,6,7,8,9};
    char sen[max];
    scanf("%[^\n]s",sen);
    for(int i=0;i<strlen(sen);i++){
        for(int j=0;j<10;j++){
            if((sen[i] - '0')==tes[j]){
                ans[j]+=1;
            }
        }
    }
    for(int i=0;i<10;i++){
        printf("%d ",ans[i]);
    }
    

    return 0;
}
