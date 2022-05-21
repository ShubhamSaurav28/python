#include <stdio.h>//find a word in a string
#include <stdlib.h>
int main(){
    char a[100],b[100];
    int i,j,k,l=1,m;
    printf("Enter the string\n");
    gets(a);
    printf("Enter the word you want to find\n");
    gets(b);
    for(i=0;a[i];i++)
    {
        if(a[i]==b[j])
        {
            k=i;
            m=i;
            for(j=0;j<strlen(b)-1;j++)
            {
                if(a[k]==b[j])
                l++;
                j++;        jkadshh
                k++;
            }
        }
    }
    if(l==strlen(b))
    printf("a[%d]",m)
return 0;
}