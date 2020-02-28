import random
r = random.randint(1, 100)

while True:
    ans = input ('請猜一個數字：')
    ans = int(ans)
    if ans == r:
        print('你猜中了！')
        break
    elif ans > r:
        print('比答案大')
    elif ans < r:
        print('比答案小')
