#include <stdio.h>
int feb(num);

int main()
{
    int i,n;
    printf("Enter the number:\n");
    scanf("%d,",&n);
    for(i=0;i<n;i++){
        printf("%d",feb(i));
    }
    return 0;
}
int feb(num){
    if(num==0 || num==1){
        return num;
    }else{
        return feb(num-1)+feb(num-2);
    }
}