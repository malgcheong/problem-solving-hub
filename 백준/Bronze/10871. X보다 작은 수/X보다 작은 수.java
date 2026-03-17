import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int inputCount = Integer.parseInt(st.nextToken());
        int comp = Integer.parseInt(st.nextToken());
        int [] problem = new int [inputCount];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < inputCount; i++) {
            problem[i] = Integer.parseInt(st.nextToken());
        }
        problem = Arrays.stream(problem)
                .filter(num -> num < comp )
                .toArray();
        StringBuilder sb = new StringBuilder();
        for(int p:problem){
            sb.append(p).append(" ");
        }
        System.out.println(sb.toString());
    }

}
