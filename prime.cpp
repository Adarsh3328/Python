#include<iostream>
using namespace std;
int main(){
    int i=1,n;
    cout<<"eneter number"<<endl;
    cin>>n;
    while(i<=n){
        if(i==1){
            cout<<i<<"not prime"<<endl;
        }
        int x=2;
        while(x<i){
        if(i%x==0){
          cout<<i<<"not prime"<<endl;
          break;
          x=x+1;
        }}
        if(x==i){
            cout<<i<<"prime"<<endl;
        }
        i=i+1;
    }
    
    return 0;
    }
    