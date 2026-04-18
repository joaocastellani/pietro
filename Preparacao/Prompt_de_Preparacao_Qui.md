# PROMPT DE PREPARAÇÃO — QUÍMICA (9º ano)

Arquivo de entrada: `qui-[u]-[c].md`
Arquivo gerado:      `qui-[u]-[c]-prep.md`
Mapa mental gerado:  `mindmap_qui[u][c].html`

---

## INSTRUÇÕES GERAIS

1. Use `project_knowledge_search` para localizar e ler
   `qui-[u]-[c].md` inteiro
   antes de gerar qualquer conteúdo
2. Todo o conteúdo é gerado de uma vez, sem interação com o aluno
3. Preserve equações químicas, símbolos e unidades exatamente
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
## DIAGRAMAS DISPONÍVEIS — qui-[u]-[c]

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
# PREPARAÇÃO DE AULA — QUÍMICA
- Unidade:
- Capítulo:
- Tema:
- Perfil: [histórico-conceitual / matemático-operacional /
           descritivo-científico / misto]
- Equações/fórmulas principais: [lista ou "nenhuma"]
- Cientistas citados: [lista ou "nenhum"]
```

---

### SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

Resumo narrativo organizado por blocos temáticos.
Cada bloco: título em negrito + explicação nível 9º ano +
conexão com cotidiano quando possível.

Para blocos com equações químicas: apresente a equação formatada
e explique em linguagem acessível o que reagentes e produtos
representam no mundo real.

---

### SEÇÃO 3 — CIENTISTAS E HISTÓRIA DA CIÊNCIA [CONDICIONAL]

Gerar se o capítulo citar cientistas com papel relevante.

Para cada cientista:
```
### [Nome completo] ([período de vida])
**Área:** [campo]
**Contribuição no capítulo:** [o que o livro descreve]
**O que mudou:** [impacto no pensamento científico ou na Química]
**Associado a:** [modelo, lei, elemento, experimento — se citado]
**Contexto histórico:** [época, movimento científico]
```

---

### SEÇÃO 4 — EQUAÇÕES QUÍMICAS, FÓRMULAS E LEIS [CONDICIONAL]

Gerar se o capítulo apresentar equações químicas ou expressões
matemáticas.

#### 4A — Equações Químicas

Para cada equação:
```
### [Nome ou tipo da reação]

**Equação balanceada:** [equação com coeficientes, fórmulas e
estados físicos]

**Condições de reação:** [temperatura, pressão, catalisador, luz
— exatamente como aparecem no material, ou "não especificadas"]

**Reagentes:** [nome e fórmula de cada reagente]
**Produtos:** [nome e fórmula de cada produto]
**Tipo de reação:** [síntese / decomposição / simples troca /
dupla troca / combustão — se classificado no material]

💡 **Pegadinha:** [erro mais comum com esta equação — ex:
esquecer de balancear, confundir reagente com produto,
ignorar o estado físico]
```

#### 4B — Fórmulas Matemáticas de Química

Para cada fórmula:
```
### [Nome da grandeza ou lei]

**Expressão:** [fórmula exata]

| Símbolo | Grandeza | Unidade | Natureza |
|---------|----------|---------|---------|
| [s] | [nome] | [unidade] | [extensiva/intensiva/adimensional/contável] |

**Válida quando:** [condições]
**Caso especial:** [exceção ou limite — se houver]
💡 **Pegadinha:** [erro mais comum com esta fórmula — ex:
usar massa em gramas onde se espera mol, inverter numerador
e denominador, esquecer de converter unidades]
```

---

### SEÇÃO 5 — GRANDEZAS E RELAÇÕES CARACTERÍSTICAS [CONDICIONAL]

Gerar se o capítulo abordar grandezas mensuráveis, conversões,
notação científica ou constantes e relações numéricas de Química.

#### 5.1 — Grandezas do capítulo

| Grandeza | Símbolo | Unidade | Símbolo | Natureza |
|----------|---------|---------|---------|---------|

#### 5.2 — Conversões importantes

```
[grandeza]: [unidade A] → [unidade B]
Fator: [regra]
Exemplo: [número do capítulo ou das questões]
⚠️ Pegadinha: [erro clássico de conversão]
```

#### 5.3 — Notação científica [se presente]

- Regra: a × 10ⁿ, onde 1 ≤ |a| < 10 e n é inteiro
- Exemplos do capítulo: [preserve os números do material]
- Erro clássico: [confundir deslocamento da vírgula com sinal de n]

#### 5.4 — Relações e constantes características

Para cada constante ou relação numérica presente:
```
[Nome]: [valor + unidade]
Uso: [como o material instrui aplicar em cálculos]
Exemplo do capítulo: [número exato do material]
⚠️ Pegadinha: [erro mais comum ao usar esta relação]
```

---

### SEÇÃO 6 — DADOS FACTUAIS DENSOS [CONDICIONAL]

Gerar se o capítulo apresentar conjuntos de dados estruturados.
Usar **tabelas markdown** — não SVG para dados tabulares.
Adicionar coluna "⚠️ Pegadinha" quando relevante.

Tipos de tabela esperados em Química do 9º ano:
- Elementos da tabela periódica (símbolo, número atômico,
  massa atômica, propriedades)
- Substâncias e suas propriedades (nome, fórmula, estado físico,
  ponto de fusão/ebulição, solubilidade)
- Classificação de misturas ou soluções
- Tipos de reação com exemplos
- Comparação de modelos atômicos

---

### SEÇÃO 7 — DICAS DE OURO

4–6 dicas inferidas do conteúdo. Foco em: pegadinhas de prova,
distinções sutis, erros comuns, macetes de memorização.

Temas prioritários para Química:
- Confusão entre mistura e substância pura
- Confusão entre transformação física e química
- Erros de balanceamento de equações
- Confusão entre mol e massa
- Nomenclatura incorreta de substâncias
- Inversão de reagente e produto

```
💡 **Dica [N] — [título curto]**
[explicação com equação ou exemplo quando útil]
```

---

### SEÇÃO 8 — ALERTAS DE INCONSISTÊNCIA [CONDICIONAL]
**ARQUIVO DE GAPS — gerar quando houver inferências ou ausências:**

Formato do arquivo `[mat]-[u]-[c]-gaps.md`:

```markdown
# GAPS — [mat]-[u]-[c]
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



