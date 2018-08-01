speed = int(input("Speed"))
is_birthday = True #bool(input("Birthday"))

if speed < 31:
	print('no ticket')
elif speed > 30 and speed < 51 :
	print('small ticket')
else:
	print('big ticket')
