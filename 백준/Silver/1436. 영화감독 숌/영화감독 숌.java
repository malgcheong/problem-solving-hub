import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) {
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int n = Integer.parseInt(br.readLine());
            int answer = 0;
            while(true){
                if(n == 0){
                    break;
                }
                answer++;
                if(String.valueOf(answer).contains("666")){
                    n--;
                }
            }
            System.out.println(answer);
        } catch(IOException e){
            e.printStackTrace();
        }
    }
}