Gerar se detectar erros factuais no material capturado,
E também quando dados relevantes estiverem ausentes do material
capturado mas forem necessários para o entendimento do aluno.

Para dados ausentes usar formato:
⚠️ DADO AUSENTE — [termo ou tabela]
- Campo: [qual informação está incompleta]
- Motivo: [não capturado / imagem não processada]
- Ação: adicionar ao arquivo [mat]-[u]-[c].md e reprocessar
  o prep antes de disponibilizar ao aluno
Em Química: verificar especialmente equações não balanceadas,
fórmulas incorretas, classificações erradas de reações e
valores de constantes desatualizados.

```
⚠️ ALERTA — [termo, equação ou conceito]
- Dado no material: "[texto exato do arquivo .md]"
- Problema: [descrição do erro]
- Dado correto: [informação correta]
- Impacto na aula: [o que o Professor deve fazer]
```

---

### SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

```
- **[Nome do conceito]**
  - Definição: `______` ([resposta esperada])
  - Exemplo: `______` ([exemplo do material])
```

#### Bloco 2 — Equações e Fórmulas [se houver]

```
- **[Nome da reação ou grandeza]**
  - Equação/Expressão: `______` ([resposta esperada])
  - [símbolo ou reagente] representa: `______` ([nome + unidade
    ou papel na reação])
```

#### Bloco 3 — Lacunas para Warm-Up

6–8 lacunas cobrindo obrigatoriamente:
- Pelo menos 1 por conceito principal do resumo (Seção 2)
- Pelo menos 1 por **categoria/tipo** que aparece como coluna
  ou classificação nas tabelas da Seção 6 — não só exemplos,
  mas a definição da categoria em si
  (ex: se a tabela tem coluna "Tipo de reação" com valores
  "Síntese" e "Decomposição", gerar lacuna para a definição
  de cada um)
- Pelo menos 1 por equação ou fórmula (se houver)
- Pelo menos 1 baseada na Síntese do livro (se imagem fornecida)
- Pelo menos 1 de aplicação contextual (substância do cotidiano,
  reação conhecida)

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
- SEÇÃO ATIVIDADES do `qui-[u]-[c].md` → Questões de Atividades (Origem: AT)
- BLOCO G (QI-N) do `qui-[u]-[c].md` → Questões Intercaladas (Origem: IC)

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| Q-N | [1 linha] | [MC/Dis/Calc/Bal/VF/Assoc] | [F/M/D] | [resposta + justificativa] | [— ou ⚠️] |

Legenda de tipos: MC = múltipla escolha · Dis = dissertativa ·
Calc = cálculo · Bal = equação e balanceamento · VF = V-F ·
Assoc = associação

Regras:
- Infira gabaritos usando o conteúdo do `.md`
- Para somatórios V-F: avalie cada item e calcule a soma
- Para cálculos: resolva e registre o desenvolvimento resumido
- Para balanceamento: apresente a equação balanceada
- Marque ⚠️ para: enunciado incompleto, equação não balanceada
  no material, alternativas corrompidas, ambiguidade factual,
  erro já registrado na Seção 8

#### Bloco B — Questões modelo originais

5 questões originais inspiradas no estilo da SEÇÃO ATIVIDADES.
NÃO copiar nem parafrasear — criar contextos novos.

Distribuição:
- 2 múltipla escolha (médio)
- 1 dissertativa (médio)
- 1 múltipla escolha estilo concurso (difícil)
- 1 cálculo ou equação e balanceamento (médio-difícil) — ou
  dissertativa difícil se o capítulo não tiver fórmulas nem
  equações

