import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int inputCount = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int count = 0;
        for(int i = 0; i < inputCount; i++) {
            int num = Integer.parseInt(st.nextToken());
            if(num == 1) continue;
            else if(num == 2 || num == 3) {
                count++;
                continue;
            }
            boolean factorFlag = false;
            double mid = Math.sqrt(num);
            for(int j = 2; j <= mid; j++){
                if(num % j == 0) {
                    factorFlag = true;
                    break;
                }
            }
            if(!factorFlag) {
                count++;
            }
        }
        System.out.println(count);
    }
}