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

def get(nums, i):

    return max(0, max(nums[i-1], nums[i+1]) - nums[i] +1 )


def main():

    sys.stdin = open('input.txt','r')
    sys.stdout = open('output.txt', 'w')
    t = int(input())

    for _ in range(t):

        # n, m  = [int(x) for x in input().strip().split()]
        n = int(input())

        nums = [int(x) for x in input().strip().split()]


        if n%2 !=0 :
            
            ans = 0
            for i in range(2, n-1):
                ans += get(nums, i)

            print(ans)
            continue

        # evern case
        total = 0
        for i in range(1, n-1, 2):
            total += get(nums, i)

        # print(total)
        ans = total
        for i in range(n-2, 0, -2):
            total -= get(nums, i-1)
            total += get(nums, i)
            ans = min(ans, total)
    
        print(ans)
        
        # print(cool, l, h, min(left_cool, right_cool))

        # if cool > l and cool >h:
        #     print(0)
        # else:
        #     print(cool, l, h min(left_cool, right_cool))
        


main()



