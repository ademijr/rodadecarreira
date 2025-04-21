
def get_situacao_atual(dimensao, valor):
    analises = {
        'Desenvolvimento Profissional / Aprendizado': {
            'baixo': "Você está em uma fase de estagnação profissional, com poucas oportunidades de aprendizado. Isso pode estar impactando seu crescimento e motivação.",
            'medio': "Você tem acesso a algumas oportunidades de desenvolvimento, mas ainda há espaço para uma abordagem mais estruturada.",
            'alto': "Você está em um ambiente rico em aprendizado, com boas oportunidades de desenvolvimento profissional."
        },
        'Satisfação / Felicidade no Trabalho': {
            'baixo': "Sua satisfação atual está comprometida, indicando possível burnout ou desalinhamento com suas atividades atuais.",
            'medio': "Você encontra momentos de satisfação em seu trabalho, mas ainda existem aspectos que precisam ser melhorados.",
            'alto': "Você demonstra alto nível de satisfação e engajamento com seu trabalho atual."
        },
        'Equilíbrio Vida Pessoal e Trabalho': {
            'baixo': "Seu equilíbrio está severamente comprometido, com o trabalho dominando aspectos importantes da vida pessoal.",
            'medio': "Você consegue manter algum equilíbrio, mas ainda enfrenta conflitos ocasionais entre trabalho e vida pessoal.",
            'alto': "Você alcançou um bom equilíbrio entre vida profissional e pessoal."
        },
        'Reconhecimento': {
            'baixo': "Suas contribuições não estão sendo adequadamente reconhecidas, o que pode estar afetando sua motivação.",
            'medio': "Você recebe algum reconhecimento, mas de forma inconsistente ou não estruturada.",
            'alto': "Seu trabalho é bem reconhecido e valorizado no ambiente profissional."
        },
        'Recompensa (salário + benefícios)': {
            'baixo': "Sua remuneração atual está significativamente abaixo de suas expectativas e do mercado.",
            'medio': "Sua remuneração está alinhada com a média do mercado, mas há espaço para melhorias.",
            'alto': "Você está bem posicionado em termos de remuneração e benefícios."
        },
        'Perspectiva de Crescimento de Carreira': {
            'baixo': "Você enfrenta limitações significativas para crescimento em sua posição atual.",
            'medio': "Existem algumas oportunidades de crescimento, mas o caminho não está claramente definido.",
            'alto': "Você tem um caminho claro de crescimento com boas oportunidades pela frente."
        },
        'Relacionamentos Profissionais': {
            'baixo': "Seus relacionamentos profissionais estão tensos ou subdesenvolvidos.",
            'medio': "Você mantém relacionamentos profissionais cordiais, mas há espaço para networking mais estratégico.",
            'alto': "Você desenvolveu uma forte rede de relacionamentos profissionais."
        },
        'Autonomia e Controle': {
            'baixo': "Você tem pouco controle sobre suas atividades e decisões profissionais.",
            'medio': "Você possui alguma autonomia, mas ainda enfrenta limitações significativas.",
            'alto': "Você possui boa autonomia e controle sobre suas responsabilidades."
        },
        'Alinhamento com Propósito Pessoal': {
            'baixo': "Seu trabalho atual está desalinhado com seus valores e propósito pessoal.",
            'medio': "Você encontra algum significado em seu trabalho, mas busca maior alinhamento.",
            'alto': "Seu trabalho está bem alinhado com seus valores e propósito pessoal."
        }
    }

    if valor <= 4:
        nivel = 'baixo'
    elif valor <= 7:
        nivel = 'medio'
    else:
        nivel = 'alto'

    return analises[dimensao][nivel]

