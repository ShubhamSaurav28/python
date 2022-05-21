#include<iostream>
using namespace std;
int maxl(int a,int b,int c){
    char d;
    if(a>b){
        if(a>c)
        d='a';
        else
        d='c';
    }
    else{
        if(b>c)
        d='b';
        else
        d='c';
    }
    return d;
}
void py(int a,int b,int c){  //use of switch
    switch(maxl(a,b,c)){
        case 'a':
        if(b*b+c*c==a*a)
        cout<<"yes"<<endl;
        break;
        case 'b':
        if(a*a+c*c==b*b)
        cout<<"yes"<<endl;
        break;
        case 'c':
        if(b*b+a*a==c*c)
        cout<<"yes"<<endl;
        break;
        default:
        cout<<"no"<<endl;
    }
}

int main(){
int a,b,c;
cin>>a>>b>>c;
py(a,b,c);
return 0;
}