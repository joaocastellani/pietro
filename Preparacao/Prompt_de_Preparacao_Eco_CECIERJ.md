# PROMPT DE PREPARAÇÃO — ECOLOGIA E CONSERVAÇÃO (Graduação)
# Livro: Elementos de Ecologia e Conservação — Vol. 1, Módulo 1
# Autores: Silva, Ferreira, Macedo, Andrade · Fundação CECIERJ, 2ª ed. 2008
#
# MODELO DE PREPS ADOTADO — 9 preps para 10 aulas:
#   eco-1-prep.md     · eco-2-prep.md · eco-3-prep.md · eco-4-prep.md
#   eco-5-prep.md     · eco-6-prep.md · eco-7-prep.md · eco-8-prep.md
#   eco-9-10-prep.md  → Aulas 9 e 10 JUNTAS
#
# Arquivos de entrada padrão:   eco-[N].md + eco-[N]-questoes.md
# Arquivos de entrada Aulas 9–10: eco-9-10.md + eco-9-10-questoes.md
#
# Arquivo gerado:      eco-[aula]-prep.md  (ou eco-9-10-prep.md)
# Mapa mental gerado:  mindmap_eco[aula].html  (ou mindmap_eco9-10.html)

---

## INSTRUÇÕES GERAIS

1. Use `project_knowledge_search` para localizar e ler
   `eco-[aula].md` e `eco-[aula]-questoes.md` inteiros
   antes de gerar qualquer conteúdo
2. Todo o conteúdo é gerado de uma vez, sem interação com o aluno
3. Preserve nomes científicos, leis, etapas de processos e
   classificações exatamente como no material capturado
4. Você pode inferir dicas e pegadinhas — não precisa citar o livro
5. Se detectar inconsistência factual, registre na Seção 8
6. Os SVGs da Seção 12 ficam embutidos no próprio `prep.md`
7. O nível de linguagem é de graduação — não simplifique demais,
   mas explique termos técnicos na Seção 2

---

## PERFIS DE AULA

Este livro tem quatro perfis de aula — declarados nos metadados
do `eco-[aula].md` (Seção 1):

| Perfil | Aulas típicas | Características |
|--------|--------------|-----------------|
| Histórico-conceitual | Aulas 1–2 | Cientistas, teorias, evolução do pensamento ecológico |
| Descritivo-científico | Aulas 3–8 | Níveis de organização, fatores abióticos, adaptações |
| Processual | Aulas 9–10 | Transferência de energia, biomassa, produtividade |
| Misto | Varia | Combinação de perfis |

---

## ESTRUTURA DO ARQUIVO DE PREPARAÇÃO

Gere nesta ordem. Seções [CONDICIONAL] só se o conteúdo existir.

---

### SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

**Gerada por último**, após a Seção 12 estar completa.

```
## DIAGRAMAS DISPONÍVEIS — eco-[aula]

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| [nome] | DIAGRAMA: [nome] | [contexto de uso] |

### Tabelas markdown (Seção 6):
- [lista das tabelas presentes]

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.
```

---

### SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — ECOLOGIA E CONSERVAÇÃO
- Aula nº:
- Título:
- Autor(a) da aula:
- Perfil: [histórico-conceitual / descritivo-científico /
           processual / misto]
- Processos principais: [lista ou "nenhum"]
- Cientistas citados: [lista ou "nenhum"]
- Leis e princípios: [lista ou "nenhum"]
- Objetivos de aprendizagem: [lista dos objetivos da aula]
```

---

### SEÇÃO 2 — RESUMO CONCEITUAL DA AULA

Resumo narrativo organizado por blocos temáticos.
Cada bloco: título em negrito + explicação em linguagem acessível
de graduação + conexão com exemplos ecológicos reais.

Para blocos com processos: apresente as etapas sequencialmente
e explique o que ocorre em cada uma e sua importância ecológica.

Para blocos histórico-conceituais: apresente a evolução das
ideias em ordem cronológica, destacando o que cada contribuição
mudou no pensamento ecológico.

Ao final desta seção, inclua sempre:
```
### Conexão com as aulas anteriores
[Como este conteúdo se relaciona com o que foi visto antes —
  útil para o aluno que estuda em sequência]
