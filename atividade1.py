primos: list=[] # Lista que vai guardar os primos
qprimos: list=[] # lista que vai soma-los
exp = 0 #expoente para testarmos os primos

while True: # Enquanto tudo que estiver abaixo, for verdade:
    exp += 1 # o expoente vai receber + 1;
    for n in range(10**(exp - 1)+ 1, (10**exp)+1): # para n (uma variável numeral) no intervalo de 10^0(exp-1) até 10^1(exp+1)
        if any(n % prime == 0 for prime in  primos if prime <= n **0.5): # se qualquer resto de divisão de n por um primo, para um primo na minha lista primos se esse primo for menor ou igual a raiz desse n 
            continue #continuo caçando primos pos ele não é primo.
        else: #caso contrário
            primos.append(n) # ele é primo pela definiçao de primo. Então, add ele a lista.
    sprimos: list=[prime for prime in primos if 10** (exp-1)<= prime <= 10**exp] # sprimos vai selecionar os primos, com a condição entre colchetes [um número primo para cada primo na lista de primos, se esse primo for maior ou igual a 10^exp-1 e menor que 10^exp]
    for prime in sprimos: #para cada número primo na lista sprimos.
            q_primos: int=prime**2 #esse primo vai ser elevado ao quadrado inteiro e aramzenado em q_primos(quadrado desse primo)
            rsprimos: int= int(str(q_primos)[::-1]) # esse pquadrado primo vai ser transformado em string(texto e não numeral), invertido e depois voltar pra inteiro, e guardado em rsprimos(reversed_square_primes)
            if q_primos == rsprimos: # se o quadrado desse primo for igual a ele revertido
                continue # continua comparando, pois é palindromo
            else: # caso o contrário
                rsprimesroot: float = rsprimos **0.5 # pego esse  quadrado primo revertido e tiro a raiz, passando ele de inteiro para flutuante.
                if rsprimesroot % 1!=0: #se o resto da divisão dessa raiz prima por 1 for diferente de 0, ele não é inteiro
                    continue # continua procurando
                else: #caso contrário, é inteiro
                    rsprimesroot: int = int(rsprimesroot) # pego esse primo transponho de float para inteiro.
                    if rsprimesroot in primos: # se depois do passo anterior, esse num inteiro estiver na lista de primos.
                        qprimos.append(q_primos)# Add ele na lista de quadrados primos
                        if len(qprimos) > 9:# se o tamanho da lista de quadrados primos for maior que 9
                            break #paro
    if len(qprimos) > 9: # mesmo passo de cima, porém agora paro o loop eterno do while.
        break
print(sum(qprimos)) # MOSTRE A SOMA DESSES 10 QUADRADOS PRIMOS.
print(qprimos)# MOSTRE ESSES PRIMOS