# cook your dish here
import sys
from collections import defaultdict


# def wrack_a_mole(A:int, B:list) ->list:

#     ans = []
    
#     minn = float('inf')
#     maxx = float('-inf')
#     mole = [0 for _ in range(A)]

#     # print(A, B, mole)

#     for query in B:

#         a,b,c = query

#         if a == 1:
#             ## chnage state from range[b, c)

#             for i in range(b, c, 1):
#                 mole[i] = int(not mole[i])

#                 if mole[i]:
#                     minn = min(minn, i)
#                     maxx = max(maxx, i)

                
#         elif a == 2:
#             ans.append(minn+b-1)

#     return ans


            
# A =8
# B = [
#     [1, 2, 5],

#     [2, 2, -1],

#     [2, 2, -1],

#     [1, 7, 8],

#     [1, 5, 8],

#     [2, 4, -1], 

#     [1, 1, 3]
    
#     ]




# print(wrack_a_mole(A, B))


# A2 = 10

# B2 = [[1, 4, 7],

# [2, 3, -1],
# [2, 3, -1],

# [2, 2, -1],

# [1, 6, 10],

# [1, 8, 9],

# [1, 0, 2],

# [2, 6, -1]]

# print(wrack_a_mole(A2, B2))



def power_speed(a, b, c):

    ans = 0 

    hm = []
    hm2 =[]

    for x, y in  zip(a, c):
        hm.append((x, y))

    for x, y in  zip(b, c):
        hm2.append((x, y))
    
    point = 2 

    #print(hm)
    for task, p in sorted(hm):

        if task <= point:
            ans += 1
            point += p
    
    ans2 = 0
    point = 2 
    for task, p in sorted(hm2):
        
        if task <= point:
            ans2 += 1
            point += p
    
    return max(ans2, ans)


a = [1, 1, 2, 7]
b = [1, 3, 4 , 4]
c = [2, 3, 1, 1]
print(power_speed(a, b, c))
        
