import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {

        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){

            int N = Integer.parseInt(br.readLine());
            int[][] arr = new int[N][2];
            for (int i = 0; i < N; i++){
                String[] text = br.readLine().split(" ");
                arr[i][0] = Integer.parseInt(text[0]);
                arr[i][1] = Integer.parseInt(text[1]);
            }
            Arrays.sort(arr, new Comparator<int[]>() {
                @Override
                public int compare(int[] a, int[] b){
                    if (a[1] == b[1]) {
                        return a[0] - b[0];
                    } else {
                        return a[1] - b[1];
                    }
                }
            });
            for(int i = 0; i < arr.length; i++){
                System.out.println(arr[i][0] + " " + arr[i][1]);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}