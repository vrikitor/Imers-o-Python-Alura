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

# --- 2. CARREGAMENTO E TRATAMENTO DE DADOS ---
@st.cache_data
def carregar_dados():
    url = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"
    df = pd.read_csv(url)
    
    # Limpeza de espaços
    df['residencia_iso3'] = df['residencia_iso3'].astype(str).str.strip()

    # --- NOVO DICIONÁRIO (AGORA COM 3 LETRAS - ISO ALPHA-3) ---
    # Isso vai resolver o problema do gráfico azul!
    mapa_continentes = {
        # América do Norte
        'USA': 'América do Norte', 'CAN': 'América do Norte', 'MEX': 'América do Norte',
        'PRI': 'América do Norte', 'CUB': 'América do Norte', 'JAM': 'América do Norte',
        'CRI': 'América do Norte', 'PAN': 'América do Norte', 'SLV': 'América do Norte',
        'GTM': 'América do Norte', 'HND': 'América do Norte', 'BHS': 'América do Norte',
        
        # América do Sul
        'BRA': 'América do Sul', 'ARG': 'América do Sul', 'COL': 'América do Sul',
        'CHL': 'América do Sul', 'PER': 'América do Sul', 'ECU': 'América do Sul',
        'URY': 'América do Sul', 'PRY': 'América do Sul', 'BOL': 'América do Sul',
        'VEN': 'América do Sul', 'GUY': 'América do Sul', 'SUR': 'América do Sul',
        
        # Europa
        'DEU': 'Europa', 'GBR': 'Europa', 'FRA': 'Europa', 'ESP': 'Europa',
        'ITA': 'Europa', 'NLD': 'Europa', 'POL': 'Europa', 'PRT': 'Europa',
        'RUS': 'Europa', 'UKR': 'Europa', 'CHE': 'Europa', 'SWE': 'Europa',
        'NOR': 'Europa', 'DNK': 'Europa', 'FIN': 'Europa', 'BEL': 'Europa',
        'AUT': 'Europa', 'GRC': 'Europa', 'IRL': 'Europa', 'CZE': 'Europa',
        'ROU': 'Europa', 'HUN': 'Europa', 'HRV': 'Europa', 'SRB': 'Europa',
        'BGR': 'Europa', 'SVK': 'Europa', 'BLR': 'Europa', 'LTU': 'Europa',
        'LVA': 'Europa', 'EST': 'Europa', 'SVN': 'Europa', 'LUX': 'Europa',
        'CYP': 'Europa', 'MLT': 'Europa', 'ISL': 'Europa', 'BIH': 'Europa',
        'MKD': 'Europa', 'ALB': 'Europa', 'MNE': 'Europa', 'MDA': 'Europa',
        'AND': 'Europa', 'SMR': 'Europa', 'LIE': 'Europa', 'MCO': 'Europa',
        'VAT': 'Europa', 'ARM': 'Europa', 'GEO': 'Europa', 'AZE': 'Europa',
        'TUR': 'Europa', # Às vezes considerada Ásia, mas no mercado tech muito ligada à Europa
        
        # Ásia
        'CHN': 'Ásia', 'IND': 'Ásia', 'JPN': 'Ásia', 'KOR': 'Ásia',
        'SGP': 'Ásia', 'TWN': 'Ásia', 'HKG': 'Ásia', 'IDN': 'Ásia',
        'MYS': 'Ásia', 'PHL': 'Ásia', 'THA': 'Ásia', 'VNM': 'Ásia',
        'PAK': 'Ásia', 'BGD': 'Ásia', 'LKA': 'Ásia', 'NPL': 'Ásia',
        'KAZ': 'Ásia', 'UZB': 'Ásia', 'ISR': 'Ásia', 'SAU': 'Ásia',
        'ARE': 'Ásia', 'QAT': 'Ásia', 'KWT': 'Ásia', 'OMN': 'Ásia',
        'JOR': 'Ásia', 'LBN': 'Ásia', 'IRQ': 'Ásia', 'IRN': 'Ásia',
        
        # Oceania
        'AUS': 'Oceania', 'NZL': 'Oceania', 'FJI': 'Oceania', 'PNG': 'Oceania',
        'ASM': 'Oceania',
        
        # África
        'NGA': 'África', 'ZAF': 'África', 'EGY': 'África', 'DZA': 'África',
        'MAR': 'África', 'KEN': 'África', 'ETH': 'África', 'GHA': 'África',
        'CIV': 'África', 'TUN': 'África', 'UGA': 'África', 'COD': 'África',
        'CMR': 'África', 'SEN': 'África', 'ZMB': 'África', 'ZWE': 'África',
        'RWA': 'África', 'MUS': 'África', 'NAM': 'África', 'BWA': 'África',
        'AGO': 'África', 'MOZ': 'África', 'MDG': 'África'
    }
    
    # Criando a coluna nova e preenchendo falhas
    df['continente'] = df['residencia_iso3'].map(mapa_continentes)
    df['continente'] = df['continente'].fillna('Outro') # Se sobrar algum, vira Outro
    
    return df

