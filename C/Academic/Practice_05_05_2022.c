#include <stdio.h>
#include <stdlib.h>
void main()
{
    int i,j,k,size;
    scanf("%d",&size);
    printf("===========================\n");
    // Top of the piramid (Filled)

    for(i=0;i<size;i++,printf("\n")){
      for(j=(-size)+1;j<size;j++){
        if(j<0 && i>=(-j) || j>=0 && i>=j){
          printf("%d",abs(j));
        }else{
          printf(" ");
        }
      }
    }printf("===========================\n");
    // Bottom of the piramid(Filled)

    for(i=size-1;i>=0;i--,printf("\n")){
      for(j=(-size)+1;j<size;j++){
        if(j<0 && i>=(-j) || j>=0 && i>=j){
          printf("%d",abs(j));
        }else{
          printf(" ");
        }
      }
    }printf("===========================\n");
    // Full piramid(Filled)

    for(i=0;i<size;i++,printf("\n")){
      for(j=(-size)+1;j<size;j++){
        if(j<0 && i>=(-j) || j>=0 && i>=j){
          printf("%d",abs(j));
        }else{
          printf(" ");
        }
      }
    }
    for(i=size-2;i>=0;i--,printf("\n")){
      for(j=(-size)+1;j<size;j++){
        if(j<0 && i>=(-j) || j>=0 && i>=j){
          printf("%d",abs(j));
        }else{
          printf(" ");
        }
      }
    }printf("===========================\n");
    // Top of piramid(Not Filled)

    for(i=0;i<size;i++,printf("\n")){
      for(j=(-size)+1;j<size;j++){
        if(i==size-1 || j<0 && i==(-j) || j>=0 && i==j){
          printf("%d",abs(j));
        }else{
          printf(" ");
        }
      }
    }printf("===========================\n");
    // Bottom of the piramid(Not Filled)

    for(i=size-1;i>=0;i--,printf("\n")){
      for(j=(-size)+1;j<size;j++){
        if(i==size-1 || j<0 && i==(-j) || j>=0 && i==j){
          printf("%d",abs(j));
        }else{
          printf(" ");
        }
      }
    }printf("===========================\n");
    // Full piramid(Not Filled)

    for(i=0;i<size;i++,printf("\n")){
      for(j=(-size)+1;j<size;j++){
        if(j<0 && i==(-j) || j>=0 && i==j){
          printf("%d",abs(j));
        }else{
          printf(" ");
        }
      }
    }
    for(i=size-2;i>=0;i--,printf("\n")){
      for(j=(-size)+1;j<size;j++){
        if(i==size-1 || j<0 && i==(-j) || j>=0 && i==j){
          printf("%d",abs(j));
        }else{
          printf(" ");
        }
      }
    }printf("===========================\n");
    k=65;
    for(i=0;i<size;i++,printf("\n")){
      for(j=0;j<=i;j++){
        printf("%c",k+i);
      }
    }printf("===========================\n");
    k=65;
    for(i=0;i<size;i++,printf("\n")){
      for(j=0;j<=i;j++){
        printf("%c",k+j);
      }
    }printf("===========================\n");
    k=65;
    int temp=0;
    for(i=0;i<size;i++,printf("\n")){
      for(j=0;j<=i;j++){
        printf("%c",(k+temp++));
      }
    }
}
