#include<iostream>
using namespace std;
int maxl(int a,int b,int c){
    int d;
    if(a>b){
        if(a>c)
        d=a;
        else
        d=c;
    }
    else{
        if(b>c)
        d=b;
        else
        d=c;
    }
    return d;
}
void py(int a,int b,int c){  // can also use switch
    if(a==maxl(a,b,c)){
        if(b*b+c*c==a*a)
        cout<<"yes"<<endl;
    }
    else if(b==maxl(a,b,c)){
        if(a*a+c*c==b*b)
        cout<<"yes"<<endl;
    }
    else if(c==maxl(a,b,c)){
        if(b*b+a*a==c*c)
        cout<<"yes"<<endl;
    }
    else
        cout<<"no"<<endl;
}
int main(){
int a,b,c;
cin>>a>>b>>c;
py(a,b,c);
return 0;
}