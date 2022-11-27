# cook your dish here
import sys
# import os
# from tkinter import E
from collections import defaultdict

def gcd(a,b):

    if b==0:
        return a

    return gcd(b, a%b)

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

def solve(nums):

    prev = nums[0]
    for num in nums[1:]:
        if num%prev:
            return "NO"


    return "YES"

def lies_between(l, h, num):
    
    if l<= num<= h:
        return True
    
    return False


def solve(n):

    l, r = 1, 3*n

    while l <r:
        print(l, r)

        l+=3
        r-=3


def main():

    # sys.stdin = open('input.txt','r')
    # sys.stdout = open('output.txt', 'w')
    t = int(input())

    for _ in range(t):

        # n, m  = [int(x) for x in input().strip().split()]
        n = int(input())
        
        print(n//2 + n%2)
        solve(n)




main()



