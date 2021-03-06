import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")
    #random.seed(100)
    numero_secreto = round(random.randrange(1, 101)) #A função round arredonda o número contido na variável
    total_de_tentativas = 0
    pontos = 1000


    print("Qual nível de dificuldade deseja jogar?")
    print("(1) Fácil \n(2) Médio \n(3) Difícil")

    nivel = int(input("Defina o nível do jogo: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #print(numero_secreto)
    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou o número secreto!\nSua pontuação {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que número secreto.")
            pontos = pontos - abs(numero_secreto - chute) #a função abs() converte um número negativo para positivo

    print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()