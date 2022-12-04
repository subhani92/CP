class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        g = defaultdict(list)
        
        self.ans = float('inf')
        for u, v, d in roads:
            g[u].append((v,d))
            g[v].append((u,d))
            self.ans = max(self.ans, d)
        
        
        vis = set()
        def dfs(s, dist=self.ans):
            vis.add(s)
            # if s == n:
            #     return self.ans
            
            
            self.ans = min(self.ans, dist)
            
            for adj, d in g[s]:
                self.ans = min(self.ans, d)
                if adj not in vis:
                    dfs(adj, d)
                    
            
        dfs(1)
        # print(vis)
            
        return self.ans