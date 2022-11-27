class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
            
        ans = []
        def dfs(i, j):
            
            if j == len(t):
                return True 
            
            if i >= len(s) :
                ans.append(j)
                return True if j ==len(t) else False 
            
            if s[i] == t[j]:
                return dfs(i+1, j+1)
            
            elif s[i] != t[j]:
                return dfs(i+1, j)
        
        if dfs(0,0) == True:
            return 0
        else:
            return len(t)-ans[0]
                
            
                