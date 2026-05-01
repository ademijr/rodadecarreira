import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Ecossistema Pessoas com IA",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Ecossistema Pessoas com IA")
st.caption("Portfólio estratégico: sobre você, agentes GPT, soluções e ferramentas de evolução profissional.")

aba_sobre, aba_caixa, aba_sites, aba_roda = st.tabs([
    "🙋 Sobre mim",
    "🧰 Caixa de Ferramentas",
    "🌐 Meus Sites",
    "📊 Roda da Carreira"
])

with aba_sobre:
    st.header("Quem sou eu")
    st.markdown(
        """
        Sou um profissional focado em **carreira, empregabilidade e produtividade com IA**, com uma proposta clara:
        transformar tecnologia em resultados práticos para pessoas reais.

        Minha atuação combina:
        - **Diagnóstico de carreira** para identificar gargalos e oportunidades.
        - **Automação com IA** para acelerar tarefas críticas (currículo, candidaturas, plano de ação).
        - **Estratégia profissional** para posicionamento e conquista de vagas.

        ### Missão
        Ajudar pessoas a saírem da estagnação profissional e alcançarem uma trajetória mais clara, competitiva e sustentável.

        ### Diferenciais
        - Linguagem simples e aplicada.
        - Foco em execução (não só teoria).
        - Soluções modulares que se conectam em um ecossistema.
        """
    )

with aba_caixa:
    st.header("Índice das minhas soluções (Agentes GPT)")

    agentes = [
        {
            "nome": "Agente Diagnóstico NR1",
            "descricao": "Realiza um raio-X da situação profissional atual e organiza os principais bloqueios em prioridades de ação.",
            "praticas": [
                "Mapear lacunas de competências para o cargo desejado.",
                "Identificar padrões que estão travando entrevistas.",
                "Transformar inseguranças em plano de melhoria semanal.",
                "Gerar um checklist de evolução em 30, 60 e 90 dias.",
                "Criar indicadores de progresso para acompanhar mudanças."
            ],
            "link": "https://diagnosticonr1.pessoascomia.com/"
        },
        {
            "nome": "Agente Gera Currículo",
            "descricao": "Converte experiências e resultados em um currículo orientado a vagas, com maior clareza, impacto e aderência.",
            "praticas": [
                "Criar versão-base do currículo a partir de histórico bruto.",
                "Adaptar currículo para vagas específicas em minutos.",
                "Reescrever conquistas com foco em métricas e impacto.",
                "Ajustar resumo profissional por senioridade.",
                "Preparar versões para áreas diferentes mantendo consistência."
            ],
            "link": "https://geracurriculo.pessoascomia.com/"
        },
        {
            "nome": "Agente Quero Vaga de Emprego",
            "descricao": "Apoia a estratégia de candidatura: seleção de vagas, personalização de mensagens e consistência no funil de aplicação.",
            "praticas": [
                "Definir meta semanal de candidaturas qualificadas.",
                "Produzir mensagem de abordagem para recrutadores.",
                "Montar rotina de follow-up sem parecer invasivo.",
                "Priorizar vagas com maior chance de match.",
                "Estruturar narrativa para entrevistas por tipo de vaga."
            ],
            "link": "https://querovagadeemprego.pessoascomia.com/"
        },
        {
            "nome": "Agente Dash NR1",
            "descricao": "Consolida dados e métricas da jornada profissional em painéis para tomada de decisão rápida.",
            "praticas": [
                "Acompanhar evolução de competências por período.",
                "Monitorar taxa de resposta das candidaturas.",
                "Comparar desempenho entre versões de currículo.",
                "Visualizar gargalos no funil (aplicação → entrevista → proposta).",
                "Apoiar ajustes estratégicos com base em evidências."
            ],
            "link": "https://dashnr1.pessoascomia.com/"
        },
    ]

    for idx, ag in enumerate(agentes, start=1):
        with st.container(border=True):
            st.subheader(f"{idx}. {ag['nome']}")
            st.markdown(f"**Descrição detalhada:** {ag['descricao']}")
            st.markdown("**5 possibilidades práticas:**")
            for i, item in enumerate(ag["praticas"], start=1):
                st.markdown(f"{i}. {item}")
            st.link_button("Acessar agente", ag["link"])

