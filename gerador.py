import mysql.connector
from random import randrange
from random import choice
from random import sample
from datetime import datetime


class GeradorDados:
    # Método Construtor.
    def __init__(self):
        self.mybd = mysql.connector.connect(host='localhost', user='root', password='', database='Biblioteca')
        self.my_cursor = self.mybd.cursor()

    # Função que preenche a tabela 'Livros'.
    def Gerador_livros(self):
        # Valores para o id do Livro.
        valores = sample(range(1111, 9999), 29)

        for c in range(29):
            id_livro = choice(valores)
            # Valores para o nome do Livro.
            random_n = ['Livro A', 'Livro B', 'Livro C',
                        'Livro D', 'Livro E', 'Livro F',
                        'Livro G', 'Livro H', 'Livro I',
                        'Livro J', 'Livro K', 'Livro L']
            nome = choice(random_n)

            # Valores para o nome do autor.
            random_a = ['Autor A', 'Autor B', 'Autor C',
                        'Autor D', 'Autor E', 'Autor F',
                        'Autor G', 'Autor H', 'Autor I',
                        'Autor J', 'Autor K', 'Autor L', ]
            autor = choice(random_a)

            # Valores para o Gênero do autor.
            random_g = ['Terror', 'Romântico', 'Educacional',
                        'Ficção Científica', 'Biografia', 'Fantasia',
                        'Poema', 'Poesia', 'Crônica',
                        'Fábula', 'Infantil', 'AutoBiografia']

            genero = choice(random_g)

            # Valores para o número de Páginas.
            paginas = randrange(100, 500)

            # Valores para a Data de Publicação.
            ano = randrange(1800, datetime.today().year)
            mes = randrange(1, 12)
            dia = randrange(1, 30)
            data = str(ano) + '-' + str(mes) + '-' + str(dia)

            # Valores para a Quantidade Disponível.
            disponivel = randrange(5, 30)

            # Valor para a Quantidade em uso.
            uso = 0

            self.my_cursor.execute(
                """INSERT INTO Livros VALUES(DEFAULT, {}, '{}', '{}', '{}', {}, '{}', {}, {})""".format(id_livro, nome,
                                                                                                        autor, genero,
                                                                                                        paginas, data,
                                                                                                        disponivel,
                                                                                                        uso))
            valores.remove(id_livro)

    # Função que preenche a tabela 'Clientes'.
    def Gerador_Clientes(self):
        # Valores para o id do Livro.
        valores = sample(range(1111, 9999), 19)

        for c in range(19):
            id_cliente = choice(valores)

            # Valores para o nome do Cliente.
            random_n = ['Cliente A', 'Cliente B', 'Cliente C',
                        'Cliente D', 'Cliente E', 'Cliente F',
                        'Cliente G', 'Cliente H', 'Cliente I',
                        'Cliente J', 'Cliente K', 'Cliente L', ]
            nome = choice(random_n)

            # Valores para o sobrenome do Cliente.
            random_sn = ['Sobrenome A', 'Sobrenome B', 'Sobrenome C',
                         'Sobrenome D', 'Sobrenome E', 'Sobrenome F',
                         'Sobrenome G', 'Sobrenome H', 'Sobrenome I',
                         'Sobrenome J', 'Sobrenome K', 'Sobrenome L', ]
            sobrenome = choice(random_sn)

            # Valores para a Data de Nascimento.
            ano = randrange(1930, datetime.today().year)
            mes = randrange(1, 12)
            dia = randrange(1, 30)
            data = str(ano) + '-' + str(mes) + '-' + str(dia)

            # Valores para o Sexo do Cliente.
            random_s = ['F', 'M']
            sexo = choice(random_s)

            self.my_cursor.execute(
                """INSERT INTO Clientes VALUES(DEFAULT, {}, '{}', '{}', '{}', '{}')""".format(id_cliente, nome,
                                                                                              sobrenome,
                                                                                              data, sexo))
            valores.remove(id_cliente)

    # Função que preenche a tabela 'Emprestimo'.
    def Gerador_Emprestimo(self):
        for v in range(9):
            # Seleciona id do Cliente.
            lista_cliente = []
            self.my_cursor.execute("SELECT id_cliente FROM Clientes")
            select = self.my_cursor.fetchall()
            for c in select:
                lista_cliente.append(c[0])
            id_cliente = choice(lista_cliente)

            # Seleciona id do Livro.
            lista_livro = []
            self.my_cursor.execute("SELECT id_livro FROM Livros")
            select = self.my_cursor.fetchall()
            for c in select:
                lista_livro.append(c[0])
            id_livro = choice(lista_livro)

            # Valores para a Data que Pegou o livro.
            ano_pegou = datetime.today().year
            mes_pegou = randrange(1, 12)
            dia_pegou = randrange(1, 30)
            data_pegou = str(ano_pegou) + '-' + str(mes_pegou) + '-' + str(dia_pegou)

            # Valores para a Data que Devolve o livro.
            ano_devolve = datetime.today().year
            mes_devolve = mes_pegou
            dia_devolve = dia_pegou + 8
            if dia_devolve > 30:
                dia_devolve = dia_devolve - 8
                mes_devolve += 1
            data_devolve = str(ano_devolve) + '-' + str(mes_devolve) + '-' + str(dia_devolve)

            # Status.
            status = 1

            self.my_cursor.execute(
                """INSERT INTO Emprestimo VALUES(DEFAULT, {}, {}, '{}', '{}', {})""".format(id_cliente, id_livro,
                                                                                            data_pegou, data_devolve,
                                                                                            status))


usuario = GeradorDados()
usuario.Gerador_Emprestimo()
