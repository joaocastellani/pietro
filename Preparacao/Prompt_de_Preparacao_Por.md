# PROMPT DE PREPARAÇÃO — PORTUGUÊS (9º ano)

Arquivos de entrada: `por-[u]-[c].md` + `por-[u]-[c]-questoes.md`
Arquivo gerado:      `por-[u]-[c]-prep.md`
Mapa mental gerado:  `mindmap_por[u][c].html`

---

## INSTRUÇÕES GERAIS

1. Use `project_knowledge_search` para localizar e ler
   `por-[u]-[c].md` e `por-[u]-[c]-questoes.md` inteiros
   antes de gerar qualquer conteúdo
2. Todo o conteúdo é gerado de uma vez, sem interação com o aluno
3. Preserve exemplos e contraexemplos gramaticais exatamente
   como aparecem no material capturado
4. Você pode inferir dicas e pegadinhas — não precisa citar o livro
5. Se detectar inconsistência factual ou erro gramatical no material,
   registre na Seção 8
6. Os SVGs da Seção 12 ficam embutidos no próprio `prep.md` —
   não gerar arquivos externos de imagem

---

## PERFIS DE CAPÍTULO

Português no 9º ano tem quatro perfis — declarados nos
metadados do `por-[u]-[c].md` (Seção 1):

| Perfil | Características |
|--------|----------------|
| leitura-interpretação | Foco em texto-base, análise literária, intertextualidade |
| gramatical | Foco em regras, classificações, exemplos e contraexemplos |
| produção textual | Foco em gênero-alvo, estrutura, processo de escrita |
| reflexão linguística | Foco em variação, oralidade, norma culta, história da língua |
| misto | Combinação dos perfis acima — típico na maioria dos capítulos |

---

## ESTRUTURA DO ARQUIVO DE PREPARAÇÃO

Gere nesta ordem. Seções [CONDICIONAL] só se o conteúdo existir.

---

### SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

**Gerada por último**, após a Seção 12 estar completa.

```
## DIAGRAMAS DISPONÍVEIS — por-[u]-[c]

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
# PREPARAÇÃO DE AULA — PORTUGUÊS
- Unidade:
- Capítulo:
- Tema:
- Perfil: [leitura-interpretação / gramatical / produção textual /
           reflexão linguística / misto]
- Seções presentes: [lista das seções do capítulo]
- Texto-base principal: [título, autor, gênero — ou "nenhum"]
- Gênero-alvo de produção: [nome do gênero — ou "nenhum"]
- Tópico(s) gramatical(is): [lista — ou "nenhum"]
```

---

### SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

Resumo narrativo organizado pelas seções do capítulo
(Interpretação de texto → Gramática → Produção textual →
Reflexão → outras seções presentes).

Para cada seção:
- Título em negrito + explicação nível 9º ano
- Conexão com o texto-base quando estabelecida pelo material
- Exemplos concretos do capítulo (frases, trechos, obras)

Para seções de gramática: apresente a regra principal,
exemplos e contraexemplos do material, e casos especiais.

Para seções de produção textual: apresente as características
do gênero-alvo e as etapas do processo de escrita.

---

### SEÇÃO 3 — TEXTO-BASE [CONDICIONAL]

Gerar SEMPRE que o capítulo apresentar texto(s) para leitura.
Cada texto-base = uma entrada separada.

Para cada texto-base:
```
### [Título] — [Autor]

**Gênero:** [poema / crônica / conto / notícia / artigo /
             tirinha / charge / carta / outro]
**Fonte:** [como aparece no material]
**Contexto:** [época, movimento literário, situação comunicativa
               — infira com base no material]

**Tema central:** [em 1–2 linhas]
**Recursos expressivos relevantes:**
- [figura de linguagem ou recurso + exemplo do texto]

**Relação com o conteúdo do capítulo:**
- [como o texto ilustra ou motiva os tópicos estudados]

**Pontos de atenção para a aula:**
- [aspectos que o aluno tende a não perceber na primeira leitura]
```

---

### SEÇÃO 4 — GRAMÁTICA [CONDICIONAL]

Gerar SEMPRE que o capítulo tiver seção de gramática,
língua em uso ou reflexão linguística gramatical.

