# PROMPT DE PREPARAÇÃO — ARTES (9º ano)

Arquivo de entrada: `art-[u]-[c].md`
Arquivo gerado:      `art-[u]-[c]-prep.md`
Mapa mental gerado:  `mindmap_art[u][c].html`

---

## INSTRUÇÕES GERAIS

1. Use `project_knowledge_search` para localizar e ler
   `art-[u]-[c].md` inteiro
   antes de gerar qualquer conteúdo
2. Todo o conteúdo é gerado de uma vez, sem interação com o aluno
3. Preserve títulos de obras, nomes de artistas, datas, técnicas,
   dimensões e acervos exatamente como aparecem no material
4. Você pode inferir dicas e pegadinhas — não precisa citar o livro
5. Se detectar inconsistência factual, registre na Seção 8
6. Os SVGs da Seção 12 ficam embutidos no próprio `prep.md`
7. O `art-[u]-[c].md` pode ter sido gerado em múltiplas execuções
   (append) — leia o arquivo completo antes de iniciar

---

## PERFIS DE CAPÍTULO

Artes no 9º ano tem quatro perfis:

| Perfil | Características | Exemplos |
|--------|----------------|---------|
| Histórico-conceitual | Movimentos artísticos, contexto histórico, manifestos | Neoconcretismo, Tropicalismo, Semana de 1922 |
| Analítico-temático | Análise formal de obras, relação obra-espectador, linguagens | Arte engajada, Arte e religião |
| Prático-criativo | Propostas de criação, experimentação de linguagens | Capítulos com "Arte e você" como eixo central |
| Misto | Combinação dos perfis acima | — |

---

## ESTRUTURA DO ARQUIVO DE PREPARAÇÃO

Gere nesta ordem. Seções [CONDICIONAL] só se o conteúdo existir.

---

### SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

**Gerada por último**, após a Seção 12 estar completa.

```
## DIAGRAMAS DISPONÍVEIS — art-[u]-[c]

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| [nome] | DIAGRAMA: [nome] | [contexto de uso] |

### Tabelas markdown (Seção 6):
- [lista das tabelas presentes]

### Obras para image_search (Seção 3):
- [lista de obras com termos de busca recomendados]

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.
Para obras: use image_search com os termos da Seção 3 ou
printscreens das páginas do livro se disponíveis.
```

---

### SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — ARTES
- Unidade:
- Capítulo:
- Tema:
- Perfil: [histórico-conceitual / analítico-temático /
           prático-criativo / misto]
- Movimentos artísticos: [lista ou "nenhum"]
- Artistas principais: [lista ou "nenhum"]
- Linguagens artísticas: [lista: pintura / escultura /
  instalação / performance / dança / música / etc.]
```

---

### SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

Resumo narrativo organizado por blocos temáticos.
Cada bloco: título em negrito + explicação nível 9º ano +
conexão com obras e artistas reais do material.

Para blocos de movimento artístico: apresente o contexto
histórico que o originou, suas características formais
principais e os artistas e obras representativos do material.

Para blocos de análise de obra: apresente a obra, seu artista,
os elementos formais analisados no texto e a relação com o
espectador ou contexto histórico descrita no material.

Para blocos de linguagem artística integrada: explique como
as diferentes linguagens se combinam e qual o resultado
estético ou conceitual dessa integração.

---

### SEÇÃO 3 — ARTISTAS E OBRAS [CONDICIONAL]

Gerar se o capítulo citar artistas com obra relevante.
Inclui artistas das seções "Conheça o artista" e do Bloco G
("Arte e você") quando pertinentes ao conteúdo teórico.

Para cada artista:
```
### [Nome completo] ([datas — se citadas])
**Origem:** [nacionalidade / cidade — se citada]
**Movimento(s):** [movimento(s) ao qual pertence]
**Contribuição descrita no material:** [trajetória e inovação]
**Obras no capítulo:**
  - *[Título]* ([ano]) · [técnica] · [dimensões] · [acervo]
    → [descrição e relevância no capítulo]
🔍 **image_search:** "[título] [artista] [ano]"
💡 **Pegadinha:** [confusão mais comum sobre este artista ou obra]
```

---

### SEÇÃO 4 — MOVIMENTOS ARTÍSTICOS [CONDICIONAL]

Gerar se o capítulo apresentar movimentos com origem,
características e contexto histórico identificáveis.

Para cada movimento:
```
### [Nome do movimento]
**Período e local:** [época e país/região de origem]
**Contexto:** [o que motivou o surgimento do movimento]
**Características formais:**
  - [característica 1]
  - [característica 2]
**Artistas principais citados:** [lista com datas se presentes]
**Obras representativas no capítulo:** [lista]
**Relação com outros movimentos:** [oposição, influência, ruptura]
💡 **Pegadinha:** [confusão mais comum — ex: trocar Expressionismo
   por Cubismo, confundir Concretismo com Neoconcretismo]
