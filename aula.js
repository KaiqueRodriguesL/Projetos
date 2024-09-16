const media1 = 1
const media2 = 8
const media3 = 6

const media = (media1 + media2 + media3) / 3
console.log (media);

if (media < 5) {
    console.log('Reprova')
} else if (media >= 5 && media <= 7) {
    console.log('Recuperação')
} else {
    console.log('Passou de semestre')
}