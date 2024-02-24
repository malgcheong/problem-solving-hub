#include <iostream>
using namespace std;

int main(){

    int n;
    int max, min;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++){
        cin >>  arr[i];
    }
    max = arr[0];
    min = arr[0];
    for(int i = 0; i < n; i++){
        if(i != n-1){
            if(max < arr[i+1]){
                max = arr[i+1];
            }
            if(min > arr[i+1]){
                min = arr[i+1];
            }
        }
    }
    cout << min << " " << max << "\n";
}