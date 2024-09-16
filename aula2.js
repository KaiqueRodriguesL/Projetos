const peso = 140
const altura = 1.80
const imc = peso / (altura * altura)

if (imc < 18.5) {
    console.log(imc);
    console.log('você está abaixo do peso');
} else if (imc >= 18.5 && imc <= 25) {
    console.log(imc);
    console.log('você está no peso normal');
} else if (imc > 25 && imc <= 30) {
    console.log(imc);
    console.log('você está acima do peso');
} else if (imc > 30 && imc <= 40) {
    console.log(imc);
    console.log('você está obeso');
} else {
    console.log(imc);
    console.log('você está muito gordo');
}