Para cada tópico gramatical:
```
### [Nome do tópico — exato como no material]

**Regra principal:**
[conforme o material — não parafrasear a essência da regra]

**Exemplos do material:**
- [frase de exemplo 1 — preserve exatamente]
- [frase de exemplo 2 — preserve exatamente]

**Contraexemplos (se presentes no material):**
- [frase incorreta / caso especial]

**Subseções / classificações:**
[lista ou tabela se houver subdivisões no material]

**Casos especiais ou exceções:**
[conforme o material — se houver]

💡 **Pegadinha:** [erro mais comum dos alunos neste tópico]
```

---

### SEÇÃO 5 — PRODUÇÃO TEXTUAL [CONDICIONAL]

Gerar SEMPRE que o capítulo incluir seção de produção textual
com conteúdo teórico sobre o gênero.

```
### Gênero-alvo: [nome]

**Definição e função social:**
[para que serve, quem escreve, onde circula]

**Características do gênero:**
- Estrutura: [introdução / desenvolvimento / conclusão
              ou outra organização específica do gênero]
- Linguagem e registro: [formal / coloquial / técnico /
                         objetivo / subjetivo]
- Recursos linguísticos característicos: [lista]
- Situação comunicativa: [emissor, receptor, suporte]

**Processo de escrita conforme o material:**
1. Planejamento: [o que o material orienta]
2. Rascunho: [estrutura recomendada]
3. Revisão: [critérios de avaliação, se presentes]

**Critérios de avaliação (se listados no material):**
[tabela ou lista conforme o material]

**Exemplos do gênero apresentados no capítulo:**
[título, autor, fonte — se houver]

💡 **Pegadinha:** [erro mais comum ao escrever este gênero]
```

---

### SEÇÃO 6 — DADOS TABULARES [CONDICIONAL]

Gerar se o capítulo apresentar tabelas, quadros comparativos
ou listas estruturadas com múltiplos atributos.
Ex: tabela de conjunções, quadro de pronomes, conjugações verbais,
comparativo entre gêneros textuais.

Reproduzir cada tabela em markdown fiel ao material.
Não omitir nenhuma coluna ou linha da tabela original.

---

### SEÇÃO 7 — DICAS DE OURO

Liste 4–6 dicas inferidas a partir do conteúdo do capítulo.
Foco em: pegadinhas de prova, distinções sutis entre conceitos,
erros comuns de gramática, macetes para identificar gênero
textual, armadilhas de interpretação.

```
💡 **Dica 1 — [título curto]**
[explicação objetiva, com exemplo do capítulo quando útil]
```

---

### SEÇÃO 8 — ALERTAS E LACUNAS [CONDICIONAL]

Gerar se houver dados inferidos, inconsistências ou lacunas
no material capturado.

```
## DADOS INFERIDOS — verificar antes de usar na aula

| Seção | Campo | Valor inferido | Fonte da inferência |
|-------|-------|----------------|---------------------|
| [seção] | [campo] | [valor usado] | [base da inferência] |

## DADOS AUSENTES — ação necessária

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|--------------------|------------------|
| [seção] | [campo] | [motivo] | [ação concreta] |
```

Para erros gramaticais ou inconsistências no material:
```
⚠️ ALERTA — [termo ou regra]
- Dado no material: "[texto exato do arquivo .md]"
- Problema: [descrição do erro ou imprecisão]
- Dado correto: [informação correta]
- Impacto na aula: [o que o Professor deve fazer]
```

Para fragmentos truncados no arquivo de captura:
```
⚠️ FRAGMENTO TRUNCADO — [seção/bloco do .md]
- Texto: "[trecho exato como aparece no arquivo]"
- Problema: texto interrompido — conteúdo ausente
- Ação: rever o material original e completar a captura
```

---

### SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

```
- **[Conceito linguístico ou gramatical]**
  - Definição: `______` ([resposta esperada])
  - Exemplo: `______` ([frase ou caso do material])
```

#### Bloco 2 — Texto-base e Gênero [se houver]

```
- **[Título do texto / Gênero estudado]**
  - Autor: `______` ([resposta])
  - Gênero: `______` ([resposta])
  - Tema central: `______` ([resposta em 1 linha])
  - Característica definidora do gênero: `______` ([resposta])
```

