"""
-Inicializa o sistema
-Contém a classe App responsável pela criação
 de toda a base do sistema incluindo a janela
 do gerenciador, a janela do sistema, os layouts
 tanto das janelas quanto das guias contidas no
 sistema.
-Métodos da Classe App:
 A classe App contém métodos para criação das janelas e
 layouts, um método para atualizar a Treeview e outro para
 mostrar as informações de entrada no cadastro de uma pessoa.
"""
from tkinter import Tk, Button, Toplevel,LabelFrame,\
                    RAISED, Frame, Label, Entry,\
                    GROOVE, SOLID, W, CENTER, E
from tkinter import ttk, messagebox, PhotoImage
import webbrowser
from logic.data_manipulation import Manipulador
from logic.database import GuardaDados


class App(Tk):
    """
    Classe principal do sistema:
    -Cria a janela 'Gerenciador - Registerthon'
    -Cria a janela que traz acesso às guias 'Cadastro' e 'Exibição'
    -Contém o layout das guias
    -Contém o método para atualizar a Treeview
    -Contém o método para mostrar as informações de entrada na tela.
    """

    def __init__(self):
        Tk.__init__(self)
        self.title('Gerenciador Registerthon')
        self.geometry('400x120')
        self.resizable(False, False)
        self.configure(bg='cornflowerblue')

    tree = ''

    @classmethod
    def mostrar_informacao(cls):
        """
        -Mostra um mensagem informativa sobre as restrições das entradas de dados no registro.
        """
        messagebox.showinfo(
            title='Informações',
            message='- Os campos precedidos por um asterisco (*) são obrigatórios;\n'
                    '- Os campos CPF, Telefone, Celular e Nº devem conter apenas números;\n'
                    '- O CPF deve conter 11 dígitos.')

    @classmethod
    def criar_widgets_app(cls):
        """
        -Cria o botão que serve para inicializar o sistema no gerenciador Registerthon
        -Cria o ícone das janelas
        """
        iniciar = Button(app, text='Iniciar', command=app.criar_widgets_cadastro,
                         font='Arial 10 bold', borderwidth=2, bg='gold')
        iniciar.grid(column=0, row=0, pady=94, ipadx=40)

        sobre = Button(app, text='Sobre', font='Arial 10 bold',
                       borderwidth=2, bg='gold', command=app.criar_widgets_sobre)
        sobre.grid(column=1, row=0, padx=20, ipadx=40)

        app.iconphoto(True, PhotoImage(file='icons/favicon32.png'))

    @classmethod
    def callback(cls, url):
        """
        -Recebe uma URL e pede a requisição.
        """
        webbrowser.open_new(url)

    @classmethod
    def criar_widgets_sobre(cls):
        """
        -Cria a janela 'Sobre Registerthon' junto com seus widgets.
        """
        # JANELA
        janela_sobre = Toplevel(app)
        janela_sobre.geometry('602x402')
        janela_sobre.title('Sobre Registerthon')
        janela_sobre.configure(background='blue')
        janela_sobre.resizable(False, False)

        # NOTEBOOK
        gerenciador_abas = ttk.Notebook(janela_sobre)
        gerenciador_abas.place(x=0, y=0, width=602, height=402)

        # FRAME
        painel_sobre = Frame(gerenciador_abas, borderwidth=2, bg='Teal')
        painel_sobre.place(x=0, y=40, width=600, height=400)

        gerenciador_abas.add(painel_sobre, text='Sobre')

        # LABEL
        Label(painel_sobre, text='Registerthon 0.2.2 - é um sistema de cadastro simples'
                                 ' desenvolvido pelo estudante Nilson Santos. O programa'
                                 ' permite registrar, alterar, deletar e pesquisar'
                                 ' cadastros.',
              font='pacifico 16 bold', bg='springgreen', wraplength=500, fg='black',
              justify='left').pack(pady=10)

        acessar_projeto = Label(painel_sobre, text='Acessar Projeto', cursor='hand2',
                                font='Arial 14 underline bold', fg='blue', bg='teal')
        acessar_projeto.pack(side='top', anchor='nw', ipadx=50, ipady=10)
        acessar_projeto.bind(
            '<Button-1>', lambda e: app.callback('https://github.com/Nilsonsantos-s/Registerthon'))

        Label(painel_sobre, text='MINHAS REDES', font='Arial 15 bold',
              bg='gold').pack(side='top', anchor='ce', pady=10, fill='both')

        github = Label(painel_sobre, text='Github', cursor='hand2',
                  font='Arial 13 underline bold', bg='teal')
        github.pack(side='top', anchor='ce', ipadx=50, ipady=10)
        github.bind('<Button-1>',
                    lambda e: app.callback('https://github.com/Nilsonsantos-s'))

        linkedin = Label(painel_sobre, text='Linkedin', bg='teal',
                  cursor='hand2', font='Arial 13 underline bold')
        linkedin.pack(side='top', anchor='ce', ipadx=50, ipady=10)
        linkedin.bind('<Button-1>',
                      lambda e: app.callback('https://www.linkedin.com/in/nilson-santos-7306a9210/'))

        email = Label(painel_sobre, text='E-mail: Nilsonc.s@outlook.com',font='Arial 13 underline bold', bg='teal',
                  cursor='hand2')
        email.pack(side='top', anchor='ce', ipadx=50, ipady=10)
        email.bind('<Button-1>', lambda e: app.callback('mailto:nilsonc.s@outlook.com'))

    @classmethod
    def criar_widgets_cadastro(cls):
        """
        -Cria e configura a janela do sistema
        -Invoca o método app.criar_widgets_exibicao(cls, frame)
         responsável por construir o layout da guia 'Exibição'
        -Invoca o método app.atualizar_arvore() responsável
         por atualizar a Treeview com os dados contidos
         no banco de dados.

         BOTÕES
         Botão para Salvar Registro
         -Invoca o método Manipulador.inserir_dados(*dados) responsável
          por pegar os dados das entradas e inserí-los no banco de dados.

         Botão para Limpar Tudo
         -Invoca o método Manipulador.limpar_cadastro(*dados) responsável
          por pegar os dados da entrada e deletar cada um.

         Botão para Ver Informações de Entrada
         -Invoca o método app.mostrar_informacao() responsável
          por gerar uma messagebox com informações referentes
          à entrada de dados.
        """

        # JANELA
        janela_cadastro = Toplevel(app)
        janela_cadastro.geometry('602x402')
        janela_cadastro.title('Registerthon 0.2.2')
        janela_cadastro.configure(background='blue')
        janela_cadastro.resizable(False, False)

        # NOTEBOOK
        gerenciador_abas = ttk.Notebook(janela_cadastro)
        gerenciador_abas.place(x=0, y=0, width=602, height=402)

        # LABELFRAME
        painel_cadastro = Frame(gerenciador_abas, borderwidth=2, bg='Teal')
        painel_cadastro.place(x=0, y=40, width=600, height=400)

        gerenciador_abas.add(painel_cadastro, text='Cadastro')

        cadastro_principal = LabelFrame(
            painel_cadastro, text='Dados Principais', font='Arial 15 bold',
            borderwidth=2, bg='MediumSeaGreen', fg='gold', relief=RAISED)
        cadastro_principal.place(x=0, y=10, width=500, height=150)

        cadastro_endereco = LabelFrame(
            painel_cadastro, text='Endereço', font='Arial 15 bold',
            borderwidth=2, bg='MediumSeaGreen', fg='gold', relief=RAISED)
        cadastro_endereco.place(x=0, y=180, width=500, height=150)

        painel_exibicao = Frame(gerenciador_abas, bg='Teal')
        painel_exibicao.place(x=0, y=40, width=600, height=400)

        gerenciador_abas.add(painel_exibicao, text='Exibição')

        app.criar_widgets_exibicao(painel_exibicao)

        # __________________________PAINEL DE DADOS PRINCIPAIS__________________________

        # LABEL--------------------
        # Coluna 0
        Label(
            cadastro_principal, text='*CPF:',
            bg='MediumSeaGreen').grid(column=0, row=0, sticky=W)
        Label(
            cadastro_principal, text='*Nome:',
            bg='MediumSeaGreen').grid(column=0, row=1, sticky=W)
        Label(
            cadastro_principal, text='*Sobrenome:',
            bg='MediumSeaGreen').grid(column=0, row=2, sticky=W)
        Label(
            cadastro_principal, text='E-mail:',
            bg='MediumSeaGreen').grid(column=0, row=3, sticky=W)

        # Coluna 2
        Label(
            cadastro_principal, text='Telefone:',
            bg='MediumSeaGreen').grid(column=2, row=1, padx=5, sticky=W)
        Label(
            cadastro_principal, text='Celular:',
            bg='MediumSeaGreen').grid(column=2, row=2, padx=5, sticky=E)

        # ENTRY--------------------
        # Coluna 1
        entrada_cpf = Entry(cadastro_principal, relief=GROOVE)
        entrada_cpf.grid(column=1, row=0, pady=5)
        entrada_nome = Entry(cadastro_principal, relief=GROOVE)
        entrada_nome.grid(column=1, row=1, pady=5)
        entrada_sobrenome = Entry(cadastro_principal, relief=GROOVE)
        entrada_sobrenome.grid(column=1, row=2, pady=5)
        entrada_email = Entry(cadastro_principal, relief=GROOVE)
        entrada_email.grid(column=1, row=3, pady=5, ipadx=100, columnspan=10)

        # Coluna 3
        entrada_telefone = Entry(cadastro_principal, relief=GROOVE)
        entrada_telefone.grid(column=3, row=1)
        entrada_celular = Entry(cadastro_principal, relief=GROOVE)
        entrada_celular.grid(column=3, row=2, pady=5)

        # __________________________PAINEL DE ENDEREÇO__________________________

        # LABEL--------------------
        # Coluna 0
        Label(
            cadastro_endereco, text='Rua:',
            bg='MediumSeaGreen').grid(column=0, row=0, sticky=W, pady=5)
        Label(
            cadastro_endereco, text='Nº:',
            bg='MediumSeaGreen').grid(column=0, row=1, sticky=W, pady=5)

        # Coluna 2:
        Label(
            cadastro_endereco, text='Bairro:',
            bg='MediumSeaGreen').grid(column=2, row=0, sticky=W, pady=5)
        Label(
            cadastro_endereco, text='Cidade:',
            bg='MediumSeaGreen').grid(column=2, row=1, sticky=W, pady=5)
        Label(
            cadastro_endereco, text='Estado:',
            bg='MediumSeaGreen').grid(column=2, row=2, sticky=W, pady=5)

        # ENTRY--------------------
        # Coluna 1
        entrada_rua = Entry(cadastro_endereco, relief=GROOVE, width=25)
        entrada_rua.grid(column=1, row=0, padx=5, pady=5)
        entrada_numero = Entry(cadastro_endereco, relief=GROOVE, width=7)
        entrada_numero.grid(column=1, row=1, padx=4, sticky=W, pady=5)

        # Coluna 3
        entrada_bairro = Entry(cadastro_endereco, relief=GROOVE, width=25)
        entrada_bairro.grid(column=3, row=0, pady=5)
        entrada_cidade = Entry(cadastro_endereco, relief=GROOVE, width=25)
        entrada_cidade.grid(column=3, row=1, pady=5)
        entrada_estado = Entry(cadastro_endereco, relief=GROOVE, width=10)
        entrada_estado.grid(column=3, row=2, pady=5, padx=0, sticky=W)

        # __________________________BUTTON__________________________
        Button(painel_cadastro, text='Salvar Registro',
               relief=SOLID, borderwidth=2, font='Arial 10',
               command=lambda: Manipulador.inserir_dados(
                   entrada_cpf.get(), entrada_nome.get(), entrada_sobrenome.get(),
                   entrada_email.get(), entrada_telefone.get(), entrada_celular.get(),
                   entrada_rua.get(), entrada_numero.get(), entrada_bairro.get(),
                   entrada_cidade.get(), entrada_estado.get())).place(x=30, y=340, width=100)

        Button(painel_cadastro, text='Limpar Tudo', relief=SOLID, borderwidth=2, font='Arial 10',
               command=lambda: Manipulador.limpar_cadastro(
                   entrada_cpf, entrada_nome, entrada_sobrenome, entrada_celular,
                   entrada_telefone, entrada_email, entrada_rua, entrada_numero,
                   entrada_bairro, entrada_cidade, entrada_estado)).place(x=380, y=340, width=100)

        Button(painel_cadastro, text='Ver Informações de Entrada',
               relief=SOLID, borderwidth=2, font='Arial 10 bold', fg='red', bg='gold',
               command=app.mostrar_informacao).place(x=161, y=340)

        app.atualizar_arvore()

    @classmethod
    def atualizar_arvore(cls):
        """
        -Recebe os dados do banco de dados através da
         invoção do método GuardaDados.carregar_dados_banco()
        -Invoca a função Manipulador.subir_dados_na_arvore(dados)
         que pega os dados e insere-os na Treeview.
        """
        dados = GuardaDados.carregar_dados_banco()
        Manipulador.subir_dados_na_arvore(dados)

    @classmethod
    def criar_widgets_exibicao(cls, frame):
        """
        :param frame: Recebe um frame configurado como guia
        -Constrói o layout contido no frame

        BOTÕES
        Botão para Pesquisar
        -Invoca o método Manipulador.pesquisar(entrada, opcoes) responsável
         por pegar a input da entry 'entrada_pesquisa' e também pegar a opção
         contida no Combobox 'opcoes' e com eles realizar a consulta dos dados
         e a atualização na Treeview.

        Botão para Apagar
        -Invoca o método Manipulador.deletar_registro() que
         exclui os registros selecionados na Treeview

        Botão para Obter
        -Invoca o método Manipulador.abrir_nova_janela() responsável
         por criar uma nova janela contendo os dados do registro
         selecionado na Treeview

        Botão para Mostrar Todos
        -Invoca a método app.atualizar_arvore() responsável
         por atualizar a Treeview com os dados contidos
         no banco de dados.
        """

        # TREEVIEW--------------------
        arvore = ttk.Treeview(frame, columns=('CPF', 'NOME', 'SOBRENOME'), show='headings')
        arvore.column('CPF', minwidth=0, width=90, anchor=CENTER)
        arvore.column('NOME', minwidth=0, width=100, anchor=CENTER)
        arvore.column('SOBRENOME', minwidth=0, width=180, anchor=CENTER)
        arvore.heading('CPF', text='CPF', anchor=CENTER)
        arvore.heading('NOME', text='NOME', anchor=CENTER)
        arvore.heading('SOBRENOME', text='SOBRENOME', anchor=CENTER)
        arvore.place(x=50, y=10, width=500, height=250)
        Manipulador.copia_arvore = arvore

        # LABELFRAME--------------------
        painel_pesquisa = LabelFrame(frame, text='Pesquisar Registros',
                                     font='Arial 12 bold', fg='gold',
                                     borderwidth=2, bg='MediumSeaGreen', relief=RAISED)
        painel_pesquisa.place(x=60, y=280, width=275, height=60)
        lista = ['CPF', 'NOME']

        opcoes = ttk.Combobox(painel_pesquisa, values=lista, width=6)
        opcoes.set('NOME')
        opcoes.grid(column=0, row=0)

        # ENTRY--------------------
        entrada_pesquisa = Entry(painel_pesquisa, width=20)
        entrada_pesquisa.grid(column=1, row=0, ipady=1, padx=5, pady=10)

        # BUTTON--------------------
        Button(frame, text='Pesquisar', relief=SOLID,
               command=lambda: Manipulador.pesquisar(
                   entrada_pesquisa.get(), opcoes.get())).place(x=260, y=300, width=60, height=30)
        Button(frame, text='Apagar', relief=SOLID,
               command=Manipulador.deletar_registro).place(x=350, y=300, width=70, height=30)
        Button(frame, text='Obter', relief=SOLID,
               command=Manipulador.abrir_nova_janela).place(x=450, y=300, width=70, height=30)
        Button(frame, text='Mostrar Todos', relief=SOLID,
               command=app.atualizar_arvore).place(x=60, y=345, height=25, width=100)


app = App()
app.criar_widgets_app()
app.mainloop()
