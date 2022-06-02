#include <stdio.h>

int main(){
    int size,i,j,k;
    scanf("%d",&size);
    printf("=======================\n");
    // For right Cross
    for(i=0;i<size;i++,printf("\n")){
        for(j=0;j<size;j++){
            if(i==j){
                printf("*");
            }else{
                printf(" ");
            }
        }
    }printf("=======================\n");
    // For left Cross
    for(i=0;i<size;i++,printf("\n")){
        for(j=size-1;j>=0;j--){
            if(i==j){
                printf("*");
            }else{
                printf(" ");
            }
        }
    }printf("=======================\n");
    // For X pattern
    for(i=1;i<=size;i++,printf("\n")){
        for(j=0;j<size;j++){
            if(i-1==j || j==size-i){
                printf("*");
            }else{
                printf(" ");
            }
        }
    }printf("=======================\n");
    // For Triple Space Pattern
    for(i=1;i<=size;i++,printf("\n")){
        printf("   ");
        for(j=0;j<i;j++){
            printf("*");
        }
    }printf("=======================\n");
    // For Changing logic
    for(i=0;i<size;i++,printf("\n")){
        for(j=size-1;j>=0;j--){
            if(i>=j){printf("*");}
            else printf(" ");
        }
    }printf("=======================\n");
    // For Changing Logic [Box pattern]
    for(i=0;i<size;i++,printf("\n")){
        if(i==0 || i==size-1){
            for(j=0;j<size;j++)printf("* ");
        }else{
            for(j=0;j<size;j++){
                if(j==0 || j==size-1){
                    printf("* ");
                }else printf("  ");
            }
        }
    }printf("=======================\n");
}