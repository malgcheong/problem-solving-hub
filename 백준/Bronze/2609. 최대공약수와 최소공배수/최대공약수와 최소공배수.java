import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){

            String text = br.readLine();
            int a = Integer.parseInt(text.split(" ")[0]);
            int b = Integer.parseInt(text.split(" ")[1]);
            int roop = a < b ? a : b;
            int divisor = 0;
            int multiple = 0;
            for (int i = 1; i <= roop; i++) {
                if (a % i == 0 && b % i == 0) {
                    divisor = i;
                }
            }
            multiple = a * b / divisor;
            StringBuilder sb = new StringBuilder();
            sb.append(divisor);
            sb.append("\n" + multiple);
            System.out.println(sb);
        } catch(IOException e) {
            e.printStackTrace();
        }
    }
}