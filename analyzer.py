import pandas as pd # ler o CSV e manipular os dados em tabela
import matplotlib.pyplot as plt # gerar os graficos





# funcao para ler um arquivo CSV 

def carregar_dados(caminho="data/jobs.csv"):
    df = pd.read_csv(caminho) # lê o arquivo CSV e transforma em DataFrame, o inverso do scraper com to_csv
    print(f"{len(df)} vagas carregadas!") #conta quantas linhas tem o DataFrame, quantas vagas
    return df # retorna o DataFrame pra ser usado nas outras funções






# função que gera o gráfico dos países

def grafico_paises(df):  
    paises = df["localizacao"].str.split(", ").explode()  # separa os países e transforma em várias linhas
    contagem = paises.value_counts().head(10)  # conta os países e pega os 10 mais frequentes
    
    plt.figure(figsize=(12, 6))  # cria a figura com tamanho 12x6
    contagem.plot(kind="bar", color="steelblue")  # cria o gráfico de barras
    plt.title("Top 10 Países com Mais Vagas")  # define o título do gráfico
    plt.xlabel("País")  # define o rótulo do eixo X
    plt.ylabel("Número de Vagas")  # define o rótulo do eixo Y
    plt.xticks(rotation=45, ha="right")  # gira os rótulos do eixo X para melhor visualização
    plt.tight_layout()  # ajusta o layout automaticamente
    plt.savefig("output/graficos/paises.png")  # salva o gráfico como imagem
    plt.close()  # fecha a figura
    
    print("Gráfico de países salvo!")  # imprime mensagem 





# função que gera o gráfico de contratos


def grafico_contratos(df):
    contagem = df["tipo"].value_counts() #Pega a coluna "tipo" e Conta quantas vezes cada tipo aparece

    plt.figure(figsize=(8, 8)) # cria a figura com tamanho 8x8
    contagem.plot(kind="pie", autopct="%1.1f%%") #gera um gráfico de pizza a partir de 'contagem' e exibe os valores em porcentagem
    plt.title("Tipos de contrato") #define o titulo do grafico
    plt.ylabel("")
    plt.tight_layout() # ajusta o layout automaticamente
    plt.savefig("output/graficos/contratos.png") #salva o grafico como imagem
    plt.close() #fecha a figura
    print("Gráfico de contratos salvo!") # imprime a imagem





    # função para gerar um gráfico dos 10 cargos com mais vagas

def grafico_cargos(df): 
    contagem = df["titulo"].value_counts().head(10)  #quantas vezes cada cargo aparece e seleciona os 10 mais frequentes
    
    plt.figure(figsize=(12, 6))  #  cria a figura com tamanho 12x6
    contagem.plot(kind="barh", color="green")  # gráfico de barras horizontal com as contagens verde
    plt.title("Top 10 Cargos com Mais Vagas")  # adiciona o título do gráfico
    plt.xlabel("Número de Vagas")  # rótulo do eixo X mostrando o número de vagas
    plt.ylabel("Cargo")  # define o rótulo do eixo Y mostrando o nome do cargo
    plt.tight_layout()  # ajusta automaticamente o layout para que nada fique cortado
    plt.savefig("output/graficos/cargos.png")  # salva o como imagem no caminho especificado
    plt.close()  # fecha a figura para liberar memoria e evitar sobreposição de gráficos
    print("Gráfico de cargos salvo!")  # imprime mensagem confirmando que o gráfico foi salvo





# graficos salarios especificados

def grafico_salarios(df):
    contagem = df["salario"].apply(  # Aplica uma transformação na coluna 'salario' do DataFrame
        lambda x: "Especificado" if x != "unspecified" else "Não Especificado"  # Se o valor do salário não for "unspecified", marca como "Especificado", caso contrário marca como "Não Especificado"
    )
    contagem = contagem.value_counts()  # Conta quantas vezes cada valor ('Especificado' ou 'Não Especificado') aparece na coluna 'salario' transformada

    plt.figure(figsize=(8, 8))  # Cria uma figura para o gráfico com tamanho 8x8 
    contagem.plot(kind="pie", autopct="%1.1f%%", colors=["#2ecc71", "#e74c3c"])  # Cria o gráfico de pizza usando os dados da contagem
    # 'autopct' formata a exibição das porcentagens no gráfico e 'colors' define as cores do gráfico
    plt.title("Vagas com Salário Especificado")  # Define o título do gráfico
    plt.ylabel("")  # Remove o rótulo do eixo y 
    plt.tight_layout()  # Ajusta o layout para garantir que o gráfico não sobreponha nada
    plt.savefig("output/graficos/salarios.png")  # Salva o gráfico como um arquivo PNG no diretório especificado
    plt.close()  # Fecha o gráfico após salvar
    print("Gráfico de salários salvo!")  # Exibe uma mensagem de confirmação de que o gráfico foi salvo






if __name__ == "__main__":
    df = carregar_dados()
    grafico_paises(df)
    grafico_contratos(df)
    grafico_cargos(df)
    grafico_salarios(df)


    