import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        s = s.toLowerCase();
        char[] alpabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        int[] answer = new int[26];

        for (int i = 0; i < alpabet.length; i++) {
            answer[i] = -2;
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == alpabet[i]){
                    answer[i] = j;
                    break;
                }
            }
            if (answer[i] == -2) {
                answer[i] = -1;
            }
        }

        for (int i = 0; i < answer.length; i++) {
            System.out.print(answer[i] + " ");
        }

        scanner.close();
    }
}
