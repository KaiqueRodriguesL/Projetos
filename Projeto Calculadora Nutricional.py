import random

# Função para exibir uma mensagem de introdução
def introducao():
    mensagem = """
    ********************************************
    * Bem-vindo à Calculadora Nutricional!     *
    *                                          *
    * Este programa ajudará você a calcular    *
    * as necessidades nutricionais diárias     *
    * com base em suas informações pessoais.   *
    *                                          *
    * Vamos começar a cuidar da sua saúde?     *
    ********************************************
    """
    print(mensagem)

introducao()

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Função para calcular a Taxa Metabólica Basal (TMB)
def calcular_tmb(sexo, peso, altura, idade):
    if sexo == 'm':
        return 88.36 + (13.4 * peso) + (4.8 * altura * 100) - (5.7 * idade)
    else:
        return 447.6 + (9.2 * peso) + (3.1 * altura * 100) - (4.3 * idade)

# Função para ajustar a ingestão calórica com base no objetivo do usuário
def calcular_calorias_adicionais(tmb, objetivo):
    if objetivo == 'perder':
        return tmb * 0.8  # redução de 20%
    elif objetivo == 'ganhar':
        return tmb * 1.2  # aumento de 20%
    else:
        return tmb  # manter o peso

# Alimentos e suas calorias por grama
alimentos = {
    "Arroz": {"calorias_por_grama": 1.3},
    "Feijão": {"calorias_por_grama": 1.5},
    "Frango": {"calorias_por_grama": 2.5},
    "Ovos": {"calorias_por_grama": 1.8},
    "Brócolis": {"calorias_por_grama": 0.4},
    "Banana": {"calorias_por_grama": 0.9},
    "Aveia": {"calorias_por_grama": 3.0}
}

# Quantidades diárias em gramas
quantidades_diarias = {
    "Arroz": 200,
    "Feijão": 150,
    "Frango": 180,
    "Ovos": 100,
    "Brócolis": 120,
    "Banana": 80,
    "Aveia": 50
}

# Função para calcular as calorias de um alimento dado a quantidade em gramas
def calcular_calorias(alimento, quantidade):
    calorias_por_grama = alimentos[alimento]["calorias_por_grama"]
    calorias_total = quantidade * calorias_por_grama
    return calorias_total

# Função para gerar um plano de dieta baseado na TMB ajustada
def gerar_dieta():
    dieta = [
        ["Aveia", "Banana", "Ovos"],
        ["Arroz", "Feijão", "Frango", "Brócolis"],
        ["Banana", "Aveia"],
        ["Ovos", "Arroz", "Feijão"],
        ["Frango", "Brócolis", "Banana"],
        ["Aveia", "Ovos"],
        ["Arroz", "Feijão", "Brócolis"]
    ]

    plano_semanal = []
    for dia in dieta:
        refeicoes_diarias = []
        for alimento in dia:
            quantidade = quantidades_diarias[alimento]
            calorias = round(calcular_calorias(alimento, quantidade))
            refeicao = {
                "nome": alimento,
                "calorias": calorias,
                "quantidade": quantidade
            }
            refeicoes_diarias.append(refeicao)
        plano_semanal.append(refeicoes_diarias)

    return plano_semanal

# Função para gerar um plano de treino baseado no objetivo do usuário
def gerar_treino(objetivo):
    treino_perder = [
        "Segunda-feira: Treino de membros superiores: costas e bíceps",
        "Terça-feira: 10 min caminhada + 20 min caminhada rápida",
        "Quarta-feira: Treino de membros superiores: ombro e peito",
        "Quinta-feira: 10 min caminhada (alternar entre 3 min de caminhada + 1 min de trote (6 vezes))",
        "Sexta-feira: Treino de inferiores: perna completo",
        "Sábado: 10 min caminhada (alternar entre 3 min de caminhada + 2 min de trote (5 vezes))",
        "Domingo: Descanso"
    ]

    treino_ganhar = [
        "Segunda-feira: Treino de membros superiores: peitoral e tríceps",
        "Terça-feira: Treino de membros superiores: costas e bíceps",
        "Quarta-feira: 1 hora de exercícios aeróbicos",
        "Quinta-feira: Treino de membros inferiores: pernas e glúteos",
        "Sexta-feira: Treino de ombro e abdominais",
        "Sábado: Descanso",
        "Domingo: Descanso"
    ]

    treino_manter = [
        "Segunda-feira: Treino de membros superiores: básico",
        "Terça-feira: Descanso",
        "Quarta-feira: 45 minutos de exercícios aeróbicos",
        "Quinta-feira: Descanso",
        "Sexta-feira: Treino de membros inferiores: básico",
        "Sábado: Descanso",
        "Domingo: Descanso"
    ]

    if objetivo == 'perder':
        treino = treino_perder
    elif objetivo == 'ganhar':
        treino = treino_ganhar
    else:
        treino = treino_manter

    return treino

