def somaRiemann(startX, endX, endY, startY, dataX, dataY, area, indexEqc):
    resultado = 0
    lenX = len(dataX)
    lenY = len(dataY)

    eqc = ["(1 - x**2)**1/2", "x**2 + y**2", "e**(-x**2 - y**2 - z**2)"]

    if(indexEqc == 0):
        for x in range(startX, lenX-endX):
            for y in range(startY, lenY-endY):
                resultado += ((1 - (dataX[x]**2))**0.5)*area 
        return resultado
    
    elif(indexEqc == 1):
        for x in range(startX, lenX-endX):
            for y in range(startY, lenY-endY):
                resultado += ((dataX[x]**2) + (dataY[y]**2))*area 
        return resultado
    else:
        return 1

from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')

eqc = ["(1 - x**2)**1/2", "x**2 + y**2", "e**(-x**2 - y**2 - z**2)"]

datas = [
    [sg.T("Cantos Inferiores:",size=(15,1))],
    [sg.T("   Esquerdo:", key="1",size=(15,1))],
    [sg.T("   Direito:", key="2",size=(15,1))],
    [sg.T("   Ponto Médio:", key="3",size=(15,1))],
    [sg.T("Cantos Superiores:",size=(15,1))],
    [sg.T("   Esquerdo:", key="4",size=(15,1))],
    [sg.T("   Direito:", key="5",size=(15,1))]
]

ly = [
    [sg.Listbox(eqc, size=(20,4), key='lista'), sg.Column(datas)],
    [sg.Text("M ="), sg.In(size=(5,1), key="m"), sg.Text("N ="), sg.In(size=(5,1), key="n")],
    [sg.Text("A ="), sg.In(size=(5,1), key="a"), sg.Text("B ="), sg.In(size=(5,1), key="b")],
    [sg.Text("C ="), sg.In(size=(5,1), key="c"), sg.Text("D ="), sg.In(size=(5,1), key="d")],
    [sg.Button("CALCULAR", key="calcular")]
]

wd = sg.Window('Soma de Riemann de Preguiçoso', ly, size=(400,400))

ok = 1
while ok:
    event, values = wd.read()
    if event == sg.WINDOW_CLOSED:
        ok = 0

    if event == 'calcular':
        val = values['lista']

        deltaX = (int(values['b']) - int(values['a']))/int(values['m'])
        deltaY = (int(values['d']) - int(values['c']))/int(values['n'])
        area =   deltaX * deltaY
        
        xm = int(values['a'])
        allX = []
        for i in range(int(values['m']) + 1):
            #print("{:.2f}".format(xm))
            allX.append(xm)
            xm += deltaX

        yn = int(values['c'])
        allY = []
        for i in range(int(values['n']) + 1):
            #print("{:.2f}".format(yn))
            allY.append(yn)
            yn += deltaY
        
        ciE = somaRiemann(0, 1, 0, 1, allX, allY, area, eqc.index(val[0]))
        ciD = somaRiemann(1, 0, 0, 1, allX, allY, area, eqc.index(val[0]))
        pM = 0
        csE = somaRiemann(0, 1, 0, 1, allX, allY, area, eqc.index(val[0]))
        csD = somaRiemann(1, 0, 1, 0, allX, allY, area, eqc.index(val[0]))
                
        wd.Element("1").Update("  Esquerdo: {:.4f}".format(ciE))
        wd.Element("2").Update("  Esquerdo: {:.4f}".format(ciD))
        wd.Element("3").Update("Ponto Médio: {:.4f}".format(pM))
        wd.Element("4").Update("  Esquerdo: {:.4f}".format(csE))
        wd.Element("5").Update("  Direto: {:.4f}".format(csD))
