import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) {
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int N = Integer.parseInt(br.readLine());
            // N = 11
            int quotient = N / 5;
            int answer = -1;
            for (int i = quotient; i >= 0; i--){
                int remainder = N - i * 5;
                if (remainder % 3 == 0) {
                    answer = remainder / 3 + i;
                    break;
                } else {
                    continue;
                }
            }
            System.out.println(answer);
        } catch(IOException e){
            e.printStackTrace();
        }
    }
}