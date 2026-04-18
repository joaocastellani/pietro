# PROMPT DE PREPARAÇÃO — MATEMÁTICA (9º ano)

Arquivo de entrada: `mat-[u]-[c].md`
Arquivo gerado:      `mat-[u]-[c]-prep.md`
Mapa mental gerado:  `mindmap_mat[u][c].html`

---

## INSTRUÇÕES GERAIS

1. Use `project_knowledge_search` para localizar e ler
   `mat-[u]-[c].md` inteiro antes de gerar qualquer conteúdo
2. Todo o conteúdo é gerado de uma vez, sem interação com o aluno
3. Preserve expressões matemáticas, fórmulas e notações exatamente
4. Você pode inferir dicas e pegadinhas — não precisa citar o livro
5. Se detectar inconsistência factual, registre na Seção 8
6. Os SVGs da Seção 12 ficam embutidos no próprio `prep.md` —
   não gerar arquivos externos de imagem

---

## ESTRUTURA DO ARQUIVO DE PREPARAÇÃO

Gere nesta ordem. Seções [CONDICIONAL] só se o conteúdo existir.

---

### SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

**Gerada por último**, após a Seção 12 estar completa.

```
## DIAGRAMAS DISPONÍVEIS — mat-[u]-[c]

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
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade:
- Capítulo:
- Tema:
- Perfil: [álgebra | geometria | misto]
- Fórmulas principais: [lista ou "nenhuma"]
- Matemáticos citados: [lista ou "nenhum"]
```

---

### SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

Resumo narrativo organizado por blocos temáticos.
Cada bloco: título em negrito + explicação nível 9º ano +
conexão com situações reais quando possível.

**Perfil álgebra:** apresente cada conceito com sua notação
simbólica e pelo menos um exemplo numérico concreto do material.

**Perfil geometria:** apresente cada figura ou relação com
descrição das propriedades e elementos relevantes (lados,
ângulos, diagonais, razões). Para figuras com medidas: indique
as relações entre os elementos.

**Perfil misto:** organize em dois blocos separados — primeiro
algébrico/aritmético, depois geométrico.

Para blocos com fórmulas: apresente a expressão, declare as
variáveis e dê um exemplo resolvido do Bloco E do `.md`.

---

### SEÇÃO 3 — MATEMÁTICOS E HISTÓRIA DA MATEMÁTICA [CONDICIONAL]

Gerar se o capítulo citar matemáticos com papel histórico.

Para cada matemático:
```
### [Nome completo] ([período de vida])
**Área:** [campo da matemática]
**Contribuição no capítulo:** [o que o livro descreve]
**O que desenvolveu:** [teorema, área ou conceito associado]
**Contexto histórico:** [época, civilização ou movimento]
```

---

### SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS [CONDICIONAL]

Gerar se o capítulo apresentar expressões matemáticas ou
propriedades operacionais.

Para cada fórmula ou propriedade:
```
### [Nome da fórmula ou propriedade]

**Expressão:** [fórmula exata com notação do livro]

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| [s] | [nome] | [unidade ou tipo — escalar/vetor/inteiro/real] |

**Válida quando:** [condições — se mencionadas]
**Caso especial:** [exceção ou limite — se houver]
💡 **Pegadinha:** [erro mais comum com esta fórmula/propriedade]
```

---

### SEÇÃO 5 — REPRESENTAÇÕES E SISTEMAS [CONDICIONAL]

Gerar se o capítulo abordar representações gráficas, conjuntos,
reta numérica, plano cartesiano ou sistemas de classificação
numérica.

Para cada sistema ou representação:
- Nome e definição
- Elementos que compõem a representação
- Regras de construção ou leitura
- Exemplos do material (preserve notações e valores)
- Relações entre elementos (inclusão, interseção, complemento)

---

### SEÇÃO 6 — TABELAS DE REFERÊNCIA [CONDICIONAL]

Gerar se o capítulo apresentar dados tabulares relevantes —
ex: tabelas de conjuntos, classificações, propriedades
comparadas, valores de referência.

Apresentar como tabela markdown fiel ao material.
NÃO reconstituir a partir de texto corrido.

---

### SEÇÃO 7 — DICAS DE OURO

Liste 4–6 dicas inferidas a partir do conteúdo do capítulo.
Foco em: pegadinhas de prova, distinções sutis entre conceitos,
erros comuns em cálculo, macetes de memorização.

**Perfil álgebra:** priorize pegadinhas de notação, sinais,
ordem de operações e confusões entre conjuntos ou propriedades.

