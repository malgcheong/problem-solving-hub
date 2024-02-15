#include <iostream>
using namespace std;

int main(void){
    int t;
    string star = "";
    cin >> t;
    for(int i = 0; i < t; i++){
        star += "*";
        cout << star << "\n";
    }
}