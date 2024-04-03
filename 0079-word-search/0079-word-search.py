class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word, seen): # returns true if word exists
            if not word:
                return True
           
            for d in ((0,1),(1,0),(0,-1),(-1,0)):
                di, dj = i + d[0], j + d[1]
                if 0 <= di < m and 0 <= dj < n:
                    if (di, dj) not in seen and board[di][dj] == word[0]:
                        seen[i, j] = True
                        if dfs(di, dj, word[1:], seen):
                            return True
                        del seen[i, j]
            
                        
            return False
        
        m, n = len(board), len(board[0])
        
     
        # this check gives you 100% performace boost
		# check if all characters of the word exist in the grid first
        all_chars = set(word)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in all_chars:
                    all_chars.remove(board[i][j])
                    
		# exit if missing any character
        if all_chars: return False
        
		# ok, all characters exist, do DFS now
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[1:], {(i, j) : True}):
                        return True
        return False