#include <stdio.h>

int main()
{
    int a,b,c;
    printf("Enter the number A,B,C;");
    scanf("%d%d%d",&a,&b,&c);
    if (a>=b && a>=c){
        printf("%d is the largest Numebr",a);
    }
    if (b>=a && b>=c){
        printf("%d is the largest Numebr",b);
    }
    if (c>=a && c>=b){
        printf("%d is the largest Numebr",c);
    }

    return 0;
}
