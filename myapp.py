import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Dashboard Salários de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CARREGAMENTO E TRATAMENTO DE DADOS (COM CACHE) ---
@st.cache_data
def carregar_dados():
    url = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"
    df = pd.read_csv(url)
    
    # 1. Limpeza de espaços em branco (Isso evita erros de mapeamento)
    # Converte para string e remove espaços no começo/fim
    df['residencia_iso3'] = df['residencia_iso3'].astype(str).str.strip()

    # --- DICIONÁRIO DE CONTINENTES ---
    mapa_continentes = {
        'US': 'América do Norte', 'CA': 'América do Norte', 'MX': 'América do Norte',
        'BR': 'América do Sul', 'AR': 'América do Sul', 'BO': 'América do Sul', 
        'CL': 'América do Sul', 'CO': 'América do Sul', 'EC': 'América do Sul', 
        'PE': 'América do Sul', 'PY': 'América do Sul', 'UY': 'América do Sul', 
        'VE': 'América do Sul', 'SR': 'América do Sul',
        'DE': 'Europa', 'GB': 'Europa', 'FR': 'Europa', 'ES': 'Europa', 
        'CH': 'Europa', 'AT': 'Europa', 'NL': 'Europa', 'IE': 'Europa', 
        'DK': 'Europa', 'SE': 'Europa', 'PT': 'Europa', 'IT': 'Europa', 
        'PL': 'Europa', 'AD': 'Europa', 'BE': 'Europa', 'BG': 'Europa', 
        'CZ': 'Europa', 'EE': 'Europa', 'GR': 'Europa', 'HR': 'Europa', 
        'HU': 'Europa', 'LU': 'Europa', 'MD': 'Europa', 'MT': 'Europa', 
        'RS': 'Europa', 'RU': 'Europa', 'SI': 'Europa', 'SK': 'Europa', 
        'UA': 'Europa', 'CY': 'Europa', 'BA': 'Europa', 'LT': 'Europa', 
        'GG': 'Europa', 'MK': 'Europa', 'LV': 'Europa', 'JE': 'Europa', 
        'RO': 'Europa', 'SM': 'Europa', 'LI': 'Europa',
        'IN': 'Ásia', 'JP': 'Ásia', 'CN': 'Ásia', 'HK': 'Ásia', 'ID': 'Ásia', 
        'IL': 'Ásia', 'IR': 'Ásia', 'MY': 'Ásia', 'PH': 'Ásia', 'PK': 'Ásia', 
        'SG': 'Ásia', 'TH': 'Ásia', 'TR': 'Ásia', 'AE': 'Ásia', 'AM': 'Ásia', 
        'VN': 'Ásia', 'AF': 'Ásia', 'AZ': 'Ásia', 'GE': 'Ásia', 'IQ': 'Ásia', 
        'KG': 'Ásia', 'KP': 'Ásia', 'KW': 'Ásia', 'KZ': 'Ásia', 'LA': 'Ásia', 
        'LB': 'Ásia', 'LK': 'Ásia', 'MM': 'Ásia', 'MN': 'Ásia', 'MV': 'Ásia', 
        'NP': 'Ásia', 'OM': 'Ásia', 'QA': 'Ásia', 'SY': 'Ásia', 'TJ': 'Ásia', 
        'TM': 'Ásia', 'YE': 'Ásia',
        'AU': 'Oceania', 'NZ': 'Oceania', 'PG': 'Oceania', 'PW': 'Oceania', 'AS': 'Oceania',
        'NG': 'África', 'GH': 'África', 'DZ': 'África', 'EG': 'África', 
        'KE': 'África', 'BI': 'África', 'BJ': 'África', 'BW': 'África', 
        'CF': 'África', 'CM': 'África', 'GA': 'África', 'LR': 'África', 
        'MW': 'África', 'MZ': 'África', 'NA': 'África', 'NE': 'África', 
        'RW': 'África', 'SD': 'África', 'SL': 'África', 'SN': 'África', 
        'SO': 'África', 'TG': 'África', 'TN': 'África', 'TZ': 'África', 
        'UG': 'África', 'ZM': 'África',
        'CR': 'América do Norte', 'PR': 'América do Norte', 'BS': 'América do Norte', 
        'CU': 'América do Norte', 'JM': 'América do Norte', 'PA': 'América do Norte', 
        'SV': 'América do Norte'
    }
    
    # Criando a coluna nova
    df['continente'] = df['residencia_iso3'].map(mapa_continentes)
    
    # 2. Tratamento de Nulos (Crucial para o gráfico não ficar vazio)
    # Se não achou o continente, coloca "Outro"
    df['continente'] = df['continente'].fillna('Outro / Desconhecido')
    
    return df

df = carregar_dados()

# --- 3. BARRA LATERAL (FILTROS) ---
st.sidebar.header("🔍 Filtros")
st.sidebar.markdown("Use os filtros abaixo para refinar a análise.")

