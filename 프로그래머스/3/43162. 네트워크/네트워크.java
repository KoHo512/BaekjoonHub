import java.util.Queue;
import java.util.ArrayDeque;

class Solution {
    static boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        visited = new boolean[n];
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(i, computers);
                count++;
            }
        }
        
        return count;
    }
    
    static void bfs(int start, int[][] computers) {
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(start);
        visited[start] = true;
        
        while (!queue.isEmpty()) {
            int current = queue.poll();
            
            for (int next = 0; next < computers.length; next++) {
                if (computers[current][next] == 1 && !visited[next]) {
                    visited[next] = true;
                    queue.offer(next);
                }
            }
        }
    }
}