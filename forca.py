def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou):
        # lower() converte toda str para minusculo.
        # upper() para maiusculo.
        # strip() retira os respaços digitados em uma string.
        chute = input("Qual letra?").lower().strip()

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(chute, index))
            index += 1
    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()