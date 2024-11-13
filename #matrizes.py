#matrizes
idade=[[15,19,22,32],[43,33,54,67],[34,25,51,37]]
print(idade)

x=int(input('Matriz: Digite X:'))
y=int(input('Matriz: Digite Y:'))
matriz = []
for i in range(x):
    linha=[]
    for j in range(y):
        linha.append(j)
    matriz.append(linha)
print(matriz)
