import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static boolean[] primeArr = new boolean[10001];
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int inputCount = Integer.parseInt(br.readLine());
        Arrays.fill(primeArr, true);
        for(int i = 2; i <= 10000; i++) {
            if(isPrime(i)){
                for(int j = i*2; j < primeArr.length; j+=i){
                    primeArr[j] = false;
                }
            } else {
                primeArr[i] = false;
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < inputCount; i++) {
            int num = Integer.parseInt(br.readLine());
            sb.append(findAnswer(num));
        }
        System.out.println(sb.toString());
    }

    public static boolean isPrime(int i) {
        if(i == 2 || i == 3) return true;
        for(int j = 2; j <= Math.sqrt(i); j++) {
            if(i % j == 0) return false;
        }
        return true;
    }

    public static String findAnswer(int num) {
        for(int j = num/2; j > 1; j--) {
            if(primeArr[j]){
                for(int k = j; k < num; k++){
                    if(primeArr[k]){
                        if(j + k == num) {
                            return j + " " + k + "\n";
                        }
                    }
                }
            }
        }
        return "";
    }
}