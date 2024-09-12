import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {

        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            int n = Integer.parseInt(br.readLine());
            String text = br.readLine();
            long sum = 0;
            long pow = 1; 
            for (int i = 0; i < text.length(); i++) {
                sum += (text.charAt(i)-96) * pow;
                pow = pow * 31 % 1234567891;
            }
            System.out.println(sum % 1234567891);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}