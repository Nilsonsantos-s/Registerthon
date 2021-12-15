"""
-Manipula dados no sistema e cria a janela para visualizar registros
"""
from tkinter import Toplevel, Label, LabelFrame, RAISED,\
                    FLAT, Text, INSERT, Button,\
                    W, SOLID, END
from tkinter import messagebox
import pymysql.err

from logic.database import GuardaDados


class Manipulador:
    """
    Classe intermediária do Sistema:
    -Realiza a checagem, manipulação, edição, pesquisa, e atualização dos dados
    -Cria e configura a janela que mostra o registro juntamente com seu layout.
    """
    main_contador = 0
    copia_arvore = ''
    cpf = ''

    @classmethod
    def pesquisar(cls, entrada, opcoes):
        """
        :param entrada: Recebe a entrada da pesquisa
        :param opcoes: Recebe a opção para pesquisar
        -Realiza a consulta no banco de dados e atualiza
         os dados na Treeview.
        """
        opcoes = opcoes.lower()
        if entrada.isnumeric() and opcoes == 'cpf':
            resultado_consulta = GuardaDados.consultar_no_banco(entrada, cpf=True)
            Manipulador.subir_dados_na_arvore(resultado_consulta)
        elif entrada.isnumeric() is False and opcoes == 'nome':
            resultado_consulta = GuardaDados.consultar_no_banco(entrada)
            Manipulador.subir_dados_na_arvore(resultado_consulta)

    @classmethod
    def subir_dados_na_arvore(cls, dados):
        """
        :param dados: Recebe os dados da consulta no banco de dados
        -Realiza a inserção dos valores na Treeview.
        """
        if Manipulador.copia_arvore.get_children():
            for dado in Manipulador.copia_arvore.get_children():
                Manipulador.copia_arvore.delete(dado)
        for dado in dados:
            Manipulador.copia_arvore.insert('', 'end', values=dado)

    @classmethod
    def checagem_de_dados(cls, dados, edicao=False):
        """
        :param dados: Recebe os dados das entradas
        :param edicao: Se os dados forem referentes a edição
        :return: Retorna um resultado lógico:
                -Falso se alguma dos condições forem falsas
                -Verdadeiro se todos os condições forem verdadeiras
        """
        resultado_logico = False
        if edicao is False:
            if not dados[0] or not dados[1] or not dados[2]:
                if not dados[0] and not dados[1] and not dados[2]:
                    messagebox.showerror(title='ERRO',
                                         message='CPF, Nome, Sobrenome são campos obrigatórios')
                elif not dados[0] and not dados[1]:
                    messagebox.showerror(title='ERRO',
                                         message='CPF, Nome são campos obrigatórios')
                elif not dados[0] and not dados[2]:
                    messagebox.showerror(title='ERRO',
                                         message='CPF, Sobrenome são campos obrigatórios')
                elif not dados[1] and not dados[2]:
                    messagebox.showerror(title='ERRO',
                                         message='Nome, Sobrenome são campos obrigatórios')
                elif not dados[0]:
                    messagebox.showerror(title='ERRO',
                                         message='CPF é um campo obrigatório')
                elif not dados[1]:
                    messagebox.showerror(title='ERRO',
                                         message='Nome é um campo obrigatório')
                elif not dados[2]:
                    messagebox.showerror(title='ERRO',
                                         message='Sobrenome é um campo obrigatório')
            elif dados[0].isnumeric() is False:
                messagebox.showerror(title='ERRO',
                                     message='O campo CPF deve conter apenas números.')
            elif len(dados[0]) != 11:
                messagebox.showerror(title='ERRO',
                                     message='O campo CPF deve compor 11 dígitos')
            elif dados[4] and dados[4].isnumeric() is False:
                messagebox.showerror(title='ERRO',
                                     message='O campo Telefone deve conter apenas números.')
            elif dados[5] and dados[5].isnumeric() is False:
                messagebox.showerror(title='ERRO',
                                     message='O campo Celular deve conter apenas números.')
            elif dados[7] and dados[7].isnumeric() is False:
                messagebox.showerror(title='ERRO',
                                     message='O campo Nº deve conter apenas números.')
            else:
                resultado_logico = True
        elif edicao is True:
            if not dados[0] or not dados[1] or not dados[2]:
                if not dados[0] and not dados[1] and not dados[2]:
                    messagebox.showerror(title='ERRO',

                                         message='CPF, Nome, Sobrenome são campos obrigatórios')
                elif not dados[0] and not dados[1]:
                    messagebox.showerror(title='ERRO',

                                         message='CPF, Nome são campos obrigatórios')
                elif not dados[0] and not dados[2]:
                    messagebox.showerror(title='ERRO',

                                         message='CPF, Sobrenome são campos obrigatórios')
                elif not dados[1] and not dados[2]:
                    messagebox.showerror(title='ERRO',

                                         message='Nome, Sobrenome são campos obrigatórios')
                elif not dados[0]:
                    messagebox.showerror(title='ERRO',

                                         message='CPF é um campo obrigatório')
                elif not dados[1]:
                    messagebox.showerror(title='ERRO',

                                         message='Nome é um campo obrigatório')
                elif not dados[2]:
                    messagebox.showerror(title='ERRO',

                                         message='Sobrenome é um campo obrigatório')
            elif dados[0].isnumeric() is False:
                messagebox.showerror(title='ERRO',

                                     message='O campo CPF deve conter apenas números.')
            elif len(dados[0]) != 11:
                messagebox.showerror(title='ERRO',

                                     message='O campo CPF deve compor 11 dígitos')
            elif dados[4].isnumeric() is False and dados[4] != '---':
                messagebox.showerror(title='ERRO',

                                     message='O campo Telefone deve conter apenas números.')
            elif dados[5].isnumeric() is False and dados[5] != '---':
                messagebox.showerror(title='ERRO',

                                     message='O campo Celular deve conter apenas números.')
            elif dados[7].isnumeric() is False and dados[7] != '---':
                messagebox.showerror(title='ERRO',

                                     message='O campo Nº deve conter apenas números.')
            else:
                resultado_logico = True
        return resultado_logico

    @classmethod
    def inserir_dados(cls, *dados):
        """
        :param dados: Recebe os inputs das entries
        -Insere os dados na Treeview e adiciona-os no
         banco de dados.
        """
        resultado_logico = Manipulador.checagem_de_dados(dados)
        if resultado_logico:
            try:
                lista_dados = list(dados)
                for contador in range(0, len(lista_dados)):
                    if not lista_dados[contador]:
                        lista_dados[contador] = '---'
                    lista_dados[contador] = lista_dados[contador].upper()
                Manipulador.copia_arvore.insert('', 'end', values=lista_dados)
                GuardaDados.persistir_dados_no_banco(lista_dados)
                dados = GuardaDados.carregar_dados_banco()
                Manipulador.subir_dados_na_arvore(dados)
            except pymysql.err.IntegrityError:
                messagebox.showerror('ERRO', 'CPF já cadastrado no sistema')

    @classmethod
    def limpar_cadastro(cls, *entradas):
        """
        :param entradas: Recebe os inputs das entries
        -Apaga cada input
        """
        for entrada in entradas:
            entrada.delete(0, END)

    @classmethod
    def deletar_registro(cls):
        """
        -Se nenhum registro for selecionado na Treeview:
            O usuário recebe uma mensagem de erro.
        Caso algum registro seja selecionado:
            -Pega os registros selecionados
            -Mostra uma mensagem de confirmação da exclusão dos dados
            -Caso a mensagem seja 'Sim':
                -Exclui esses valores, atualizando
                 a Treeview e removendo os dados
                 no banco de dados.
            -Caso o usuário clique em 'Cancelar':
                Nenhuma ação é realizada.
        """
        try:
            registro_selecionado = Manipulador.copia_arvore.selection()[0]
            registros_selecionados = Manipulador.copia_arvore.selection()
            if len(registros_selecionados) == 1:
                valores = Manipulador.copia_arvore.item(registros_selecionados, "values")
                cpf = [valores[0]]
                confirmacao = messagebox.askokcancel(
                    'Confirmação', 'Tem certeza de que quer excluir este registro?')
                if confirmacao is True:
                    Manipulador.copia_arvore.delete(registro_selecionado)
                    GuardaDados.excluir_dados_banco(cpf)
                else:
                    pass
            elif len(registros_selecionados) > 1:
                confirmacao = messagebox.askokcancel(
                    'Confirmação', 'Tem certeza de que quer excluir este registro?')
                if confirmacao is True:
                    cpfs = []
                    for linha in registros_selecionados:
                        valores = Manipulador.copia_arvore.item(linha, 'values')
                        cpfs.append(valores[0])
                    GuardaDados.excluir_dados_banco(cpfs)
                else:
                    pass

        except IndexError:
            messagebox.showerror('ERRO', message='Selecione um registro a ser deletado')
        finally:
            dados = GuardaDados.carregar_dados_banco()
            Manipulador.subir_dados_na_arvore(dados)

    @classmethod
    def obter_registro(cls):
        """
        -Recebe os dados selecionados
        :return: Retorna os valores dos dados.
        """
        item_selecionado = Manipulador.copia_arvore.selection()[0]
        valores = Manipulador.copia_arvore.item(item_selecionado, 'values')
        return valores

    @classmethod
    def receber_app(cls, app=None):
        """
        :param app: Recebe o objeto app
        :return: Retorna o objeto
        """
        return app

    @classmethod
    def abrir_nova_janela(cls):
        """
        -Cria uma janela contendo os dados do registro obtido

        BOTÕES

        Botão para Restaurar Dados
        -Invoca a função Manipulador.restaurar_dados(*outputs, cpf)
         responsável por pegar os inputs dos widgets tipo Text no
         momento em que o usuário abre uma janela através do botão
         'Obter' e depois insere os inputs dos dados nos Text widgets.

        Botão para Salvar Edição
        -Invoca o método Manipulador.salvar_edicao(*ouputs, cpf)
         responsável por pegar os inputs dos widgets tipo Text a
         partir da sua edição, fazer a alteração dos dados no banco
         de dados, restaurar os dados na janela e atualizar a Treeview.
        """
        Manipulador.main_contador = 0
        try:
            dados = Manipulador.obter_registro()
        except IndexError:
            messagebox.showerror(
                'ERRO', message='Selecione um registro a ser obtido')
        else:
            app = Manipulador.receber_app()
            janela_registro = Toplevel(app)
            janela_registro.title(dados[1])
            janela_registro.configure(bg='DarkGoldenrod')
            janela_registro.geometry('602x402')
            janela_registro.resizable(False, False)

            # LABELFRAME
            painel_dados = LabelFrame(janela_registro, text=dados[1]+' '+dados[2],
                                      bg='Teal', borderwidth=3, font='Arial 14 bold')
            painel_dados.place(x=0, y=10, width=600, height=400)

            dados_principal = LabelFrame(janela_registro, text='Dados Principais',
                                         font='Arial 15', borderwidth=2, fg='gold',
                                         bg='MediumSeaGreen', relief=RAISED)
            dados_principal.place(x=5, y=60, width=570, height=150)

            dados_endereco = LabelFrame(janela_registro, text='Endereço',
                                        font='Arial 15', borderwidth=2,
                                        fg='gold', bg='MediumSeaGreen',
                                        relief=RAISED)
            dados_endereco.place(x=5, y=220, width=570, height=150)

            # __________________________PAINEL DE DADOS PRINCIPAIS__________________________
            # LABEL--------------------

            # Coluna 0
            Label(dados_principal, text='CPF:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=0, row=0, sticky=W)
            Label(dados_principal, text='Telefone:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=0, row=1, sticky=W)
            Label(dados_principal, text='Celular:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=0, row=2, sticky=W)
            Label(dados_principal, text='E-mail:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=0, row=3, sticky=W)

            # Coluna 2
            Label(dados_principal, text='Nome:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=2, row=0, sticky=W, padx=5)
            Label(dados_principal, text='Sobrenome:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=2, row=1, sticky=W, padx=5)

            # LABEL(OUTPUT)--------------------
            # Coluna 1
            output_cpf = Text(dados_principal, font='Arial 9', relief=FLAT, width=11, height=1)
            output_cpf.insert(INSERT, dados[0])
            output_cpf.grid(column=1, row=0, pady=5, sticky=W)

            output_telefone = Text(dados_principal, font='Arial 9', relief=FLAT, width=13, height=1)
            output_telefone.insert(INSERT, dados[4])
            output_telefone.grid(column=1, row=1, sticky=W)

            output_celular = Text(dados_principal, font='Arial 9', relief=FLAT, width=13, height=1)
            output_celular.insert(INSERT, dados[5])
            output_celular.grid(column=1, row=2, pady=5, sticky=W)

            output_email = Text(dados_principal, font='Arial 9', relief=FLAT, width=10, height=1)
            output_email.insert(INSERT, dados[3])
            output_email.grid(column=1, row=3, pady=5, ipadx=50, columnspan=10, sticky=W)

            # Coluna 3
            output_nome = Text(dados_principal, font='Arial 9', relief=FLAT,
                               width=10, height=1)
            output_nome.insert(INSERT, dados[1])
            output_nome.grid(column=3, row=0, pady=5, ipadx=50, columnspan=10, sticky=W)

            output_sobrenome = Text(dados_principal, font='Arial 9',
                                    relief=FLAT, width=10, height=1)
            output_sobrenome.insert(INSERT, dados[2])
            output_sobrenome.grid(column=3, row=1, pady=5, ipadx=50, columnspan=10, sticky=W)

            # __________________________PAINEL DE ENDERECO__________________________
            # LABEL--------------------
            # Coluna 0
            Label(dados_endereco, text='Rua:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=0, row=0, sticky=W, pady=5)
            Label(dados_endereco, text='Nº:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=0, row=1, sticky=W, pady=5)
            # Coluna 2:
            Label(dados_endereco, text='Bairro:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=2, row=0, sticky=W, pady=5)
            Label(dados_endereco, text='Cidade:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=2, row=1, sticky=W, pady=5)
            Label(dados_endereco, text='Estado:', font='Arial 10',
                  bg='MediumSeaGreen').grid(column=2, row=2, sticky=W, pady=5)

            # TEXT(OUTPUT)--------------------
            # Coluna 1
            output_rua = Text(dados_endereco, font='Arial 9', relief=FLAT, width=30, height=1)
            output_rua.insert(INSERT, dados[6])
            output_rua.grid(column=1, row=0, padx=5, pady=5)

            output_numero = Text(dados_endereco, font='Arial 9', relief=FLAT, width=5, height=1)
            output_numero.insert(INSERT, dados[7])
            output_numero.grid(column=1, row=1, padx=4, sticky=W, pady=5)

            # Coluna 3
            output_bairro = Text(dados_endereco, font='Arial 9', relief=FLAT, width=30, height=1)
            output_bairro.insert(INSERT, dados[8])
            output_bairro.grid(column=3, row=0, pady=5, sticky=W)

            output_cidade = Text(dados_endereco, font='Arial 9', relief=FLAT, width=30, height=1)
            output_cidade.insert(INSERT, dados[9])
            output_cidade.grid(column=3, row=1, pady=5, sticky=W)

            output_estado = Text(dados_endereco, font='Arial 9', relief=FLAT, width=10, height=1)
            output_estado.insert(INSERT, dados[10])
            output_estado.grid(column=3, row=2, pady=5, padx=0, sticky=W)

            if Manipulador.main_contador == 0:
                Manipulador.cpf = output_cpf.get('1.0', 'end')

            # BUTTON--------------------
            Button(janela_registro, text='Restaurar Dados', relief=SOLID,
                   command=lambda: Manipulador.restaurar_dados(
                        output_cpf, output_nome, output_sobrenome, output_email, output_telefone,
                        output_celular, output_rua, output_numero, output_bairro, output_cidade,
                        output_estado, cpf=Manipulador.cpf)).place(x=390, y=30)

            Button(janela_registro, text='Salvar Edição', relief=SOLID,
                   command=lambda: Manipulador.realizar_edicao(
                        output_cpf, output_nome, output_sobrenome, output_email, output_telefone,
                        output_celular, output_rua, output_numero, output_bairro, output_cidade,
                        output_estado, cpf=Manipulador.cpf)).place(x=500, y=30)

    @classmethod
    def restaurar_dados(cls, *outputs, cpf, saved=False):
        """
        :param outputs: Recebe os inputs dos widgets tipo Texts na primeira vez em que
                        que o usuário clicar no botão 'Obter'
        :param cpf: Recebe o input do 'output_cpf' na primeira vez em que o usuário clicar
                    no botão 'Obter'
        :param saved: Caso o restaurar_dados seja efetuado após uma alteração de dados
                      em que não houve mensagem de erro, o valor será verdadeiro.
                      Caso contrário, o valor será falso.
        -Carrega os dados utilizando o cpf e depois insere os inputs dos dados nos Text widgets.
        :return:
        """
        Manipulador.main_contador += 1
        cpf_antigo = cpf
        cpf_alterado = outputs[0].get('1.0', 'end')
        if saved is False:
            dados = GuardaDados.carregar_linha_unica(cpf_antigo)
        else:
            Manipulador.cpf = cpf_alterado
            dados = GuardaDados.carregar_linha_unica(cpf_alterado)
        dados = dados[0]

        contador = 0
        for output in outputs:
            output.delete('1.0', 'end')
            output.insert(INSERT, dados[contador])
            contador += 1

    @classmethod
    def realizar_edicao(cls, *outputs, cpf):
        """
        :param outputs: Recebe os inputs dos widgets tipo Text
        :param cpf: Recebe o input do output_cpf na primeira vez
                    em que o usuário clicar no botão 'Obter'
        -Faz a alteração dos dados no banco de dados utilizando
         a variável 'cpf' mudando os valores com os outputs recebidos,
         restaurando os dados na janela e atualizando a Treeview.
        """
        lista_outputs = []
        for pos, output in enumerate(outputs):
            lista_outputs.append(output.get('1.0', 'end'))
            lista_outputs[pos] = lista_outputs[pos].replace('\n', '')
        resultado_logico = Manipulador.checagem_de_dados(
            lista_outputs, edicao=True)
        if resultado_logico:
            confirmacao = messagebox.askokcancel(
                'CONFIRMAÇÃO', 'Tem certeza que deseja salvar a edição?')
            if confirmacao is True:
                copia = cpf
                caso_de_erro = GuardaDados.alterar_dados_banco(lista_outputs, copia)
                dados = GuardaDados.carregar_dados_banco()
                Manipulador.subir_dados_na_arvore(dados)
                if caso_de_erro is True:
                    Manipulador.restaurar_dados(*outputs, cpf=cpf, saved=False)
                else:
                    Manipulador.restaurar_dados(*outputs, cpf=cpf, saved=True)