```

---

### SEÇÃO 5 — ANÁLISE DE OBRAS [CONDICIONAL]

Gerar se o capítulo apresentar análise formal ou interpretativa
de obras específicas — elementos visuais, composição, relação
com o espectador.

Para cada obra analisada:
```
### *[Título]* — [Artista] ([ano])
**Linguagem:** [pintura / escultura / instalação / performance /
  dança / misto]
**Técnica e dimensões:** [conforme o material]
**Acervo:** [conforme o material]
**Elementos formais analisados:**
  - Cor: [uso de cor conforme o texto]
  - Forma: [uso de forma conforme o texto]
  - Espaço: [uso do espaço conforme o texto]
  - Movimento: [se citado]
  - Outros: [textura, luz, sombra — se citados]
**Relação obra-espectador:** [conforme o material]
**Contexto de exibição:** [espaço, evento, ano — se citados]
💡 **Pegadinha:** [erro mais comum na leitura desta obra]
```

---

### SEÇÃO 6 — DADOS DENSOS [CONDICIONAL]

Gerar se o capítulo apresentar conjuntos estruturados de dados.
Usar **tabelas markdown** — não SVG para dados tabulares.
Adicionar coluna "⚠️ Pegadinha" quando relevante.

Tipos de tabela esperados em Artes do 9º ano:
- Comparação entre movimentos (período, características, artistas)
- Obras com ficha técnica completa (artista, ano, técnica,
  dimensões, acervo)
- Artistas com datas, movimento e obras principais
- Linguagens artísticas e suas características

REGRAS CRÍTICAS para tabelas:
- Se um dado não foi capturado no material, NÃO deixe célula
  vazia sem explicação. Em vez disso:
  1. Gere um alerta na SEÇÃO 8 com o formato:
     ⚠️ DADO AUSENTE — [tabela/campo]
     Campo: [qual célula está incompleta]
     Motivo: [não capturado / legenda ilegível no screenshot]
     Ação: verificar printscreen original ou reprocessar
  2. Na tabela, marque a célula com "⚠️ ver Seção 8"
- Célula com dado inferido → marcar "⚠️ inferido" +
  registrar no gaps.md

---

### SEÇÃO 7 — DICAS DE OURO

4–6 dicas inferidas do conteúdo. Foco em: pegadinhas de prova,
confusões entre movimentos, inversão de características formais,
artistas com obras parecidas, termos com definições próximas.

Temas prioritários para Artes:
- Confusão entre movimentos artísticos próximos
  (ex: Concretismo vs. Neoconcretismo; Futurismo vs. Cubismo)
- Inversão de características formais entre movimentos
- Confusão entre artistas do mesmo movimento
- Obras com títulos parecidos de artistas diferentes
- Distinção entre linguagens artísticas integradas
  (ex: instalação vs. performance vs. happening)
- Confusão entre técnica e linguagem

```
💡 **Dica [N] — [título curto]**
[explicação com exemplo de obra ou artista concreto do material]
```

---

### SEÇÃO 8 — ALERTAS DE INCONSISTÊNCIA [CONDICIONAL]

**ARQUIVO DE GAPS — gerar quando houver inferências ou ausências:**

Formato do arquivo `art-[u]-[c]-gaps.md`:

```markdown
# GAPS — art-[u]-[c]
# Gerado automaticamente pelo Prompt de Preparação

## INFERÊNCIAS USADAS NO PREP
Dados não capturados no material mas inferidos.
Verificar com os screenshots originais antes de disponibilizar
ao aluno.

| Seção | Campo | Valor inferido | Fonte da inferência |
|-------|-------|---------------|---------------------|
| [seção] | [campo] | [valor usado no prep] | [base] |

## DADOS AUSENTES — AÇÃO NECESSÁRIA
Dados que não puderam ser inferidos. Verificar nos screenshots.

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|--------------------|
| [seção] | [campo] | [motivo] | [ação concreta] |

## IMAGENS PARA REVISÃO
Obras identificadas no material mas com legenda ilegível
no screenshot. Verificar printscreen original.

| Obra | Dado ilegível | Screenshot de referência |
|------|--------------|--------------------------|
| [título/artista] | [dado ausente] | [pág. X] |
```

Gerar também para inconsistências factuais:
```
⚠️ ALERTA — [obra, artista ou dado]
- Dado no material: "[texto exato do arquivo .md]"
- Problema: [descrição do erro ou imprecisão]
- Dado correto: [informação correta]
- Impacto na aula: [o que o Professor deve fazer]
```

**Fragmentos truncados — verificar no material capturado:**
Se o `.md` contiver texto interrompido no meio de uma frase,
gerar alerta:
```
⚠️ FRAGMENTO TRUNCADO — [seção/bloco]
Texto interrompido: "[trecho incompleto]"
Ação: reprocessar o screenshot correspondente
```

---

### SEÇÃO 9 — MATERIAL DE AULA

#### Bloco 1 — Roteiro de Apresentação

Sequência sugerida para a Etapa 1 (resumo):

```
1. [tema/obra/movimento] — [tempo estimado] min
   Visuais: [image_search / SVG Seção 12 / printscreen]
