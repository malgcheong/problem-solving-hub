import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int inputCount = 1;
        int[] input = new int[inputCount];
        int n = Integer.parseInt(br.readLine());
        input[0] = n;

        Main T = new Main();
        System.out.println(T.solution(input));
    }

    public String solution(int[] arr) {
        StringBuilder sb = new StringBuilder();
        int n = arr[0];
        sb.append(n).append(" * 1 = ").append(n*1).append(System.lineSeparator());
        sb.append(n).append(" * 2 = ").append(n*2).append(System.lineSeparator());
        sb.append(n).append(" * 3 = ").append(n*3).append(System.lineSeparator());
        sb.append(n).append(" * 4 = ").append(n*4).append(System.lineSeparator());
        sb.append(n).append(" * 5 = ").append(n*5).append(System.lineSeparator());
        sb.append(n).append(" * 6 = ").append(n*6).append(System.lineSeparator());
        sb.append(n).append(" * 7 = ").append(n*7).append(System.lineSeparator());
        sb.append(n).append(" * 8 = ").append(n*8).append(System.lineSeparator());
        sb.append(n).append(" * 9 = ").append(n*9).append(System.lineSeparator());
        return sb.toString();
    }
}
