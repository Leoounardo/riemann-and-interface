from pylab import *

# M = N = 10
deltaX = 0.2
deltaY = 0.2
area =   0.4

xm = -1
allX = []
for i in range(11):
    #print("{:.2f}".format(xm))
    allX.append(xm)
    xm += deltaX

yn = -1
allY = []
for i in range(11):
    #print("{:.2f}".format(yn))
    allY.append(yn)
    yn += deltaY

allDataX = []
allDataY = []
# VISUALIZANDO TODOS OS DADOS
for x in range(11):
    for y in range(11):
        allDataX.append(allX[x])
        allDataY.append(allY[y])

scatter(allDataX, allDataY, s=100, marker='o')
show()