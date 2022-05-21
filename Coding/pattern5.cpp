#include<iostream>
using namespace std;
int main(){
int n;
cin>>n;
int i,j;
for(i=n;i>=1;i--){
    for(j=1;j<=i-1;j++){
        cout<<" ";
    }
    for(j=1;j<=n;j++){
        cout<<"*";
    }
    cout<<endl;
}
return 0;
}