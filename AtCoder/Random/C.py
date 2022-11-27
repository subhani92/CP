# cook your dish here
import sys
from collections import defaultdict


neiv = [(1,0), (0,1), (0,-1), (-1, 0), (1,1), (-1,-1)]
def dfs(x,y, val, graph):

    if (x,y) not in val:
        return False
    
    for (i,j) in graph[(x,y)]:
        val.remove((i,j))
        dfs(i,j, val, graph)

    return True 



def main():
    sys.stdin = open('input.txt','r')
    sys.stdout = open('output.txt', 'w')
   
    n, target = list(map(int, input().strip().split()))

    hm = {}

    head = []
    tail = []
    for i in range(n):
        x,y = list(map(int, input().strip().split()))

        hm[x] = 'H'
        hm[y] = 'T'

        head.append(x)
        tail.append(y)

   
    ans =[]
    # print(head, tail)
    def solve( i, curr =[]):
        
        if i >= n:
            if sum(curr) == target:
                ans.append(curr[:])
            return 
        
        # if t == 0:
            
        #     ans.append(curr[:])
        #     return 
        
        # print(curr)
        curr.append(head[i])
        
        solve(i+1, curr)
        curr.pop()

        curr.append(tail[i])
        solve(i+1, curr)
        curr.pop()
        
    
    solve(0)

    if not ans:
        print('No')
    else:
        print('Yes')

        res = ""
        for x in ans[0]:
            res += hm[x]
        
        print(res)
    
        
    # for num in ans:

    #     if len(num) == n:
            
    #         print("Yes")

    #         res = ""
    #         for x in num:
    #             res += hm[x]
    #         print(res)
    #         break




   
main()



