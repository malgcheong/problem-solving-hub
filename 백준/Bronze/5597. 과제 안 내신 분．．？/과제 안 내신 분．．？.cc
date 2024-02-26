#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int arr[31] = {0, };
    int index;
    for(int i = 0; i < 28; i++){
         cin >> index;
         arr[index] = 1;
    }

    for(int i = 1; i < 31; i++){
        if(arr[i] == 0){
            cout << i << "\n";
        }
    }
    
}