from scraper import obter_pagina, extrair_vagas, extrair_dados_vaga, salvar_csv
from analyzer import carregar_dados, grafico_paises, grafico_contratos, grafico_cargos, grafico_salarios



if __name__ == "__main__":
    print("Iniciando coleta de vagas")


    urls =  [
        "https://remotive.com/remote-jobs/software-development",
        "https://remotive.com/remote-jobs?category=Artificial+Intelligence",
        "https://remotive.com/remote-jobs/data",
        "https://remotive.com/remote-jobs/devops",
        ]


    vagas = []
    for url in urls:
        print(f"Acessando {url}...")
        html = obter_pagina(url)
        if html:
            vagas_brutas = extrair_vagas(html)
            for vaga in vagas_brutas:
                dados = extrair_dados_vaga(vaga)
                if dados:
                    vagas.append(dados)

    salvar_csv(vagas)

    print("Iniciando analise")
    df = carregar_dados()
    grafico_paises(df)
    grafico_contratos(df)
    grafico_cargos(df)
    grafico_salarios(df)


    print("Processo completo")