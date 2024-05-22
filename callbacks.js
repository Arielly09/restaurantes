const nomes = ["Kiko","Zinho","Lindo"]

nomes.forEach(function(nome){
    console.log(nome);
});

nomes.forEach((nome) => {
    console.log(nomes);
});

function imprimirNome(){
    console.log(nome);
};

nomes.forEach(imprimirNome);
