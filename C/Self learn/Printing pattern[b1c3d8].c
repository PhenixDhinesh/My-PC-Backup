#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
    char a[1000],b;
    int i=0,temp=0,temp1,j,n;
    scanf("%[^\n]s",a);
    n=strlen(a);
    while(i<n){
        if ((int)a[i]-48<0 || (int)a[i]-48>9){
            b=a[i];
            temp=0;
            i++;
        }else{
            do{
                temp1=a[i]-'0';
                temp*=10;
                temp+=temp1;
                i++;
            }while(((int)a[i]-48<0 || (int)a[i]-48>9)==0);
        }
        for(j=0;j<temp;j++)printf("%c",b);
    }
    return 0;
}
