#Sieve of Erastóteles utilized.

import math


def EPrimo(n):# função para formar os primos
           if n <= 1: # se n for menor ou igual a 1.
               return False# falso, se n = 0, pq b pode ser o primeiro número
           if n == 2: # se n = 2.
               return True #verdadeiro, 2 é o único primo par.
           for i in range(3, math.floor(math.sqrt(n)) + 1): # Para cada elemento i, em um intervalo de  3 ao piso(floor: maior inteiro não maior que) da raíz de n.
               if n % i == 0: # se o resto da razão de n por i = 0
                   return False # falso, não é primo.

           return True # retorna apenas os de verdade ;-;

primes = [] #Lista primos.

for i in range(1000): # para cada elemento em 1000.
    if EPrimo(i): #se o elemento for apontado primo pela função anterior.
        primes.append(i)# lista primos recebe este elemento.

longest = 0 #mais longo
maiorA= 0 #nem necessário comentar...
maiorB = 0

for a in range(-1000, 1000): # para cada a no intervalo de -1000 a 1000.
    for b in primes: #para cada b na lista de primos:

        n = 0 # n starta com 0
        term = n ** 2 + a * n + b # termo geral da equação de Euler.

        while EPrimo(term): # Enquanto a função de primos afirmar um primo para o termo.
            term = n ** 2 + a * n + b # o termo permanece igual.
            n += 1 # n recebe 1. 
             # Princípio da indução ( se vale para n, prove para n+1)
        if n > longest: # se n for maior que o mais longo.
                   longest = n # iguala n a longest.
                   maiorA= a # maiorA recebe o valor de a em que o ciclo terminou. 
                   maiorB = b # mesmo em b

print(maiorA* maiorB) # imprime os resultados
print('O maior valor de a é: {}, \n e o maior de b: {}.'.format(maiorA, maiorB)) # imprime os maiores valores.