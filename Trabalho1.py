# Boas-Vindas
print('=' * 40)
print('Seja Bem-Vindo(a) a Loja do Pedro Fouchy')
print('=' * 40)

# Condições do Sistema
valorPedido = float(input('Digite o valor do pedido: '))
quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))

# Examina as condições dos juros
juros = 0
if quantidadeParcelas <= 3:
    valorPedido = valorPedido
elif 4 <= quantidadeParcelas < 6:
    juros = valorPedido * (4 / 100)
elif 6 <= quantidadeParcelas < 9:
    juros = valorPedido * (8 / 100)
elif 9 <= quantidadeParcelas < 13:
    juros = valorPedido * (16 / 100)
else:
    juros = valorPedido * (32 / 100)

# Cálculo
valor_total = valorPedido + juros
valor_parcela = valor_total / quantidadeParcelas

# Resultados
print('-' * 40)
print(f'O valor das Parcelas ficaram em: R${valor_parcela:.2f}')
print(f'O valor total ficou em: R${valor_total:.2f}')
