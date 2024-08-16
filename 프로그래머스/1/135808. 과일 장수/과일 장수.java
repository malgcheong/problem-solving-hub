import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        Arrays.sort(score);
        for (int i = score.length-1; i >= 0; i-=m){
            int price = i - m + 1;
            if (price < 0)
                break;
            answer += score[price] * m;
        }
        
        return answer;
    }
}