import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

    public static void main (String[] args) {

        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            while(true) {
                String text = br.readLine();
                if (text.equals("0")) {
                    break;
                }
                String result = "yes";
                for (int i = 0; i < text.length()/2; i++) {
                    if (text.charAt(i) != text.charAt(text.length() - 1 - i)) {
                        result = "no";
                        break;
                    }
                }
                System.out.println(result);
            }


        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}