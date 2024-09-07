import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{

    public static void main(String[] args) {
        
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            int a = Integer.parseInt(br.readLine());
            int b = Integer.parseInt(br.readLine());
            int c = Integer.parseInt(br.readLine());
            System.out.println(a+b-c);
            System.out.println(Integer.parseInt(String.valueOf(a) + String.valueOf(b)) - c);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}