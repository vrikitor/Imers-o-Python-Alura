# 📊 Dashboard de Salários: Data Science (Global)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red)
![Plotly](https://img.shields.io/badge/Plotly-Express-green)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

> Projeto desenvolvido durante a Imersão de Dados da Alura, com melhorias e refatoração de código para análise avançada.

## Visão Geral do Projeto

Este projeto consiste em um Dashboard Interativo desenvolvido em Python para analisar a faixa salarial de profissionais da área de Dados (Data Science, Data Engineering, Analyst, etc.) ao redor do mundo.

O objetivo é permitir que o usuário explore como fatores como **experiência**, **tipo de emprego**, **tamanho da empresa** e **localização geográfica** influenciam na remuneração em Dólar (USD).

### Screenshots
![Dashboard Overview](<img width="930" height="720" alt="Mapa_mundi" src="https://github.com/user-attachments/assets/a54970fc-b159-4277-ab74-91b90c74e079" />
)


![Análise por Continente](<img width="930" height="738" alt="Grafico_mundi" src="https://github.com/user-attachments/assets/6e36ba56-4102-4a70-bc8b-aa256ee03228" />
)

---

## Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **Streamlit:** Framework para criação da interface web interativa.
* **Pandas:** Manipulação e limpeza de dados (ETL).
* **Plotly Express:** Criação de gráficos dinâmicos e mapas interativos.

---

## Funcionalidades & Melhorias Implementadas

Além do conteúdo base da imersão, foram implementadas as seguintes melhorias técnicas:

1.  **Limpeza de Dados (Data Cleaning):**
    * Tratamento de strings (remoção de espaços em branco) na coluna de países ISO-3.
    * Mapeamento personalizado de **Países para Continentes** usando dicionário Python.
    * Correção de dados nulos (`fillna`) para evitar gráficos vazios.

2.  **Otimização de Performance:**
    * Uso do decorador `@st.cache_data` para carregar o dataset apenas uma vez, tornando a filtragem instantânea.

3.  **Visualização Avançada:**
    * **Mapa Mundi (Choropleth):** Configuração de escala de cores divergente (`YlOrRd`) e adição de bordas para países sem dados, melhorando a leitura geográfica.
    * **Gráfico Comparativo:** Drill-down de Salários por Continente e País, permitindo identificar disparidades regionais.

4.  **UX (Experiência do Usuário):**
    * Barra lateral retrátil (`collapsed`) para priorizar a visualização dos dados.
    * Uso de abas (`st.tabs`) para organizar visualizações complexas sem poluir a tela.

---

## Como Rodar o Projeto Localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Certifique-se de ter as bibliotecas `streamlit`, `pandas` e `plotly` instaladas)*

3.  **Execute a aplicação:**
    ```bash
    streamlit run app.py
    ```

---

## Estrutura dos Dados

O dataset utilizado (`dados-imersao-final.csv`) contém as seguintes colunas principais:
* `ano`: Ano de referência do salário.
* `cargo`: Título da vaga (ex: Data Scientist).
* `senioridade`: Nível de experiência (Júnior, Pleno, Sênior, Executivo).
* `usd`: Salário anual convertido para Dólar.
* `residencia_iso3`: Código do país de residência do profissional.
* `tamanho_empresa`: Pequena (S), Média (M) ou Grande (L).

---

## Autor

Desenvolvido por **Victor Godoi Souza**
* [LinkedIn](https://www.linkedin.com/in/vicotr/)
* [GitHub](http://github.com/vrikitor)

---