# Função principal do programa
def main():
    input("\nPressione Enter para começar.")

    # Validar sexo
    while True:
        sexo = input("\nSexo (M/F): ").strip().lower()
        if sexo in ['m', 'f']:
            break
        else:
            print("Por favor, insira 'M' para masculino ou 'F' para feminino.")

    # Validar peso
    while True:
        try:
            peso = float(input("Peso (kg): "))
            if peso > 0:
                break
            else:
                print("Por favor, insira um peso válido maior que zero.")
        except ValueError:
            print("Por favor, insira um valor numérico válido para o peso.")

    # Validar altura
    while True:
        try:
            altura = float(input("Altura em (m): "))
            if altura > 0:
                break
            else:
                print("Por favor, insira uma altura válida maior que zero.")
        except ValueError:
            print("Por favor, insira um valor numérico válido para a altura.")

    # Validar idade
    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0:
                break
            else:
                print("Por favor, insira uma idade válida maior que zero.")
        except ValueError:
            print("Por favor, insira um valor numérico válido para a idade.")

    # Validar objetivo
    while True:
        objetivo = input("Objetivo (perder, manter, ganhar): ").strip().lower()
        if objetivo in ['perder', 'manter', 'ganhar']:
            break
        else:
            print("Por favor, insira 'perder', 'manter' ou 'ganhar' para o objetivo.")

    imc = calcular_imc(peso, altura)
    tmb = calcular_tmb(sexo, peso, altura, idade)
    calorias_ajustadas = calcular_calorias_adicionais(tmb, objetivo)
    classificacao_imc = classificar_imc(imc)

    print(f"\nIMC: {imc:.2f} ({classificacao_imc})")
    print(f"TMB: {round(tmb)} kcal/dia")
    print(f"Ingestão calórica recomendada: {round(calorias_ajustadas)} kcal/dia")

    dieta = gerar_dieta()
    treino = gerar_treino(objetivo)

    print("\nPlano de Treino:")
    for dia, treino_dia in enumerate(treino, 1):
        print(f"Dia {dia}: {treino_dia}")

    print("\nPlano de Dieta para a semana:")
    for dia, refeicoes in enumerate(dieta, 1):
        print(f"\nDia {dia}:")
        for refeicao in refeicoes:
            print(f"- {refeicao['quantidade']}g de {refeicao['nome']} ({refeicao['calorias']} kcal)")

# Função principal que inicia o programa. Coleta informações do usuário, calcula IMC, TMB e ingestão calórica ajustada.
# Depois, gera e imprime os planos de dieta e treino para a semana.
if __name__ == "__main__":
    main()
    
while True:
    continuar = input ("Deseja Fazer mais uma consulta? (sim/nao) " ).lower()
    if continuar == "sim":
        introducao ()
        main ()
    elif continuar == "nao":
        print ("Espero ter ajudado")
        break
    else:
        print ("não entendi, Deseja continuar? (sim/nao:) ")
        while True:
            continuar = input ("Deseja Fazer mais uma consulta? sim/nao: " ).lower
            if continuar == "sim":
                introducao ()
                main ()
            elif continuar == "nao":
                print ("Espero ter ajudado")
                break
            else:
                print ("não entendi, Deseja continuar? sim/nao: ")