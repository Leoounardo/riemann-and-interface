from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

eqc = ["(1 - x**2)**1/2", "x**2 + y**2", "e**(-x**2 - y**2 - z**2)"]

ciE = 0
ciD = 0
pM = 0
csE = 0
csD = 0

datas = [
    [sg.T("Cantos Inferiores:")],
    [sg.T("   Esquerdo: {:.4f}".format(ciE))],
    [sg.T("   Direito: {:.4f}".format(ciD))],
    [sg.T("   Ponto Médio: {:.4f}".format(pM))],
    [sg.T("   Cantos Superiores:")],
    [sg.T("   Esquerdo: {:.4f}".format(csD))],
    [sg.T("   Direito: {:.4f}".format(csD))]
]

ly = [
    [sg.Listbox(eqc, size=(20,4),enable_events=True, key='_LIST_'), sg.Column(datas)],
    [sg.Text("M ="), sg.In(size=(5,1), key="m"), sg.Text("N ="), sg.In(size=(5,1), key="n")],
    [sg.Text("A ="), sg.In(size=(5,1), key="a"), sg.Text("B ="), sg.In(size=(5,1), key="b")],
    [sg.Text("C ="), sg.In(size=(5,1), key="c"), sg.Text("D ="), sg.In(size=(5,1), key="d")],
    [sg.Button("CALCULAR", key="do")]
]

wd = sg.Window('Soma de Riemann de Preguiçoso', ly, size=(400,400), keep_on_top=True)

ok = 1
while ok:
    event, values = wd.read()
    if event == sg.WINDOW_CLOSED:
        ok = 0

    if event == 'do':
        print(values['_LIST_'])
        print("M = ", values['m'])
        print("N = ", values['n'])
        print("A = ", values['a'])
        print("B = ", values['b'])
        print("C = ", values['c'])
        print("D = ", values['d'])
        print()