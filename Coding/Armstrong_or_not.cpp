#include<iostream>
#include<cmath>
using namespace std;
int main(){
int n,a,c=0,b,d;
cin>>n;
d=n;
b=log10(n)+1;
while(n>0){
    a=n%10;
    c=c+pow(a,b);
    n=n/10;
}
if(c==d)
cout<<d<<" is a armstrong number";
else 
cout<<d<<" is not a armstrong number";
return 0;
}