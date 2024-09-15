import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {

        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {

            int T = Integer.parseInt(br.readLine());
            for(int i = 0; i < T; i++) {
                int k = Integer.parseInt(br.readLine());
                int n = Integer.parseInt(br.readLine());
                solution(k,n);
            }
        } catch(IOException e) {
            e.printStackTrace();
        }
    }

    public static void solution(int k, int n){
        int[][] arr = new int[k+1][n+1];

        for (int i = 1; i <= n; i++) {
            arr[0][i] = i;
        }
        for (int i = 1; i <= k; i++) {
            for (int j = 1; j <= n; j++) {
                arr[i][j] += arr[i][j-1] + arr[i-1][j];
            }
        }
        System.out.println(arr[k][n]);
    }
}