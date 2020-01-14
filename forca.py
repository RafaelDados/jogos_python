import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = gera_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    letras_faltando = len(palavra_secreta)

    acertou = False
    tentativas = 0

    #enquanto não enforcou e não acertou
    while(True):
        chute = pede_chute_do_jogador()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        if(tentativas == 7):
            mensagem_perdedor(palavra_secreta)
            break

        if("_" not in letras_acertadas):
            mensagem_ganhador(letras_acertadas)
            break

        if(acertou != True):
            print('Ainda faltam acertar {} letras'.format(letras_faltando))

        print(letras_acertadas)


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************")

def gera_palavra_secreta():
    # lendo arquivo
    arquivo = open("palavras.txt", "r", encoding="utf-8")
    palavras = []
    for linha in arquivo:
        # retira todos espaços e caracteres especiais e ainda deixa todas palavras maiusculas
        palavras.append(linha.strip().upper())
    # fechando arquivo
    arquivo.close()

    # função len() devolve a quantidade de itens em uma lista
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]

    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    '''
        letras_acertadas = []
        for letra in palavra_secreta:
            letras_acertadas.append("_")
        Utilizando a linguagem Python pode ser feito da seguinte maneira
    '''
    letras_acertadas = ["_" for letra in palavra_secreta]
    return letras_acertadas

def pede_chute_do_jogador():
    # lower() converte toda str para minusculo.
    # upper() para maiusculo.
    # strip() retira os respaços digitados em uma string.
    chute = input("Qual letra?").strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra.upper()
            letras_faltando = str(letras_acertadas.count('_'))
        index += 1

def mensagem_ganhador(letras_acertadas):
    print(letras_acertadas)
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


def mensagem_perdedor(palavra_secreta):
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

def desenha_forca(erros):
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
if(__name__ == "__main__"):
    jogar()