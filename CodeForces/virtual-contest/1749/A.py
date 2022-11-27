import sys


def main():

    # sys.stdin = open("../input.txt",'r')
    # sys.stdout = open("../output.txt", 'w')

    t = int(input())

    for _ in range(t):
        # n = int(input())
        n,m = list(map(int, input().strip().split()))
        rooks = []
        for _ in range(m):
            x,y = list(map(int, input().strip().split()))
            rooks.append([x,y])

        if n == m:
            print("NO")
        else:
            print("YES")
        

        # if l1==l2:
        #     print(0)
        # else:
        #     # l1.sort()
        #     # l2.sort()
        #     if sorted(l1) == sorted(l2):
        #         print(1)
        #     else:
        #         ans = 0
        #         #print(l1, l2)
        #         for i in range(n):
        #             if sorted(l1[i:]) == sorted(l2[i:]):
        #                 ans+=1
        #                 break
        #             if l1[i]!=l2[i]:
        #                 ans+=1 
                    
    
        #         print(ans)
            
        
        # print(visited)
        



main()



