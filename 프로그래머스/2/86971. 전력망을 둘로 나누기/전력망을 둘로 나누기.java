import java.util.*;

class Solution {
    static int n;
    static int[][] wires;
    
    static ArrayList<Integer>[] A;
    static boolean[] visited;
    static int min = Integer.MAX_VALUE;
    
    public int solution(int n, int[][] wires) {
        this.n = n;
        this.wires = wires;

        A = new ArrayList[n + 1];
        for(int i = 1; i <= n; i++) A[i] = new ArrayList<>();
        
        for(int i = 0; i < wires.length; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            A[a].add(b);
            A[b].add(a);
        }
        
        for(int i = 0; i < wires.length; i++){
            int a = wires[i][0];
            int b = wires[i][1];
            
            visited = new boolean[n + 1];
            
            A[a].remove(Integer.valueOf(b));
            A[b].remove(Integer.valueOf(a));
            
            int cnt = dfs(1);
            
            int diff = Math.abs(cnt - (n - cnt));
            min = Math.min(min, diff);
            
            A[a].add(b);
            A[b].add(a);
        }
        
        return min;
    }
    
    static int dfs(int v){
        visited[v] = true;
        int cnt = 1;
        
        for (int next : A[v]){
            if(!visited[next]) {
                cnt += dfs(next);
            }
        }
        
        return cnt;
    }
}