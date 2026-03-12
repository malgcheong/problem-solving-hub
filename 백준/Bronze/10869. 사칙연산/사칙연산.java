import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] input = new int[2];
        int i = 0;
        while(st.hasMoreTokens()){
            int num = Integer.parseInt(st.nextToken());
            input[i++] = num;
        }

        Main T = new Main();
        System.out.println(T.solution(input));
    }

    public String solution(int[] arr) {
        StringBuilder sb = new StringBuilder();
        int a = arr[0], b = arr[1];
        sb.append(a+b).append(System.lineSeparator());
        sb.append(a-b).append(System.lineSeparator());
        sb.append(a*b).append(System.lineSeparator());
        sb.append(a/b).append(System.lineSeparator());
        sb.append(a%b).append(System.lineSeparator());
        return sb.toString();
    }
}
