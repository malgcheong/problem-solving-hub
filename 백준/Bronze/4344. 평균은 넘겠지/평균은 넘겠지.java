import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int inputCount = Integer.parseInt(br.readLine());

        for (int i = 0; i < inputCount; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int totalScore = 0;
            int[] arr = new int[n];
            while(st.hasMoreTokens()) {
                int score = Integer.parseInt(st.nextToken());
                totalScore += score;
                arr[--n] = score;
            }
            float avg = (float) totalScore/arr.length;
            int hi = 0;
            for(int a : arr) {
                if(a > avg) {
                    hi++;
                }
            }
            float answer = (float) hi/arr.length * 100;
            sb.append(String.format("%.3f%%", answer)).append(System.lineSeparator());
        }
        System.out.println(sb.toString());
    }
}