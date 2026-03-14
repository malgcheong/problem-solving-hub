import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int inputCount = 1;
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
        int score = arr[0];
        if (score >= 90 && score <= 100) {
            sb.append('A');
        } else if (score >= 80 && score <= 89) {
            sb.append('B');
        } else if (score >= 70 && score <= 79) {
            sb.append('C');
        } else if (score >= 60 && score <= 69) {
            sb.append('D');
        } else if (score >= 0 && score <= 59) {
            sb.append('F');
        } else {
            sb.append("시험 점수 범위에 어긋납니다.");
        }

        return sb.toString();
    }
}
