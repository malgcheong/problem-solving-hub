import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String a = scanner.nextLine();
        String[] arr = a.split(" ");
        int answer = 0;
        for (int i = 0; i < arr.length; i++){
            int num = Integer.parseInt(arr[i]);
            num = num * Integer.parseInt(arr[i]);
            answer += num;
        }
        System.out.println(answer%10);
    }
}