'''
#Exercicio
idade_str = input("Digite sua idade: ")
idade = int(idade_str)


if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")

#Exercicio
usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")

#Exercicio
dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017
print("Em {} o carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim))
#"Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28"


#Estudando List Comprehension
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
        print("É par número {}".format(numero))
#exemplo da mesma funcção a cima utilizando List Comprehension
pares = [numero for numero in inteiros if numero % 2 == 0]
print(pares)
'''