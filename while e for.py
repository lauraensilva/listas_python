#exercicio1
soma=0
for i in range(1278,1255,-1):
    soma+=i
print(soma)

#exercício2
a=int(input('Digite o maior número do intervalo que deseja elevar ao quadrado'))
b=int(input('Digite o menor número do intervalo que deseja elevar ao quadrado'))
for i in range(a,b-1,-1):
    print(i**2)

#exercicio3
prazo=int(input('Digite a quantidade de meses que deseja aplicar'))
contador=1
result=1000
while (contador<=prazo):
    result = result + (result*0.1)
    contador+=1
print(result)

#exercicio4
soma=0
for i in range(160,191,2):
    soma+=i
print(soma)

#exercicio5
valor=0
consorcio=1000
for i in range(1,10,1):
    consorcio = consorcio * 1.02
    valor=consorcio
print(valor)

#exercicio6
for i in range(1,20,2):
    print(i**3)

#exercicio7
#letra A
for x in range(1,4,1):
    for y in range (1,4,1):
        for z in range(1,4,1):
            print(x,y,z)

#letra B
for a in range (1,5,1):
    for b in range (1,5,1):
        for c in range (1,5,1):
            for d in range (1,5,1):
                print(a,b,c,d)

#letra C
for a in range (1,6,1):
    for b in range (1,6,1):
        for c in range (1,6,1):
            for d in range (1,6,1):
                for e in range (1,6,1):
                    print(a,b,c,d,e)

#letra D
for a in range (1,7,1):
    for b in range (1,7,1):
        for c in range (1,7,1):
            for d in range (1,7,1):
                for e in range (1,7,1):
                    for f in range (1,7,1):
                        print(a,b,c,d,e,f)

#letra F
for a in range (1,8,1):
    for b in range (1,8,1):
        for c in range (1,8,1):
            for d in range (1,8,1):
                for e in range (1,8,1):
                    for f in range (1,8,1):
                        for g in range (1,8,1):
                            print(a,b,c,d,e,f,g)