
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Roda da Carreira - Análise Profissional",
    page_icon="📊",
    layout="wide"
)

# Título e introdução
st.title("🎯 Roda da Carreira - Análise Profissional")
st.markdown("""
Esta ferramenta ajudará você a avaliar sua situação profissional atual e definir seus objetivos de carreira.
Preencha os campos abaixo com valores de 0 a 10 para cada dimensão.
""")

# Dimensões da carreira
dimensoes = [
    'Desenvolvimento Profissional / Aprendizado',
    'Satisfação / Felicidade no Trabalho',
    'Equilíbrio Vida Pessoal e Trabalho',
    'Reconhecimento',
    'Recompensa (salário + benefícios)',
    'Perspectiva de Crescimento de Carreira',
    'Relacionamentos Profissionais',
    'Autonomia e Controle',
    'Alinhamento com Propósito Pessoal'
]

# Criar duas colunas para informações do cargo
col1, col2 = st.columns(2)
with col1:
    cargo_atual = st.text_input("Cargo Atual")
with col2:
    cargo_desejado = st.text_input("Cargo Desejado")

# Criar containers para as avaliações
st.markdown("### Avaliação das Dimensões")

# Dicionário para armazenar os valores
valores = {'atual': {}, 'desejado': {}}

# Criar sliders para cada dimensão
for dim in dimensoes:
    st.markdown(f"#### {dim}")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Estado Atual**")
        valores['atual'][dim] = st.slider(
            f"Atual - {dim}",
            0, 10, 5,
            key=f"atual_{dim}",
            help=f"Avalie sua situação atual em relação a {dim}"
        )

    with col2:
        st.markdown("**Estado Desejado**")
        valores['desejado'][dim] = st.slider(
            f"Desejado - {dim}",
            0, 10, 8,
            key=f"desejado_{dim}",
            help=f"Defina seu objetivo para {dim}"
        )

    # Adicionar descrição dos níveis
    st.markdown("""
    **Guia de Avaliação:**
    - 0-2: Nível crítico/insatisfatório
    - 3-4: Nível baixo/necessita melhorias significativas
    - 5-6: Nível médio/adequado com espaço para melhorias
    - 7-8: Nível bom/satisfatório
    - 9-10: Nível excelente/excepcional
    """)
    st.markdown("---")

# Botão para gerar análise
if st.button("Gerar Análise"):
    # Criar gráfico radar com Plotly
    fig = go.Figure()

    # Adicionar o primeiro valor novamente para fechar o polígono
    dimensoes_plot = dimensoes + [dimensoes[0]]
    valores_atual = [valores['atual'][dim] for dim in dimensoes] + [valores['atual'][dimensoes[0]]]
    valores_desejado = [valores['desejado'][dim] for dim in dimensoes] + [valores['desejado'][dimensoes[0]]]

    # Adicionar traces
    fig.add_trace(go.Scatterpolar(
        r=valores_atual,
        theta=dimensoes_plot,
        fill='toself',
        name='Estado Atual',
        line_color='#FF6B6B'
    ))

    fig.add_trace(go.Scatterpolar(
        r=valores_desejado,
        theta=dimensoes_plot,
        fill='toself',
        name='Estado Desejado',
        line_color='#4ECDC4'
    ))

    # Atualizar layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        ),
        showlegend=True,
        title="Análise da Roda da Carreira"
    )

    # Mostrar o gráfico
    st.plotly_chart(fig, use_container_width=True)

    # Análise dos gaps
    st.markdown("### Análise Detalhada e Plano de Desenvolvimento")

    gaps = {dim: valores['desejado'][dim] - valores['atual'][dim] for dim in dimensoes}
    maiores_gaps = sorted(gaps.items(), key=lambda x: x[1], reverse=True)

    for dim, gap in maiores_gaps:
        if gap > 0:  # Só mostrar dimensões com gap positivo
            st.markdown(f"#### {dim} (Gap: {gap})")

            # Análise personalizada baseada no estado atual e gap
            atual = valores['atual'][dim]
            desejado = valores['desejado'][dim]

            st.markdown(f"""
            **Situação Atual ({atual}/10):**
            {get_situacao_atual(dim, atual)}

            **Objetivo ({desejado}/10):**
            {get_objetivo(dim, desejado)}

            **Análise do Gap:**
            {get_analise_gap(dim, gap)}

            **Plano de Desenvolvimento:**

            *Ações Imediatas (30 dias):*
            {get_acoes_imediatas(dim, atual, desejado)}

            *Médio Prazo (90 dias):*
            {get_acoes_medio_prazo(dim, atual, desejado)}

            *Longo Prazo (180 dias):*
            {get_acoes_longo_prazo(dim, atual, desejado)}

            **Métricas de Sucesso:**
            {get_metricas_sucesso(dim)}

            **Recursos Recomendados:**
            {get_recursos_recomendados(dim)}
            """)
            st.markdown("---")

    # Salvar dados
    if st.button("Exportar Análise"):
        dados = {
            'Dimensão': dimensoes,
            'Estado Atual': [valores['atual'][dim] for dim in dimensoes],
            'Estado Desejado': [valores['desejado'][dim] for dim in dimensoes],
            'Gap': [gaps[dim] for dim in dimensoes]
        }
        df = pd.DataFrame(dados)
        df.to_csv('analise_carreira.csv', index=False)
        st.success("Análise exportada com sucesso!")

# Funções de análise personalizada
def get_situacao_atual(dimensao, valor):
    # Implementar análises personalizadas para cada dimensão e valor
    return "Análise detalhada da situação atual baseada na dimensão e valor"

def get_objetivo(dimensao, valor):
    return "Descrição do objetivo ideal baseado na dimensão e valor desejado"

def get_analise_gap(dimensao, gap):
    return "Análise detalhada do gap e suas implicações"

def get_acoes_imediatas(dimensao, atual, desejado):
    return "Lista de ações específicas para os primeiros 30 dias"

def get_acoes_medio_prazo(dimensao, atual, desejado):
    return "Lista de ações para os próximos 90 dias"

def get_acoes_longo_prazo(dimensao, atual, desejado):
    return "Lista de ações para os próximos 180 dias"

def get_metricas_sucesso(dimensao):
    return "Lista de métricas específicas para medir o progresso"

def get_recursos_recomendados(dimensao):
    return "Lista de recursos, cursos, livros e ferramentas recomendadas"

# Adicionar informações de ajuda
with st.expander("📖 Como usar esta ferramenta"):
    st.markdown("""
    1. **Preencha seu cargo atual e desejado**
    2. **Avalie cada dimensão:**
       - Estado Atual (0-10): Como você se sente hoje
       - Estado Desejado (0-10): Onde você quer chegar
    3. **Clique em 'Gerar Análise'** para ver o gráfico e recomendações
    4. **Exporte os resultados** para acompanhamento futuro

    **Dicas para avaliação:**
    - Seja honesto em suas avaliações
    - Considere suas experiências nos últimos 3-6 meses
    - Pense em exemplos concretos para justificar cada nota
    """)
