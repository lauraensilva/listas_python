#Manipulando string
variavel='O curso de Ciência da Computação é o melhor!'
print('quant de caracteres',len(variavel))
variavel = variavel.replace('melhor','MELHOR')
print('resultado da substituição:',variavel)
print('quantidade de letra r',variavel.count('r'))
print('encontra a posição de r',variavel.find('r'))
print('a posição 14 da frase é a letra {}'.format(variavel[14]))
print('separa as palavras de toda a str', variavel.split())
print('separa a frase em um ponto específico',variavel.split(' '))

#manipulação de arquivo

conteudo = str(input("digite o conteudo do arquivo"))
with open ('arquivo.txt', 'w') as arquivo:
    arquivo.write(conteudo)

with open ('arquivo.txt', 'r') as ler_arquivo:
    ler_arquivo.read(arquivo)

#matriz 
matriz = []
for x in range (4):
    linha = []
    for y in range (4):
        linha.append(int(input('Digite o valor na posição ['+ str(x) +','+ str(y) +':]')))
    matriz.append(linha)
conta_pares=0
conta_impares = 0
for x in range (4):
    for y in range (4):
        if matriz [x][y] % 2 == 0:
            conta_pares = conta_pares + 1
        else:
            conta_impares = conta_impares + 1
for x in range(4):
    print(matriz[x])
print('A matriz contém',conta_pares,'numeros pares e', conta_impares,'numeros impares.')