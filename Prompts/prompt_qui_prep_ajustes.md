Tenho tudo que preciso. Aqui está o prompt para rodar no Claude Code:

---

```
Você é um editor de arquivo markdown. Sua tarefa é aplicar edições cirúrgicas no arquivo `qui-1-3-prep.md`, sem alterar nenhum conteúdo fora dos trechos indicados.

---

## EDIÇÃO 1 — Substituir a tabela de diagramas da Seção 0

Localizar este bloco exato:

```
| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Linha do tempo — Tabela Periódica | DIAGRAMA: timeline | Ao apresentar Mendeleev e Moseley |
| Classificação dos elementos | DIAGRAMA: classificacao_elementos | Ao explicar metais, não-metais, metaloides e gases nobres |
| Blocos s, p, d, f (tabela real) | DIAGRAMA: blocos_tabela_real | Ao explicar os blocos — exibir ANTES do texto explicativo |
| Grupos e famílias (tabela real) | DIAGRAMA: grupos_familias | Ao explicar períodos e grupos — exibir ANTES do texto |
| Blocos da tabela (esquemático) | DIAGRAMA: blocos_tabela | Fallback — usar apenas se Visualizer falhar |
```

Substituir por:

```
| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Linha do tempo — Tabela Periódica | DIAGRAMA: timeline | Ao apresentar Mendeleev e Moseley |
| Célula do elemento | DIAGRAMA: celula_elemento | Ao explicar a representação dos elementos (Tópico 2) — exibir ANTES da explicação textual |
| Classificação dos elementos | DIAGRAMA: classificacao_elementos | Ao explicar metais, não-metais, metaloides e gases nobres |
| Blocos s, p, d, f (tabela real) | DIAGRAMA: blocos_tabela_real | Ao explicar os blocos — exibir ANTES do texto explicativo. ⚠️ Nunca substituir pelo blocos_tabela esquemático |
| Blocos da tabela (esquemático) | DIAGRAMA: blocos_tabela | Exibir APÓS o blocos_tabela_real como síntese dos grupos — os dois são obrigatórios, não alternativos |
| Grupos e famílias (tabela real) | DIAGRAMA: grupos_familias | Ao explicar períodos e grupos — exibir ANTES do texto |
```

---

## EDIÇÃO 2 — Substituir o bloco de Tabelas markdown da Seção 0

Localizar este bloco exato:

```
### Tabelas markdown (Seção 6):
- Tabela 1: Comparação Metais × Não-metais × Metaloides × Gases Nobres
- Tabela 2: Elementos químicos no corpo humano
```

Substituir por:

```
### Tabelas markdown (Seção 6):
- Tabela 1: Comparação Metais × Não-metais × Metaloides × Gases Nobres → exibir ao final do Tópico 6, antes das dicas de ouro
- Tabela 2: Elementos químicos no corpo humano → exibir logo após a Tabela 1, como extensão do Tópico 6
```

---

## EDIÇÃO 3 — Substituir a Nota ao Professor da Seção 0

Localizar este bloco exato:

```
### Nota ao Professor:
- DIAGRAMA: blocos_tabela_real e DIAGRAMA: grupos_familias → gerar via Visualizer (show_widget) com o SVG da Seção 12
- Tabela periódica completa → usar image_search (imagem real do material)
- Tabelas da Seção 6 são apresentadas como markdown no chat
```

Substituir por:

```
### Nota ao Professor:
- Todos os DIAGRAMAS → gerar via Visualizer (show_widget) com o SVG/HTML da Seção 12
- Tabela periódica completa → usar image_search (imagem real do material)
- Tabelas da Seção 6 são apresentadas como markdown no chat
- Sequência obrigatória ao explicar blocos:
  1. DIAGRAMA: blocos_tabela_real (posição na tabela real)
  2. DIAGRAMA: blocos_tabela (síntese dos grupos — esquemático)
  3. DIAGRAMA: grupos_familias (distribuição A/B/8A)
```

---

## EDIÇÃO 4 — Adicionar novo diagrama ao final da Seção 12

Localizar o fim da Seção 12 (última linha do arquivo ou último bloco de diagrama SVG/HTML da seção) e anexar o seguinte bloco após ele:

```
---

