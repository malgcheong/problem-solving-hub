import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int inputCount = Integer.parseInt(br.readLine());
        for (int i = 0; i < inputCount; i++) {
            String input = br.readLine();
            int score = 0;
            int result = 0;
            for(char c : input.toCharArray()){
                switch (c) {
                    case 'O':
                        result += ++score;
                        break;
                    case 'X':
                        score = 0;
                        break;
                }
            }
            System.out.println(result);
        }
    }
}