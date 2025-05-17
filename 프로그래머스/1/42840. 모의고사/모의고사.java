import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        
        int[] stu1 = {1, 2, 3, 4, 5};
        int[] stu2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] stu3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int score1, score2, score3;
        score1 = score2 = score3 = 0;
        
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == stu1[i % stu1.length]) score1++;
            if (answers[i] == stu2[i % stu2.length]) score2++;
            if (answers[i] == stu3[i % stu3.length]) score3++;
        }
        
        int highScore = Math.max(Math.max(score1, score2), score3);
        
        if (score1 == highScore) answer.add(1);
        if (score2 == highScore) answer.add(2);
        if (score3 == highScore) answer.add(3);
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}