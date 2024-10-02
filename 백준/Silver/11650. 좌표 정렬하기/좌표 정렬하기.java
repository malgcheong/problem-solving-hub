import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args){

        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int n = Integer.parseInt(br.readLine());
            int[][] arr = new int[n][2];
            for (int i = 0; i < n; i++){
                String[] input = br.readLine().split(" ");
                arr[i][0] = Integer.parseInt(input[0]);
                arr[i][1] = Integer.parseInt(input[1]);
            }
            Arrays.sort(arr, new Comparator<int[]>(){
                @Override
                public int compare(int[] a, int[] b){
                    if(a[0] == b[0]) {
                        return a[1] - b[1];
                    }
                    else {
                        return a[0] - b[0];
                    }
                }
            });

            for(int i = 0; i < n; i++) {
                System.out.println(arr[i][0] + " " + arr[i][1]);
            }

        }catch(IOException e){
            e.printStackTrace();
        }
    }
}