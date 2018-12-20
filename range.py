# range 範圍
# python 內建功能：
import random

range(3) # [0, 1, 2]

for i in range(100):
    r = random.randint(1, 1000)
    print('這是第', i +1, '次產生隨機數: ', r)

range(2, 5) # [2, 3, 4] 包含起始值，不包含結尾值
range(2, 10, 3) # [2, 5, 8], 2為起始值, 10為結尾值, 3為遞增值
range(10, 3, -2) # [10, 8, 6, 4]

for i in range(100):
    print('hi')