**Perfil geometria:** priorize confusões entre fórmulas de
figuras semelhantes, condições de validade e erros de unidade.

Formato:
```
💡 **Dica [N] — [título curto]**
[explicação com exemplo numérico quando útil]
```

---

### SEÇÃO 8 — ALERTAS E LACUNAS [CONDICIONAL]

#### Bloco A — Lacunas de dados

Gerar se houver campos ausentes no arquivo de captura.

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| [seção] | [campo] | [motivo] | [ação concreta] |

#### Bloco B — Inconsistências factuais

Gerar se detectar erros matemáticos no material capturado.
Em Matemática: verificar fórmulas incorretas, propriedades
com condições faltando, exemplos com resultado errado,
notações inconsistentes.

```
⚠️ ALERTA — [conceito ou fórmula]
- Dado no material: "[texto exato do arquivo .md]"
- Problema: [descrição do erro]
- Dado correto: [informação correta]
- Impacto na aula: [o que o Professor deve fazer]
```

---

### SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

```
- **[Conceito]**
  - Definição: `______` ([resposta esperada])
  - Notação: `______` ([símbolo ou expressão])
```

#### Bloco 2 — Fórmulas e Propriedades [se houver]

```
- **[Nome da fórmula/propriedade]**
  - Expressão: `______` ([fórmula exata])
  - Variável [símbolo]: `______` ([significado])
  - Condição: `______` ([condição de validade])
```

#### Bloco 3 — Lacunas para Warm-Up

6–8 lacunas cobrindo obrigatoriamente:
- Pelo menos 1 por conceito principal do resumo (Seção 2)
- Pelo menos 1 por fórmula ou propriedade (Seção 4)
- Pelo menos 1 por matemático citado (Seção 3, se houver)
- Pelo menos 1 de aplicação contextual (situação real do Bloco F
  ou G do material de captura)
- Pelo menos 1 de representação ou notação simbólica

REGRA CRÍTICA: gere lacuna APENAS para dados explicitamente
presentes no material capturado. Nunca crie lacuna cuja resposta
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
- SEÇÃO ATIVIDADES do `mat-[u]-[c].md` → Questões de Atividades (Origem: AT)
- BLOCO E (QI-N) do `mat-[u]-[c].md` → Questões Intercaladas (Origem: IC)

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| Q-N | [1 linha] | [MC/Cal/Dis/VF/Assoc/Const] | [F/M/D] | [IC/AT] | [resposta + resolução resumida] | [— ou ⚠️] |

Legenda: MC = múltipla escolha · Cal = cálculo · Dis = dissertativa
VF = V-F · Assoc = associação · Const = construção

Regras:
- Infira gabaritos usando o conteúdo do `.md` e das fórmulas
- Para questões de cálculo: apresente o desenvolvimento resumido
- Para QC: indique banca e ano na coluna Obs.
- Marque ⚠️ para: figura não capturada, alternativas vazias
  (ex: QC com imagem ilegível), enunciado ambíguo, erro
  já registrado na Seção 8

#### Bloco B — Questões modelo originais

5 questões originais inspiradas no estilo da SEÇÃO ATIVIDADES.
NÃO copiar nem parafrasear — criar contextos e valores novos.

Distribuição:
- 2 múltipla escolha (médio)
- 1 cálculo (médio)
- 1 estilo concurso (difícil)
- 1 dissertativa ou construção (médio-difícil)

```
**QM-[N]** · [tipo] · [dificuldade] · inspirada em: [Q-N]

[enunciado completo]

a) [alt]  b) [alt]  c) [alt]  d) [alt]

✅ Gabarito: [letra ou resposta]
📝 Resolução: [desenvolvimento passo a passo]
⚠️ Professor: referência de estilo — crie variações originais.
```

---

### SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

Os SVGs ficam embutidos no próprio prep.md.

**Formato de cada diagrama:**
```
### DIAGRAMA: [nome]
[descrição em 1 linha]
<svg width="100%" viewBox="0 0 680 H">...</svg>
```

**Regras obrigatórias:** width="100%", viewBox="0 0 680 H",
classes c-purple/c-teal/c-amber/c-coral/c-gray/c-green,
text classes t/ts/th, sem gradientes, sem emojis,
dark mode automático. `<defs>` com marker de seta OBRIGATÓRIO
em todos os SVGs, mesmo nos que não usam setas:

