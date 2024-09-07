import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++){
            String answer = "";
            int h = scanner.nextInt();
            int w = scanner.nextInt();
            int n = scanner.nextInt();
            int divide = ((n-1) / h) + 1;
            int rest = n % h;
            if ( rest == 0) {
                rest = h;
            }
            answer += rest;
            if (divide < 10) {
                answer += "0";
            }
            if (divide > w) {
                divide = w;
            }
            answer += divide;
            System.out.println(answer);
        }

    }
}