```
**QM-[N]** · [tipo] · [dificuldade] · inspirada em: [Q-N]

[enunciado completo]

a) [alt]  b) [alt]  c) [alt]  d) [alt]

✅ Gabarito: [letra ou resposta]
📝 Resolução: [desenvolvimento ou justificativa]
⚠️ Professor: referência de estilo — crie variações originais,
   nunca reproduza diretamente.
```

---

### SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

Os SVGs ficam **embutidos no próprio prep.md** como blocos de código.
O Professor lê o SVG da Seção 12 e passa ao Visualizer para
renderizar inline — sem arquivos externos, sem dependência de KB.

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
  `c-coral`, `c-gray`
- Classes de texto: `class="t"` (14px), `class="ts"` (12px),
  `class="th"` (14px bold)
- Alertas/pegadinhas: `c-coral` ou `c-red`
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


**Por perfil do capítulo:**

**Histórico-conceitual → DIAGRAMA: timeline**
Linha do tempo dos cientistas ou modelos atômicos.
Eixo horizontal = tempo. Nós alternados acima/abaixo com box
colorido (nome + período) e contribuição em texto ts fora do box.
Cores: c-purple (antigos) · c-teal (transição) ·
       c-amber (modernos) · c-coral (comunicadores/divulgadores)

**Histórico-conceitual → DIAGRAMA: modelos_atomicos** [se houver
evolução de modelos atômicos no capítulo]
Sequência horizontal: cada modelo em um nó colorido com nome do
cientista (c-purple) e características do modelo em ts abaixo.
Setas de progressão entre os nós. Limitações de cada modelo em
c-coral abaixo da característica correspondente.

**Matemático-operacional → DIAGRAMA: formulas**
Uma linha por fórmula: nó nome (c-purple) → nó expressão (c-teal)
→ texto ts de variáveis + unidades.
Pegadinha em c-coral abaixo de cada fórmula.

**Matemático-operacional → DIAGRAMA: conversoes** [se houver]
Nós = unidades (c-gray) · setas com fator de conversão em ts ·
exemplo numérico do capítulo.

**Descritivo-científico → DIAGRAMA: transformacao_[tema]**
Fluxo de transformação química ou classificação hierárquica.
Exemplos: reagentes → produtos com condições de reação ·
          matéria → mistura/substância pura → ramos de classificação.
Use nós c-teal para substâncias/reagentes, c-amber para produtos,
c-coral para condições de reação e observações de cuidado.
NÃO usar SVG para tabelas densas de dados — usar markdown na Seção 6.

**Descritivo-científico → DIAGRAMA: blocos_tabela_real**
[gerar se o capítulo tratar de blocos s, p, d, f da tabela periódica]
Tabela periódica real com os quatro blocos coloridos nas posições corretas.
Usar formato HTML+SVG (show_widget) — ver template em qui-1-3-prep.md Seção 12.
Legenda obrigatória abaixo do SVG identificando cada bloco e os grupos.

**Descritivo-científico → DIAGRAMA: grupos_familias**
[gerar se o capítulo tratar de grupos A/B ou famílias de elementos]
Tabela periódica real diferenciando grupos A (representantes), grupos B
(transição) e grupo 8A (gases nobres) por cor. Usar formato HTML+SVG.
Ver template em qui-1-3-prep.md Seção 12.

**Misto → gerar os diagramas de todos os perfis presentes.**

---

## EXECUÇÃO

1. Leia `qui-[u]-[c].md` inteiro
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
6. Salve em `/mnt/user-data/outputs/qui-[u]-[c]-prep.md`
7. Apresente com `present_files`
8. Gere o Mapa Mental inline (ver seção abaixo)
9. Salve em `/mnt/user-data/outputs/mindmap_qui[u][c].html`
   (cópia de referência — não precisa ir para o KB)
10. Apresente com `present_files`
11. Informe:
    "✅ Preparação concluída!
    - `qui-[u]-[c]-prep.md` → adicionar ao knowledge base
    - `mindmap_qui[u][c].html` → referência visual (não vai para o KB)"

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
- `[COR_PRIMARIA]` → `#006080`
- `[TEMA DO CAPÍTULO]` → título da Seção 1 do prep
- `[Matéria]` → `Química`
- Um `.branch` por tópico da Seção 2
- Leaves com bullets, fórmulas (tag `.fm`) e alertas (tag `.warn`)
- Dicas de ouro da Seção 7

### Entrega
Chamar `show_widget` com:
- `title`: `"mindmap_qui[u][c]"`
- `loading_messages`: `["Montando o mapa do capítulo..."]`
- `widget_code`: HTML preenchido

Após renderizar, salvar também uma cópia em
`/mnt/user-data/outputs/mindmap_qui[u][c].html`
e apresentar com `present_files` como referência.
