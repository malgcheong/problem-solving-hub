import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
	public static int binarySearch(int[] arr, int target, int left, int right){
		if (right < left) return 0; 
		int mid = (right + left) / 2;
		if(arr[mid] < target){
			left = mid + 1;
			return binarySearch(arr, target, left, right);
		} else if(arr[mid] > target){
			right = mid - 1; 
			return binarySearch(arr, target, left, right);
		} else{
			return 1;
		}
	}

	public static void main(String[] args) {
		try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
			int N = Integer.parseInt(br.readLine());
			String[] input = br.readLine().split(" ");
			int[] array = new int[N];
			for(int i = 0; i < input.length; i++){
				array[i] = Integer.parseInt(input[i]);
			}
			Arrays.sort(array);

			int M = Integer.parseInt(br.readLine());
			input = br.readLine().split(" ");
			for(int i = 0; i < input.length; i++){
				int target = Integer.parseInt(input[i]);
				System.out.println(binarySearch(array, target, 0, array.length - 1));
			}
		} catch(IOException e){
			e.printStackTrace();
		}
	}

}