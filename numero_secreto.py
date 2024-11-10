import random

numero_secreto = random.randint (1,20)

print (numero_secreto)

while True:
    chute_usuario = int(input('Digite um número entre 1 a 20: '))
    if chute_usuario == numero_secreto:
        print ('Parabéns, você acertou!')
        break
    elif chute_usuario > numero_secreto:
        print ('Uhnn muito alto, tente novamente.')
    elif chute_usuario < numero_secreto:
        print ('Uhnn muito baixo, tente novamente.')