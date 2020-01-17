import sys
from ex01.ImageProcessor import ImageProcessor as ImgP
from ex03.ColorFilter import ColorFilter as CF

ip = ImgP()
cf = CF()
arr = ip.load('./resources/mario.png')
#ip.display(arr)
#ip.display(cf.invert(arr))
#ip.display(cf.to_blue(arr))
#ip.display(cf.to_green(arr))
#ip.display(cf.to_red(arr))
#cell = cf.celluloid(arr, 7)
#ip.display(cell)
grym = cf.to_greyscale(arr, 'm')
ip.display(grym)
gryw = cf.to_greyscale(arr, 'weighted')
ip.display(gryw)
