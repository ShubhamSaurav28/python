#include<iostream>
#include<cmath>
using namespace std;
int main(){
int n,i;
bool t=0;
cin>>n;
for(i=2;i<=sqrt(n);i++){
    if(n%i==0){
        t=1;
        break;
    }
}
if(t==0)
cout<<n<<" is prime"<<endl;
else
cout<<n<<" is not prime"<<endl;

return 0;
}