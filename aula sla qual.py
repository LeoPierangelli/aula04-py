'''pares = 0
impares = 0

v = int(input('Digite um número: '))
if v%2 == 0:
    pares = pares + 1
else:
    impares = impares + 1
v = int(input('Digite um número: '))
if v%2 == 0:
    pares = pares + 1
else:
    impares = impares + 1
v = int(input('Digite um número: '))
if v%2 == 0:
    pares = pares + 1
else:
    impares = impares + 1
v = int(input('Digite um número: '))
if v%2 == 0:
    pares = pares + 1
else:
    impares = impares + 1
v = int(input('Digite um número: '))
if v%2 == 0:
    pares = pares + 1
else:
    impares = impares + 1
v = int(input('Digite um número: '))
if v%2 == 0:
    pares = pares + 1
else:
    impares = impares + 1
v = int(input('Digite um número: '))
if v%2 == 0:
    pares = pares + 1
else:
    impares = impares + 1
v = int(input('Digite um número: '))
if v%2 == 0:
    pares = pares + 1
else:
    impares = impares + 1
v = int(input('Digite um número: '))
if v%2 == 0:
    pares = pares + 1
else:
    impares = impares + 1
v = int(input('Digite um número: '))
if v%2 == 0:
    pares = pares + 1
else:
    impares = impares + 1

print(pares,impares)'''



i = 0
while i < 10:
    v = int(input(f'Digite o {i+1}º número: '))
    if v%2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    i = i + 1

print(pares,impares)
