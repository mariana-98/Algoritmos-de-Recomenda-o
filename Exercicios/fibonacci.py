"""
A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. 
Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. 
Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.
n = int(input())
fib_list = [     ]
n = n - 1
for i in range(      ):
    fib_list.append(     )
fib_string = ' '.join(     )
print(fib_string)
"""



n = int(input())

t1 = 0
t2 = 1
n= n-1
fib_list = [t1]


for i in range(0,n):
  t3 = t1 + t2
  t1 = t2
  t2 = t3
  fib_list.append(t1)


fib_string = (' '.join(str(x) for x in fib_list))
print(fib_string)


"""
OUTRA SOLUÇÃO POSSÍVEL
"""

n = int(input())
t1 = 0
t2 = 1
fib_list = [     ]
cont = 3
fib_list.append(t1)
fib_list.append(t2)
while cont <= n:
    t3 = t1 + t2
    fib_list.append(t3)
    t1 = t2
    t2 = t3
    cont += 1
print(str(fib_list).strip('[]').replace(',',''))
