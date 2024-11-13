#Exercício letra A
def dobro (numero):
    return numero * 2
def triplo (numero):
    return numero * 3
def quadruplo (numero):
    return numero * 4
def quintuplo (numero):
    return numero * 5

numero = 16

valordois = dobro(numero)
valortres = triplo(numero)
valorquatro = quadruplo(numero)
valorcinco = quintuplo(numero)

print(f"o Dobro de {numero} é {valordois}, o triplo é {valortres}, o quadruplo é {valorquatro} e o quintuplo é {valorcinco}")

#Exercício letra B
def desconto (valor,taxa):
    produto = valor - valor*(taxa/100)
    return produto


itens = [
    ("item 1", 10, 3.0),
    ("item 2", 15, 3.5),
    ("item 3", 20, 4.2),
    ("item 4", 30, 4.75),
    ("item 5", 40, 5.12),
    ("item 6", 50, 5.23),
]    

for i in itens:
    nome, preco, taxa = i
    produto = desconto(preco,taxa)
    print(f"O {nome}, de valor {preco}, vai sair com desconto por: {produto}")

#Exercício letra C
def idade (ano, ano_nasc):
    id = ano - ano_nasc
    return id
def faixa_etaria (idade):
    if idade (ano, ano_nasc) <18:
        print ("A idade atual é de: {} anos. Faixa etária: Menor de idade.".format(idade(ano, ano_nasc)))
    elif idade(ano, ano_nasc) >=18 and idade(ano, ano_nasc) <30:
        print ("A idade atual é de: {} anos. Faixa etária: entre 18 e 30 anos".format(idade(ano, ano_nasc)))
    elif idade(ano, ano_nasc) >=30 and idade(ano, ano_nasc)<50:
        print("A idade atual é de: {} anos. Faixa etária: entre 30 e 50 anos".format(idade(ano, ano_nasc)))
    elif idade(ano, ano_nasc) >=50 and idade(ano, ano_nasc)<80:
        print ("A idade atual é de: {} anos. Faixa etária: entra 50 e 80 anos.".format(idade(ano, ano_nasc)))


ano = 2019
ano_nasc = int(input("Digite o ano de nascimento, para sair digite '0000'"))
while (ano_nasc!=0000):
    idade(ano, ano_nasc)
    faixa_etaria(idade)
    ano_nasc = int(input("Digite o ano de nascimento, para sair digite '0000'"))
    

#Exercício letra D
def resultado ():
    soma=0
    for i in range(1,11,1):
        if i % 2 == 0:
            soma = soma - i
        else:
            soma = soma + i
    return soma

valor = resultado ()

print ("O valor da operação será igual a: {}".format(valor))

#Exercício letra E
def resultado ():
    soma = 0
    for i in range (1,11,1):
        if i % 2 == 0:
            soma = soma + 1/i
        else:
            soma = soma - 1/i
    return soma

valor = resultado()
print ("O valor da operação é igual a: {:.4f}".format(valor))

#Exercício letra F
def resultado ():
    soma = 0
    for x in range (1,11,1):
        for y in range (10,0,-1):
            if x % 2 == 0:
                soma = soma - x/y
            else:
                soma = soma + x/y
    return soma

valor = resultado ()
print ("O valor da operação é de: {:.4f}".format(valor))