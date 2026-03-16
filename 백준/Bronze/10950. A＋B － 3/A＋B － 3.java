import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int inputCount = Integer.parseInt(br.readLine());
        int[] input = new int[inputCount * 2];
        for(int i = 0; i < inputCount; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            input[i*2] = Integer.parseInt(st.nextToken());
            input[i*2+1] = Integer.parseInt(st.nextToken());
        }

        Main T = new Main();
        System.out.println(T.solution(input));
    }

    public String solution(int[] arr) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < arr.length / 2; i++) {
            sb.append(arr[i*2] + arr[i*2+1]).append(System.lineSeparator());
        }
        return sb.toString();
    }
}