```
<defs>
  <style>...</style>
  <marker id="arr" markerWidth="8" markerHeight="8"
    refX="6" refY="3" orient="auto">
    <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
  </marker>
</defs>
```

**Regras anti-sobreposição — verificar ANTES de posicionar:**

Regra 1 — Packing: `soma(larguras) + (n-1)×8 ≤ espaço_disponível`
  Calcule explicitamente. Espaço = x_final − x_inicial.

Regra 2 — Texto: `caracteres × 7 + 24 ≤ largura_caixa`
  Se não couber: 2 linhas com palavras inteiras. Nunca cortar palavra.

Regra 3 — Altura mínima:
  1 linha → h=44px · 2 linhas → h=58px · 3 linhas → h=72px
  dominant-baseline="central" em todos os <text>.
  Linha 1: y=topo+20 · Linha 2: y=topo+38 · Linha 3: y=topo+56

Regra 4 — viewBox height:
  H = y_máximo_do_elemento_mais_baixo + 40. Nunca fixar sem verificar.

**Por perfil do capítulo:**

**Álgebra → DIAGRAMA: conjuntos** [se houver conjuntos numéricos]
Diagrama de Venn ou hierarquia de inclusão.
Nós = conjuntos (c-purple para R, c-teal para Q, c-amber para Z,
c-green para N, c-coral para I).
Setas de inclusão com rótulo ⊂. Exemplos de números em ts fora.

**Álgebra → DIAGRAMA: formulas** [se houver fórmulas]
Uma linha por fórmula: nó nome (c-purple) → nó expressão (c-teal)
→ texto ts de variáveis. Pegadinha em c-coral abaixo.

**Álgebra → DIAGRAMA: reta_numerica** [se houver reta numérica]
Linha horizontal com seta. Inteiros em c-gray. Irracionais em
c-coral com valor aproximado em ts. π indicado com rótulo.

**Geometria → DIAGRAMA: hierarquia_[tema]**
Hierarquia de figuras ou classificações geométricas.
Nó raiz (c-purple) → tipos (c-teal) → propriedades (c-gray).

**Geometria → DIAGRAMA: semelhanca** [se houver semelhança]
Dois polígonos lado a lado com razão k indicada.
Setas duplas com rótulo k entre lados correspondentes.

**Misto → gerar os diagramas de todos os perfis presentes.**

---

## EXECUÇÃO

1. Leia `mat-[u]-[c].md` inteiro
2. Verifique se imagem da Síntese foi anexada:
   - ✅ Sim: gere todas as seções incluindo a 10
   - ⬜ Não: gere seções 0–9, 11, 12; indique que Seção 10
     pode ser adicionada depois com a imagem
3. Gere Seções 1–11 (conteúdo textual)
4. Antes de gerar a Seção 12, varra todas as imagens anexadas:
   identifique diagramas visuais (esquemas, fluxos, tabelas
   estruturais, mapas, gráficos) e decida para cada um:
   SVG embutido na Seção 12 · markdown na Seção 6 · ou registrar
   na Seção 8 como ausente (para image_search na aula).
   Depois gere a Seção 12 com todos os SVGs identificados.
5. Gere Seção 0 (índice) e posicione no início do arquivo
6. Salve em `/mnt/user-data/outputs/mat-[u]-[c]-prep.md`
7. Apresente com `present_files`
8. Gere o Mapa Mental inline (ver seção abaixo)
9. Salve em `/mnt/user-data/outputs/mindmap_mat[u][c].html`
   (cópia de referência — não precisa ir para o KB)
10. Apresente com `present_files`
11. Informe:
    "✅ Preparação concluída!
    - `mat-[u]-[c]-prep.md` → adicionar ao knowledge base
    - `mindmap_mat[u][c].html` → referência visual (não vai para o KB)"

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
- `[COR_PRIMARIA]` → `#1a4fa0`
- `[TEMA DO CAPÍTULO]` → título da Seção 1 do prep
- `[Matéria]` → `Matemática`
- Um `.branch` por tópico da Seção 2
- Leaves com bullets, fórmulas (tag `.fm`) e alertas (tag `.warn`)
- Dicas de ouro da Seção 7

### Entrega
Chamar `show_widget` com:
- `title`: `"mindmap_mat[u][c]"`
- `loading_messages`: `["Montando o mapa do capítulo..."]`
- `widget_code`: HTML preenchido

Após renderizar, salvar também uma cópia em
`/mnt/user-data/outputs/mindmap_mat[u][c].html`
e apresentar com `present_files` como referência.