2. [próximo tema] — [tempo estimado] min
   Visuais: [...]
```

#### Bloco 2 — Perguntas de Verificação

5–7 perguntas orais para o professor verificar compreensão
durante o resumo. Foco em: movimento → característica,
obra → artista → contexto, linguagem → técnica.

```
N. [pergunta direta sobre o conteúdo]
   *(resposta esperada: [resposta])*
```

#### Bloco 3 — Lacunas para Warm-Up

6–8 lacunas cobrindo obrigatoriamente:
- Pelo menos 1 por movimento artístico principal
- Pelo menos 1 de obra → artista ou artista → obra
- Pelo menos 1 de característica formal de movimento
- Pelo menos 1 de contexto histórico ou período
- Pelo menos 1 de técnica ou linguagem artística

REGRA CRÍTICA — lacunas:
- Gere lacuna APENAS para dados explicitamente presentes
  no material capturado. Nunca crie lacuna cuja resposta
  exige inferência ou conhecimento externo ao material.

```
N. [enunciado com `______` marcando a lacuna]
*(resposta: [resposta esperada])*
```

#### Bloco 4 — Tabela Síntese

Tabela markdown obrigatória (6–10 linhas). Cobre conceitos
principais, fórmulas-chave, pelo menos 1 aplicação prática e
1 pegadinha/alerta. Formato exato:

```
| Conceito | Lacuna — resposta esperada |
|---|---|
| [conceito 1] | `______` → *[resposta]* |
| [conceito 2] | `______` → *[resposta]* |
| [fórmula ou dado] | `______` → *[resposta]* |
| [aplicação prática] | `______` → *[resposta]* |
| [pegadinha ou alerta] | `______` → *[resposta]* |
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

**Fontes:**
- SEÇÃO ATIVIDADES do `art-[u]-[c].md` → Questões de Atividades (Origem: AT)
- BLOCO H (QI-N) do `art-[u]-[c].md` → Questões Intercaladas (Origem: IC)

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Obs. |
|---|---|---|---|---|---|
| Q-N | [1 linha] | [MC/Dis/Obra/Ident/Assoc/VF] | [F/M/D] | [— ou ⚠️] |

Legenda: MC = múltipla escolha · Dis = dissertativa ·
Obra = análise de obra · Ident = identificação ·
Assoc = associação · VF = V-F

Regras:
- A apostila NÃO traz gabarito — NUNCA inferir ou preencher
  a coluna Gabarito. O campo não existe nesta tabela.
- Para questões dissertativas: registre apenas o enunciado
  resumido, tipo e dificuldade
- Marque ⚠️ para: obra com legenda ilegível no screenshot,
  enunciado ambíguo, erro já registrado na Seção 8

#### Bloco B — Questões modelo originais

5 questões originais inspiradas no estilo da SEÇÃO ATIVIDADES.
NÃO copiar nem parafrasear — criar contextos novos.

Distribuição:
- 2 múltipla escolha (médio) — pelo menos 1 com obra visual
- 1 análise de obra com descrição formal (médio)
- 1 questão de comparação entre movimentos (médio-difícil)
- 1 dissertativa sobre relação obra-contexto histórico (difícil)

```
**QM-[N]** · [tipo] · [dificuldade] · inspirada em: [Q-N]
🔍 image_search: "[título da obra] [artista] [ano]"

[enunciado completo]

a) [alt]  b) [alt]  c) [alt]  d) [alt]  (apenas para MC)

✅ Gabarito: [letra] (apenas para MC)
📝 Resolução: [desenvolvimento ou justificativa — para todos os tipos]
⚠️ Professor: referência de estilo — crie variações originais,
   nunca reproduza diretamente.
```

Nota: questões dissertativas originais NÃO têm gabarito único —
fornecer apenas a resolução com os pontos essenciais esperados.

---

### SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

Os SVGs ficam embutidos no próprio prep.md.

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
  ⚠️ OBRIGATÓRIO em todos os SVGs, mesmo nos que não usam setas.

**Regras anti-sobreposição — verificar ANTES de posicionar:**

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
  1 linha → h = 44px · 2 linhas → h = 58px · 3 linhas → h = 72px
  Usar `dominant-baseline="central"` em todos os `<text>`.
  Linha 1: y = topo + 20px · Linha 2: y = topo + 38px · Linha 3: y = topo + 56px

