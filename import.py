import random

r = random.randint(1,100)

i = 9999
while True:
	number = input('請輸入1~100的數字: ')
	number = int(number)
	if number > r:
		print('再小一些')
	elif number < r:
		print('再大一些')
	else:
		print('答對了!')
		break