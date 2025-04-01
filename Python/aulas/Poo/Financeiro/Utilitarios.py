from dataclasses import dataclass

from Guanabara.aulas.Poo.Financeiro.Categoria import Categoria
from Guanabara.aulas.Poo.Financeiro.Transacao import Transacao

LISTA_CATEGORIA = []
LISTA_TRASACAO = []


def cadastrarCategoria(nome):
    novaCategoria = Categoria(nome=nome)
    LISTA_CATEGORIA.append(novaCategoria)
    return novaCategoria


def cadastrarTransacao(descricao, valor, categoria):
    novaTransacao = Transacao(
        descricao=descricao,
        valor=valor,
        categoria=categoria
    )
    LISTA_TRASACAO.append(novaTransacao)
    return novaTransacao


def saldoTotal():
    total = 0
    for t in LISTA_TRASACAO:
        total = total + t.valor
    return total
