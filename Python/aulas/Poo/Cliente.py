from dataclasses import dataclass
from logging import log

@dataclass
class Cliente:
    nome: str
    idade: int


will = Cliente(nome="Will", idade=20)
print(will)

