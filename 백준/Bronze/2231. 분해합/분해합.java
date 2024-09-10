import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {

        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int n = Integer.parseInt(br.readLine());
            int answer = 0;
            for (int i = 0; i < n; i++) {
                answer += i;
                String text = "" + i;
                String[] arr = text.split("");
                for (int j = 0; j < arr.length; j++){
                    int num = Integer.parseInt(arr[j]);
                    answer += num;
                }
                if (answer == n) {
                    answer = Integer.parseInt(text);
                    break;
                }
                answer = 0;
            }
            System.out.println(answer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}