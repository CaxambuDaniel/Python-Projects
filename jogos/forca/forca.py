import random

def mensagem_inicio():
    # Imprime a mensagem inicial do jogo da forca
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    # Carrega palavras de um arquivo de texto chamado 'palavras.txt'
    # e escolhe uma palavra aleatória do arquivo como a palavra secreta

    with open('palavras.txt', 'r') as arquivo:
        palavras =[]
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    # Cria uma lista contendo '_' para cada letra na palavra secreta
    return ['_' for letra in palavra]

def pede_chute():
    # Solicita ao usuário um palpite e retorna a letra em maiúsculas
    chute = input('Qual a letra? ').strip().upper()
    return chute

def chute_correto(chute, letras_acertadas, palavra_secreta):
    # Atualiza a lista de letras acertadas com o chute correto do usuário
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
        
def imprime_mensagem_perdedor(palavra_secreta):
# Imprime a mensagem e desenho de enforcado se o usuário perder o jogo
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def imprime_mensagem_vencedor():
# Imprime a mensagem e desenho de vencedor se o usuário ganhar o jogo
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def desenha_forca(erros):
# Desenha a forca com base no número de erros
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
# Função principal do jogo

    mensagem_inicio()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou  and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = (erros == 7)
        acertou = ('_' not in letras_acertadas)
        print (letras_acertadas)

    if(acertou == True):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


if(__name__ == "__main__"):
    jogar()
