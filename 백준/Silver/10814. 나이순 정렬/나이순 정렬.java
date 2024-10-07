import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
    public static void main(String[] args){
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){

            int N = Integer.parseInt(br.readLine());
            Member[] m = new Member[N];
            for(int i = 0; i < N; i++){
                String[] text = br.readLine().split(" ");
                m[i] = new Member();
                m[i].age = Integer.parseInt(text[0]);
                m[i].name = text[1];
            }
            Arrays.sort(m, new Comparator<Member>() {
                @Override
                public int compare(Member a, Member b){
                    return Integer.compare(a.age, b.age);
                }
            });

            for (Member member : m) {
                System.out.println(member.age + " " + member.name);
            }


        } catch(IOException e){
            e.printStackTrace();
        }
    }

    public static class Member {
        int age;
        String name;
    }
}