df = carregar_dados()

# --- 3. BARRA LATERAL (FILTROS) ---
st.sidebar.header("🔍 Filtros")
anos = st.sidebar.multiselect("Ano", sorted(df['ano'].unique()), default=sorted(df['ano'].unique()))
senioridade = st.sidebar.multiselect("Senioridade", sorted(df['senioridade'].unique()), default=sorted(df['senioridade'].unique()))
contrato = st.sidebar.multiselect("Tipo de Contrato", sorted(df['contrato'].unique()), default=sorted(df['contrato'].unique()))
tamanho = st.sidebar.multiselect("Tamanho da Empresa", sorted(df['tamanho_empresa'].unique()), default=sorted(df['tamanho_empresa'].unique()))

df_filtrado = df[
    (df['ano'].isin(anos)) & (df['senioridade'].isin(senioridade)) &
    (df['contrato'].isin(contrato)) & (df['tamanho_empresa'].isin(tamanho))
]

# --- 4. LAYOUT PRINCIPAL ---
st.title("💵 Dashboard de Salários na Área de Dados")
st.markdown("Visão geral do mercado de dados.")

# --- 5. KPIs ---
if not df_filtrado.empty:
    media = df_filtrado['usd'].mean()
    maximo = df_filtrado['usd'].max()
    contagem = df_filtrado.shape[0]
    cargo_top = df_filtrado["cargo"].mode()[0]
else:
    media, maximo, contagem, cargo_top = 0, 0, 0, "N/A"

c1, c2, c3, c4 = st.columns(4)
c1.metric("Média Salarial", f"${media:,.2f}")
c2.metric("Maior Salário", f"${maximo:,.2f}")
c3.metric("Total de Vagas", f"{contagem:,}")
c4.metric("Cargo + Comum", cargo_top)

st.markdown("---")

# --- 6. GRÁFICOS INICIAIS ---
col1, col2 = st.columns(2)
with col1:
    if not df_filtrado.empty:
        top_c = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        fig = px.bar(top_c, x='usd', y='cargo', orientation='h', title="Top 10 Cargos", labels={'usd':'USD', 'cargo':''})
        st.plotly_chart(fig, use_container_width=True)
with col2:
    if not df_filtrado.empty:
        fig = px.histogram(df_filtrado, x='usd', nbins=30, title="Distribuição Salarial", labels={'usd':'USD'})
        st.plotly_chart(fig, use_container_width=True)

# --- 7. GRÁFICOS AVANÇADOS (COM SUAS ALTERAÇÕES) ---
col3, col4 = st.columns(2)

with col3:
    if not df_filtrado.empty:
        remoto = df_filtrado['remoto'].value_counts().reset_index()
        remoto.columns = ['tipo', 'total']
        fig = px.pie(remoto, names='tipo', values='total', title='Modalidade', hole=0.5)
        st.plotly_chart(fig, use_container_width=True)

with col4:
    st.markdown("##### Geografia dos Salários")
    aba_mapa, aba_continente = st.tabs(["🌎 Mapa Global", "📊 Por Continente (Detalhado)"])

    # --- ABA 1: O MAPA (Amarelo -> Verde) ---
    with aba_mapa:
        if not df_filtrado.empty:
            df_mapa = df_filtrado.groupby('residencia_iso3')['usd'].mean().reset_index()
            fig_mapa = px.choropleth(
                df_mapa,
                locations='residencia_iso3',
                color='usd',
                # MUDANÇA: 'YlGn' (Yellow -> Green)
                color_continuous_scale='YlGn', 
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

    # --- ABA 2: SEU GRÁFICO (Colorido por Continente) ---
    with aba_continente:
        if not df_filtrado.empty:
            df_cont = df_filtrado.groupby(['continente', 'residencia_iso3'])['usd'].mean().reset_index()
            df_cont = df_cont.sort_values(by='usd', ascending=True)

            if not df_cont.empty:
                fig_cont = px.bar(
                    df_cont,
                    x='usd',
                    y='residencia_iso3',
                    # MUDANÇA: Agora que o dicionário funciona, isso vai colorir!
                    color='continente', 
                    orientation='h',
                    title='Comparativo: País e Continente',
                    labels={'usd': 'Média (USD)', 'residencia_iso3': 'País', 'continente': 'Região'},
                    height=500
                )
                st.plotly_chart(fig_cont, use_container_width=True)
            else:
                st.warning("Sem dados agrupados.")
