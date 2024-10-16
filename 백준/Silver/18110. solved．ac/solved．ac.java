import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;



public class Main{
    public static void main(String[] args) {
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];
            float excludeRatio = N * 0.15f;
            int excludePeople = Math.round(excludeRatio);
            for (int i = 0; i < N; i++){
                arr[i] = Integer.parseInt(br.readLine());
            }
            Arrays.sort(arr);
            int sum = 0;
            for (int i = excludePeople; i < N - excludePeople; i++){
                sum += arr[i];
            }
            System.out.println(Math.round((float)sum/(N-(excludePeople*2))));

        } catch(IOException e){
            e.printStackTrace();
        }
    }
}