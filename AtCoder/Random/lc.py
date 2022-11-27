res = 0
amount = sorted(amount, reverse = True)
cold = amount[0]
worm = amount[1]
hot = amount[2]

while cold > 0 and worm > 0 and hot > 0:
    nums = [cold, worm, hot]
    nums = sorted(nums)
    max1, max2, max3 = nums[-1], nums[-2], nums[-3]
    res += 1
    max1 -= 1
    max2 -= 1
    cold, worm, hot = max1, max2, max3
while cold > 0 and worm > 0:
    res += 1
    cold -= 1
    worm -= 1
while cold > 0 and hot > 0:
    res += 1
    cold -= 1
    worm -= 1
while worm > 0 and hot > 0:
    res += 1
    worm -= 1
    hot -= 1
while cold >= 0 and worm >= 0 and hot >= 0:
    print(cold, worm, hot)
    res += max(cold, worm, hot)
    return res
return res