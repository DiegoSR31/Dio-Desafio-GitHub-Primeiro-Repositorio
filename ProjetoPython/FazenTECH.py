import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='fazenda_bd'
)

while True:
    print('''Escolha qual a inserção deseja fazer:
[ 1 ] Equipamentos.
[ 2 ] Funcionários.
[ 3 ] Produtos.
[ 4 ] Produção de Leite.
[ 5 } Varejista.
''')
    opcao = int(input('sua opção: '))
    if opcao == 1:
        cursor = connection.cursor ()
        nome = input('Diegite o nome do equipamento: ')
        tipo = input('Digite o tipo do equipamento: ')
        cursor.execute('insert into equipamentos (nome, tipo) values (%s, %s)', (nome, tipo))
        cursor.execute('SELECT * FROM equipamentos')
        for x in cursor:
            print(x)
    elif opcao == 2:
        cursor = connection.cursor()
        cpf = int(input('Digite o CPF fo funcionário: '))
        nome = input('Diegite o Nome do funcionario: ')
        funcao = input('Diegite a função do funcionario: ')
        salario = float(input('Digite o salário do funcionario: R$ '))
        cursor.execute ('insert into funcionarios (cpf, nome, funcao, salario) values (%s, %s, %s, %s)', (cpf, nome, funcao, salario))
        cursor.execute('SELECT * FROM funcionarios')
        for x in cursor:
            print(x)
    elif opcao == 3:
        cursor = connection.cursor()
        nome = input('Digite o Nome do produto: ')
        tipo = input('Digite o Tipo do produto: ')
        quantidade_em_estoque = int(input('Diegite a quantidade em estoque: '))
        preco = float(input('Diegite o preço de venda para este produto: '))
        cursor.execute('insert into produtos (nome, tipo, quantidade_em_estoque, preco)values (%s, %s, %s, %s)', (nome, tipo, quantidade_em_estoque, preco))
        cursor.execute('SELECT * FROM produtos')
        for x in cursor:
            print(x)
    elif opcao ==4:
        cursor = connection.cursor()
        especie = input('Digite a espécie: ')
        ultima_ordenha = input('Digite a data da última ordenha xxxx-xx-xx: ')
        temperatura_do_leite = float(input('Digite a temperatura do leite:º '))
        produtividade_em_litros = float(input('Digite a produtividade do leite em litros: '))
        inseminacao = input('Digite se o gado foi inseminado "SIM/NÃO": ')
        estimativa_parto = input('Data da estimativa do parto XXXX-XX-XX: ')
        cursor.execute('insert into producao_de_leite (especie, ultima_ordenha, temperatura_do_leite, produtividade_em_litros, inseminacao, estimativa_parto) values (%s, %s, %s, %s, %s, %s)', (especie, ultima_ordenha, temperatura_do_leite, produtividade_em_litros, inseminacao, estimativa_parto))
        cursor.execute('SELECT * FROM producao_de_leite')
        for x in cursor:
            print(x)
    elif opcao == 5:
        cursor = connection.cursor()
        nome = input('Diegite o nome do comprador: ')
        cpf = int(input('Diegite o CPF do comprador: '))
        comprador = input('Diegite qual o tipo de produto ele compra: ')
        cursor.execute('insert into varejistas (nome, cpf, comprador) values (%s, %s, %s)', (nome, cpf, comprador))
        cursor.execute('SELECT * FROM varejistas')
        for x in cursor:
            print(x)
    else:
        print('Código invalido!')
    resp=str(input('Quer continuar cadastrando? [S/N]'))
    if resp in 'Nn':
        break