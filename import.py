import random

r = random.randint(1,100)
count = 0
i = 9999

while True:
	count += 1 # count = count + 1
	number = input('請輸入1~100的數字: ')
	number = int(number)
	if number > r:
		print('再小一些')
	elif number < r:
		print('再大一些')
	else:
		print('答對了!')
		print('恭喜你猜對了，這是你的第', count, '次')
		break
	print('這是你猜的第', count, '次')