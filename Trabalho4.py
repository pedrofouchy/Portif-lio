# Variáveis principais
lista_funcionario = []
id_global = 5174053

# Boas-Vindas
print('=-' * 30)
print('Bem-Vindo a empresa do Pedro Fouchy')
print('=-' * 30)

# Funções
def cadastrar_funcionario(id):
    # Função para cadastrar funcionário no dicionário/lista
    nome = input('Nome Funcionário: ')
    setor = input('Setor Funcionário: ')
    salario = float(input('Salário Funcionário: '))
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    # Faz a cópia
    lista_funcionario.append(funcionario.copy())
    print(f'Funcionário {nome} Adicionado com Sucesso')


def consultar_funcionarios():
    # Função para consultar
    # Loop para menu/consulta
    while True:
        print("1) - Consultar todos.")
        print('2) - Consultar por id.')
        print('3) - Consultar por setor.')
        print('4) - Retornar ao menu.')
        opcao = int(input('\nEscolha a opção: '))

        # Condições para consulta
        if opcao == 1:
            for func in lista_funcionario:
                print(func)
        elif opcao == 2:
            id_busca = int(input("Digite o ID do funcionário: "))
            encontrado = False
            for func in lista_funcionario:
                if func['id'] == id_busca:
                    print(func)
                    encontrado = True
            if not encontrado:
                print("ID não encontrado.")
        elif opcao == 3:
            setor_busca = input("Digite o setor: ")
            encontrado = False
            for func in lista_funcionario:
                if func['setor'].lower() == setor_busca.lower():
                    print(func)
                    encontrado = True
            if not encontrado:
                print("Nenhum funcionário encontrado nesse setor.")
        elif opcao == 4:
            return
        else:
            print("Opção inválida. Tente novamente.")


def remover_funcionario():
    # Função para remover funcionário do sistema
    while True:
        try:
            id_remove = int(input("Digite o ID do funcionário a ser removido: "))
            for i, func in enumerate(lista_funcionario):
                if func['id'] == id_remove:
                    del lista_funcionario[i]
                    print("Funcionário removido com sucesso!")
                    return
            print("ID inválido. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")


# Loop para navegar no menu
while True:
    print("\nMENU PRINCIPAL")
    print("[1] Cadastrar Funcionário")
    print("[2] Consultar Funcionário")
    print("[3] Remover Funcionário")
    print("[4] Encerrar Programa")
    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':
        cadastrar_funcionario(id_global)
        id_global += 1
    elif escolha == '2':
        consultar_funcionarios()
    elif escolha == '3':
        remover_funcionario()
    elif escolha == '4':
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
