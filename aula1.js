const precoGasol = 5.59;
const precoEtanol = 3.79;
const kmPorLitroGasol = 11;
const kmPorLitroEtanol = 8;
const distanciaEmKm = 100;
const tipoCombustivel = 'Etanol'

const litrosConsumidos = distanciaEmKm / kmPorLitroEtanol;

if (tipoCombustivel === 'Etanol') {
    const valorGasto = litrosConsumidos * precoEtanol;
    console.log(valorGasto.toFixed(2));
} else {
    const valorGasto = litrosConsumidos * precoGasol;
    console.log(valorGasto.toFixed(2));
}



