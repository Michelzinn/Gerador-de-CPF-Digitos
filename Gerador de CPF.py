import random

cpf = str(random.randint (10000000,999999999))
multiplicador = 10
soma = 0
somatotal = 0
print(' o cpf escolhido foi',cpf)

# operacores para conseguir o primeiro digito
for i in cpf:
    i = int(i)
    multiplicacao = i * multiplicador
    multiplicador -= 1
    somatotal = somatotal + multiplicacao

if 11 - (somatotal % 11) > 9:
    digito1 = 0
else:
    digito1 = (somatotal % 11)

multiplicador2 = 11
soma2 = 0
somatotal2 = 0

# operações para conseguir o segundo digito
for i in cpf:
    i = int(i)

    multiplicacao2 = i * multiplicador2
    multiplicador2 -= 1
    somatotal2 = somatotal2 + multiplicacao2

somatotal2 = somatotal2 + (digito1 * 2)

digito2 = 11 - (somatotal2 % 11)
if digito2 > 9:
    print(' O cpf é inválido')
    quit()

print(f" O digito 1 do seu cpf é {digito1}\n", f"e o digito 2 do seu cpf é {digito2}")
