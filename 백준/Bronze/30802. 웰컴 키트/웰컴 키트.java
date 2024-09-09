import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{

    public static void main(String[] args) {

        int n = 0, t = 0, p = 0;
        Integer[] arr = null;
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            n = Integer.parseInt(br.readLine());
            String[] strArr = br.readLine().split(" ");
            arr = new Integer[strArr.length];
            for(int i = 0; i < strArr.length; i++){
                arr[i] = Integer.parseInt(strArr[i]);
            }
            strArr = br.readLine().split(" ");
            t = Integer.parseInt(strArr[0]);
            p = Integer.parseInt(strArr[1]);
        } catch (IOException e) {
            e.printStackTrace();
        }

        int count = 0;
        for (int i = 0; i < arr.length; i++){
            count += arr[i] % t == 0 ? arr[i] / t : (arr[i] / t) + 1;
        }
        System.out.println(count);
        System.out.println(n/p + " " + n%p);
    }
}