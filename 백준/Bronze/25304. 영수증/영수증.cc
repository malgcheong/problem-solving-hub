#include <iostream>
using namespace std;

int main(void){
    int a, n, x, p, b=0;
    cin >> a >> n;
    for(int i = 1; i <= n; i++){
        cin >> x >> p;
        b+=x*p;
    }
    if(a == b){
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
}