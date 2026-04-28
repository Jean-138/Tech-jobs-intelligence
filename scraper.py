import requests # faz requisicoes http

from bs4 import BeautifulSoup # le e interpreta o html que o request baixou

from fake_useragent import UserAgent # faz o scraper paracer um navegador real, evitando o bloqueio do site

import pandas as pd # organiza os dados em tabela

import time # pausa o programa entre requisições para evitar bloqueio do site

import re # importa o módulo de expressões regulares para buscar e manipular padrões de texto

import json # importa o módulo nativo do Python que converte texto JSON em dicionário Python




# funcao para fazer a requisição HTTP à URL informada,
# simulando um navegador real e retornando o HTML da página caso a requisição seja bem-sucedida.


def obter_pagina(url):  # função chamada obter_pagina que recebe uma URL como parâmetro
    ua = UserAgent()  # Cria um objeto UserAgent para gerar um navegador aleatório
    headers = {"User-Agent": ua.random}  # Cria um cabeçalho HTTP com um User-Agent aleatório
    
    response = requests.get(url, headers=headers)  # Faz uma requisição GET para a URL usando os cabeçalhos
    
    if response.status_code == 200:  # Verifica se o código de resposta é 200 (sucesso)
        return response.text  # Retorna o conteúdo HTML da página
    else:  # Caso a requisição não tenha dado certo
        print(f"erro ao acessar pagina {response.status_code}")  # Mostra o código do erro
        return None  # Retorna None indicando que não conseguiu obter a página
    



#funcao para extrair vagas

def extrair_vagas(html):  # define uma função chamada extrair_vagas que recebe o HTML da página
    soup = BeautifulSoup(html, "html.parser")  # Converte o HTML em objeto navegável
    scripts = soup.find_all("script")  # Busca todas as tags <script> do HTML
    
    for script in scripts:  # Itera por cada script encontrado
        if script.string and "__INITIAL_SEARCH_RESULTS__" in script.string:  # Verifica se o script tem texto e contém a variável desejada
            match = re.search(r"window\.__INITIAL_SEARCH_RESULTS__\s*=\s*(\{.*\});", script.string)  # Usa regex para capturar o JSON dentro do script
            if match:  # Se encontrou o padrão
                dados = json.loads(match.group(1))  # Converte o JSON capturado em dicionário Python
                return dados["results"][0]["hits"]  # Retorna a lista de vagas dentro da estrutura do JSON
    return []  # Retorna lista vazia se não encontrar os dados








def extrair_dados_vaga(vaga):  # Define a função que recebe uma vaga (HTML)
    
    try:  # Tenta executar o bloco de código, para evitar que erros quebrem o programa
        titulo = vaga.get("title", "N/A")  # Pega o título da vaga; se não existir, usa "N/A"
        empresa = vaga.get("company_name", "N/A")  # Pega o nome da empresa; padrão "N/A"
        categoria = vaga.get("category", "N/A")  # Pega a categoria da vaga; padrão "N/A"
        tipo = vaga.get("job_type", "N/A")  # Pega o tipo de trabalho (CLT, remoto, etc.); padrão "N/A"
        salario = vaga.get("salary", "N/A")  # Pega o salário; padrão "N/A"
        localizacao = vaga.get("locations", [])  # Pega lista de localizações; se não existir, lista vazia
        link = vaga.get("url", "N/A")  # Pega o link da vaga; padrão "N/A"

        return {  # Retorna um novo dicionário com os dados organizados
            "titulo": titulo,  # Chave "titulo" recebe o valor da variável titulo
            "empresa": empresa,  # Chave "empresa" recebe o valor da variável empresa
            "categoria": categoria,  # Chave "categoria" recebe o valor da variável categoria
            "tipo": tipo,  # Chave "tipo" recebe o valor da variável tipo
            "salario": salario,  # Chave "salario" recebe o valor da variável salario
            "localizacao": ", ".join(localizacao),  # Junta a lista de localizações em uma string separada por vírgula
            "link": link  # Chave "link" recebe o valor da variável link
        }
    except:  # Se qualquer erro acontecer dentro do try
        return None  # Retorna None indicando que não foi possível extrair os dados




# Funcao para salvar uma lista de vagas em um arquivo CSV

def salvar_csv(vagas, caminho="data/jobs.csv"):
    
    df = pd.DataFrame(vagas)  # Converte a lista de vagas em um DataFrame (tabela)
    df.to_csv(caminho, index=False, encoding="utf-8-sig")  # Salva a tabela em CSV, sem índice, com codificação UTF-8 para funcionar bem em excel e outros 
    print(f"{len(df)} vagas salvas em {caminho}")  # Mostra quantas vagas foram salvas e onde





# bloco principal do scraper

if __name__ == "__main__":  # Executa apenas se este arquivo for rodado diretamente (não se for importado)
    urls = [  # Cria uma lista de URLs para cada categoria de vaga tech
        "https://remotive.com/remote-jobs/software-development",  # Vagas de desenvolvimento de software
        "https://remotive.com/remote-jobs/ai-ml",  # Vagas de AI / Machine Learning
        "https://remotive.com/remote-jobs/data",  # Vagas de ciência de dados
        "https://remotive.com/remote-jobs/devops",  # Vagas de DevOps
    ]

    vagas = []  # Lista vazia para armazenar todas as vagas coletadas

    for url in urls:  # Loop para acessar cada URL da lista
        print(f"acessando {url}...")  # Mostra no terminal qual URL está sendo acessada
        html = obter_pagina(url)  # Chama a função para obter o HTML da página
        if html:  # Se a página foi carregada com sucesso
            print("Extraindo vagas...")  # Mensagem informando que a extração vai começar
            vagas_brutas = extrair_vagas(html)  # Chama a função que extrai as vagas do HTML (JSON embutido)
            for vaga in vagas_brutas:  # Loop sobre cada vaga extraída
                dados = extrair_dados_vaga(vaga)  # Extrai os campos importantes de cada vaga
                if dados:  # Se conseguiu extrair os dados corretamente
                    vagas.append(dados)  # Adiciona a vaga processada na lista final
            print(f"{len(vagas)} vagas coletadas até agora...")  # Exibe quantas vagas foram coletadas até o momento
            time.sleep(2)  # Pausa de 2 segundos entre requisições para não sobrecarregar o site
        else:  # Se não conseguiu acessar a página
            print(f"Erro ao acessar {url}")  # Mostra mensagem de erro
    
    salvar_csv(vagas)  # Salva todas as vagas coletadas em um arquivo CSV