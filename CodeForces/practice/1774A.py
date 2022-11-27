import sys

def main():


    sys.stdin = open('input.txt','r')
    sys.stdout = open('output.txt', 'w')
    t = int(input())

    for _ in range(t):

        m = int(input())
        nums = [int(x) for x in input().strip().split()]
        s = input()

        ans = ""
        hm1 = set()
        hm2 = {}
        for num in nums:
            hm1[num] = hm1.get(num, 0) +1

        for char in s:
            hm2[char] = hm2.get(char, 0) +1

        print(hm1.values(), hm2.values())
        print("YES") if sorted(hm1.values()) == sorted(hm2.values()) else print("NO")

if __name__ == "__main__":
    main()