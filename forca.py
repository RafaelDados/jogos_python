def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_","_","_","_","_"]


    enforcou = False
    acertou = False

    print(letras_acertadas)

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
        # lower() converte toda str para minusculo.
        # upper() para maiusculo.
        # strip() retira os respaços digitados em uma string.
        chute = input("Qual letra?").strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra.upper()
                letras_faltando = str(letras_acertadas.count('_'))
            index += 1
        print(letras_acertadas)
        print('Ainda faltam acertar {} letras'.format(letras_faltando))
    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()