var nome =  prompt("Seu nome");
var senha = prompt("Senha");
var data = 2023;
var nasc = prompt("Digite seu nascimento");

function calcular(data, nasc) {
    //Função calcular idade
    return  data - nasc;
}

var idade = calcular (data, nasc) ;
//console.log(idade)
if (idade < 19) {
    //Retornar o valor se caso for maior de idade
    console.log("Sua idade é" + idade);
    console.log("Você tem:");
    //alert("Menor de 18 anos");
} else {
    //Retorna o valor se caso for menor de idade
    console.log("MAIOR DE 18 ANOS \n " + idade);
    console.log("Você tem:" + idade);
};
