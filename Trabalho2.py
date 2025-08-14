# Boas-Vindas
print('-' * 5, 'Bem-Vindo Ao Restaurante', '-' * 5)
print('=' * 58)
print(' ' * 25 + 'CARDÁPIO')
print('=' * 58)

# Cardápio
print('\nTamanho        |  Bife Acebolado(BA)    |  Filé de Frango(FF)     |')
print('-' * 58)
print('P (Pequena)    |     R$16.00            |      R$14.00            |')
print('M (Média)      |     R$20.00            |      R$18.00            |')
print('G (Grande)     |     R$24.00            |      R$22.00            |')

# Variáveis de condição
sabor = ''
tamanho = ''
preco = 0
total = 0

# Loop principal para o sistema
while True:
    sabor = str(input('Selecione o sabor desejado[BA/FF]: ')).upper()
    if sabor not in ['BA', 'FF']:
        print('Digite um sabor válido. Tente novamente.')
        continue

    tamanho = str(input('Selecione o tamanho desejado[P/M/G]: ')).upper()
    if tamanho not in ['P', 'M', 'G']:
        print('Digite um tamanho válido. Tente novamente.')
        continue

    # Condições para somar o valor
    if sabor == 'BA' and tamanho == 'P':
        preco = 16
    elif sabor == 'BA' and tamanho == 'M':
        preco = 20
    elif sabor == 'BA' and tamanho == 'G':
        preco = 24
    elif sabor == 'FF' and tamanho == 'P':
        preco = 14
    elif sabor == 'FF' and tamanho == 'M':
        preco = 18
    elif sabor == 'FF' and tamanho == 'G':
        preco = 22

    # Cálculo do total
    total = total + preco
    print(f'Item adicionado! O valor é de R${total:.2f}')

    # Encerramento
    sair = input('Deseja pedir mais alguma coisa?[S/N]: ').upper()
    if sair == 'N':
        break

# Resultado
print(f'Pedido finalizado. O total foi de: R${total:.2f}')
