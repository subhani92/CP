class Solution:
    def isCircularSentence(self, s: str) -> bool:
        
        s = s.split()
        n = len(s)
        for i in range(n):
            if s[i]:
                if s[i][-1] !=s[(i+1)%n][0]:
                    return False
        
        return True 
                    