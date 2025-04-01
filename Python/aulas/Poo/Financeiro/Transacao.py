from dataclasses import dataclass

from Guanabara.aulas.Poo.Financeiro.Categoria import Categoria


@dataclass
class Transacao:
    descricao: str
    valor: float
    categoria: Categoria

    def imprimirDados(self):
        print(f'DESCRIÇÂO {self.descricao} | VALOR {self.valor} | CATEGORIA {self.categoria.categoria}')
