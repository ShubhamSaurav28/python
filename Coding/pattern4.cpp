#include<iostream>
using namespace std;
int main(){
int n;
cin>>n;
int i,j,k;
for(i=1;i<=n;i++){
    for(j=1,k=i;j<=i;j++,k++){
        cout<<k%2<<" ";
    }
    cout<<endl;
}
return 0;
}