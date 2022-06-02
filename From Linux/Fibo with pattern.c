#include <stdio.h>

// int fibo(int a){
//     if(a==1)return 0;
//     if(a==2)return 1;
//     if(a>2){
//         int t1=0,t2=1,c;
//         for(int i=2;i<a;i++){
//             c=t1+t2;
//             t1=t2;
//             t2=c;
//         }return c;
//     }
// }

int main()
{
    int k=1,i,size;
    int t1=0,t2=1,c;
    scanf("%d",&size);
    for(i=1;i<=size;i++){
        if(i%2==1)printf("%d ",k*k*k);
        else{
            printf("%d ",t1);
            c=t1+t2;
            t1=t2;
            t2=c;
            // printf("%d",fibo(k));
            k++;
        }
    }
}
