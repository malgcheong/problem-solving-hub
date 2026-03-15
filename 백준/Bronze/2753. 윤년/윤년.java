import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int inputCount = 1;
        int[] input = new int[inputCount];
        String line;
        for(int i = 0; i < inputCount; i++) {
            input[i] = Integer.parseInt(br.readLine());
        }


        Main T = new Main();
        System.out.println(T.solution(input));
    }

    public int solution(int[] arr) {
        StringBuilder sb = new StringBuilder();
        int year = arr[0];
        // 1 - 윤년, 0 - 윤년 아님
        // 윤년 조건: 4의 배수이면서 100의 배수가 아닐 때 또는 400의 배수일 때
        int flag = 0;
        if(year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)){
            flag = 1;
        }
        return flag;
    }
}
