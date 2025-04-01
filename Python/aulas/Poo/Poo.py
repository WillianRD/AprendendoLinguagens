from dataclasses import dataclass

@DataClass
class Poo:
    def __init__(self, nome):
        self.nome = nome

    def imprime(self):
        print(self.nome)


will = Poo("Willian")
will.imprime()
