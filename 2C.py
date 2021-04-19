def somaRiemann(startX, endX, endY, startY, dataX, dataY, area):
    resultado = 0
    lenX = len(dataX)
    lenY = len(dataY)

    for x in range(startX, lenX-endX):
        for y in range(startY, lenY-endY):
            resultado += ((dataX[x]**2) + dataY[y]**2)*area 
    return resultado

def showData(allX, allY):
    for x in range(len(allX)):
        for y in range(len(allY)):
            print("xi = {:.2f}, yj = {:.2f}".format(allX[x], allY[y]))

# M = N = 500
deltaX = 0.004
deltaY = 0.004
area =   0.000016

xm = 0
allX = []
for i in range(501):
    #print("{:.2f}".format(xm))
    allX.append(xm)
    xm += deltaX

yn = 0
allY = []
for i in range(501):
    #print("{:.2f}".format(yn))
    allY.append(yn)
    yn += deltaY

# VISUALIZANDO TODOS OS DADOS, só tirar o #
#showData(allX, allY)

#equação: z = x**2 + y**2
#canto inferior esquerdo
resultado = somaRiemann(0, 1, 0, 1, allX, allY, area)
print("CANTO INFERIOR ESQUERDO: {:.4f}".format(resultado))

resultado = 0
#Ponto Médio:
for x in range(len(allX)-1):
    pontoMedioX = (allX[x] + allX[x+1])/2
    for y in range(len(allY)-1):
        pontoMedioY = (allY[y] + allY[y+1])/2
        resultado += ((pontoMedioX**2) + (pontoMedioY**2))*area
print("PONTO MEDIO: {:.4f}".format(resultado))

#Canto Superior direito:
resultado = somaRiemann(1, 0, 1, 0, allX, allY, area)
print("CANTO SUPERIOR DIREITO: {:.4f}".format(resultado))
