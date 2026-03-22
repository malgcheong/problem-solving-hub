import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int[] arr = new int[2];
        int n = 0;
        while(st.hasMoreTokens()){
            String num = st.nextToken();
            String newNum = String.valueOf(num.charAt(2))+
                            String.valueOf(num.charAt(1))+
                            String.valueOf(num.charAt(0));
            arr[n++] = Integer.parseInt(newNum);
        }
        if(arr[0] > arr[1]){
            System.out.println(arr[0]);
        } else {
            System.out.println(arr[1]);
        }
    }
}