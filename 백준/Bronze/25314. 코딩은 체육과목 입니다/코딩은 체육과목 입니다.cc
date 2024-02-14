#include <iostream>
using namespace std;

int main(void){
    int n;
    string output;
    cin >> n;
    for(int i = 0; i < n/4; i++){
        output += "long ";
    }
    output += "int";
    cout << output + "\n";
}