import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {

        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {

            String text = br.readLine();

            int n = Integer.parseInt(text.split(" ")[0]);
            int k = Integer.parseInt(text.split(" ")[1]);

            int n_factorial = 1;
            int nk_factorial = 1;
            int k_factorial = 1;

            for (int i = 1; i <= n; i++) {
                n_factorial *= i;
            }
            for (int i = 1; i <= n-k; i++) {
                nk_factorial *= i;
            }
            for (int i = 1; i <= k; i++) {
                k_factorial *= i;
            }

            // System.out.println(n_factorial);
            // System.out.println(nk_factorial);
            // System.out.println(k_factorial);

            System.out.println(n_factorial / nk_factorial / k_factorial);

        } catch(IOException e) {
            e.printStackTrace();
        }
    }
}