print('1) Tabuada')
x = int(input('Qual o número? '))
y = 0
while y <= 10:
    print(f'{x} * {y} = {x * y}')
    y = y + 1
    
print('\n***************************\n')

print('2) Contador de Pontos por acertos')

pontos = 0
questão = 1 
while questão <= 3:
    resposta = input(f'Resposta da questão {questão}: ')
    if questão == 1 and (resposta == 'b' or resposta == 'B'):
        pontos = pontos + 1
    if questão == 2 and (resposta == 'a' or resposta == 'A'):
        pontos = pontos + 1
    if questão == 3 and (resposta == 'd' or resposta == 'D'):
            pontos = pontos + 1
    questão = questão + 1
print(f'O aluno fez {pontos} ponto(s)')

print('\n***************************\n')

print('3) Cálculo mensal de rentabilidade de um investimento')

valor = float(input('Valor investido: R$ '))
juros = float(input('Percentual de juros mensal: '))
mês = 0

while mês <= 12:
    print(f'Mês {mês} -- R$ {valor:.2f}.')

    valor = valor + (valor * juros / 100)
    mês = mês + 1
    
print('\n***************************\n')

print('4) Cálculo mensal de rentabilidade de um investimento, com aporte mensal')

valor = float(input('Valor investido: R$ '))
juros = float(input('Percentual de juros mensal: '))
aporte = float(input('Valor aportado mensalmente: R$ '))
mês = 0

while mês <= 12:
    print(f'Mês {mês} -- R$ {valor:.2f}.')

    valor = valor + (valor * juros / 100) + aporte
    mês = mês + 1

print('\n***************************\n')

print('5) Cálculo de evolução de dívida')

valor = float(input('Valor da dívida: R$ '))
juros = float(input('Percentual de juros mensal: '))
pagamento = float(input('Pagamento mensal: R$ '))
total_pago = 0
juros_pago = 0
mês = 0

while valor > 0:
    
    print(f'Mês {mês} -- Dívida: R$ {valor:.2f}')
    print(f'Pago: R$ {total_pago:.2f} | Juros pago R$ {juros_pago:.2f}')
    print('--------------------')

    juros_pago = juros_pago + (juros * valor / 100)
    total_pago = total_pago + pagamento
    valor = valor + (juros * valor / 100) - pagamento
    mês = mês + 1

print('\n***************************\n')

print('6) Programa que leia numeros inteiros do teclado até que seja digitado 0. Exibir soma, quantidade de insersões e média')

s = 0
c = 0

while True:
    n = int(input('Insira um número para somar o 0 para sair: '))
    if n == 0:
        break
    s += n
    c += 1

    print(f'Total: {s}')
    print(f'Contagem: {c}')
    print(f'Média: {s / c}')

print('\n***************************\n')

print('7) Caixa Registradora')

s = 0

while True:
    cod = float(input('Digite o código do produto: '))

    if cod == 0:
        break
    elif cod == 1:
        s += 0.5
    elif cod == 2:
        s += 1
    elif cod == 3:
        s += 4
    elif cod == 5:
        s += 7
    elif cod == 9:
        s += 8
    else:
        print('Código não registrado')
    print(f'Total: R$ {s:.2f}
          

    
                      
