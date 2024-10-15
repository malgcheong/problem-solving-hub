import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class Main{
    public static void main(String[] args) {
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            StringBuilder sb = new StringBuilder();
            int n = Integer.parseInt(br.readLine());
            ArrayList<Integer> queue = new ArrayList<>();
            for(int i = 0; i < n; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                String command = st.nextToken();
                if(command.equals("push")){
                    queue.add(Integer.parseInt(st.nextToken()));
                } else if(command.equals("pop")){
                    sb.append(queue.isEmpty() ? "-1\n" : queue.get(0) + "\n");
                    if(!queue.isEmpty()) queue.remove(0);
                } else if(command.equals("size")){
                    sb.append(queue.size() + "\n");
                } else if(command.equals("empty")){
                    sb.append(queue.isEmpty() ? "1\n" : "0\n");
                } else if(command.equals("front")){
                    sb.append(queue.isEmpty() ? "-1\n" : queue.get(0) + "\n");
                } else if(command.equals("back")){
                    sb.append(queue.isEmpty() ? "-1\n" : queue.get(queue.size()-1) + "\n");
                }
            }
            System.out.println(sb);
        } catch(IOException e){
            e.printStackTrace();
        }
    }
}