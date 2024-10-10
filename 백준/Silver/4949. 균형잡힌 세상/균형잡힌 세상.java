import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main{
    public static void main(String[] args) {
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
            boolean tf = true;
            Deque baskets = new ArrayDeque<String>();
            while(true){
                String input = br.readLine();
                if(input.charAt(0) == '.'){
                    break;
                }
                for(int i = 0; i < input.length(); i++){
                    if(input.charAt(i) == '('){
                        baskets.add("(");
                    } else if(input.charAt(i) == '['){
                        baskets.add("[");
                    } else if(input.charAt(i) == ')'){
                        if(baskets.size() == 0 || baskets.getLast() == "[") {
                            tf = false;
                            break;
                        }
                        baskets.pollLast();
                    } else if(input.charAt(i) == ']'){
                        if(baskets.size() == 0 || baskets.getLast() == "(") {
                            tf = false;
                            break;
                        }
                        baskets.pollLast();
                    }
                }
                if(baskets.size() > 0){
                    tf = false;
                }
    
                if(tf) {
                    System.out.println("yes");
                } else {
                    System.out.println("no");
                }

                tf = true;
                baskets.clear();
            }

            
        } catch(IOException e){
            e.printStackTrace();
        }
    }
}