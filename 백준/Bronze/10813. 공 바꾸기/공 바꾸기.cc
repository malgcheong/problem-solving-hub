#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n,m;
    cin >> n >> m;
    int arr[100];
    int a,b,temp;
    for(int i = 0; i < n; i++){
        arr[i] = i+1;
    }
    for(int i = 0; i < m; i++){
        cin >> a >> b;
        temp = arr[a-1];
        arr[a-1] = arr[b-1];
        arr[b-1] = temp;
    }
    for(int i = 0; i < n; i++){
        cout << arr[i] << " ";
    }
}