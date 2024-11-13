numero=float(input('insira um numero com duas casas decimais'))
numero=str(numero).replace('.',',')
print(numero)

#questao
listalivros=['Java','C#','C++','.NET','PHP']
print(listalivros)
remover=int(input('digite a posição que deseja remover (entre 0 e 4)'))
listalivros.pop(remover)
listalivros.insert(remover,'Python')
print(listalivros)

#questão
b1=9
b2=8.5
b3=7
b4=6
media=(b1*1)+(b2*2)+(b3*3)+(b4*4)/10
media=str(round(media,2)).replace('.',',')
print(media)

#questão
soma=0
maioridade=0
menoridade=1000
contador=1
while contador<=5:
    nome=str(input('digite o nome do aluno \n'))
    idade=int(input('digite a idade do aluno \n'))
    if idade>maioridade:
        maioridade=idade
    if idade<menoridade:
        menoridade=idade
    soma=soma+idade
    contador=contador+1
    media=soma/contador
print('a media das idade é:',round(media,2))
print('a maior idade do grupo é:',maioridade)
print('a menor idade do grupo é:',menoridade)