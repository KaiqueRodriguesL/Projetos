import random

def jogar_jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']
    placar_usuario = 0
    placar_computador = 0
    
    while True:
        print("Escolha sua jogada: pedra, papel ou tesoura (ou 'sair' para encerrar o jogo)")
        jogada_usuario = input().lower()
        
        if jogada_usuario == 'sair':
            break
        
        if jogada_usuario not in opcoes:
            print("Opção inválida. Por favor, escolha entre pedra, papel ou tesoura.")
            continue  # Essa linha deve estar aqui para evitar que o jogo continue após uma opção inválida
        
        jogada_computador = random.choice(opcoes)
        print("O computador escolheu:", jogada_computador)
        
        if jogada_usuario == jogada_computador:
            print("Empate!")
        elif (jogada_usuario == 'pedra' and jogada_computador == 'tesoura') or \
             (jogada_usuario == 'papel' and jogada_computador == 'pedra') or \
             (jogada_usuario == 'tesoura' and jogada_computador == 'papel'):
            print("Você venceu!")
            placar_usuario += 1
        else:
            print("Você perdeu!")
            placar_computador += 1
        
        print("Placar: Você", placar_usuario, "-", placar_computador, "Computador")
    
    print("Jogo encerrado. Placar final: Você", placar_usuario, "-", placar_computador, "Computador")

# Inicia o jogo
jogar_jokenpo()
