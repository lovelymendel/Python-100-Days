"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
"""

# should start from 0
for i0 in range(0, 21):
	for i1 in range(0, 34):
		for i2 in range(0, 100):
			if 5 * i0 + 3 * i1 + i2 == 100:
				print('%d, %d, %d' % (i0, i1, i2))

# 2 nested loops are enough, don't need 3 nested loops