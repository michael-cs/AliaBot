![logoAliaBot](https://user-images.githubusercontent.com/103940775/227815676-dbb162a0-87c1-4e22-9bb5-f6bbb25fcdcc.jpg)

# Alia Bot

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

### Tópicos

🔹 [Descrição do projeto](#descrição-do-projeto)

🔹 [Funcionalidades](#funcionalidades)

🔹 [Download da Aplicação](#download-da-aplicação)

🔹 [Linguagens e libs utilizadas](#linguagens-e-libs-utilizadas)

🔹 [Como rodar a aplicação](#como-rodar-a-aplicação)

## Descrição do projeto

Projeto de RPA em Python para acesso ao painel da empresa Alia Inclui (https://painel.aliainclui.com.br/login), com o objetivo de cadastrar os produtos conforme planilha padronizada pela empresa.
Com isto,as empresas aliadas que contratarem os serviços de acessibilidade de rótulo da Alia, poderão enviar a planilha preenchida e sua base de produtos será cadastrada sem a
necessidade de manter um colaborador efetuando a tarefa de inserção dos dados um a um. Evita-se assim o uso de mão de obra técnica para a tarefa e minimiza-se o fator
de erro humano nos cadastros.

## Funcionalidades

✔️ Funcionalidade 1

GUI para interação entre o usuário e o sistema de cadastramento, onde o usuário precisa informar seu email e senha de acesso ao painel, além da planilha de dados a ser
utilizada como fonte de dados para os cadastros. Nesta primeira versão, estaremos utilizando a planilha padrão "produtos.xlsx" contida na pasta do projeto.

✔️ Funcionalidade 2

Cadastramento básico de produtos, contendo: imagem padrão, barcode, título, nome do produto, marca, peso, empresa aliada, descrição do produto.

❌ Funcionalidade 3

TODO:Criação de regras de validação para o preenchimento de campos, onde o usuário recebe um alerta caso digite um email fora de padrão ou não preencha um dos campos, etc.

❌ Funcionalidade 4

TODO:Criação de lógica de cadastramento de seções, sendo esta uma aba opcional a ser utilizada quando necessário cadastro completo do produto. Neste tipo de cadastro
a empresa aliada pode disponibilizar ao usuário final informações extras e segmentadas de forma a facilitar a leitura com assistentes de acessibilidade dos smartphones
através de gestos de varredura, podendo ir diretamente a seção desejada sem ter de ouvir toda a descrição do produto.

## Download da Aplicação

💡 Link para downlad da aplicação(pasta zipada, contendo nesta, o arquivo executável "AliaBot.exe"):
https://drive.google.com/file/d/bc1qzk3kxhdxnzkpdgdn9ueg34y08smxgfv0hxvcu3-wu5z5E/view?usp=share_link

## Linguagens e libs utilizadas

🐍 Python
📚 Selenium
📚 Custom Tkinter
📚 Pandas

## Como rodar a aplicação

Baixe a pasta zipada (link no ítem "Download da Aplicação), e após descompacta-la, execute o arquivo "AliaBot.exe". O programa irá abrir o navegador Chrome em plano de fundo
e a GUI abaixo estará disponível:

![gui](https://user-images.githubusercontent.com/103940775/227797709-f30a0eaf-b9ee-48ce-80c6-fb49f5035247.JPG)

Preencha os campos com as informações de acesso ao portal Alia e clique em "Iniciar Cadastro". Automaticamente o navegador em segundo plano irá iniciar o cadastro dos
produtos conforme dados contidos na planilha "produtos.xlsx" contida na pasta do programa.
Os produtos cadastrados poderão ser localizados conforme mostrado no exemplo abaixo:

![produto_cadastrado_com_sucesso](https://user-images.githubusercontent.com/103940775/227797860-28e22525-58ea-4b8a-854b-ac7a54b2913b.JPG)
