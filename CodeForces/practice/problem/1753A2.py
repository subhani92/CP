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

catalon = []

def catalan(n):
     
    cat_ = 1
 
    # For the first numbe
    catalon.append(0)
    catalon.append(1)
    # Iterate till N
    for i in range(1, n):
         
        # Calculate the number
        # and print it
        cat_ *= (4 * i - 2)
        cat_ //= (i + 1)
        catalon.append(cat_)

# def solve(s):

#     bal1, bal2 = 0, 0
#     for c in s:
#         if c=="(":
#             bal1 +=1
#         elif c =="?":
#             bal2 +=1
#         else:
#             bal1 -=1


#     return bal1
def solve(nums):
    
    ans = 0
    def dp(nums):
        

            

def main():

    sys.stdin = open('input.txt','r')
    sys.stdout = open('output.txt', 'w')
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums  = list(map(int, input().strip().split()))

        prefix = []
        for i in range(n):
            if i ==0:
                prefix.append(nums[0])
            else:
                num = prefix[-1]+nums[i]
                if i%2 ==0:
                    prefix.append(-num)
                else:
                    prefix.append(num)


        print(prefix)
        
        solve(prefix)
        # print(visited)
        



main()



