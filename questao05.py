# Inicio do contador de números pares
np = 0
# faça um loop para ler 5 numeros
for i in range(5):
    # Peça para o usuario colocar os números para o loop
    valor = int(input(f"Digite o {i + 1} número: "))
    # Verificar se o valor do número digitado é par
    if valor % 2 == 0:
        np += 1
# mostre a contagem de numeros pares
print(f"\nQuantidade de pares: {np}")