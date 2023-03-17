import pandas as pd
from automations import Tasks


arquivo = "produtos.xlsx"
data_frame = pd.read_excel(arquivo)
url_alia = "https://painel.aliainclui.com.br/login"
login_email = "michaelcristianodesouza@gmail.com"
login_password = "Strike09@"


class Cadastro():

    def CadastraProdutos(data_frame):
        Tasks.AbrePainelAlia(url_alia)
        Tasks.EfetuaLogin(login_email, login_password)

        for index, row in data_frame.iterrows():
            barcode_produto = row["Código de Barras"]
            titulo_produto = row["Título"]
            nome_produto = row["Nome"]
            marca_produto = row["Marca"]
            peso_produto = row["Peso"]
            empresa_produto = row["Empresa"]
            descricao_produto = row["Descrição"]

            Tasks.AbreCadastroDeProdutos()
            Tasks.InsereImagem()
            Tasks.PreencheCampos(barcode_produto,
                                 titulo_produto,
                                 nome_produto,
                                 marca_produto,
                                 peso_produto,
                                 empresa_produto,
                                 descricao_produto)
        Tasks.CloseBrowser()


Cadastro.CadastraProdutos(data_frame)
