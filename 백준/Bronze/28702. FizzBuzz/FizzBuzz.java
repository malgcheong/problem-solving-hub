import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            String first = br.readLine();
            String twice = br.readLine();
            String third = br.readLine();
            int a = solution(first);
            int b = solution(twice);
            int c = solution(third);
            int d = 0;
            if(c > 0) {
                d = c+1;
            } else if(b > 0) {
                d = b+2;
            } else if (a > 0) {
                d = a+3;
            }

            if(d % 3 == 0 && d % 5 == 0){
                System.out.println("FizzBuzz");
            } else if (d % 3 == 0){
                System.out.println("Fizz");
            } else if (d % 5 == 0){
                System.out.println("Buzz");
            } else{
                System.out.println(d);
            }
        }catch(IOException e){
            e.printStackTrace();
        }
    }

    public static int solution(String text){
        int num = 0;
        if(text.equals("Fizz")){
            
        }
        else if(text.equals("Buzz")){
            
        }
        else if(text.equals("FizzBuzz")){
            
        } else {
            num = Integer.parseInt(text);
        }
        return num;
    }
}
