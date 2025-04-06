function buscarGato() {
    fetch("https://api.thecatapi.com/v1/images/search")
      .then(response => response.json())
      .then(data => {
        const urlImagem = data[0].url;
        document.getElementById("imagemGato").src = urlImagem;
        window.onload(buscarGato)
      })
      .catch(error => {
        console.error("Erro ao buscar gato:", error);
      });
  }