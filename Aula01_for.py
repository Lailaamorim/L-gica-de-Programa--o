soma = 0 # onde vamos guardar a soma final
n = 1 # o primeiro número que será somado

for index in range(1, 11):
    print(index) # Mostra o valor de index no momento
    soma = soma + n   # Adiciona o valor de n à soma
    n = n + 1   # Aumenta n em 1

# soma= sun ([i for i in range 1,11)])
print(f"A soma dos números de 1 a 10 é: {soma}")