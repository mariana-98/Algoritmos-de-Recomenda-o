print("0) cáculo de multa")
velocidade = float(input("Velocidade Registrada: "))
print (f"Você percorreu uma velocidade de {velocidade} KM/H, gerando uma multa de R$ {(velocidade - 80) * 5}")
print("\n ************************ \n")

print("1) cáculo de imposto de renda")
salário =  float(input( "Seu salário: "))
base = salário
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print (f"Saário: R$ {salário:6.2f}.\n Imposto a pagar: R${imposto:6.2f}")
print("\n ************************ \n")

print('2) Maior de três')
a = int(input('Primeiro Número: '))
b = int(input('Segundo Número: '))
c = int(input('Terceiro Número: '))

if a != b and a != c and b != c:
    if a > b and a > c:
        maior = a
    if a < b and a < c:
        menor = a
    if (a < b and a > c) or (a > b and a < c):
        meio = a
    if b > a and b > c:
        maior = b
    if b < a and b < c:
        menor = b
    if (b < a and b > c) or (b > a and b < c):
        meio = b
    if c > a and c > b:
        maior = c
    if c < a and c < b:
        menor = c
    if (c < a and c > b) or (c > a and c < b):
        meio = c
    print(f'\nOrdem crescente: {menor, meio, maior}')
else:
    print('\nNúmeros inválidos!')

print("\n ************************ \n")

print('3) Cálculo de aumento de acordo com salário')

salário = float(input('Salário: R$ '))

if salário >= 1250:
    print(f'Aumento de 10%, salário alterado para R$ {1.1 * salário:2.2f}')
if salário < 1250:
    print(f'Aumento de 15%, salário alterado para R$ {1.15 * salário:2.2f}')

print("\n ************************ \n")

print('4) Cálculo de valor de viagem')

distância = float(input('Qual a distância da viagem em KM? '))

if distância <= 200:
    print(f'Sua viagem custará R$ {0.5 * distância}, sendo R$ 0,50 por KM')
else:
    print(f'O valor total da viagem será de R$ {0.45 * distância}, sendo R$ 0,45 por KM')
print('Obrigado!')


print("\n ************************ \n")

print('5) Recebe dois números e a operação, retornando o resultado')

primeiro_numero = float(input('Insita o primeiro em ordem de operação: '))
segundo_numero = float(input('Insira o segundo número em ordem de operação: '))
operação = int(input('Insira o número correspondente à operação desejada:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n'))

if operação == 1:
    print(float(primeiro_numero + segundo_numero))
elif operação == 2:
    print(float(primeiro_numero - segundo_numero))
elif operação == 3:
    print(float(primeiro_numero * segundo_numero))
elif operação == 4:
    print(float(primeiro_numero / segundo_numero))
else:
    print('Cálculo inválido!')

print("\n ************************ \n")

print('6)Aprovação de empréstimo imobiliário. O valor da parcela não pode ultrapassar 30% do salário')

valor_imóvel = float(input('Insira o valor do imóvel: '))
salário = float(input('Renda mensal: '))
anos_parcela = int(input('Insira a quantidade de anos: '))

if (salário * 0.3) >= (valor_imóvel / (anos_parcela * 12)):
    print(f'Valor do Imóvel: {valor_imóvel}\nSalário: R${salário}\nTempo de Parcelamento: {anos_parcela * 12} meses\nParcela: R$ {valor_imóvel / (anos_parcela * 12)}')
else:
    print(f'Inviável! Valor da parcela superior a 30% do salário')
    print(f'Valor do Imóvel: {valor_imóvel}\nSalário: R${salário}\nTempo de Parcelamento: {anos_parcela * 12} meses\nParcela: R$ {valor_imóvel /anos_parcela * 12}')

print("\n ************************ \n")

print('7) Calcula o preço a pagar pelo consumo de energia')

consumo = float(input("Quantidade de kWh consumido: "))
tipo = int(input("Selecione o número correspondente ao tipo de instalação:\n1. Residencial\n2.Industrial\n3.Comércio\n"))

if tipo == 1:
    if consumo <= 500:
        print(f"Total: R$ {consumo * 0.40}")
    else:
        print(f"Total: R$ {consumo * 0.65}")
elif tipo == 2:
    if consumo <= 5000:
        print(f"Total: R$ {consumo * 0.55}")
    else:
        print(f"Total: R$ {consumo * 0.60}")
elif tipo == 3:
    if consumo <= 1000:
        print(f"Total: R$ {consumo * 0.55}")
    else:
        print(f"Total: R$ {consumo * 0.60}")

print("\n ************************ \n")



