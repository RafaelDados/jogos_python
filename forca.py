import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************")

    #lendo arquivo
    arquivo = open("palavras.txt", "r", encoding="utf-8")
    palavras = []
    for linha in arquivo:
        # retira todos espaços e caracteres especiais e ainda deixa todas palavras maiusculas
        palavras.append(linha.strip().upper())
    #fechando arquivo
    arquivo.close()

    #função len() devolve a quantidade de itens em uma lista
    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero]

    '''
    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append("_")'''
    #Utilizando a linguagem Python pode ser feito da seguinte maneira
    letras_acertadas = ["_" for letra in palavra_secreta]

    letras_faltando = len(palavra_secreta)

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    #enquanto não enforcou e não acertou
    while(True):
        # lower() converte toda str para minusculo.
        # upper() para maiusculo.
        # strip() retira os respaços digitados em uma string.
        chute = input("Qual letra?").strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra.upper()
                    letras_faltando = str(letras_acertadas.count('_'))
                index += 1
        else:
            tentativas += 1

        #Caso as tentativas chegue ao número 6 a váriavel enforcou será False
        if(tentativas == 6):
            print("Você perdeu!!")
            break

        if("_" not in letras_acertadas):
            print("Você ganhou!!")
            print(letras_acertadas)
            break

        if(acertou != True):
            print('Ainda faltam acertar {} letras'.format(letras_faltando))

        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()