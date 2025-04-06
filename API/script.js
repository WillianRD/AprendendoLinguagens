function buscarGato() {
    fetch("https://api.thecatapi.com/v1/images/search") // Url da API
      .then(response => response.json()) // Converte os dados em formato JSON
      .then(data => { // Json retorna os dados
        const urlImagem = data[0].url; // .url e o campo da API
        document.getElementById("imagemGato").src = urlImagem;
      })
      .catch(error => {
        console.error("Erro ao buscar gato:", error);
      });
  }