```

---

### SEÇÃO 3 — CIENTISTAS E HISTÓRIA DA ECOLOGIA [CONDICIONAL]

Gerar se a aula citar cientistas, naturalistas ou filósofos
com papel relevante no desenvolvimento da Ecologia.

Para cada cientista:
```
### [Nome completo] ([período ou data citada])
**Área:** [campo]
**Contribuição na aula:** [o que o livro descreve]
**O que mudou:** [impacto no pensamento ecológico]
**Associado a:** [obra, teoria, conceito — se citado]
**Contexto histórico:** [época, movimento intelectual]
```

---

### SEÇÃO 4 — LEIS, PRINCÍPIOS E TEORIAS [CONDICIONAL]

Gerar se a aula apresentar leis científicas, princípios
ecológicos nomeados ou teorias com enunciado identificável.

Para cada lei ou princípio:
```
### [Nome completo]
**Enunciado:** [conforme o material]
**Autor:** [origem — se citada]
**Aplicação ecológica:** [como o livro usa este princípio]
**Limitações ou controvérsias:** [se mencionadas]
💡 **Pegadinha:** [erro mais comum de interpretação]
```

---

### SEÇÃO 5 — PROCESSOS E FLUXOS ECOLÓGICOS [CONDICIONAL]

Gerar se a aula apresentar processos sequenciais ou fluxos
com etapas identificáveis (transferência de energia, ciclos
de matéria, sucessão, etc.).

Para cada processo:
```
### [Nome do processo]

**Etapas:**
1. [etapa 1 — local + substâncias envolvidas]
2. [etapa 2]
...

**Entradas:** [substâncias/energia de entrada]
**Saídas:** [substâncias/energia produzidas]
**Local/compartimento:** [organismo, bioma, ecossistema]
**Leis envolvidas:** [termodinâmica, etc. — se citadas]
**Equação resumida:** [se presente no material]

💡 **Pegadinha:** [erro mais comum com este processo]
```

---

### SEÇÃO 6 — DADOS FACTUAIS DENSOS [CONDICIONAL]

Gerar se a aula apresentar conjuntos de dados estruturados.
Usar **tabelas markdown** — não SVG para dados tabulares.
Adicionar coluna "⚠️ Pegadinha" quando relevante.

Tipos de tabela esperados neste livro:
- Fatores abióticos e seus efeitos nos organismos
- Comparação de adaptações por bioma ou grupo taxonômico
- Níveis de organização ecológica com exemplos
- Grandezas ecológicas (produtividade, biomassa, eficiência)
- Comparação de processos (fotossíntese vs. respiração,
  produção primária vs. secundária)

---

### SEÇÃO 7 — DICAS DE OURO

4–6 dicas inferidas do conteúdo. Foco em: pegadinhas de prova,
distinções sutis, erros comuns, macetes de memorização.

Temas prioritários para Ecologia:
- Confusão entre níveis de organização (população vs. comunidade
  vs. ecossistema vs. biosfera)
- Confusão entre fatores bióticos e abióticos
- Inversão de fluxo de energia vs. fluxo de matéria
- Confusão entre produtividade primária bruta e líquida
- Erros nas Leis da Termodinâmica aplicadas à Ecologia
- Distinção entre habitat e nicho ecológico

```
💡 **Dica [N] — [título curto]**
[explicação com exemplo ecológico quando útil]
```

---

### SEÇÃO 8 — ALERTAS DE INCONSISTÊNCIA [CONDICIONAL]

**ARQUIVO DE GAPS — gerar quando houver inferências ou ausências:**

Formato do arquivo `eco-[aula]-gaps.md`:

```markdown
# GAPS — eco-[aula]
# Gerado automaticamente pelo Prompt de Preparação

## INFERÊNCIAS USADAS NO PREP
Dados não capturados no material mas inferidos com conhecimento
geral. Verificar com o material original antes de disponibilizar
ao aluno.

| Seção | Campo | Valor inferido | Fonte da inferência |
|-------|-------|---------------|---------------------|
| [seção] | [campo] | [valor usado no prep] | [base da inferência] |

