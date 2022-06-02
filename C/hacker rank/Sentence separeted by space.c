#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
const int max=1000;

int main() {

    char sen[max];
    scanf("%[^\n]s",sen);
    for(int i=0;i<strlen(sen);i++){
        if(sen[i]==' '){
            printf("\n");
        }else{
            printf("%c",sen[i]);
        }
    }
    return 0;
}