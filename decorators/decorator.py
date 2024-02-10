def decor1(func):
		def wrap_1():
			print("************")
			func()
			print(func.__name__)
			print("************")
		return wrap_1
def decor2(func):
		def wrap_2():
			print("@@@@@@@@@@@@")
			func()
			print(func.__name__)
			print("@@@@@@@@@@@@")
		return wrap_2
	
@decor1
@decor2
def sayhellogfg():
		print("Hello")
sayhellogfg()