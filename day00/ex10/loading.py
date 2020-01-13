import datetime
import sys
from time import sleep

def ft_progress(listy):
	ti = datetime.datetime.now()
	for i in listy:
		t = datetime.datetime.now()
		tdelta = t - ti
		e_time = tdelta.total_seconds()
		p = (i+1)/(max(listy)+1)
		eta = e_time / p
		str = '{:=>{}s}>'.format('', p*30)
		print("\rETA {:.2f}s [{:3d}%][{:<30s}] {}/{} | elapsed time {:.2f}s".format(eta, int(p*100), str, i + 1, max(listy)+1, e_time), end='')
		yield i

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
