class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        int size = my_string.length();
        
        for (int i = 0; i < n; i ++) {
            answer += my_string.charAt(size - n + i);
        }
        
        return answer;
    }
}