#include<iostream>
using namespace std;
void fib(int n){
    int a,x=0,y=1;
    for(int i=1;i<=n;i++){
    cout<<x<<endl;
    a=x+y;
    x=y;
    y=a;
}
return;
}
int main(){
int n;
cin>>n;
fib(n);
return 0;
}