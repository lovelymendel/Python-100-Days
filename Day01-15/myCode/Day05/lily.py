"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
"""

for num in range(100, 1000):
    digit_0 = num % 10
    digit_1 = num // 10 % 10
    digit_2 = num // 100
    if num == digit_0 ** 3 + digit_1 ** 3 + digit_2 ** 3:
    	print(num)