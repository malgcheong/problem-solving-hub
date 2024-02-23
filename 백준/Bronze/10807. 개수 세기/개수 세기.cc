#include <iostream>
using namespace std;

int main(){
    int n,x,v,count = 0;
    cin >> n;
    int arr[n];
    
    // 배열 생성
    for(int i = 0; i < n; i++){
        cin >> x;
        arr[i] = x;
    }

    // 주어진 v가 배열에서 몇개인지 출력
    cin >> v;
   for(int i = 0; i < n; i++){
        if(arr[i] == v){
            count += 1;
        }
    }
    cout << count << "\n";

}