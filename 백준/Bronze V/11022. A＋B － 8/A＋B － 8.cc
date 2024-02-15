#include <iostream>
using namespace std;

int main(void){
    int t, a, b;
    cin.tie(NULL);
    cin >> t;
    for(int i = 0; i < t; i++){
        cin >> a >> b;
        cout << "Case #" << i+1 << ": " << a << " + " << b << " = " << a+b << "\n";
    }
}