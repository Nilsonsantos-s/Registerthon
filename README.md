# Registerthon
## **Descrição**
Sistema de cadastro integrado com banco de dados MySQL e com interface gráfica criada através da biblioteca tkinter. Insere, exclui, altera e pesquisa registros.

___

- ## Como usar
### Instalando
Clone este repositório:

```git clone https://github.com/Nilsonsantos-s/Registerthon.git```

### Configurando

Para rodar o sistema é necessário possuir o sistema gerenciador de banco de dados MySQL e conhecimento básico de criação de banco de dados e tabelas.

Passo a passo para fazer a configuração:

<ol>
    <li>Crie um banco de dados chamado registerthon_sistema</li>
    <li>Crie uma tabela chamada pessoas contendo as seguintes colunas: cpf, nome, sobrenome, email, telefone, celular, rua, numero, bairro, cidade, estado. A coluna 'cpf' deve ser do tipo char(11), todas as outras colunas devem ser do tipo varchar, no mínimo 20 para telefone e celular, 10 para número e 50 para as outras colunas.</li>
    <li>Dentro da pasta do projeto, abra o arquivo 'database.py' com um editor ou uma IDE e na seção de conexão com o banco de dados coloque as informações requeridas como o tipo de host, o usuário e a senha (está comentado no código o que é necessário colocar)</li>
</ol>

Feito esses procedimentos, o sistema não deve apresentar erro algum em relação à conexão com o banco de dados. A próxima etapa é executar o sistema.

### Executando o Sistema

Verifique se a conexão com o MySQL está ativa. Após isso:

<ol>
    <li>Abra o CMD ou PowerShell</li>
    <li>Entre no repositório, na pasta "Registerthon"</li>
    <li>Rode o comando: <code>python system.py</code></li>
</ol>

