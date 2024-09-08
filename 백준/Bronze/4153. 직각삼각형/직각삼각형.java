import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            String line;
            while((line = br.readLine()) != null){
                if (line.equals("0 0 0")){
                    break;
                }
                
                String[] arr = line.split(" ");
                int[] sides = new int[3];
                sides[0] = Integer.parseInt(arr[0]);
                sides[1] = Integer.parseInt(arr[1]);
                sides[2] = Integer.parseInt(arr[2]);

                Arrays.sort(sides);

                if (sides[2] * sides[2] == sides[0] * sides[0] + sides[1] * sides[1]) {
                    System.out.println("right");
                } else {
                    System.out.println("wrong");
                }
            }
        } catch(IOException e) {
            e.printStackTrace();
        }
    }
}
