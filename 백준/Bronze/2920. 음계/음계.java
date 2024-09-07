import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            String inputText = br.readLine();
            String[] arr = inputText.split(" ");
            int[] intArr = new int[arr.length];

            for (int i = 0; i < arr.length; i++) {
                intArr[i] = Integer.parseInt(arr[i]);
            }

            boolean ascending = true;
            boolean descending = true;

            for (int i = 0; i < intArr.length - 1; i++) {
                if (intArr[i] < intArr[i + 1]) {
                    descending = false;
                } else if (intArr[i] > intArr[i + 1]) {
                    ascending = false;
                }
            }
            if (ascending) {
                System.out.println("ascending");
            } else if (descending) {
                System.out.println("descending");
            } else {
                System.out.println("mixed");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
