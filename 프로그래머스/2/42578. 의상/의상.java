import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        Map<String, Integer> cc = new HashMap<>();
        
        for (String[] cloth : clothes) {
            String c = cloth[1];
            cc.put(c, cc.getOrDefault(c, 0) + 1);
        }
        
        for (int c : cc.values()) {
            answer *= c + 1;
        }
        
        return answer - 1;
    }
}