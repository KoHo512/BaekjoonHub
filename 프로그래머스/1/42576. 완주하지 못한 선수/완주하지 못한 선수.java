import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> partiMap = new HashMap<>();
        
        for (String parti: participant) {
            partiMap.put(parti, partiMap.getOrDefault(parti, 0) + 1);
        }
        
        for (String compl: completion) {
            if (partiMap.get(compl) > 1) {
                partiMap.put(compl, partiMap.get(compl) - 1);
            } else {
                partiMap.remove(compl, 1);
            }
        }
        
        for (String key: partiMap.keySet()) {
            return key;
        }
        
        return "";
    }
}