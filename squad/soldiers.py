sd_form = {}

class Soldado:

    def __init__(self, nm, num, aloj, hora, val):
        self.nome = nm
        self.numero = num
        self.alojamento = aloj
        self.horario = hora
        self.valor = val

        sd_form[self.numero] = {
            "Numero": self.numero,
            "Nome": self.nome,
            "Alojamento": self.alojamento,
            "Horario": self.horario,
            "Valor": self.valor
        }
        