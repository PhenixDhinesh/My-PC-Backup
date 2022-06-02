#include <stdio.h>

int main()
{
    int size,i,j,k;
    scanf("%d",&size);
    for(i=0;i<size;i++,printf("\n")){
        for(j=0;j<i*size-1;j++)printf(" ");
        for(k=0;k<size;k++)printf("*");
    }
    for(i=size-1;i>=0;i--,printf("\n")){
        for(j=0;j<i*size-1;j++)printf(" ");
        for(k=0;k<size;k++)printf("*");
    }
    return 0;
}
