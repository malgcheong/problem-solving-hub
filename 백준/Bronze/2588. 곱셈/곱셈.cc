#include <stdio.h>

int main(void){
    int a,b;
    scanf("%d %d",&a, &b);
 
    int c = a * (b % 10);
    int d = a * ((b % 100) / 10);
    int e = a * (b / 100);

    printf("%d\n", c);
    printf("%d\n", d);
    printf("%d\n", e);
    printf("%d\n", c + (d*10) + (e*100));

    return 0;
}