def somaRiemann(startX, endX, endY, startY, dataX, dataY, area, indexEqc):
    resultado = 0
    lenX = len(dataX)
    lenY = len(dataY)

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


def calcula():
    try:
        indexEqc = lbxEquacao.curselection()[0]

        deltaX = (int(valB.get()) - int(valA.get()))/int(valM.get())
        deltaY = (int(valD.get()) - int(valC.get()))/int(valN.get())
        area =   deltaX * deltaY

        xm = int(valA.get())
        allX = []
        for i in range(int(valM.get()) + 1):
            allX.append(xm)
            xm += deltaX

        yn = int(valC.get())
        allY = []
        for i in range(int(valN.get()) + 1):
            allY.append(yn)
            yn += deltaY

        ciE = somaRiemann(0, 1, 0, 1, allX, allY, area, indexEqc)
        ciD = somaRiemann(1, 0, 0, 1, allX, allY, area, indexEqc)

        # Ponto médio
        pM = 0.0
        if indexEqc == 0:
            for x in range(len(allX)-1):
                for y in range(len(allY)-1):
                    pontoMedio = (allX[x] + allX[x+1])/2
                    pM += ((1 - (pontoMedio**2))**0.5)*area

        elif indexEqc == 1:
            for x in range(len(allX)-1):
                pontoMedioX = (allX[x] + allX[x+1])/2
                for y in range(len(allY)-1):
                    pontoMedioY = (allY[y] + allY[y+1])/2
                    pM += ((pontoMedioX**2) + (pontoMedioY**2))*area

        csE = somaRiemann(0, 1, 0, 1, allX, allY, area, indexEqc)
        csD = somaRiemann(1, 0, 1, 0, allX, allY, area, indexEqc)

        valCIE.set("{:.6f}".format(float(ciE)))
        valCID.set("{:.6f}".format(float(ciD)))
        valCSE.set("{:.6f}".format(float(csE)))
        valCSD.set("{:.6f}".format(float(csD)))
        valPM.set("{:.6f}".format(float(pM)))

    except:
        valCIE.set("???")
        valCID.set("???")
        valCSE.set("???")
        valCSD.set("???")
        valPM.set("???")


from tkinter import *
from tkinter import ttk

# Cria janela principal
window = Tk()
window.title("Soma de Riemann de Preguiçoso")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
frmMain = ttk.Frame(window, padding=(12,12,12,12))
frmMain.grid(column=0, row=0, sticky=("N", "W", "S", "E"))


# Painel de equações
lbxEquacao = Listbox(frmMain, height=5, selectmode=SINGLE, activestyle="dotbox")
lbxEquacao.grid(row=0, column=0, rowspan=4, columnspan=4, padx=6, pady=6, sticky=("N", "W", "S", "E"))
lbxEquacao.insert(0, "(1 - x^2)^1/2")
lbxEquacao.insert(1, "x^2 + y^2")
lbxEquacao.insert(2, "e^(- x^2 - y^2 - z^2)")
lbxEquacao.select_set(0)


# Painel de entrada dos dados
valM = StringVar(frmMain)
valN = StringVar(frmMain)
valA = StringVar(frmMain)
valB = StringVar(frmMain)
valC = StringVar(frmMain)
valD = StringVar(frmMain)

ttk.Label(frmMain, text="M =").grid(row=0, padx=6, column=4, sticky="E")
ttk.Label(frmMain, text="N =").grid(row=0, padx=6, column=6, sticky="E")
ttk.Label(frmMain, text="A =").grid(row=1, padx=6, column=4, sticky="E")
ttk.Label(frmMain, text="B =").grid(row=1, padx=6, column=6, sticky="E")
ttk.Label(frmMain, text="C =").grid(row=2, padx=6, column=4, sticky="E")
ttk.Label(frmMain, text="D =").grid(row=2, padx=6, column=6, sticky="E")

ttk.Entry(frmMain, width=10, textvariable=valM).grid(row=0, column=5, padx=0, pady=6, sticky="W")
ttk.Entry(frmMain, width=10, textvariable=valN).grid(row=0, column=7, padx=6, pady=6, sticky="W")
ttk.Entry(frmMain, width=10, textvariable=valA).grid(row=1, column=5, padx=0, pady=6, sticky="W")
ttk.Entry(frmMain, width=10, textvariable=valB).grid(row=1, column=7, padx=6, pady=6, sticky="W")
ttk.Entry(frmMain, width=10, textvariable=valC).grid(row=2, column=5, padx=0, pady=6, sticky="W")
ttk.Entry(frmMain, width=10, textvariable=valD).grid(row=2, column=7, padx=6, pady=6, sticky="W")

ttk.Button(frmMain, text="Calcular", command=calcula).grid(row=3, column=4, columnspan=4, padx=6, pady=6, sticky=("N", "W", "S", "E"))


# Painel dos resultados
valCIE = StringVar(frmMain)
valCID = StringVar(frmMain)
valCSE = StringVar(frmMain)
valCSD = StringVar(frmMain)
valPM  = StringVar(frmMain)

lfrCI = ttk.Labelframe(frmMain, text="Cantos inferiores")
lfrCS = ttk.Labelframe(frmMain, text="Cantos superiores")

lfrCI.grid(row=4, column=0, rowspan=2, columnspan=4, padx=6, sticky=("N", "W", "S", "E"))
lfrCS.grid(row=4, column=4, rowspan=2, columnspan=4, padx=6, sticky=("N", "W", "S", "E"))

ttk.Label(lfrCI, text="  Esquerdo: ").grid(row=0, column=0, sticky="W")
ttk.Label(lfrCI,  text="  Direito: ").grid(row=1, column=0, sticky="W")
ttk.Label(lfrCI, textvariable=valCIE).grid(row=0, column=1, sticky="E")
ttk.Label(lfrCI, textvariable=valCID).grid(row=1, column=1, sticky="E")

ttk.Label(lfrCS, text="  Esquerdo: ").grid(row=0, column=0, sticky="W")
ttk.Label(lfrCS,  text="  Direito: ").grid(row=1, column=0, sticky="W")
ttk.Label(lfrCS, textvariable=valCSE).grid(row=0, column=1, sticky="E")
ttk.Label(lfrCS, textvariable=valCSD).grid(row=1, column=1, sticky="E")

ttk.Label(frmMain, text="  Ponto médio:").grid(row=6, column=0, sticky="W")
ttk.Label(frmMain,    textvariable=valPM).grid(row=6, column=0, sticky="E")


# Configura redimensionamento da janela principal
frmMain.columnconfigure(0, weight=4)
frmMain.columnconfigure(4, weight=1)
frmMain.columnconfigure(5, weight=1)
frmMain.columnconfigure(6, weight=1)
frmMain.columnconfigure(7, weight=1)

frmMain.rowconfigure(0, weight=1)
frmMain.rowconfigure(1, weight=1)
frmMain.rowconfigure(2, weight=1)
frmMain.rowconfigure(3, weight=0)
frmMain.rowconfigure(4, weight=0)
frmMain.rowconfigure(5, weight=0)

window.minsize(window.winfo_reqwidth()+320,window.winfo_reqheight()+90)


# Exibe a interface
window.mainloop()
