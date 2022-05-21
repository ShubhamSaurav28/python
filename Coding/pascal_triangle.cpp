#include<iostream>
using namespace std;
int fact(int a){
    int i,x=1;
    for(i=a;i>0;i--){
        x=x*i;
    }
    return x;
}
int nCr(int n,int r){
    return fact(n)/(fact(r)*fact(n-r));
}
int main(){
int n,i,j;
cin>>n;
for(i=0;i<=n;i++){
    for(j=0;j<=i;j++){
        cout<<" "<<nCr(i,j);
    }
    cout<<endl;
}
return 0;
}