# Filtros
anos = st.sidebar.multiselect("Ano", sorted(df['ano'].unique()), default=sorted(df['ano'].unique()))
senioridade = st.sidebar.multiselect("Senioridade", sorted(df['senioridade'].unique()), default=sorted(df['senioridade'].unique()))
contrato = st.sidebar.multiselect("Tipo de Contrato", sorted(df['contrato'].unique()), default=sorted(df['contrato'].unique()))
tamanho = st.sidebar.multiselect("Tamanho da Empresa", sorted(df['tamanho_empresa'].unique()), default=sorted(df['tamanho_empresa'].unique()))

# Aplicando os filtros
df_filtrado = df[
    (df['ano'].isin(anos)) &
    (df['senioridade'].isin(senioridade)) &
    (df['contrato'].isin(contrato)) &
    (df['tamanho_empresa'].isin(tamanho))
]

# --- 4. LAYOUT PRINCIPAL ---
st.title("💵 Dashboard de Salários na Área de Dados")
st.markdown("Visão geral do mercado de dados. **Abra a barra lateral à esquerda para filtrar.**")

# --- 5. KPIs (Métricas) ---
st.subheader("Métricas Gerais (Anual / USD)")

if not df_filtrado.empty:
    media = df_filtrado['usd'].mean()
    maximo = df_filtrado['usd'].max()
    contagem = df_filtrado.shape[0]
    cargo_top = df_filtrado["cargo"].mode()[0]
else:
    media, maximo, contagem, cargo_top = 0, 0, 0, "N/A"

col1, col2, col3, col4 = st.columns(4)
col1.metric("Média Salarial", f"${media:,.2f}")
col2.metric("Maior Salário", f"${maximo:,.2f}")
col3.metric("Total de Vagas", f"{contagem:,}")
col4.metric("Cargo mais Comum", cargo_top)

st.markdown("---")

# --- 6. GRÁFICOS (LINHA 1) ---
st.subheader("Análises de Mercado")
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        fig_cargos = px.bar(top_cargos, x='usd', y='cargo', orientation='h', 
                            title="Top 10 Cargos (Média Salarial)", labels={'usd': 'Salário (USD)', 'cargo': ''})
        st.plotly_chart(fig_cargos, use_container_width=True)
    else:
        st.warning("Sem dados.")

with col_graf2:
    if not df_filtrado.empty:
        fig_hist = px.histogram(df_filtrado, x='usd', nbins=30, title="Distribuição dos Salários",
                                labels={'usd': 'Salário (USD)'})
        st.plotly_chart(fig_hist, use_container_width=True)
    else:
        st.warning("Sem dados.")

# --- 7. GRÁFICOS (LINHA 2 - COM AS ABAS) ---
col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto = df_filtrado['remoto'].value_counts().reset_index()
        remoto.columns = ['tipo', 'total']
        fig_pizza = px.pie(remoto, names='tipo', values='total', title='Modalidade de Trabalho', hole=0.5)
        st.plotly_chart(fig_pizza, use_container_width=True)
    else:
        st.warning("Sem dados.")

with col_graf4:
    st.markdown("##### Geografia dos Salários")
    aba_mapa, aba_continente = st.tabs(["🌎 Mapa Global", "📊 Por Continente (Detalhado)"])

    # --- ABA 1: O MAPA (Visual Ajustado) ---
    with aba_mapa:
        if not df_filtrado.empty:
            df_mapa = df_filtrado.groupby('residencia_iso3')['usd'].mean().reset_index()
            
            fig_mapa = px.choropleth(
                df_mapa,
                locations='residencia_iso3',
                color='usd',
                color_continuous_scale='YlOrRd', # Amarelo -> Vermelho
                title='Média Global por País',
                labels={'usd': 'Média (USD)'}
            )
            
            fig_mapa.update_geos(
                showcountries=True, countrycolor="black", countrywidth=0.5,
                showland=True, landcolor="white",
                showframe=False, showcoastlines=False,
                projection_type='natural earth'
            )
            st.plotly_chart(fig_mapa, use_container_width=True)
        else:
            st.warning("Sem dados para o mapa.")

    # --- ABA 2: O SEU GRÁFICO (Dados já limpos na origem) ---
    with aba_continente:
        if not df_filtrado.empty:
            # Como já tratamos o 'continente' lá no começo, podemos usar direto!
            df_cont = df_filtrado.groupby(['continente', 'residencia_iso3'])['usd'].mean().reset_index()
            df_cont = df_cont.sort_values(by='usd', ascending=True)

            if not df_cont.empty:
                fig_cont = px.bar(
                    df_cont,
                    x='usd',
                    y='residencia_iso3',
                    color='continente',
                    orientation='h',
                    title='Comparativo: País e Continente',
                    labels={'usd': 'Média (USD)', 'residencia_iso3': 'País', 'continente': 'Região'},
                    height=500
                )
                st.plotly_chart(fig_cont, use_container_width=True)
            else:
                st.warning("Erro no agrupamento.")
        else:
            st.warning("Sem dados para o gráfico de continentes.")
