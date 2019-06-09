"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""
from random import randint

c = 1000

while c > 0:
	print('you have %d capitals' % c)
	debt = int(input('how much to debt this round : '))

	first = randint(1, 6) + randint(1, 6)
	print('dice result : %d' % first)
	if first == 7 or first == 11:
		c += debt
		print('you win this round')
		continue
	elif first == 2 or first == 3 or first == 12:
		c -= debt
		print('you lose this round')
		continue

	while True:
		second = randint(1, 6) + randint(1, 6)
		print('dice result : %d' % second)
		if second == 7:
			c -= debt
			print('you lose this round')
			break
		elif first == second:
			c += debt
			print('you win this round')
			break

print('you have no money, game end')

