import ai42
from time import sleep

load = ai42.loading.Loading()
listy = range(1000)
ret = 0
for elem in load.ft_progress(listy):
	ret += elem
	sleep(0.002)
print()
print(ret)
ai42.logger.TestC().test()
