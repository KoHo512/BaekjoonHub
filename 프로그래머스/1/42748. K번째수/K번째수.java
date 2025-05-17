import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int l = 0; l < commands.length; l++) {
            int i = commands[l][0];
            int j = commands[l][1];
            int k = commands[l][2];
            int[] new_array = new int[j - i + 1];
        
            for (int m = 0; m < new_array.length; m++) {
                new_array[m] = array[m + i - 1];
            }
            
            Arrays.sort(new_array);
            
            answer[l] = new_array[k - 1];
        }  
        
        return answer;
    }
}