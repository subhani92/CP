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

def loop(n):

    for i in range(n):
        pass
    

def solve(n, m):

    
    ans = (0, 0)

    for i in range(1, 10):
        x = 0 
        for j in range(1, n+1):

            x = (x *10+i)%m
            # print(x)
            if x == 0:
                ans = max(ans, (j, i))


    
    # print(ans)
    if ans != (0,0):
        return str(ans[1])*ans[0]
    return -1 


def main():
    sys.stdin = open('input.txt','r')
    sys.stdout = open('output.txt', 'w')
   

    n, m = list(map(int, input().strip().split()))

    # nums = [str(i)*n for  i in range(1, 10)]
    
    # print(nums)

    
    # for num in sorted(nums, reverse= True):
    #     # print(num)
        
    
    print(solve(n,m))





   
main()



