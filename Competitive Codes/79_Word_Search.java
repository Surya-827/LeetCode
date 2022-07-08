class Solution {

    public boolean exist(char[][] board, String word) {

        

        int m = board.length;

        int n = board[0].length;

        

        for (int i = 0; i < m; i++) {

            for (int j = 0; j < n; j++) {

                boolean[][] visited = new boolean[m][n];

                if (word.charAt(0) == board[i][j] && dfs(board, i, j, visited, word, 0)) {

                    return true;

                }

            }

        }

        return false;

    }

    public boolean dfs(char[][] board, int i, int j, boolean[][] visited, String word, int index) {

        // base condition

        if (index == word.length()) {

            return true;

        }

        if (i < 0 || j < 0 || i >= board.length || j >= board[i].length || visited[i][j] || board[i][j] != word.charAt(index)) {

            return false;

        }

        visited[i][j] = true;

        

        if (dfs(board, i, j + 1, visited, word, index + 1) ||

               dfs(board, i + 1, j, visited, word, index + 1) || 

               dfs(board, i, j - 1, visited, word, index + 1) || 

               dfs(board, i - 1, j, visited, word, index + 1)) {

            return true;

        }

        visited[i][j] = false;

        return false;

    }

}
