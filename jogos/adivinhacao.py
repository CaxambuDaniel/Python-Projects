import random

def jogar():

    # Imprime a mensagem de boas-vindas
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    # Gera um número secreto aleatório entre 1 e 100
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    # Solicita ao usuário que escolha o nível de dificuldade
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    # Define o total de tentativas com base no nível escolhido
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # Loop para as tentativas do usuário
    for rodada in range(1, total_de_tentativas + 1):
        # Informa a tentativa atual e o total de tentativas
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        # Solicita ao usuário que digite um número entre 1 e 100
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        # Verifica se o chute está fora do intervalo válido e, em caso afirmativo, solicita ao usuário que insira um número válido
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        # Verifica se o usuário acertou o número, caso contrário, informa se o chute foi maior ou menor que o número secreto
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        # Se o usuário acertar o número, informa a pontuação e encerra o loop
        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            # Atualiza a pontuação do usuário com base na diferença entre o chute e o número secreto
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    # Informa o fim do jogo
    print("Fim do jogo")

# Verifica se o arquivo atual é o arquivo principal e, em caso afirmativo, executa a função jogar()
if(__name__ == "__main__"):
    jogar()
