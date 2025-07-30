import random, time

MAX_INT = 2**31 - 1

def somasegura(a, b):
    if a > MAX_INT - b:
        raise OverflowError(f"Soma excede o valor máximo permitido de {MAX_INT}")
    return a + b

n = 10000
m = 10000

amostra = []
bigsoma = 0

inicio = time.time()

for i in range(m):
    soma = 0
    for j in range(n):
        gerado = random.randint(0, 20)
        soma = somasegura(soma, gerado)
    media = soma/n
    print(f"dado {i} de {m}")
    bigsoma = somasegura(bigsoma, soma)
    amostra.append(soma)    

bigmedia = bigsoma/(n*m)
print(f"\nvalor total = {bigsoma}")
print(f"bigmedia = {bigmedia}")

fim = time.time()
print(f"Tempo de execução: {fim - inicio:.4f} segundos")