with aba_sites:
    st.header("Meus sites e descritivo detalhado")
    st.info(
        "Os descritivos abaixo foram estruturados para uso comercial, onboarding de clientes e posicionamento digital do seu ecossistema."
    )

    sites = [
        {
            "nome": "Gera Currículo",
            "url": "https://geracurriculo.pessoascomia.com/",
            "descricao": "Plataforma orientada à criação e otimização de currículos com foco em empregabilidade. A proposta central é converter experiências em valor percebido pelo recrutador, com linguagem objetiva e aderente às exigências de mercado.",
            "valor": [
                "Clareza de posicionamento profissional.",
                "Aumento da qualidade das candidaturas.",
                "Padronização e rapidez na atualização do currículo.",
            ],
        },
        {
            "nome": "Diagnóstico NR1",
            "url": "https://diagnosticonr1.pessoascomia.com/",
            "descricao": "Ferramenta de diagnóstico estratégico que identifica nível atual de carreira, obstáculos críticos e prioridades de evolução. Atua como etapa inicial para construção de um plano de desenvolvimento consistente.",
            "valor": [
                "Visão estruturada dos gaps profissionais.",
                "Direcionamento prático para próximas ações.",
                "Base analítica para decisões de transição de carreira.",
            ],
        },
        {
            "nome": "Quero Vaga de Emprego",
            "url": "https://querovagadeemprego.pessoascomia.com/",
            "descricao": "Ambiente focado em execução da busca por emprego: escolha de vagas, personalização de aplicação e rotina disciplinada de acompanhamento. Ideal para transformar intenção em pipeline real de oportunidades.",
            "valor": [
                "Mais foco na candidatura certa.",
                "Melhor taxa de resposta em processos seletivos.",
                "Organização completa da jornada de aplicação.",
            ],
        },
        {
            "nome": "Dash NR1",
            "url": "https://dashnr1.pessoascomia.com/",
            "descricao": "Dashboard de desempenho profissional com indicadores da jornada de carreira. Permite leitura rápida de resultados, comparação entre ciclos e melhoria contínua baseada em dados.",
            "valor": [
                "Tomada de decisão com métricas.",
                "Acompanhamento de evolução ao longo do tempo.",
                "Visibilidade de gargalos e oportunidades de otimização.",
            ],
        },
    ]

    for site in sites:
        with st.container(border=True):
            st.subheader(site["nome"])
            st.markdown(site["descricao"])
            st.markdown("**Principais entregas de valor:**")
            for v in site["valor"]:
                st.markdown(f"- {v}")
            st.link_button("Visitar site", site["url"])

with aba_roda:
    st.header("Roda da Carreira")
    st.markdown("Avalie seu estado atual e desejado em cada dimensão para criar um plano de desenvolvimento profissional.")

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

    col1, col2 = st.columns(2)
    with col1:
        cargo_atual = st.text_input("Cargo Atual")
    with col2:
        cargo_desejado = st.text_input("Cargo Desejado")

    valores = {'atual': {}, 'desejado': {}}

    for dim in dimensoes:
        st.markdown(f"#### {dim}")
        c1, c2 = st.columns(2)
        with c1:
            valores['atual'][dim] = st.slider(f"Atual - {dim}", 0, 10, 5, key=f"a_{dim}")
        with c2:
            valores['desejado'][dim] = st.slider(f"Desejado - {dim}", 0, 10, 8, key=f"d_{dim}")

    if st.button("Gerar Análise"):
        fig = go.Figure()
        dims_plot = dimensoes + [dimensoes[0]]
        atual = [valores['atual'][d] for d in dimensoes] + [valores['atual'][dimensoes[0]]]
        desejado = [valores['desejado'][d] for d in dimensoes] + [valores['desejado'][dimensoes[0]]]

        fig.add_trace(go.Scatterpolar(r=atual, theta=dims_plot, fill='toself', name='Estado Atual', line_color='#FF6B6B'))
        fig.add_trace(go.Scatterpolar(r=desejado, theta=dims_plot, fill='toself', name='Estado Desejado', line_color='#4ECDC4'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

        gaps = {d: valores['desejado'][d] - valores['atual'][d] for d in dimensoes}
        df = pd.DataFrame({
            "Dimensão": dimensoes,
            "Atual": [valores['atual'][d] for d in dimensoes],
            "Desejado": [valores['desejado'][d] for d in dimensoes],
            "Gap": [gaps[d] for d in dimensoes],
        }).sort_values("Gap", ascending=False)

        st.markdown("### Priorização de Gaps")
        st.dataframe(df, use_container_width=True)
