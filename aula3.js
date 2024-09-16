const preco = 2000;
const formaDePagamento = 1;

if (formaDePagamento === 1) {
    console.log (preco - (preco * 0.1))
} else if (formaDePagamento === 2) {
    console.log (preco - (preco * 0.15))
} else if (formaDePagamento === 3) {
    console.log (preco)
} else {
    console.log(preco + (preco * 0.1))
}
