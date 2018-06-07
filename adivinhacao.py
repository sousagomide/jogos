print("***************************************")
print("** Bem vindo no jogo de Adivinhação! **")
print("***************************************")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você digitou", chute)

if(numero_secreto == int(chute)):
    print("Acertou")
else:
    print("Errou")
print("Fim do jogo")