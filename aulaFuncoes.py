'''
def calculoDaArea(largura, comprimento):
    area = largura*comprimento
    return area

def precoDoTerreno(largura, comprimento, preco):
    area = calculoDaArea(largura, comprimento)
    precoTerreno = area*preco
    return precoTerreno


#Execucao Padrao
print('1 - Calculo da metragem (m^2) / 2 - Calcular preco do terreno / 3 - Calcular Impostos')
operacao = int(input("Selecione a operacao: "))
if operacao == 1:
    #codigo operacao 1
    largura = int(input("Digite a largura: "))
    comprimento = int(input("Digite o comprimento: "))
    area = calculoDaArea(largura, comprimento)
    print(f"Area do terreno: {area}")

elif operacao == 2:
    #codigo operacao 2
    largura = int(input("Digite a largura: "))
    comprimento = int(input("Digite o comprimento: "))
    precoM2 = float(input("Digite o preco do metro quadrado: "))
    print(f"O preco do terreno é: {precoDoTerreno(largura, comprimento, precoM2)}")

elif operacao == 3:
    largura = int(input("Digite a largura: "))
    comprimento = int(input("Digite o comprimento: "))
    precoM2 = float(input("Digite o preco do metro quadrado: "))
    precoTerreno = precoDoTerreno(largura, comprimento, precoM2)
    ValorImposto = precoTerreno*0.2
    print(f"O valor do imposto é: ", ValorImposto)
'''

def calculoCustos(*contas):
    total = 0.0
    for conta in contas:
        total = total + conta
    return total

custoTotal = calculoCustos(120,100,50,500,1000,50,60,20)
print(custoTotal)





    
