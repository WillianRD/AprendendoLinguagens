// Primeiro Exercicio - Checked
function diferenteDeParOuImpar(num1) {
    const result = num1 % 2 == 0;
    if (result) {
        console.log('Esse número é Par');
    }
    else {
        console.log('Esse número é impar');
    }
}

diferenteDeParOuImpar(11);

// Segundo Exercicio - Checked
function mediaDoAluno(nota1, nota2) {
    resultado = (nota1 + nota2) / 2;
    if (resultado >= 7) {
        console.log("Aluno aprovado \nNota: " + resultado);
    } else {
        console.log("Aluno reprovado!!");
    }
}

mediaDoAluno(10, 10);

// Terceiro Exercicio - Checked
function maiorNumero(num1, num2, num3) {
    const maiorNumer = Math.max(num1, num2, num3)
    console.log("O maior número é: " + maiorNumer);
}

maiorNumero(24, 23, 90);

//Quarto Exercicio - Check
function verificarIdade(idade) {
    if (idade >= 16) {
        console.log("Permitido a votação para a idade: " + idade);
    } else {
        console.log("Não permitido, sua idade atual: " + idade)
    }
}
verificarIdade(15);

// Quinto Exercicio - Checked
function desconto(valorProduto, quantidadeProduto) {
    const descontoDaCompra = 0.10;

    if (quantidadeProduto >= 10) {
        const descontoComProduto = valorProduto * descontoDaCompra;
        const valorCompra = valorProduto - descontoComProduto;

        console.log("Valor total da compra: R$", valorProduto, "\nValor com desconto R$:", valorCompra, "\nTotal Desconto: ", descontoComProduto);
    } else {
        console.log("Não possui desconto\nValor total da compra: R$ ", valorProduto);
    }
}

desconto(1000, 10);

//Sexto Exercicio -- Checked
function triangulo(num1, num2, num3) {
    if (num1 + num2 > num3 && num1 + num3 > num2 && num2 + num3 > num1) {
        if (num1 == num2 && num2 == num3) {
            console.log("Triangulo Equilaterio");

        } else if (num1 == num2 || num2 == num3 || num3 == num1) {
            console.log("Triangulo Isósceles");

        } else {
            console.log("Triangulo Escaleno");
        }
    } else {
        console.log("Não é um triagulo")
    }
}

triangulo(3, 3, 4);

//Setimo Exercicio -- Checked
function calcularImc(peso, altura) {
    const imc = peso / (altura * altura);
    console.log("Seu IMC:", imc.toFixed(2));

    if (peso <= 0 || altura <= 0) {
        console.log("Por favor, insira um valor positivo\nExemplo:92 para seu peso\nExemplo: 1.60 para sua altura ")
    }
    if (imc < 18.5) {
        console.log("Menor que 18,5 - Magreza");
    } else if (imc >= 18.5 && imc <= 24.9) {
        console.log("18,5 a 24,9 - Normal");
    } else if (imc >= 25 && imc <= 29.9) {
        console.log("25 a 29,9 - Sobrepeso");
    } else if (imc >= 30 && imc <= 34.9) {
        console.log("30 a 34,9 - Obesidade grau I");
    } else if (imc >= 35 && imc <= 39.9) {
        console.log("35 a 39,9 - Obesidade grau II");
    } else if (imc > 39.9) {
        console.log("Maior que 40 - Obesidade grau III");
    }
}

calcularImc(72.3, 1.80);

//Oitava Exercicio -Checked
function anoBissexto(ano) {
    if (ano <= 0) {
        console.log("Insira um valor válido");

    } else if (ano >= 2500) {
        console.log("O valor ultrapassa o limite permitido (2500)");

    } else if ((ano % 4 === 0 && ano % 100 != 0) || ano % 400 === 0) {
        console.log(ano, "Ano é bissexto");

    } else {
        console.log(ano, "O ano não é bissexto");
    }
}

anoBissexto(2501);

// Nono Exercicio - Checked
function aumentoSalarioCalculo(salario) {
    if (salario <= 0) {
        console.error("ERRO: Insira um valor positivo");

    } else if (salario < 1000) {
        const aumentoSalarioQuizePorCento = salario * 0.15;
        const total = aumentoSalarioQuizePorCento + salario;
        console.log("Salário Antigo:", salario, "\nAumento de 15%\nNovo salário: R$", total);

    } else if (salario >= 1000 && salario <= 2000) {
        const aumentoSalarioDezPorCento = salario * 0.10;
        const total = aumentoSalarioDezPorCento + salario;
        console.log("Salário Antigo: R$", salario, "\nAumento de 10%\nNovo Salário: R$", total)

    } else if (salario > 2000) {
        const aumentoSalarioCincoPorCento = salario * 0.05;
        const total = aumentoSalarioCincoPorCento + salario;
        console.log("Salário Atual: R$ ", salario, "\nAumento de 5%\nNovo Salário R$", total);
    }

}
aumentoSalarioCalculo(10000);

//Decimo Exercicio - Checked
function jogoDaAdvinhacao() {
    const numeroAleatorioGerado = Math.floor(Math.random() * 10);
    let tentativasDoUsuario = 10;

    console.log("Tente advinhar o número!");
    while (tentativasDoUsuario > 0) {
        const num1 = 1;
        console.log("Você tem", tentativasDoUsuario, " tentativas. Insira um número:");

        if (num1 <= 0 || num1 > 10) {
            console.log("Por favor, insira um número válido entre 1 e 10");
            break;
        }
        if (num1 == numeroAleatorioGerado) {
            console.log("Parábens!!,Você acertou!");
            break;

        } else if (num1 > numeroAleatorioGerado) {
            console.log("O número é menor!")

        } else if (num1 < numeroAleatorioGerado) {
            console.log("O número e maior!");
        }
        tentativasDoUsuario--;

        if (tentativasDoUsuario == 0) {
            console.log('Números de tentativas esgotados. O número era', numeroAleatorioGerado);
        }
    }
}

jogoDaAdvinhacao()