#include <stdio.h>
#define max 100
int main()
{
    int a[max];
    int n,i,s,f,k,j;
    printf("enter the size of the arr:");
    scanf("%d",&n);
    printf("enter the elements of arr:");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    printf("Enter the element to search:");
    scanf("%d",&s);
    for (i=0;i<n;i++){
        if(a[i]==s){
            f=1;
            break;
        }
    }
    if(f==1){
        printf("%d is found on position : %d\n",s,i+1);
    }
    else{
        printf("element is not found\n");
    }
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++){
            if(a[i]>a[j]){
                k=a[i];
                a[i]=a[j];
                a[j]=k;
            }
            
        }
        
    }
    printf("Here is sorted list of arr:\n");
    for(i=0;i<n;i++){
        printf("%d",a[i]);
    }
    
    return 0;
}
