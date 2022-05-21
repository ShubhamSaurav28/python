#include<iostream>
#include<cmath>
using namespace std;
int main(){
int a,b,i,j;
bool t=1;
cin>>a>>b;
for(i=a;i<=b;i++){
    for(j=2;j<=sqrt(i);j++){
        if(i%j==0){
            t=0;
            break;
        }
        
    }
    if(t==1)
    cout<<i<<endl;
    t=1;

}
return 0;
}