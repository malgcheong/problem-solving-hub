import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) {
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int n = Integer.parseInt(br.readLine());
            int[][] arr = new int[n][2];
            int[] answer = new int[n];
            for(int i = 0; i < n; i++){
                String[] a = br.readLine().split(" ");
                arr[i][0] = Integer.parseInt(a[0]);
                arr[i][1] = Integer.parseInt(a[1]);
            }
            while(n != 0){
                int count = 1;
                int weight = arr[n-1][0];
                int height = arr[n-1][1];
                for(int i = 0; i < arr.length; i++){
                    if (weight < arr[i][0] && height < arr[i][1]){
                        count++;
                    }
                }
                answer[n-1] = count;
                n--;
            }
            
            for(int i = 0; i < answer.length; i++){
                System.out.print(answer[i]+" ");
            }
        } catch(IOException e){
            e.printStackTrace();
        }
    }
}