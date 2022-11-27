# cook your dish here
import sys
# import os
# from tkinter import E


# def prime_factors(n):
#     ans = set()
#     c = 2
#     while(n > 1):
 
#         if(n % c == 0):
#             ans.add(c)
#             n = n / c
#         else:
#             c = c + 1

#     return len(ans)




# def solve(nums):
#     hm = {}
#     for x in nums:
#         hm[x] = hm.get(x,0) +1

#     for k,v in hm.items():
#         if k!=v:
#             return 'NO' 
#             break
#         else:
#             continue

#     return 'YES'

dp = [0 for _ in range(100001)]     
def solve():

    n, k  = [int(x) for x in input().strip().split()]
    s = input()
    
    typeable = [False]*26
    c = [x for x in input().strip().split()]

    for i in range(k):
        typeable[ord(c[i])-ord('a')] =1
    
    for i in range(n):

        if typeable[ord(s[i])-ord('a')]:
            dp[i] = 1
        else:
            dp[i] =0

    fib = [0]*(n+1)
    fib[0] =0
    ans = 0
    for i in range(n):
        if dp[i] ==0:
            fib[i+1] = 0
        else:
            fib[i+1] = 1 + fib[i]

        ans += fib[i+1]

    print(ans)

    


def main():

    sys.stdin = open('input.txt','r')
    sys.stdout = open('output.txt', 'w')      
    solve()


main()



