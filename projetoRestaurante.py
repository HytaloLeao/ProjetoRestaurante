# Projetos de Lógica de Programação com Python

# Para cada objeto criar no mínimo dois dados.

# Exemplo: Médico(nome, crm), Pacientes(nome, cpf)
# 
# # O sistema deverá realizar operações de CRUD com programação estruturada.

# O projeto deve ser colocado no GitHub.

# No dia ? será realizado um sorteio para definir a apresentação dos projetos.

# Restaurante e Pedidos
# - Descrição: Um restaurante recebe vários pedidos. Cada
# pedido é feito por um cliente específico no restaurante.
# - Relação: Um restaurante -> Muitos pedidos

restaurantes = []
pedidos = []
prox_id_pedido = 1

# Funções para CRUD

def criar_restaurantes(nome, localizacao, tipo_cozinha):
    restaurante = {
        'nome': nome,
        'localizacao': localizacao,
        'tipo_cozinha': tipo_cozinha
    }
    restaurantes.append(restaurante)
    print(f"Restaurante '{nome}' criado com sucesso!")

def listar_restaurantes():
    if not restaurantes:
        print('Nenhum restaurante cadastrado.')
    else:
        print('Lista de Restaurantes:')
        for restaurante in restaurantes:
            print(f'Nome: {restaurante["nome"]}, Localização: {restaurante["localizacao"]}, Tipo de cozinha: {restaurante["tipo_cozinha"]}')

def atualizar_restaurante(nome_antigo, nome_novo, localizacao_nova, tipo_cozinha_nova):
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_antigo:
            restaurante['nome'] = nome_novo
            restaurante['localizacao'] = localizacao_nova
            restaurante['tipo_cozinha'] = tipo_cozinha_nova
            print(f"Restaurante '{nome_antigo}' atualizado com sucesso!")
            return True
    print(f"Restaurante '{nome_antigo}' não encontrado.")
    return False

def excluir_restaurante(nome):
    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            restaurantes.remove(restaurante)
            print(f"Restaurante '{nome}' excluído com sucesso!")
            return True
    print(f"Restaurante '{nome}' não encontrado.")
    return False

def criar_pedido(cliente, itens):
    global prox_id_pedido
    pedido = {
        'numero_pedido': prox_id_pedido,
        'cliente': cliente,
        'itens': itens,
        'status': 'Em andamento'
    }
    prox_id_pedido += 1
    pedidos.append(pedido)
    print(f"Pedido número '{pedido['numero_pedido']}' para o cliente '{cliente}' criado com sucesso!")
    return pedido

def listar_pedidos():
    if not pedidos:
        print('Nenhum pedido cadastrado.')
    else:
        print('Lista de Pedidos:')
        for pedido in pedidos:
            print(f'Número do pedido: {pedido["numero_pedido"]}, Cliente: {pedido["cliente"]}, Itens: {pedido["itens"]}, Status: {pedido["status"]}')

def atualizar_pedido(numero_pedido, novos_itens):
    for pedido in pedidos:
        if pedido['numero_pedido'] == numero_pedido:
            pedido['itens'] = novos_itens
            print(f"Pedido número '{numero_pedido}' atualizado com sucesso!")
            return True
    print(f"Pedido número '{numero_pedido}' não encontrado.")
    return False

def excluir_pedido(numero_pedido):
    for pedido in pedidos:
        if pedido['numero_pedido'] == numero_pedido:
            pedidos.remove(pedido)
            print(f"Pedido número '{numero_pedido}' excluído com sucesso!")
            return True
    print(f"Pedido número '{numero_pedido}' não encontrado.")
    return False

# Loop do Sistema (MENU)

while True:
    print('\n(1) Criar restaurante.')
    print('(2) Modificar restaurante.')
    print('(3) Excluir restaurante.')
    print('(4) Listar restaurantes.')
    print('======================================')
    print('(5) Criar pedido.')
    print('(6) Modificar pedido.')
    print('(7) Excluir pedido.')
    print('(8) Listar pedidos.')
    print('(0) Sair.')

    escolha = input('Escolha sua opção: ')

    if escolha == '1':
        nome = input('Digite o nome do restaurante: ')
        localizacao = input('Digite a localização do restaurante: ')
        tipo_cozinha = input('Digite o tipo de cozinha: ')
        criar_restaurantes(nome, localizacao, tipo_cozinha)
    elif escolha == '2':
        nome_antigo = input('Digite o nome do restaurante a ser modificado: ')
        nome_novo = input('Digite o novo nome do restaurante: ')
        localizacao_nova = input('Digite a nova localização do restaurante: ')
        tipo_cozinha_nova = input('Digite o novo tipo de cozinha: ')
        atualizar_restaurante(nome_antigo, nome_novo, localizacao_nova, tipo_cozinha_nova)
    elif escolha == '3':
        nome = input('Digite o nome do restaurante a ser excluído: ')
        excluir_restaurante(nome)
    elif escolha == '4':
        listar_restaurantes()
    elif escolha == '5':
        cliente = input('Digite o nome do cliente: ')
        itens = input('Digite os itens do pedido (separados por vírgula): ').split(',')
        criar_pedido(cliente, itens)
    elif escolha == '6':
        numero_pedido = int(input('Digite o número do pedido a ser modificado: '))
        novos_itens = input('Digite os novos itens do pedido (separados por vírgula): ').split(',')
        atualizar_pedido(numero_pedido, novos_itens)
    elif escolha == '7':
        numero_pedido = int(input('Digite o número do pedido a ser excluído: '))
        excluir_pedido(numero_pedido)
    elif escolha == '8':
        listar_pedidos()
    elif escolha == '0':
        print('Programa finalizado com sucesso!')
        break
    else:
        print('Erro, opção inválida.')