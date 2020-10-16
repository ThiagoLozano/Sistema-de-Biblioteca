import mysql.connector


class Biblioteca:
    # Método Construtor.
    def __init__(self):
        self.mybd = mysql.connector.connect(host='localhost', user='root', password='', database='Biblioteca')
        self.my_cursor = self.mybd.cursor()
        self.status = 1

    # Logar o ADM.
    def Logar(self):
        print('=' * 30)
        print('{:^30}'.format('LOGAR'))
        print('=' * 30)

        # Pergunta para o usuário.
        nome = str(input('Nome: '))
        senha = str(input('Senha: '))

        # Valida se os dados batem com o registro da tabela 'Login_adm'.
        self.my_cursor.execute("SELECT * FROM Login_adm")
        select = self.my_cursor.fetchall()
        for c in select:
            if c[1] == nome and c[2] == senha:
                print("Login Efetuado com sucesso!")
                self.Menu()
                break
        else:
            print("Erro: Nome ou senha estão incorretos")

    # Inseri um Livro novo.
    def Inserir_Livro(self):
        print('=' * 30)
        print('{:^30}'.format('INSERIR LIVROS'))
        print('=' * 30)

        # Pergunta para o usuário.
        id_livro = int(input('\nNúmero do Livro: '))
        nome = str(input('Nome do Livro: '))
        autor = str(input('Autor do Livro: '))
        genero = str(input('Genêro do Livro: '))
        paginas = int(input('Total de Páginas do Livro: '))
        publicacao = str(input('Data da Publicação(AA/MM/DD): '))
        disponivel = int(input('Quantidade disponível: '))
        usando = 0

        # Insere dados na tabela 'Livros'.
        self.my_cursor.execute(
            "INSERT INTO Livros VALUES (DEFAULT, {},'{}','{}','{}',{},'{}',{},{})".format(id_livro, nome, autor,
                                                                                          genero, paginas,
                                                                                          publicacao, disponivel,
                                                                                          usando))
        # Laço para inserir mais livros ou não.
        while True:
            mais_livros = str(input('\nDeseja Inserir mais Livros?(S/N): ')).upper()
            if mais_livros == 'N':
                self.Menu()
                break
            elif mais_livros != 'S':
                print("Erro: Tipo de escolha inválido")
            else:
                self.Inserir_Livro()

    # Remove um Livro do Banco de Dados.
    def Remover_Livro(self):
        print('=' * 30)
        print('{:^30}'.format('REMOVER LIVROS'))
        print('=' * 30)

        # Pergunta para o usuário.
        id_livro = int(input("Digite o id do filme: "))
        print()

        # Busca o Livro na tabela 'Livros'.
        self.my_cursor.execute("""
        SELECT id_livro, nome_livro, autor, genero FROM Livros
        WHERE id_livro = {}""".format(id_livro))

        # Mostra dados do livro que deseja remover.
        select = self.my_cursor.fetchall()
        for c in select:
            print(c)

        # Laço para confirmar a remoção do livro.
        while True:
            mais_livros = str(input('\nDeseja Mesmo remover este Livro?(S/N): ')).upper()
            if mais_livros == 'S':
                self.my_cursor.execute("""
                DELETE FROM Livros
                WHERE id_livro = {}""".format(id_livro))
                print("Livro removido com sucesso!")

                # Laço para remover mais livros ou não.
                while True:
                    mais_livros = str(input('\nDeseja remover mais algum Livro?(S/N): ')).upper()
                    if mais_livros == 'S':
                        self.Remover_Livro()
                    elif mais_livros != 'N':
                        print("Erro: Tipo de escolha inválido")
                    else:
                        self.Menu()

            elif mais_livros != 'N':
                print("Erro: Tipo de escolha inválido")
            else:
                self.Remover_Livro()

    # Lista os livros já resgistrados no Banco de Dados.
    def Mostrar_Livros(self):
        print('=' * 30)
        print('{:^30}'.format('MOSTRAR LIVROS'))
        print('=' * 30)

        # Retorna todos os livros registrados da tabela 'Livros'.
        self.my_cursor.execute("SELECT id_livro, nome_livro, autor, genero FROM Livros")

        # Mostra os dados de todos os livros já registrados.
        select = self.my_cursor.fetchall()
        for c in select:
            print(c)

        self.Menu()

    # Registra um Cliente Novo.
    def Registrar_Cliente(self):
        print('=' * 30)
        print('{:^30}'.format('REGISTRAR CLIENTE'))
        print('=' * 30)

        # Pergunta para o usuário.
        id_cliente = int(input("Identificação do Cliente: "))
        nome = str(input("Nome do cliente: "))
        sobrenome = str(input("Sobrenome do cliente: "))
        nascimento = str(input("Data de Nascimento do cliente(AA-MM-DD): "))
        sexo = str(input("Sexo do cliente(M/F): "))

        # Insere os dados na tabela 'Clientes'.
        self.my_cursor.execute(
            "INSERT INTO Clientes VALUES (DEFAULT, {},'{}','{}','{}', '{}')".format(id_cliente, nome, sobrenome,
                                                                                    nascimento, sexo))

        # Laço para inserir mais clientes ou não.
        while True:
            mais_clientes = str(input('\nDeseja Inserir mais Clientes?(S/N): ')).upper()
            if mais_clientes == 'N':
                self.Menu()
                break
            elif mais_clientes != 'S':
                print("Erro: Tipo de escolha inválido")
            else:
                self.Registrar_Cliente()

    # Empresta o livro.
    def Emprestar_Livro(self):
        print('=' * 30)
        print('{:^30}'.format('EMPRESTAR LIVRO'))
        print('=' * 30)

        # Pergunta para o usuário.
        id_cliente = int(input("Identificação do Cliente: "))
        id_livro = int(input("Identificação do Livro: "))
        data_pegou = str(input("Data que pegou o Livro: "))
        data_entregar = str(input("Data que deve ser devolvido: "))

        # Insere dados na tabela 'Emprestimo'.
        self.my_cursor.execute(
            "INSERT INTO Emprestimo VALUES (DEFAULT, {},{},'{}','{}',{})".format(id_cliente, id_livro, data_pegou,
                                                                                 data_entregar, self.status))
        # Atualiza a tabela 'Livros'.
        self.my_cursor.execute("""
        UPDATE Livros
        SET quant_disponivel = quant_disponivel - 1
        WHERE id_livro = {}""".format(id_livro))

        # Atualiza a Tabela 'Livros'.
        self.my_cursor.execute("""
                UPDATE Livros
                SET quant_uso = quant_uso + 1
                WHERE id_livro = {}""".format(id_livro))
        self.Menu()

    # Recebe a devolução do Livro.
    def Receber_Livro(self):
        print('=' * 30)
        print('{:^30}'.format('RECEBER LIVRO'))
        print('=' * 30)

        # Pergunta para o usuário.
        id_cliente = int(input("Identificação do Cliente: "))
        id_livro = int(input("Identificação do Livro: "))

        # Atualiza a Tabela 'Emprestimo'.
        self.my_cursor.execute("""
        UPDATE Emprestimo
        SET status_entrega = 2
        WHERE id_cliente = {} AND id_livro = {}""".format(id_cliente, id_livro))

        # Atualiza a Tabela 'Livros'.
        self.my_cursor.execute("""
                UPDATE Livros
                SET quant_disponivel = quant_disponivel + 1
                WHERE id_livro = {}""".format(id_livro))

        # Atualiza a Tabela 'Livros'.
        self.my_cursor.execute("""
                        UPDATE Livros
                        SET quant_uso = quant_uso - 1
                        WHERE id_livro = {}""".format(id_livro))
        self.Menu()

    # Mostra o menu de opções.
    def Menu(self):
        print('=' * 30)
        print('{:^30}'.format('MENU'))
        print('=' * 30)
        print("""1) Inserir Livros
2) Remover Livros
3) Mostrar Livros
4) Cadastrar um Novo Cliente
5) Emprestar Livro
6) Receber Livro
7) Sair
""")
        # Valida a opção do usuário.
        opcao = int(input("Escolha sua opção: "))
        if opcao == 1:
            self.Inserir_Livro()
        elif opcao == 2:
            self.Remover_Livro()
        elif opcao == 3:
            self.Mostrar_Livros()
        elif opcao == 4:
            self.Registrar_Cliente()
        elif opcao == 5:
            self.Emprestar_Livro()
        elif opcao == 6:
            self.Receber_Livro()
        else:
            print("\033[31mErro: Escolha inválida, tente novamente\033[m\n")


usuario = Biblioteca()
usuario.Logar()
