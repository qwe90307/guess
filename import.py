import random
start = input ('請決定number range初始值: ')
end = input ('請決定number range結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)

count = 0

while True:
	count += 1 # count = count + 1	
	num = input('請猜數字: ')
	num = int(num)
	if num > r:
		print('再小一些')
	elif num < r:
		print('再大一些')
	else:
		print('答對了!')
		print('恭喜你猜對了，這是你的第', count, '次')
		break
	print('這是你猜的第', count, '次')