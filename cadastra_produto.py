import pandas as pd
from tasks import Tasks


class Cadastro():

    @staticmethod
    def CadastraProdutos(email, password, file):
        url_alia = "https://painel.aliainclui.com.br/login"
        arquivo = file
        data_frame = pd.read_excel(arquivo)

        Tasks.AbrePainelAlia(url_alia)
        Tasks.EfetuaLogin(email, password)

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
