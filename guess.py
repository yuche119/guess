import random
r = random.randint(1, 100)
count = 0
while True:
    ans = input ('請猜一個數字：')
    ans = int(ans)
    count += 1 
    if ans == r:
        print('你猜中了！')
        print('這是你猜的第',  count, '次')
        break
    elif ans > r:
        print('比答案大')
    elif ans < r:
        print('比答案小')
    print('這是你猜的第',  count, '次')