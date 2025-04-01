from Utilitarios import (
    cadastrarCategoria,
    cadastrarTransacao,
    saldoTotal
)

categoriaOne = cadastrarCategoria("Receitas")
categoriaTwo = cadastrarCategoria("Contas Fixas")
categoriaThree = cadastrarCategoria("Lazer")
categoriaFor = cadastrarCategoria("Viagens")

cadastrarTransacao(
    descricao="Salário Jan/2025", valor=20.0, categoria=categoriaOne
)