#### Bloco 3 — Lacunas para Warm-Up

6–8 lacunas cobrindo obrigatoriamente:
- Pelo menos 1 por conceito principal da Seção 2
- Pelo menos 1 de regra gramatical com exemplo (se houver — Seção 4)
- Pelo menos 1 de gênero textual ou texto-base (se houver — Seção 3)
- Pelo menos 1 de produção textual (se houver — Seção 5)
- Pelo menos 1 de aplicação contextual (frase ou situação real)

REGRA CRÍTICA — lacunas:
- Gere lacuna APENAS para termos e dados explicitamente presentes
  no material capturado. Nunca crie lacuna cuja resposta exige
  inferência ou conhecimento externo ao material.
- Para regras gramaticais: a lacuna deve testar a regra,
  não a memorização de nome técnico.

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

**Só gerada se imagem da página Síntese for anexada.**

A página Síntese do livro de Português apresenta tipicamente
dois esquemas: um sobre o gênero textual do capítulo e um
sobre um conceito linguístico. Gere uma entrada para cada
esquema identificado na imagem.

Para cada esquema:
```
### Síntese — [TEMA CENTRAL DO ESQUEMA]

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| [posição no esquema] | [texto dado] | [resposta] |
```

LACUNAS — CRÍTICO:
O livro de Português apresenta a Síntese com os esquemas
preenchidos (sem campos em branco para o aluno preencher).
Nesse caso, gere lacunas inferidas para TODOS os nós
secundários — o Professor cobre o nó e o aluno reconstitui.
NUNCA deixe a coluna 'Lacuna — resposta esperada' vazia:
- Se o nó tem texto dado: a lacuna é esse texto
  acrescido de contexto mínimo para o aluno reconstituir.
- Exemplo: nó 'Introdução' → lacuna = 'Introdução
  (primeira parte do texto informativo — apresenta o tema)'

Se não houver imagem: escreva
"Seção 10 não gerada — anexe a imagem da Síntese para incluir."

---

### SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

**Fontes:**
- Atividades: `por-[u]-[c]-questoes.md`
- Intercaladas: Bloco G do `por-[u]-[c].md`

Se nenhum arquivo disponível: "Seção 11 não gerada — adicione
os arquivos ao KB."

#### Bloco A — Catálogo das questões

**A.1 — Questões intercaladas (Bloco G do conteúdo)**

| # | Seção de origem | Enunciado resumido | Tipo | Dif. | Obs. |
|---|---|---|---|---|---|
| QI-N | [seção] | [1 linha] | [Interp/Gram/Assoc/Dis/PT] | [F/M/D] | [— ou ⚠️] |

**A.2 — Questões das Atividades**

| # | Enunciado resumido | Tipo | Dif. | Gabarito | Obs. |
|---|---|---|---|---|---|
| Q-N | [1 linha] | [MC/Interp/Gram/Assoc/Dis/PT/VF/Reesc] | [F/M/D] | [resposta + justificativa] | [— ou ⚠️] |
| QC-N | [1 linha] | [MC/Interp/Gram/...] | [F/M/D] | [letra + justificativa] | [— ou ⚠️] |

Legenda de tipos:
MC = múltipla escolha · Interp = interpretação · Gram = gramática ·
Assoc = associação · Dis = dissertativa · PT = produção textual ·
VF = V-F · Reesc = reescrita · Id = identificação · Cor = correção gramatical

Regras:
- Para questões intercaladas (QI-): A apostila não traz gabarito
  — NUNCA inferir. Coluna Gabarito não existe na tabela A.1.
- Para questões das Atividades (Q- e QC-): infira gabaritos
  usando o conteúdo do `.md`
- Para questões de interpretação: indique o elemento do texto
  que leva à resposta correta
- Para questões de múltipla escolha: indique a alternativa
  correta e justifique em 1 linha
- Marque ⚠️ para: enunciado incompleto, imagem não capturada,
  ambiguidade, erro já registrado na Seção 8

#### Bloco B — Questões modelo originais

5 questões originais inspiradas no estilo do `questoes.md`.
NÃO copiar nem parafrasear — criar contextos novos.