### DIAGRAMA: celula_elemento
Anatomia de uma célula da tabela periódica, usando sódio (Na) como exemplo. Mostra as quatro posições: número atômico (Z) no topo, símbolo no centro, nome abaixo e massa atômica na base, com setas e legendas coloridas. Gerar via show_widget (SVG).

```svg
<svg width="100%" viewBox="0 0 680 340" role="img">
<title>Anatomia da célula da tabela periódica</title>
<desc>Diagrama mostrando as quatro informações de uma célula da tabela periódica usando o sódio como exemplo</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</marker>
</defs>
<text class="th" x="340" y="28" text-anchor="middle" dominant-baseline="central">Anatomia da célula — exemplo: sódio (Na)</text>
<rect x="255" y="50" width="170" height="220" rx="6" fill="var(--color-background-secondary)" stroke="var(--color-border-primary)" stroke-width="1.5"/>
<line x1="255" y1="103" x2="425" y2="103" stroke="var(--color-border-tertiary)" stroke-width="0.8"/>
<line x1="255" y1="215" x2="425" y2="215" stroke="var(--color-border-tertiary)" stroke-width="0.8"/>
<line x1="255" y1="252" x2="425" y2="252" stroke="var(--color-border-tertiary)" stroke-width="0.8"/>
<text class="th" x="340" y="80" text-anchor="middle" dominant-baseline="central" font-size="20" fill="var(--color-text-secondary)">11</text>
<text x="340" y="162" text-anchor="middle" dominant-baseline="central" font-size="60" font-weight="500" fill="var(--color-text-primary)">Na</text>
<text class="ts" x="340" y="235" text-anchor="middle" dominant-baseline="central">sódio</text>
<text class="ts" x="340" y="268" text-anchor="middle" dominant-baseline="central" fill="var(--color-text-secondary)">22,99</text>
<line x1="255" y1="78" x2="175" y2="78" stroke="var(--color-text-tertiary)" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrow)"/>
<g class="c-purple">
  <rect x="10" y="52" width="162" height="52" rx="6" stroke-width="0.5"/>
  <text class="th" x="91" y="72" text-anchor="middle" dominant-baseline="central">Número atômico (Z)</text>
  <text class="ts" x="91" y="90" text-anchor="middle" dominant-baseline="central">n° de prótons; identifica</text>
  <text class="ts" x="91" y="103" text-anchor="middle" dominant-baseline="central">o elemento</text>
</g>
<line x1="255" y1="162" x2="175" y2="162" stroke="var(--color-text-tertiary)" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrow)"/>
<g class="c-teal">
  <rect x="10" y="136" width="162" height="52" rx="6" stroke-width="0.5"/>
  <text class="th" x="91" y="156" text-anchor="middle" dominant-baseline="central">Símbolo</text>
  <text class="ts" x="91" y="172" text-anchor="middle" dominant-baseline="central">1ª letra maiúscula,</text>
  <text class="ts" x="91" y="184" text-anchor="middle" dominant-baseline="central">2ª minúscula</text>
</g>
<line x1="425" y1="235" x2="505" y2="235" stroke="var(--color-text-tertiary)" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrow)"/>
<g class="c-amber">
  <rect x="508" y="212" width="162" height="46" rx="6" stroke-width="0.5"/>
  <text class="th" x="589" y="230" text-anchor="middle" dominant-baseline="central">Nome</text>
  <text class="ts" x="589" y="246" text-anchor="middle" dominant-baseline="central">nome do elemento</text>
</g>
<line x1="425" y1="268" x2="505" y2="285" stroke="var(--color-text-tertiary)" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrow)"/>
<g class="c-gray">
  <rect x="508" y="268" width="162" height="52" rx="6" stroke-width="0.5"/>
  <text class="th" x="589" y="286" text-anchor="middle" dominant-baseline="central">Massa atômica</text>
  <text class="ts" x="589" y="302" text-anchor="middle" dominant-baseline="central">média ponderada</text>
  <text class="ts" x="589" y="314" text-anchor="middle" dominant-baseline="central">dos isótopos (u)</text>
</g>
</svg>
```
```

---

Após aplicar todas as edições, confirme:
- Quantas linhas foram alteradas em cada edição
- Que nenhum outro conteúdo do arquivo foi modificado
- Que a Seção 12 agora contém o bloco `DIAGRAMA: celula_elemento` como último diagrama
```