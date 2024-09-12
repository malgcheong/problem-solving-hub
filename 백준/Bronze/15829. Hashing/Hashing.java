import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {

        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int n = Integer.parseInt(br.readLine());
            String text = br.readLine();
            int sum = 0;
            for (int i = 0; i < text.length(); i++) {
                sum += ((int)text.charAt(i)-96) * Math.pow(31, i);
            }
            if (sum >= 1234567891) {
                sum %= 1234567891;
            }
            System.out.println(sum);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}