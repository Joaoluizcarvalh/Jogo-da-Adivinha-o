from random import randint
pc = randint(0, 10)      # PC ESCOLHENDO NUMERO
print('Sou seu computador...')
print('E pensei em um numero de 0 a 10.')
print('Você consegue advinhar qual numero eu pensei ?')
acertou = False
palpites = 0
while not acertou:
    numero = int(input('Qual seu palpite? '))
    palpites += 1
    if numero == pc:
        acertou = True
    else:
        if numero > pc:
            print('Menos... Tente mais uma vez')
        elif numero < pc:
            print('Mais... Tente mais uma vez')
print('Você acertou com {} PALPITES'.format(palpites))
