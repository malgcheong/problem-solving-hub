#include <stdio.h>

int main(void){
    int a, b;
    int c;
    scanf("%d %d", &a, &b);
    scanf("%d", &c);
    a += c / 60;
    b += c % 60;
    if(b > 59){
        a += 1;
        b -= 60;
    }
    if(a > 23){
        a -= 24;
    }
    printf("%d %d",a,b);
    return 0;
}