#include<iostream>
using namespace std;
int fact(int n){
    int i,a=1;
    for(i=n;i>0;i--){
        a=a*i;
    }
    return a;
}
int nCr(int n,int r){
    return fact(n)/(fact(r)*fact(n-r));//instead of making a nCr function we can also directly 
}                                      //put fact(n)/(fact(r)*fact(n-r)) in the cout
int main(){
int n,r;
cin>>n>>r;;
cout<<nCr(n,r)<<endl;
return 0;
}