## DADOS AUSENTES — AÇÃO NECESSÁRIA
Dados que não puderam ser inferidos. Adicionar ao material
antes de disponibilizar o prep ao aluno.

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| [seção] | [campo] | [motivo] | [ação concreta] |
```

Gerar também para inconsistências factuais:
```
⚠️ ALERTA — [termo ou conceito]
- Dado no material: "[texto exato do arquivo .md]"
- Problema: [descrição do erro]
- Dado correto: [informação correta]
- Impacto na aula: [o que o Professor deve fazer]
```

Em Ecologia: verificar especialmente dados numéricos de
produtividade e biomassa, nomenclaturas taxonômicas,
enunciados de leis e classificações desatualizadas.

---

### SEÇÃO 9 — SÍNTESE DA AULA (para warm-up)

#### Bloco 1 — Conceitos e Definições

```
- **[Nome do conceito]**
  - Definição: `______` ([resposta esperada])
  - Exemplo: `______` ([exemplo do material])
```

#### Bloco 2 — Processos e Fluxos [se houver]

```
- **[Nome do processo]**
  - Entrada: `______` ([reagentes/matérias-primas])
  - Saída: `______` ([produtos])
  - Lei envolvida: `______` ([lei da termodinâmica, etc.])
```

#### Bloco 3 — Lacunas para Warm-Up

6–8 lacunas cobrindo obrigatoriamente:
- Pelo menos 1 por conceito principal do resumo (Seção 2)
- Pelo menos 1 por lei ou princípio (se houver — Seção 4)
- Pelo menos 1 por processo ou fluxo (se houver — Seção 5)
- Pelo menos 1 por **categoria/tipo** das tabelas da Seção 6
- Pelo menos 1 de cientista/contribuição histórica (se houver)
- Pelo menos 1 de aplicação contextual (exemplo de bioma,
  organismo real ou situação ecológica concreta)

```
N. [enunciado com `______` marcando a lacuna]
*(resposta: [resposta esperada])*
```

---

### SEÇÃO 10 — SÍNTESE DO LIVRO [CONDICIONAL]

**Só gerada se imagem da Síntese for anexada.**

```
### Síntese do Livro — [TEMA CENTRAL]

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| [posição no esquema] | [texto dado] | [resposta] |
```

Se não houver imagem: escreva
"Seção 10 não gerada — anexe a imagem da Síntese para incluir."

---

### SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

**Fonte exclusiva:** `eco-[aula]-questoes.md`
Se não disponível: "Seção 11 não gerada — adicione o arquivo ao KB."

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Gabarito | Obs. |
|---|---|---|---|---|---|
| Q-N | [1 linha] | [Dis/Interp/Id/Comp] | [F/M/D] | [resposta + justificativa] | [— ou ⚠️] |

Legenda de tipos: Dis = dissertativa · Interp = interpretação
de texto · Id = identificação · Comp = comparação

Regras:
- Infira gabaritos usando o conteúdo do `.md`
- Para dissertativas abertas: indique os pontos essenciais
  que a resposta deve conter
- Marque ⚠️ para: enunciado incompleto, figura não capturada,
  ambiguidade factual, erro já registrado na Seção 8

#### Bloco B — Questões modelo originais

5 questões originais inspiradas no estilo do `questoes.md`.
NÃO copiar nem parafrasear — criar contextos novos.

Distribuição:
- 2 dissertativas (médio)
- 1 interpretação de texto com trecho ecológico (médio)
- 1 questão de comparação entre conceitos (médio-difícil)
- 1 questão estilo dissertativa aprofundada (difícil)

```
**QM-[N]** · [tipo] · [dificuldade] · inspirada em: [Q-N]

[enunciado completo]

✅ Gabarito: [resposta esperada com pontos principais]
📝 Resolução: [desenvolvimento ou justificativa]
⚠️ Professor: referência de estilo — crie variações originais,
   nunca reproduza diretamente.
```

---

### SEÇÃO 12 — DIAGRAMAS SVG DA AULA

Os SVGs ficam **embutidos no próprio prep.md** como blocos de código.

**Formato de cada diagrama:**

```
### DIAGRAMA: [nome]
[descrição em 1 linha]

