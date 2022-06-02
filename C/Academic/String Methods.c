#include <stdio.h>
#include<string.h>

int main()
{
    char name[20];
    char name1[20];
    char name2[20];
    printf("Enter your name:");
    scanf("%s",name);
    strcpy(name1,name);
    printf("Your name is : %s\n",name);
    printf("size of your Name :%zu\n",strlen(name));
    printf("Here is copy of your name:%s\n",name1);
    printf("Enter your Friend name:");
    scanf("%s",name2);
    printf("Difference between You & your Frnd's Name:%d\n",strcmp(name1,name2));
    printf("Here is you & Your Frnd name :%s\n",strcat(name1,name2));
    return 0;
}
