#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int arr[10];
    float arr2[10];
    float count = 0;

    for(int i = 0; i < 10; i++){
        cin >> arr[i];
        arr[i] %= 42;
    }

    for(int i = 0; i < 10; i++){
        int cnt = 1;
        for(int j = 0; j < 10; j++){
            if(i == j) continue;
            if(arr[i] == arr[j]){
                cnt++;
            }
        }
        if(cnt > 1){
            arr2[i] = (float) 1 / cnt;
        } else if(cnt == 1){
            arr2[i] = (float) cnt;
        }
        count += arr2[i];
    }

    cout << count;
}