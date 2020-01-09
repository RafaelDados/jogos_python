def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_","_","_","_","_"]
    letras_faltando = len(palavra_secreta)

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
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
        enforcou = tentativas == 6

        acertou = "_" not in letras_acertadas
        if(acertou != True):
            print('Ainda faltam acertar {} letras'.format(letras_faltando))
        if(acertou):
            print("Você ganhou!!")
        else:
            print("Você perdeu!!")
        print(letras_acertadas)

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()