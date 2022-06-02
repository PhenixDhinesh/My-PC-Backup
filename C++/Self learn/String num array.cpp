#include <iostream>
using namespace std;
int conv_to_num(string a){
    int temp=0,temp1,i=0;
    do{
        temp1=a[i]-'0';
        temp*=10;
        temp+=temp1;
        i++;
    }while(((int)a[i]-48<0 || (int)a[i]-48>9)==0);
    return temp;
}
int main()
{
    int size;
    cin>>size;
    string a[size]={};
    int b[size]={},temp;
    for(int i=0;i<5;i++){
        cin>>a[i];
        b[i]=conv_to_num(a[i]);
    }
    for(int i=0;i<5;i++){
        for(int j=i+1;j<5;j++){
            if(b[i]>b[j]){
                temp=b[i];
                b[i]=b[j];
                b[j]=temp;
            }
        }
    }
    cout<<"Min of the array : "<<b[0];
    return 0;
}