Regra 4 — viewBox height:
  Calcular y_máximo = borda inferior do elemento mais baixo.
  Definir H = y_máximo + 40.
  Nunca fixar H sem verificar o elemento mais baixo.

**Por perfil do capítulo:**

**Histórico-conceitual → DIAGRAMA: mapa_movimentos_[tema]**
Mapa de movimentos artísticos e suas relações.
Movimento central ou período (c-purple) → movimentos derivados
ou em oposição (c-teal) → artistas e obras representativas (c-gray).
Ex: Ruptura séc. XX → Futurismo / Expressionismo / Cubismo
→ Boccioni / Kirchner / Picasso.

**Analítico-temático → DIAGRAMA: analise_[obra_ou_tema]**
Diagrama de análise formal da obra principal do capítulo.
Obra central (c-purple) → elementos formais (c-teal: cor, forma,
espaço, movimento) → relação obra-espectador (c-amber) →
contexto histórico (c-gray).

**Prático-criativo → DIAGRAMA: fluxo_criativo_[proposta]**
Fluxo da proposta criativa do capítulo.
Referência artística (c-teal) → proposta (c-purple) →
materiais/técnicas (c-amber) → resultado esperado (c-green).

**Misto → regra de priorização:**
Avalie quantos elementos reais existem por perfil no material:
- Se um perfil tem ≥ 4 movimentos/obras/processos → gerar seu diagrama
- Se um perfil tem < 4 elementos → incorporar no diagrama do perfil
  dominante como nós secundários
- Máximo 2 SVGs por capítulo misto
- Perfil dominante = o que concentra mais conteúdo no material

---

## EXECUÇÃO

1. Leia `art-[u]-[c].md` inteiro
2. Verifique se imagem da Síntese foi anexada:
   - ✅ Sim: gere todas as seções incluindo a 10
   - ⬜ Não: gere seções 0–9, 11, 12; indique que Seção 10
     pode ser adicionada depois com a imagem
3. Gere Seções 1–11 (conteúdo textual)
4. Antes de gerar a Seção 12:
   a) Varra todas as imagens anexadas: identifique diagramas
      visuais (esquemas, fluxos, tabelas estruturais, mapas,
      gráficos) e decida para cada um: SVG na Seção 12 ·
      markdown na Seção 6 · registrar na Seção 8 como ausente.
   b) Gere a Seção 12 com todos os SVGs identificados.
   c) Verifique cobertura visual: para cada bloco temático
      da Seção 2, confirme se há ao menos um recurso visual
      (SVG na Seção 12 · tabela na Seção 6 · image_search).
      Tópicos sem cobertura → adicionar à Seção 8:
      ⚠️ VISUAL AUSENTE — [tópico]
      - Sugestão: [image_search query ou tipo de SVG]
      - Ação: usar image_search na aula / gerar SVG na revisão
5. Gere Seção 0 (índice) e posicione no início do arquivo
6. Salve em `/mnt/user-data/outputs/art-[u]-[c]-prep.md`
7. Apresente com `present_files`
8. Gere o Mapa Mental inline (ver seção abaixo)
9. Salve em `/mnt/user-data/outputs/mindmap_art[u][c].html`
   (cópia de referência — não precisa ir para o KB)
10. Apresente com `present_files`
11. Informe:
    "✅ Preparação concluída!
    - `art-[u]-[c]-prep.md` → adicionar ao knowledge base
    - `mindmap_art[u][c].html` → referência visual (não vai para o KB)"

---

## GERAÇÃO DO MAPA MENTAL INLINE

O mindmap é gerado como widget HTML inline via Visualizer —
renderiza diretamente na conversa, sem abrir aba separada.
NÃO salvar como arquivo no KB.

### Fonte de conteúdo
- Tópicos: Seção 2 do prep (um nó por bloco temático)
- Fórmulas/notações: Seção 4 do prep
- Pegadinhas: Seção 7 e alertas da Seção 8
- Dicas de ouro: Seção 7 do prep

### Template HTML

Usar o template universal da Parte 1 deste prompt, preenchendo:
- `[COR_PRIMARIA]` → `#7B2D8B`
- `[TEMA DO CAPÍTULO]` → título da Seção 1 do prep
- `[Matéria]` → `Artes`
- Um `.branch` por tópico da Seção 2
- Leaves com bullets, fórmulas (tag `.fm`) e alertas (tag `.warn`)
- Dicas de ouro da Seção 7

### Entrega
Chamar `show_widget` com:
- `title`: `"mindmap_art[u][c]"`
- `loading_messages`: `["Montando o mapa do capítulo..."]`
- `widget_code`: HTML preenchido

Após renderizar, salvar também uma cópia em
`/mnt/user-data/outputs/mindmap_art[u][c].html`
e apresentar com `present_files` como referência.
