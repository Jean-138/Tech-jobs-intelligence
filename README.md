# Tech Jobs Intelligence

Sistema de coleta e análise de vagas remotas de tecnologia no mercado internacional.

## O que o projeto faz

- Coleta vagas automaticamente do site [Remotive](https://remotive.com)
- Extrai título, empresa, categoria, tipo de contrato, salário e localização
- Salva os dados em CSV
- Gera gráficos de análise do mercado tech

## Tecnologias utilizadas

- `requests` — acessa as páginas web
- `beautifulsoup4` — interpreta o HTML
- `fake-useragent` — simula um navegador real
- `pandas` — organiza e analisa os dados
- `matplotlib` — gera os gráficos

## Como rodar

1. Clone o repositório e abra no VS Code
2. Instale as dependências:

pip install -r requirements.txt

3. Execute o projeto:

python main.py


## Resultados


Os gráficos são salvos automaticamente em `output/graficos/`:

- `paises.png` — Top 10 países com mais vagas
- `contratos.png` — Tipos de contrato mais comuns
- `cargos.png` — Top 10 cargos com mais vagas
- `salarios.png` — Vagas com salário especificado