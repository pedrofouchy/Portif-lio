def escolher_modelo():
    # Serve para escolher o modelo, ao receber a escolha, define o preço de acordo com o modelo escolhido
    global preco
    print('Entre com o Modelo desejado:')
    print('=' * 30)
    print('MCS - Manga Curta Simples')
    print('MLS - Manga Longa Simples')
    print('MCE - Manga Curta com Estampa')
    print('MLE - Manga Longa Com Estampa\n')

    # Série de condições para determinar o preço do modelo escolhido
    while True:
        modelo = input('Escolha a sigla: ').upper()
        if modelo == 'MCS':
            preco = 1.80
            return modelo
        elif modelo == 'MLS':
            preco = 2.10
            return modelo
        elif modelo == 'MCE':
            preco = 2.90
            return modelo
        elif modelo == 'MLE':
            preco = 3.20
            return modelo
        else:
            print('Modelo inválido. Tente novamente.')


def num_camisetas():
    # Serve para solicitar ao usuário a quantidade de camisetas, já aplicando os descontos
    global desconto  # Variável para saber o desconto total
    global preco
    # Série de condições para definir os descontos com base na quantidade
    while True:
        try:
            numcam = int(input('Qual o número de camisetas? '))
            if numcam < 20:
                desconto = 0
                return numcam
            elif 200 > numcam >= 20:
                desconto = 5
                return numcam
            elif 2000 > numcam >= 200:
                desconto = 7
                return numcam
            elif 20000 > numcam >= 2000:
                desconto = 12
                return numcam
            elif numcam > 20000:
                print('Não aceitamos pedidos com mais de 20000 camisetas. Tente novamente.')
        except:
            print('Digite um número válido')


def escolher_frete():
    # Serve para saber o valor do frete escolhido
    while True:
        print('Escolha o tipo de frete: ')
        print('==========================')
        print('1 - Frete por transportadora - R$100,00')
        print('2 - Frete por Sedex - R$200,00')
        print('0 - Retirar pedido na fábrica - R$ 0,00')
        try:
            frete = int(input('\nEscolha uma opção: '))
            if frete == 1:
                return 100
            elif frete == 2:
                return 200
            elif frete == 0:
                return 0
        except:
            print('Digite um valor válido')


# Boas-Vindas
print('=-' * 40)
print('Seja Bem-Vindo(a) a Fábrica de camisetas do Pedro Fouchy ')
print('=-' * 40)

# Chama as funções, já armazenando as variáveis para executar o programa
escolher_modelo()
quantidade = num_camisetas()
frete = escolher_frete()

# Cálculos do pedido
subtotal = preco * quantidade
valor_desconto = subtotal * (desconto / 100)
total_final = subtotal - valor_desconto + frete

# Resultado final
print('\nResumo do Pedido')
print('=' * 40)
print(f'Quantidade de camisetas: {quantidade}')
print(f'Preço unitário: R${preco:.2f}')
print(f'Subtotal: R${subtotal:.2f}')
print(f'Desconto: R${valor_desconto:.2f} ({desconto}%)')
print(f'Frete: R${frete:.2f}')
print('=' * 40)
print(f'Total a pagar: R${total_final:.2f}')