def get_objetivo(dimensao, valor):
    objetivos = {
        'Desenvolvimento Profissional / Aprendizado': {
            'medio': "Estabelecer uma rotina consistente de aprendizado e desenvolvimento de novas habilidades.",
            'alto': "Alcançar excelência em sua área e tornar-se referência em conhecimento específico."
        },
        'Satisfação / Felicidade no Trabalho': {
            'medio': "Identificar e focar em aspectos do trabalho que trazem maior satisfação pessoal.",
            'alto': "Atingir um estado de realização profissional plena e impacto positivo."
        },
        'Equilíbrio Vida Pessoal e Trabalho': {
            'medio': "Estabelecer limites saudáveis entre trabalho e vida pessoal.",
            'alto': "Alcançar harmonia ideal entre realização profissional e pessoal."
        },
        'Reconhecimento': {
            'medio': "Aumentar a visibilidade de suas contribuições e impacto no trabalho.",
            'alto': "Ser reconhecido como profissional de alto valor e referência na área."
        },
        'Recompensa (salário + benefícios)': {
            'medio': "Alinhar remuneração com valor de mercado e contribuições.",
            'alto': "Atingir pacote de remuneração premium no mercado."
        },
        'Perspectiva de Crescimento de Carreira': {
            'medio': "Estabelecer um plano claro de progressão na carreira.",
            'alto': "Alcançar posição de liderança ou especialista sênior na área."
        },
        'Relacionamentos Profissionais': {
            'medio': "Desenvolver network estratégico e colaborativo.",
            'alto': "Construir uma rede de influência e mentoria na área."
        },
        'Autonomia e Controle': {
            'medio': "Aumentar nível de autonomia e tomada de decisão.",
            'alto': "Atingir alto nível de autonomia e influência estratégica."
        },
        'Alinhamento com Propósito Pessoal': {
            'medio': "Alinhar atividades profissionais com valores pessoais.",
            'alto': "Alcançar total integração entre propósito pessoal e atuação profissional."
        }
    }

    nivel = 'alto' if valor >= 8 else 'medio'
    return objetivos[dimensao][nivel]

def get_analise_gap(dimensao, gap):
    if gap <= 2:
        intensidade = "pequeno"
        prazo = "curto prazo"
    elif gap <= 4:
        intensidade = "moderado"
        prazo = "médio prazo"
    else:
        intensidade = "significativo"
        prazo = "longo prazo"

    return f"""O gap {intensidade} de {gap} pontos indica necessidade de desenvolvimento que pode ser alcançado em {prazo}.
    Este gap sugere uma oportunidade de crescimento que requer atenção {intensidade} e ações estruturadas."""

def get_acoes_imediatas(dimensao, atual, desejado):
    acoes = {
        'Desenvolvimento Profissional / Aprendizado': [
            "Mapear 3 principais skills técnicas para desenvolvimento",
            "Inscrever-se em um curso online relevante para sua área",
            "Criar cronograma semanal de estudos (2h/dia)",
            "Identificar mentor potencial na área desejada"
        ],
        'Satisfação / Felicidade no Trabalho': [
            "Listar aspectos positivos e negativos do trabalho atual",
            "Identificar 3 principais fontes de insatisfação",
            "Desenvolver plano de ação para cada fonte de insatisfação",
            "Iniciar prática de journaling profissional"
        ],
        'Equilíbrio Vida Pessoal e Trabalho': [
            "Estabelecer horários fixos de início e fim de trabalho",
            "Criar ritual de transição entre trabalho e vida pessoal",
            "Implementar técnica Pomodoro para melhor gestão do tempo",
            "Definir momentos 'não negociáveis' para vida pessoal"
        ]
    }
    # Continuar com outras dimensões...
    return "\n".join([f"- {acao}" for acao in acoes.get(dimensao, 
        ["Agendar sessão de feedback com gestor",
         "Criar plano de desenvolvimento individual",
         "Identificar 3 objetivos principais para os próximos 30 dias",
         "Estabelecer métricas de sucesso claras"])])

