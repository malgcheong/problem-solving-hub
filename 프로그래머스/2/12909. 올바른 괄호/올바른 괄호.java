import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        char[] charArr = s.toCharArray();
        List<Character> list = new ArrayList();
        for (int i = 0; i < charArr.length; i++){
            if (charArr[i] == '('){
                list.add('(');
            } else if (charArr[i] == ')' && list.size() > 0){
                list.remove(0);
            } else {
                answer = false;
                return answer;
            }
        }
        
        if (!list.isEmpty()) {
            answer = false;
        }

        return answer;
    }
}