<svg width="100%" viewBox="0 0 680 H">
...código SVG completo...
</svg>
```

**Regras obrigatórias para todos os SVGs:**
- `width="100%"` e `viewBox="0 0 680 H"` — não alterar o 680
- Classes do Visualizer para nós: `c-purple`, `c-teal`, `c-amber`,
  `c-coral`, `c-gray`, `c-green`
- Classes de texto: `class="t"` (14px), `class="ts"` (12px),
  `class="th"` (14px bold)
- Alertas/pegadinhas: `c-coral`
- Sem gradientes, sem emojis, sem texto rotacionado
- Dark mode automático via classes — nunca hardcode hex para texto
- Incluir `<defs>` com marker de seta em cada SVG:
  ```
  <defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
  markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
  stroke-width="1.5" stroke-linecap="round"
  stroke-linejoin="round"/></marker></defs>
  ```

**Regras anti-sobreposição — verificar ANTES de posicionar cada elemento:**

Regra 1 — Packing de caixas numa mesma linha:
  `soma(larguras) + (n-1) × gap ≥ espaço_disponível → ERRO`
  Calcule explicitamente antes de atribuir coordenadas x.
  Espaço disponível = x_final − x_inicial (ex: x=40 a x=640 = 600px).
  Gap mínimo entre caixas: 8px.

Regra 2 — Texto dentro da caixa:
  `caracteres_do_texto_mais_longo × 7 + 24 ≤ largura_da_caixa`
  Se não couber: distribuir o texto em 2 linhas com palavras inteiras.
  NUNCA quebrar uma palavra no meio para forçá-la a caber.

Regra 3 — Altura mínima por número de linhas de conteúdo:
  1 linha de conteúdo → h = 44px
  2 linhas de conteúdo → h = 58px
  3 linhas de conteúdo → h = 72px
  Usar `dominant-baseline="central"` em todos os `<text>`.
  Linha 1: y = topo_caixa + 20px · Linha 2: y = topo_caixa + 38px · Linha 3: y = topo_caixa + 56px

Regra 4 — viewBox height:
  Calcular y_máximo = borda inferior do elemento mais baixo.
  Definir H = y_máximo + 40.
  Nunca fixar H sem verificar o elemento mais baixo.

**Por perfil da aula:**

**Histórico-conceitual → DIAGRAMA: timeline**
Linha do tempo dos naturalistas e ecólogos citados.
Eixo horizontal = tempo. Nós alternados acima/abaixo com box
colorido (nome + período) e contribuição em texto ts fora do box.
Cores: c-purple (Antiguidade–séc. XVIII) ·
       c-teal (séc. XIX) ·
       c-green (séc. XX) ·
       c-coral (controvérsias ou hipóteses debatidas)

**Descritivo-científico → DIAGRAMA: hierarquia_[tema]**
Hierarquia de níveis de organização ecológica ou classificação
de fatores (abióticos/bióticos, limitantes/não-limitantes).
Nó raiz (c-green) → níveis intermediários (c-teal) →
exemplos concretos (c-gray).
NÃO usar SVG para tabelas densas — usar markdown na Seção 6.

**Processual → DIAGRAMA: fluxo_[processo]**
Fluxo de energia ou matéria em ecossistemas.
Entradas em c-teal · transformações em c-green · perdas/saídas
em c-amber · perdas irrecuperáveis (calor) em c-coral.
Para cadeias alimentares: sequência linear com setas e
eficiência de transferência indicada entre os níveis.

**Misto → gerar os diagramas de todos os perfis presentes.**

---

## EXECUÇÃO

### Aulas individuais (eco-1 a eco-8)

1. Leia `eco-[N].md` e `eco-[N]-questoes.md` inteiros
2. Verifique se imagem da Síntese foi anexada:
   - ✅ Sim: gere todas as seções incluindo a 10
   - ⬜ Não: gere seções 0–9, 11, 12; indique que Seção 10
     pode ser adicionada depois com a imagem
3. Gere Seções 1–11 (conteúdo textual)
4. Gere Seção 12 (SVGs embutidos no prep)
5. Gere Seção 0 (índice) e posicione no início do arquivo
6. Salve em `/mnt/user-data/outputs/eco-[N]-prep.md`
7. Apresente com `present_files`
8. Gere o Mapa Mental HTML (ver seção abaixo)
9. Salve em `/mnt/user-data/outputs/mindmap_eco[N].html`
10. Apresente com `present_files`
11. Informe:
    "✅ Preparação concluída!
    - `eco-[N]-prep.md` → adicionar ao knowledge base
    - `mindmap_eco[N].html` → adicionar ao knowledge base"

---

### Aulas 9–10 agrupadas (eco-9-10) — instruções especiais

As Aulas 9 e 10 formam um par natural (mesma autora, tema contínuo:
Transferência de energia e biomassa I e II) e são preparadas
em um único arquivo conjunto.

1. Leia `eco-9-10.md` e `eco-9-10-questoes.md` inteiros
2. Na **Seção 1 — Metadados**, registre:
   ```
   - Aulas: 9 e 10 (par agrupado)
   - Títulos: Transferência de energia e biomassa I · II
   - Autora: Benedita Aglai O. da Silva
   - Perfil: processual
   ```
3. Na **Seção 2 — Resumo**, organize em dois blocos:
   ```
   ### Aula 9 — Transferência de energia e biomassa I
   [conteúdo da Aula 9]

   ### Aula 10 — Transferência de energia e biomassa II
   [conteúdo da Aula 10]

   ### Síntese integrada — o que une as duas aulas
   [como os conceitos se encadeiam entre a Aula 9 e a 10]
   ```
4. Na **Seção 9 — Síntese para warm-up**, gere lacunas cobrindo
   AMBAS as aulas (mínimo 10 lacunas no total)
5. Na **Seção 11 — Questões**, catalogue todas as questões de
   eco-9-10-questoes.md com a aula de origem indicada na coluna Obs.
6. Na **Seção 12 — SVGs**, gere:
   - DIAGRAMA: fluxo_energia_aula9 (processo da Aula 9)
   - DIAGRAMA: fluxo_energia_aula10 (processo da Aula 10)
   - DIAGRAMA: integracao_9_10 (visão conjunta dos dois fluxos,
     mostrando como a Aula 10 expande o modelo da Aula 9)
7. Salve em `/mnt/user-data/outputs/eco-9-10-prep.md`
8. Apresente com `present_files`
9. Gere o Mapa Mental HTML unificado das duas aulas
10. Salve em `/mnt/user-data/outputs/mindmap_eco9-10.html`
11. Apresente com `present_files`
12. Informe:
    "✅ Preparação concluída!
    - `eco-9-10-prep.md` → adicionar ao knowledge base
    - `mindmap_eco9-10.html` → adicionar ao knowledge base"

---

## GERAÇÃO DO MAPA MENTAL HTML

Arquivo HTML com mapa mental completo. Todos os cards iniciam
em verde escuro "Não testado".

**a) HEADER** — fundo #1B4332:
- "Ecologia e Conservação · Aula [N] · Graduação — CECIERJ"
- Título da aula (32px bold)
- "Mapa Mental — gerado na preparação"
- Legenda: verde=Dominado · vermelho=Reforçar · verde escuro=Não testado

**b) PÍLULA CENTRAL** — tema da aula, fundo #1B4332

**c) GRID DE CARDS** — um por tópico, todos verde escuro:
- Faixa lateral 3px · número em círculo · título em negrito
- Bullets com conteúdo · badge "Não testado"
- Para processos: etapas numeradas + entradas e saídas
- Para leis e princípios: enunciado resumido em destaque
- Para cientistas: nome → contribuição principal
- Para classificações: hierarquia com recuo visual

**d) DICAS DE OURO** — fundo #D8F3DC, borda #1B4332,
dicas da Seção 7, badge verde escuro numerado

**CSS obrigatório:**
- Fonte: 'Inter' (Google Fonts) · Fundo: #F4F2EE
- Cards: bg #ffffff · border-radius 14px ·
  box-shadow 0 2px 8px rgba(0,0,0,0.07)
- Grid: 3 colunas · font-size mínimo 13px · header 32px bold
- Cor primária: #1B4332 (verde floresta de Ecologia)
