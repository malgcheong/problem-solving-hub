import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int inputCount = 2;
        int[] input = new int[inputCount];
        String line;
        for(int i = 0; i < inputCount; i++) {
            input[i] = Integer.parseInt(br.readLine());
        }


        Main T = new Main();
        System.out.println(T.solution(input));
    }

    public String solution(int[] arr) {
        StringBuilder sb = new StringBuilder();
        int a = arr[0], b = arr[1];
        int b1 = b / 100;
        int b2 = (b - b1*100) / 10;
        int b3 = (b - b1*100 - b2*10) / 1;
        sb.append(a * b3).append(System.lineSeparator());
        sb.append(a * b2).append(System.lineSeparator());
        sb.append(a * b1).append(System.lineSeparator());
        sb.append(a * b).append(System.lineSeparator());
        return sb.toString();
    }
}
