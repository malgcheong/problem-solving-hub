import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Map;
import java.util.TreeMap;

public class Main {
	public static void main(String[] args) {
		try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
			Map<Integer, Integer> treeMap = new TreeMap<>();
			int N = Integer.parseInt(br.readLine());
			String[] input = br.readLine().split(" ");
			
			for (int i = 0; i < N; i++) {
				int num = Integer.parseInt(input[i]); // 미리 변수로 추출
				treeMap.compute(num, (key, val) -> val == null ? 1 : val + 1);
			}
			
			int M = Integer.parseInt(br.readLine());
			input = br.readLine().split(" ");
			
			StringBuilder sb = new StringBuilder(); // 출력 최적화
			for (int i = 0; i < M; i++) {
				int queryNum = Integer.parseInt(input[i]); // 미리 변수로 추출
				int answer = treeMap.getOrDefault(queryNum, 0); // getOrDefault를 사용하여 null 처리
				sb.append(answer).append(" ");
			}
			System.out.print(sb.toString().trim()); // StringBuilder 사용
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