def get_acoes_medio_prazo(dimensao, atual, desejado):
    acoes = {
        'Desenvolvimento Profissional / Aprendizado': [
            "Completar certificação relevante para área",
            "Participar de projeto desafiador",
            "Criar blog/portfolio de conhecimentos",
            "Ministrar workshops internos"
        ],
        'Satisfação / Felicidade no Trabalho': [
            "Redesenhar escopo de trabalho com gestor",
            "Implementar projeto pessoal na empresa",
            "Desenvolver nova habilidade valorizada",
            "Criar rede de suporte profissional"
        ],
        'Equilíbrio Vida Pessoal e Trabalho': [
            "Implementar dia de trabalho remoto",
            "Desenvolver hobbies regulares",
            "Criar sistema de priorização de tarefas",
            "Estabelecer limites claros com equipe"
        ]
    }
    return "\n".join([f"- {acao}" for acao in acoes.get(dimensao,
        ["Desenvolver projeto de alto impacto",
         "Expandir network profissional",
         "Buscar novas responsabilidades",
         "Criar dashboard de progresso"])])

def get_acoes_longo_prazo(dimensao, atual, desejado):
    acoes = {
        'Desenvolvimento Profissional / Aprendizado': [
            "Tornar-se referência na área específica",
            "Publicar conteúdo especializado",
            "Desenvolver metodologia própria",
            "Criar programa de mentoria"
        ],
        'Satisfação / Felicidade no Trabalho': [
            "Alcançar posição ideal na organização",
            "Criar ambiente de trabalho modelo",
            "Desenvolver equipe de alto desempenho",
            "Implementar inovações significativas"
        ],
        'Equilíbrio Vida Pessoal e Trabalho': [
            "Estabelecer modelo de trabalho flexível",
            "Criar sistema de delegação eficiente",
            "Desenvolver equipe autônoma",
            "Implementar práticas de bem-estar corporativo"
        ]
    }
    return "\n".join([f"- {acao}" for acao in acoes.get(dimensao,
        ["Alcançar posição de liderança",
         "Criar impacto significativo na organização",
         "Desenvolver sucessores",
         "Estabelecer legado profissional"])])

def get_metricas_sucesso(dimensao):
    metricas = {
        'Desenvolvimento Profissional / Aprendizado': [
            "Número de certificações obtidas",
            "Horas de estudo/treinamento completadas",
            "Projetos práticos implementados",
            "Avaliações de competência"
        ],
        'Satisfação / Felicidade no Trabalho': [
            "Índice de satisfação semanal (1-10)",
            "Número de iniciativas próprias implementadas",
            "Feedback positivo recebido",
            "Nível de engajamento em projetos"
        ],
        'Equilíbrio Vida Pessoal e Trabalho': [
            "Horas extras realizadas",
            "Tempo dedicado a hobbies/família",
            "Nível de stress (1-10)",
            "Qualidade do sono"
        ]
    }
    return "\n".join([f"- {metrica}" for metrica in metricas.get(dimensao,
        ["Avaliações de desempenho",
         "Feedback 360º",
         "Metas alcançadas",
         "Índice de progresso pessoal"])])

def get_recursos_recomendados(dimensao):
    recursos = {
        'Desenvolvimento Profissional / Aprendizado': [
            "Cursos: Coursera, Udemy, LinkedIn Learning",
            "Livros: 'Mindset' de Carol Dweck, 'Deep Work' de Cal Newport",
            "Podcasts: 'Learning Leaders', 'The Knowledge Project'",
            "Comunidades: GitHub, Stack Overflow, Reddit r/learnprogramming"
        ],
        'Satisfação / Felicidade no Trabalho': [
            "Livros: 'Drive' de Daniel Pink, 'Flow' de Mihaly Csikszentmihalyi",
            "Apps: Headspace, Calm, Journify",
            "Workshops: Gestão de Energia, Produtividade Pessoal",
            "Coaching de Carreira"
        ],
        'Equilíbrio Vida Pessoal e Trabalho': [
            "Apps: RescueTime, Forest, Todoist",
            "Livros: 'Boundaries' de Henry Cloud, 'The 4-Hour Work Week'",
            "Workshops: Gestão do Tempo, Produtividade",
            "Terapia ocupacional"
        ]
    }
    return "\n".join([f"- {recurso}" for recurso in recursos.get(dimensao,
        ["Plataformas de e-learning",
         "Livros recomendados da área",
         "Eventos e conferências relevantes",
         "Mentorias e coaching"])])
