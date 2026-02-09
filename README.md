# Mapa da Carreira - Site HTML Interativo

Ferramenta mobile-first para diagnóstico de carreira (Roda da Vida aplicada à carreira), com gap entre estado atual e desejado, plano SMART + 5W2H e ações detalhadas por transição de cargo.

## Testar agora

### Opção 1 (rápida)
Abra `index.html` no navegador.

### Opção 2 (recomendada)
```bash
python -m http.server 8000
```
Acesse: `http://localhost:8000/index.html`

## Funcionalidades

- 13 dimensões com nota de 0 a 10 (Atual vs Desejado)
- Roda da Carreira (gráfico radar em canvas nativo)
- Cálculo de gap e prioridades
- Plano detalhado por cargo atual → cargo desejado
- Pesquisa guiada de mercado com links úteis
- Exportação em:
  - JSON
  - CSV (editável no Excel/Google Sheets)
  - PDF (via impressão do navegador)

## Stack e custo

- HTML/CSS/JavaScript puro
- Sem backend obrigatório
- Pode publicar gratuitamente em GitHub Pages, Netlify ou Vercel
