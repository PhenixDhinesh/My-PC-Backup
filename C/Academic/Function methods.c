#include <stdio.h>
void primes(int a,int b);
int isprime(int num);
int main()
{
    int a,b;
    printf("Enter two numbers :");
    scanf("%d%d",&a,&b);
    printf("Greatest Numeber of these : %d\n",max(a,b));
    swap(&a,&b);
    printf("swap of these two numbers : a=%d,b=%d \n",a,b);
    if(a>b){
        swap(&a,&b);
    }
    printf("Prime numbers from %d to %d :\n",a,b);
    primes(a,b);
    
    
    
    return 0;
}
int max(int num1,int num2){
    if(num1>num2){
        return num1;
    }
    else{
        return num2;
    }
}
void swap(int *a,int *b){
    int temp;
    temp=*a;
    *a=*b;
    *b=temp;
    return;
}
void primes(int a,int b){
    while(a<=b){
        if(isprime(a)){
            printf("%d\n",a);
        }
        a++;
    }
    return;
}
int isprime(int num){
    int i;
    for (i=2;i<num/2;i++){
        if(num%i==0){
            return 0;
        }
    }
    return 1;
}