Distribuição por perfil do capítulo:

**leitura-interpretação:**
- 2 interpretação de texto (médio)
- 1 análise de recurso expressivo (médio)
- 1 múltipla escolha estilo concurso (difícil)
- 1 dissertativa com texto-base novo (difícil)

**gramatical:**
- 2 identificação ou classificação (médio)
- 1 reescrita com transformação (médio)
- 1 múltipla escolha estilo concurso (difícil)
- 1 correção gramatical com justificativa (médio-difícil)

**produção textual:**
- 2 dissertativa sobre características do gênero (médio)
- 1 múltipla escolha estilo concurso (difícil)
- 1 reescrita com adequação de registro (médio)
- 1 proposta de produção textual resumida (difícil)

**misto:**
- 1 interpretação de texto (médio)
- 1 gramática / identificação (médio)
- 1 múltipla escolha estilo concurso (difícil)
- 1 dissertativa (médio-difícil)
- 1 produção textual ou reescrita (difícil)

```
**QM-[N]** · [tipo] · [dificuldade] · inspirada em: [QI-N ou Q-N]

[> Texto: APENAS se a questão usar fonte primária]

[enunciado completo]

a) [alt]  b) [alt]  c) [alt]  d) [alt]  (apenas para MC)

✅ Gabarito: [letra ou resposta]
📝 Resolução: [desenvolvimento ou justificativa]
⚠️ Professor: referência de estilo — crie variações originais,
   nunca reproduza diretamente.
```

Nota: questões dissertativas e de produção textual NÃO têm
gabarito único — fornecer apenas a resolução com os pontos
essenciais esperados.

---

### SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

Os SVGs ficam embutidos no próprio prep.md.
O Professor lê o SVG da Seção 12 e passa ao Visualizer para
renderizar inline — sem arquivos externos, sem dependência de KB.

**Nota:** textos literários, trechos de obras e tirinhas NÃO
são gerados como SVG — use image_search na aula para imagens
de obras, e apresente textos como markdown recuado no chat.
SVGs são para esquemas conceituais, fluxos e relações linguísticas.

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
- NUNCA usar hardcode hex em fill de qualquer elemento
  (caixas, texto, fundos). Use sempre as classes do Visualizer.
- Linhas de conexão (`<line>`, `<path>` fora de defs): usar
  `stroke="var(--c-teal)"` ou a variável CSS correspondente
  à classe do nó de origem — NUNCA `stroke="#hex"`.
  Variáveis disponíveis: `var(--c-purple)` · `var(--c-teal)` ·
  `var(--c-amber)` · `var(--c-coral)` · `var(--c-gray)` ·
  `var(--c-green)`
  Isso garante que `context-stroke` no marker herde a cor
  correta da linha e a seta apareça na cor esperada.
- Único hardcode literal permitido: `stroke="context-stroke"`
  dentro do `<path>` do marker em `<defs>` — é uma palavra-chave
  SVG, não uma cor.
- Dark mode automático garantido apenas via classes e variáveis CSS
- Incluir `<defs>` com marker de seta em cada SVG:
  ```
  <defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
  markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
  stroke-width="1.5" stroke-linecap="round"
  stroke-linejoin="round"/></marker></defs>
  ```
  ⚠️ OBRIGATÓRIO em todos os SVGs, mesmo nos que não usam setas.

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
  1 linha → h = 44px · 2 linhas → h = 58px · 3 linhas → h = 72px
  Usar `dominant-baseline="central"` em todos os `<text>`.
  Linha 1: y = topo + 20px · Linha 2: y = topo + 38px · Linha 3: y = topo + 56px

Regra 4 — viewBox height:
  Calcular y_máximo = borda inferior do elemento mais baixo.
  Definir H = y_máximo + 40.
  Nunca fixar H sem verificar o elemento mais baixo.

**Por perfil do capítulo:**

**leitura-interpretação → DIAGRAMA: mapa_texto_[titulo]**
Mapa radial do texto-base principal.
Centro (c-purple): título + autor.
Ramos (c-teal): tema central, recursos expressivos, gênero,
estrutura, relação com o conteúdo do capítulo.
Folhas (c-gray): exemplos ou dados do texto em ts.

