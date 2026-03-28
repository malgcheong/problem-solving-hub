import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static boolean[] primeArr = new boolean[10001];
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 0;
        if(n > 99) {
            count = 99;
        } else {
            count = n;
        }
        for(int i = 100; i <= n; i++) {
            if(isHansu(i)) count++;
        }
        System.out.println(count);
    }

    public static boolean isHansu(int num) {
        String numStr = String.valueOf(num);
        int a = Integer.parseInt(String.valueOf(numStr.charAt(0)));
        int b = Integer.parseInt(String.valueOf(numStr.charAt(1)));
        int c = Integer.parseInt(String.valueOf(numStr.charAt(2)));

        if(b-a == c-b) return true;
        else return false;
    }
}