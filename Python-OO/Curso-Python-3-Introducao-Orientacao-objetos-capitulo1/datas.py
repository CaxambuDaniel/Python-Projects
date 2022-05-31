from datetime import date

class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatadata(self):
        print('{:02d}/{:02d}/{}'.format(self.dia, self.mes, self.ano))


d = Data(25, 10, 2018)
d.formatadata()

