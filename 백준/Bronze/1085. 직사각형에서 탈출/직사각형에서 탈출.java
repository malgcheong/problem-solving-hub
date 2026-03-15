import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int inputCount = 4;
        int[] input = new int[inputCount];
        String line = br.readLine();
        StringTokenizer st = new StringTokenizer(line);
        int i = 0;
        while(st.hasMoreTokens()) {
            input[i++] = Integer.parseInt(st.nextToken());
        }

        Main T = new Main();
        System.out.println(T.solution(input));
    }

    public int solution(int[] arr) {
        StringBuilder sb = new StringBuilder();
        int x = arr[0];
        int y = arr[1];
        int w = arr[2];
        int h = arr[3];

        int sol = Integer.min(Integer.min(h-y,y), Integer.min(w-x, x));

        return sol;
    }
}
