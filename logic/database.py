"""
-Manipula o banco de dados
"""
from tkinter import messagebox
import pymysql


class GuardaDados:
    """
    Classe responsável pelo banco de dados:
    -Realiza a inserção, alteração, exclusão e consulta no
     banco de dados
    """
    conexao = pymysql.connect(
        host='localhost',  # Insira o tipo de host
        user='root',  # Coloque o nome do usuário do banco
        password='',  # Insira a senha do usuário
        db='registerthon_sistema',  # Coloque o nome do banco criado
        port=3306
    )
    comando = conexao.cursor()

    @classmethod
    def consultar_no_banco(cls, entrada, cpf=False):
        """
        :param entrada: Recebe uma entrada que pode ser o nome
                        ou o cpf
        :param cpf: Para caso a entrada seja um cpf
        :return: Retorna os dados da consulta
        """
        if cpf is True:
            GuardaDados.comando.execute(
                f"select * from pessoas where cpf like '%{entrada}%' order by nome, sobrenome")
            resultado_consulta = GuardaDados.comando.fetchall()
            return resultado_consulta
        GuardaDados.comando.execute(
            f"select * from pessoas where nome like '%{entrada}%' order by nome, sobrenome")
        resultado_consulta = GuardaDados.comando.fetchall()
        return resultado_consulta

    @classmethod
    def persistir_dados_no_banco(cls, dados):
        """
        :param dados: Recebe os dados das entradas
        -Insere os dados no banco de dados
        """
        GuardaDados.comando.execute(
            f"insert into pessoas values('{dados[0]}', '{dados[1]}', '{dados[2]}', '{dados[3]}',"
            f" '{dados[4]}', '{dados[5]}', '{dados[6]}', '{dados[7]}', '{dados[8]}', '{dados[9]}',"
            f" '{dados[10]}');")
        GuardaDados.conexao.commit()

    @classmethod
    def carregar_dados_banco(cls):
        """
        -Realiza uma consulta geral no banco de dados
         ordenando por nome e sobrenome.
        :return: Retorna os dados da consulta
        """
        GuardaDados.comando.execute("select * from pessoas order by nome, sobrenome")
        resultado = GuardaDados.comando.fetchall()
        return resultado

    @classmethod
    def carregar_linha_unica(cls, cpf):
        """
        :param cpf: Recebe um cpf
        :return: Retorna o registro referente ao cpf
        """
        GuardaDados.comando.execute(f"select * from pessoas where cpf = {cpf};")
        resultado = GuardaDados.comando.fetchall()
        return resultado

    @classmethod
    def excluir_dados_banco(cls, cpfs):
        """
        :param cpfs: Recebe todos os cpfs dos registros selecionados
                     na Treeview
        -No banco de dados, exclui os registros referentes a cada
         cpf se o tamanho da coleção recebida for maior que 1.
        -Caso contrário, exclui apenas o primeiro item da coleção.
        """
        if len(cpfs) == 1:
            GuardaDados.comando.execute(f"delete from pessoas where cpf = '{cpfs[0]}';")
            GuardaDados.conexao.commit()
        if len(cpfs) > 1:
            for cpf in cpfs:
                GuardaDados.comando.execute(f"delete from pessoas where cpf = '{cpf}';")
                GuardaDados.conexao.commit()

    @classmethod
    def alterar_dados_banco(cls, outputs, cpf):
        """
        :param outputs: Pega o input dos Text widgets
        :param cpf: Recebe o cpf do text widget 'output_cpf' no
                    momento em que o usuário clica no botão
                    'Obter'
        -Faz a alteração dos dados utilizando o cpf e os outputs
        -Em uma alteração de cpf, caso o cpf apresentado, que é o output[0],
         ja estiver registrado no sistema, uma mensagem de erro é apresentada
         e o método retornará a variável lógica 'erro' com o valor verdadeiro.
        """
        try:
            tupla_nome_dados = ('cpf', 'nome', 'sobrenome', 'email', 'telefone', 'celular',
                                'rua', 'numero', 'bairro', 'cidade', 'estado')
            contador = 0
            for nome_dado in tupla_nome_dados:
                if contador == 0:
                    GuardaDados.comando.execute(
                        f"update pessoas set cpf = {outputs[0]} where cpf = {cpf};")
                    GuardaDados.conexao.commit()
                GuardaDados.comando.execute(
                    f"update pessoas set {nome_dado} = '{outputs[contador].upper()}' where cpf = '{outputs[0]}';")
                GuardaDados.conexao.commit()
                contador += 1
            return None
        except pymysql.err.IntegrityError:
            messagebox.showerror('ERRO', 'CPF já registrado no sistema')
            erro = True
            return erro
