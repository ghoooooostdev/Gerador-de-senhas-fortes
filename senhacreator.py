#Gerador de senhas com dificuldade de invasão
#By: Cr1t1c4ll.
#github.com/ghoooooostdev
import random

pequenas = 'abcdefghijklmnopqrstuvwxyz'
grandes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!@#$%¨&*()_+`{}'
#Caracteres que serão utilizados na criação de senhas
ss = pequenas + grandes + numeros
tamanho = 10
sss = "".join(random.sample(ss, tamanho))
ssl = numeros + simbolos
sssl = "".join(random.sample(ssl, tamanho))
ssn = pequenas + grandes + simbolos
sssn = "".join(random.sample(ssn, tamanho))
sg = pequenas + grandes + numeros + simbolos
scg = "".join(random.sample(sg, tamanho))
sn = "".join(random.sample(numeros, tamanho))
print('Caso tenha alguma especificação para a criação, utilize o menu abaixo: ')
print('1: CRIAR SENHA SEM SIMBOLOS \n2: CRIAR SENHA SEM LETRAS \n3: CRIAR SENHA SEM NUMEROS\n4: CRIAR SENHA NÚMERICA\n5: CRIAR SENHA COM TODOS')
r = (input('Digite a opção selecionada: '))
if r == '1':
    print(f'A sua senha gerada foi: {sss}')
elif r == '2':
    print(f'A sua senha gerada foi: {sssl}')
elif r == '3':
    print(f'A sua senha gerada foi: {sssn}')
elif r == '4':
    print(f'A sua senha gerada foi: {sn}')
elif r == '5':
    print(f'A sua senha gerada foi: {scg}')
else: 
    print('Opção incorreta, tente novamente!')
exit
