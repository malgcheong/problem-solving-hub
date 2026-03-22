import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] answer = {0,0,0,0,0,0,0,0,0,0};
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());
        String result = String.valueOf(a*b*c);
        for(int i = 0; i < result.length(); i++) {
            char num = result.charAt(i);
            switch(num){
                case '0':
                    answer[0]++;
                    break;
                case '1':
                    answer[1]++;
                    break;
                case '2':
                    answer[2]++;
                    break;
                case '3':
                    answer[3]++;
                    break;
                case '4':
                    answer[4]++;
                    break;
                case '5':
                    answer[5]++;
                    break;
                case '6':
                    answer[6]++;
                    break;
                case '7':
                    answer[7]++;
                    break;
                case '8':
                    answer[8]++;
                    break;
                case '9':
                    answer[9]++;
                    break;
            }
        }
        for(int ans:answer){
            System.out.println(ans);
        }
    }
}