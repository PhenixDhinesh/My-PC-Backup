#include <stdio.h>

int main()
{
    int a,fact=1;
    printf("Enter the number for factorial : ");
    scanf("%d",&a);
    for (int i=2;i<=a;i++)fact*=i;
    printf("factorial of %d is : %d",a,fact);
    return 0;
}
