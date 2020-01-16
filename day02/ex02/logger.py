from time import sleep

def log(func):
	def wrapper(*args):
		print(args)
		res = func(*args)
		print("after")
		return res
	return wrapper

class TestC:
	wait = 1000

	
	@log
	def test(self):
		for i in range(self.wait):
			sleep(0.0001)
		print("ok")
		return self.wait;

if __name__ == "__main__":
	test0 = TestC()
	test1 = TestC()
	test2 = TestC()	
	print(test0.test())
	TestC.wait += 1
	print(test1.test())
	print(test2.test())

