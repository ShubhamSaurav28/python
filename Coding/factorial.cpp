#include<iostream>
using namespace std;
int fact(int n){
    int a=1;
    for(int i=n;i>0;i--){
        a=a*i;
    }
    return a;
}
int main(){
int n;
cin>>n;
int a=fact(n);
cout<<a<<endl;
return 0;
}