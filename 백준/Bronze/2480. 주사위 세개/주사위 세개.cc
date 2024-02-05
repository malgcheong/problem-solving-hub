#include <iostream>
using namespace std;

int main(){
    int a,b,c;
    cin >> a >> b >> c;
    if(a==b && a==c && b==c){
        cout << 10000 + a * 1000;
    } else if(a!=b && a!=c && b!=c){
        if(a > b){
            if(a > c){
                cout <<  a * 100;
            } else if(a < c){
                cout <<  c * 100;
            }
        } else if(a < b){
            if(b > c){
                cout <<  b * 100;
            } else if(b < c){
                cout <<  c * 100;
            }
        }
    } else if(a==b || a==c || b==c){
        if(a != b){
            if(a==c){
                cout <<  1000 + a * 100;
            } else if(b==c){
                cout <<  1000 + b * 100;
            }
        } else if(a == b){
            cout <<  1000 + a * 100;
        }
    }
}