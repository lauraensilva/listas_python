#Exercício letra A
def salario(vhora,fixo,hora):
    vf=fixo + vhora * hora
    return vf
sal_semanal = salario(18,50,20)
print('O salário semanal será de: {:.2f}.'.format(sal_semanal) )
#Exercício letra B
def viagem(valor_fixo,valor_diaria,quant_diaria):
    vf=valor_fixo + valor_diaria * quant_diaria
    return vf
quant_diaria = int(input('Digite quantos diarias deseja contratar'))
orcamento1= viagem(220,129,quant_diaria)
orcamento2=viagem(173,162,quant_diaria)
if orcamento1<orcamento2:
    print ('Sua viagem ficou mais barata com "Orçamento 1" e o valor a pagar será de: {:.2f}.'.format(orcamento1))
else:
    print ('Sua viagem ficou mais barata com "Orçamento 2" e o valor a pagar será de: {:.2f}.'.format(orcamento2))
#Exercício letra C
def juros (valor,taxa,prazo):
    valor_juros = valor + (valor * (taxa/100) * prazo)
    return valor_juros
mes_1 = juros(134,3,1)
mes_3 = juros(134,3,3)
print ("O valor com juros após 1 mês será de: {:.2f}".format(mes_1))
print ("O valor com juros após 3 meses será de: {:.2f}".format(mes_3))

valor = 134
taxa = 3
prazo = 1
valor_juros_160 = 134
mes = 1
while valor_juros_160 <160:
    valor_160 = valor + (valor * (taxa/100) * prazo)
    prazo +=1
    valor_juros_160 = valor_160
    mes = prazo
print ("O valor da conta ultrapassará 160,00 em {} meses e o valor da conta será de: {:.2f}".format(mes,valor_juros_160))
while valor_juros_160 < 268:
    valor_160 = valor + (valor * (taxa/100) * prazo)
    prazo +=1
    valor_juros_160 = valor_160
    mes = prazo
print ("O valor da conta terá dobrado em {} meses e o valor da conta será de: {:.2f}".format(mes,valor_juros_160))

#Exercício letra D
def inss (salario):
    if salario <= 1751.81:
        salario_liquido = salario * (8/100)
    elif salario > 1751.81 and salario <= 2919.72:
        salario_liquido = salario * (9/100)
    elif salario > 2919.72 and salario <= 5839.45:
        salario_liquido = salario * (11/100)
    return salario_liquido

def ir (salario):
    if salario <= 1903.98:
        salario_liquido = salario
    elif salario > 1903.98 and salario <= 2826.55:
        salario_liquido = (salario - 142.8) - (salario - 142.8) * (7.5/100)
    elif salario > 2826.55 and salario <= 3751.05:
        salario_liquido = (salario - 354.8) - (salario - 354.8) * (15/100)
    elif salario > 3751.05 and salario <= 4664.68:
        salario_liquido = (salario - 636.13) - (salario - 636.13) * (22.5/100)
    elif salario > 4664.68:
        salario_liquido = (salario - 869.36) - (salario - 869.36) * (27.5/100)
    return salario_liquido

salario = float(input("Digite o valor do salário bruto:"))
liquido_inss = inss(salario)
liquido_ir = ir (salario)
liquido = liquido_ir - liquido_inss
print ("O valor do salário com descontos de INSS e IR será de {:.2f}".format(liquido))


#Exercício letra E
def validade_senha (senha):
    if any(i.islower() for i in senha):
        if any(i.isdigit() for i in senha):
            if any(i.isupper() for i in senha):
                if len(senha) >= 6:
                    if len (senha)<=12:
                        return True
    return False

senha = input("Digite a senha:")

if validade_senha (senha):
    print ("A senha é válida")
else:
    print ("Senha digitada é inválida")