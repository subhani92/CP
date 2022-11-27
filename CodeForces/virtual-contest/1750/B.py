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

            

def main():

    # sys.stdin = open('input.txt','r')
    # sys.stdout = open('output.txt', 'w')
    t = int(input())

    for _ in range(t):
        n = int(input())
        s  = input()

        zero, one = 0, 0 
        
        # s = list(s)
        for i in range(n):

            if s[i] == "0":
                zero+=1
            if s[i]=="1":
                one +=1 

        ans = zero*one
        temp=1

        for i in range(1, n):
            
            if s[i] ==s[i-1]:
                temp+=1
            else:
                ans = max(ans, temp*temp)
                temp =1 

        ans = max(ans, temp*temp)
        # print("0:", zero , "1:", one, "con:", ans)
        print(ans)

        
        
        
        # print(visited)
        



main()