**gramatical → DIAGRAMA: esquema_[topico]**
Hierarquia ou árvore do tópico gramatical.
Nó raiz (c-purple): nome do tópico.
Nós secundários (c-teal): classificações ou subtipos.
Nós terminais (c-gray): exemplos do material em ts.
Pegadinhas em c-coral ao lado do nó relevante.

**gramatical → DIAGRAMA: comparativo_[topico]** [se houver
pares contrastivos — ex: coordenação vs. subordinação]
Duas colunas paralelas com nó raiz (c-purple) em cada.
Características divergentes em c-teal de um lado e c-amber
do outro. Ponto de encontro ou diferença-chave em c-coral.

**produção textual → DIAGRAMA: fluxo_[genero]**
Fluxo linear do processo de escrita.
Etapas sequenciais (c-teal): Planejamento → Rascunho →
Revisão → Reescrita.
Orientações de cada etapa em ts abaixo do nó.
Critérios de avaliação em c-gray ao final.

**reflexão linguística → DIAGRAMA: espectro_[variacao]**
Espectro ou eixo da variação linguística.
Eixo horizontal: norma popular ↔ norma culta (ou
oralidade ↔ escrita, conforme o capítulo).
Exemplos do material posicionados ao longo do eixo em ts.
Contextos de uso em c-gray acima/abaixo.

**misto → gerar os diagramas dos perfis presentes.**
Priorizar o diagrama do tópico com maior peso no capítulo.
Máximo 3 diagramas por prep.

---

## EXECUÇÃO

1. Leia `por-[u]-[c].md` e `por-[u]-[c]-questoes.md` inteiros
2. Verifique se imagem da página Síntese foi anexada:
   - ✅ Sim: gere todas as seções incluindo a 10
   - ⬜ Não: gere seções 0–9, 11, 12; registre ausência na Seção 10
3. Gere Seções 1–11 (conteúdo textual)
4. Gere Seção 12 (SVGs embutidos no prep)
5. Gere Seção 0 (índice) e posicione no início do arquivo
6. Salve em `/mnt/user-data/outputs/por-[u]-[c]-prep.md`
7. Apresente com `present_files`
8. Gere o Mapa Mental HTML (ver seção abaixo)
9. Salve em `/mnt/user-data/outputs/mindmap_por[u][c].html`
10. Apresente com `present_files`
11. Informe:
    "✅ Preparação concluída!
    - `por-[u]-[c]-prep.md` → adicionar ao knowledge base
    - `mindmap_por[u][c].html` → adicionar ao knowledge base"

---

## GERAÇÃO DO MAPA MENTAL HTML

Arquivo HTML com mapa mental completo do capítulo.
Todos os cards iniciam em roxo "Não testado".

**a) HEADER** — fundo #800020 (vinho):
- "Português · Unidade X · Capítulo Y · 9º ano"
- Título do capítulo (32px bold)
- "Mapa Mental — gerado na preparação"
- Legenda: verde=Dominado · vermelho=Reforçar · roxo=Não testado

**b) PÍLULA CENTRAL** — tema, fundo #800020

**c) GRID DE CARDS** — um por tópico principal, todos roxo:
- Faixa lateral 3px · número em círculo · título em negrito
- Bullets com conteúdo · badge "Não testado"
- Para regras gramaticais: regra em destaque + exemplos
- Para gêneros textuais: características estruturais
- Para texto-base: autor, gênero, tema, recurso expressivo principal

**d) DICAS DE OURO** — fundo #FFF0F0, borda #800020,
dicas da Seção 7, badge roxo numerado

**CSS obrigatório:**
- Fonte: 'Inter' (Google Fonts) · Fundo: #F4F2EE
- Cards: bg #ffffff · border-radius 14px ·
  box-shadow 0 2px 8px rgba(0,0,0,0.07)
- Grid: 3 colunas · font-size mínimo 13px · header 32px bold
- Cor de destaque: #800020 (vinho)
- Badge "Não testado": fundo #800020, texto branco
- Badge "Dominado": fundo #2e7d32, texto branco
- Badge "Reforçar": fundo #c62828, texto branco
- Cards clicáveis: alternam badge entre os três estados
