import java.util.List;
import java.util.ArrayList;

class Solution {
    static List<List<Integer>> graph;
    static boolean[] visited;
    
    static void dfs(int node) {
        visited[node] = true;
        for (int next: graph.get(node)) {
            if (!visited[next]) dfs(next);
        }
    }

    public int solution(int n, int[][] computers) {
        graph = new ArrayList<>();
        visited = new boolean[n];
            
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && computers[i][j] == 1) {
                    graph.get(i).add(j);
                }
            }
        }
        
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i);
                count++;
            }
        }
        
        return count;
    }
}