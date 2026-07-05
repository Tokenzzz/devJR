import random 
numero_secreto = random.randint(1,20)
chute = 0 

while chute != numero_secreto:
    chute = int(input("Digite um número entre 1 e 20: "))
    if chute == numero_secreto:
        print (" Você acertou, parabéns!! ")
    
    elif chute < numero_secreto:
        print (" Você errou, o número que você busca é maior que o digitado, tente novamente")

    else:
        print (" Você errou, o número que você busca é menor que o digitado, tente novamente ")


