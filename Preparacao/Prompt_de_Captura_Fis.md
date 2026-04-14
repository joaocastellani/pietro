# PROMPT DE CAPTURA — FÍSICA (9º ano)

Arquivo gerado: `fis-[unidade]-[capitulo].md`
Exemplo: `fis-1-2.md`

---

## CONTEXTO

O livro de Física do 9º ano não possui uma estrutura fixa de seções —
cada capítulo pode ser histórico-conceitual, matemático-operacional,
descritivo-científico ou uma combinação desses perfis.

Por isso, este prompt opera em dois níveis:
- **Nível 1 — Captura universal:** sempre executada, independente do capítulo
- **Nível 2 — Captura condicional:** executada apenas para os tipos de
  conteúdo que existem no capítulo analisado

---

## PROMPT

```
Tarefa: Extraia todo o conteúdo desta página de Física e gere um
markdown estruturado seguindo as instruções abaixo.

REGRAS GERAIS:
- Preserve todos os dados exatamente como aparecem no material
- Não resuma, não interprete, não omita dados numéricos
- Para fórmulas: capture todas as variáveis e unidades presentes
- Para questões: capture enunciado completo, alternativas e gabarito
- ATENÇÃO: Retorne APENAS o markdown estruturado conforme as seções
  abaixo. Não adicione comentários, sugestões, perguntas ao usuário,
  observações finais nem qualquer texto fora da estrutura solicitada.
  O output termina com o último bloco preenchido — nada mais.
- IMAGENS ANEXADAS: se imagens da apostila forem anexadas junto
  com este prompt, extraia também o conteúdo textual visível
  nelas — legendas, textos sobrepostos, rótulos de esquemas,
  títulos de figuras, dados de tabelas — e incorpore nas seções
  correspondentes. Não ignore imagens.
- BLOCOS DE ATIVIDADES E QUESTÕES: a seção Atividades (bloco final
  numerado) vai na SEÇÃO ATIVIDADES ao final deste arquivo.
  EXCEÇÃO: questões intercaladas no corpo do capítulo (antes das
  Atividades) devem ser capturadas no BLOCO G deste arquivo com
  prefixo QI-N e tag [IC].
- SEÇÃO FINAL OPCIONAL — IMAGENS RECOMENDADAS PARA CAPTURA:
  Se identificar figuras, esquemas ou tabelas cujo conteúdo não
  foi possível extrair por texto, adicione ao final do arquivo:
  ## IMAGENS RECOMENDADAS PARA CAPTURA
  - [descrição] · [conteúdo esperado] · [por que é necessária]

---

## NÍVEL 1 — CAPTURA UNIVERSAL (execute sempre)

### 1. METADADOS
- Matéria: Física
- Unidade:
- Capítulo/Tema:
- Nível de ensino: 9º ano
- Perfil do capítulo: [histórico-conceitual / matemático-operacional /
  descritivo-científico / misto — identifique com base no conteúdo]

### 2. CONCEITOS E DEFINIÇÕES
Para cada conceito presente no capítulo:
- Nome do conceito em destaque
- Definição completa conforme o material
- Exemplos dados pelo livro (preserve números e unidades)
- Observações ou ressalvas explícitas no texto

### 3. FLASHCARDS DO CAPÍTULO
Gere flashcards para revisão rápida cobrindo os conceitos,
definições, fórmulas, cientistas e dados factuais do capítulo.

Regras:
- Mínimo de 10 flashcards
- Cobertura obrigatória por bloco — gere ao menos 1 card por:
  · Cada conceito principal da Seção 2
  · Cada cientista do Bloco A
  · Cada fórmula ou lei do Bloco B
  · Cada grandeza principal do Bloco C
  A cobertura obrigatória tem precedência absoluta — satisfaça
  todos os itens acima antes de aplicar qualquer limite.
  Só após cobrir todos os itens obrigatórios aplica-se o teto
  de 20: se ainda houver itens relevantes além dos obrigatórios,
  selecione os mais importantes até o máximo de 20.
- Priorize os tópicos mais cobrados nas questões do capítulo
- Alterne os sentidos: algumas frente→verso são termo→definição,
  outras são definição→termo, outras são fórmula→variáveis
- Para fórmulas: frente = expressão, verso = nome + variáveis + unidades
- Para cientistas: frente = nome, verso = contribuição principal
- Para dados factuais: frente = pergunta direta, verso = dado preciso
- NÃO crie flashcard de questão de exercício

Formato de cada flashcard (use exatamente este padrão, uma linha em branco entre cards):

**FC-[N]**
🔵 Frente: [texto da frente]
🟢 Verso: [texto do verso]

---

## NÍVEL 2 — CAPTURA CONDICIONAL

REGRA DE OMISSÃO — OBRIGATÓRIA:
Se um bloco não tiver dados reais para preencher, NÃO o inclua
no output. Não escreva "Não especificado", "Não aplicável" nem
nenhuma variação. O bloco simplesmente não aparece no arquivo.
Um bloco só existe no output se tiver pelo menos um item concreto
extraído do material.

---

### BLOCO A — CIENTISTAS CITADOS NO MATERIAL
[Execute se o capítulo citar cientistas, matemáticos, físicos
ou exploradores científicos. NÃO inclua artistas, músicos ou
escritores citados apenas como recurso cultural.]

PROIBIDO incluir no Bloco A:
- Fotógrafos ou créditos de acervo citados em legendas de imagem
- Autores de obras bibliográficas citadas apenas como fonte
- Qualquer nome que apareça exclusivamente como crédito de imagem
  sem papel no conteúdo físico do capítulo

Para cada cientista citado, capture APENAS o que está explícito
no material — não infira, não complemente com conhecimento externo:
- Nome completo
- Contribuição descrita no texto (palavras do material)
- Instrumento, obra ou experimento associado (se citado no material)

---

### BLOCO B — FÓRMULAS, LEIS E PRINCÍPIOS
[Execute se o capítulo apresentar expressões matemáticas ou leis físicas]

Para cada fórmula ou lei:
- Nome da lei ou grandeza
- Expressão matemática exata (preserve símbolos e expoentes)
- Cada variável identificada: símbolo + nome + unidade SI
- Constantes envolvidas: símbolo + valor + unidade (se citadas)
- Enunciado completo da lei (se presente no material)
- Condições de validade ou aplicabilidade (se mencionadas)
- Casos especiais ou exceções explicitados no texto

---

### BLOCO C — GRANDEZAS, UNIDADES E SISTEMA INTERNACIONAL
[Execute se o capítulo abordar o SI, conversões ou notação científica]

#### C1 — Grandezas fundamentais e derivadas
Para cada grandeza citada:
- Nome da grandeza
- Símbolo
- Unidade SI + símbolo da unidade
- Tipo: [fundamental / derivada / adimensional / vetorial / escalar]
- Grandezas fundamentais das quais deriva (se derivada)

#### C2 — Conversões de unidades
Para cada conversão presente:
- Grandeza convertida
- Fator de conversão exato conforme o material
- Exemplo de aplicação (preserve os números do livro)

#### C3 — Notação científica e ordens de grandeza
- Regra da notação científica conforme o material (a × 10ⁿ)
- Exemplos resolvidos presentes no texto (preserve os números)
- Regra de ordem de grandeza (se descrita)

---

### BLOCO D — DADOS FACTUAIS DENSOS
[Execute se o capítulo apresentar tabelas comparativas, planetas,
elementos, instrumentos, organismos ou conjuntos de dados estruturados]

CHECAGEM OBRIGATÓRIA — responda internamente antes de executar:
"Existe uma tabela com linhas e colunas visíveis no material,
que eu possa copiar célula a célula sem inferir nenhum valor?"
→ Não → omita o bloco inteiro, sem exceção
→ Sim → copie célula a célula, sem adicionar nada

PROIBIDO reconstituir tabela a partir de:
- Texto corrido ou parágrafos expositivos
- Gráficos ou esquemas visuais sem células explícitas
- Legendas de figuras ou imagens
- Alternativas ou enunciados de questões

Organize em tabela fiel ao material:
- Preserve todos os atributos e valores presentes
- Use o mesmo critério de comparação do livro
- Não omita nenhum item da lista ou tabela original
- Se houver dados numéricos (distâncias, temperaturas, massas):
  preserve valores e unidades exatamente como aparecem

---

### BLOCO E — EXPERIMENTOS E DEMONSTRAÇÕES
[Execute se o capítulo descrever experimentos, demonstrações
ou procedimentos investigativos]

Para cada experimento:
- Nome ou título (se houver)
- Objetivo
- Materiais citados
- Procedimento (em sequência ordenada)
- Resultado observado
- Conclusão apresentada pelo material
- Cientista associado (se citado)

---

### BLOCO F — TEXTO COMPLEMENTAR / LEITURA DE CONTEXTUALIZAÇÃO
[Execute se o capítulo incluir texto de leitura, reportagem,
artigo adaptado ou seção de contextualização separada do corpo
expositivo principal.
NÃO capture o conteúdo expositivo normal do capítulo — esse vai
nas Seções 2 e Blocos A–E.
NÃO capture trechos cujo conteúdo já está no corpo expositivo
do capítulo — se a fonte for o próprio livro didático, não é
texto complementar.
NÃO capture afirmativas de questões como fatos — enunciados de
exercícios podem conter afirmações falsas propositalmente.
Se a fonte não estiver citada, omita o campo — nunca preencha
com "Não especificada".]

- Título do texto
- Tema central
- Dados, valores e fatos relevantes mencionados
  (preserve números, datas, nomes e unidades)
- Conceitos físicos presentes ou exemplificados no texto
- Fonte ou origem (se citada no material)

### BLOCO G — QUESTÕES INTERCALADAS
[Se houver questões autônomas inseridas no corpo do capítulo,
antes da seção Atividades. Sinais: número ou caixa destacada
com título "Pratique"/"Resolva"/"Verifique"/"Atividade" dentro
do fluxo expositivo — não no bloco final de Atividades.]

DISTINÇÃO — CRÍTICO:
Questão intercalada = aparece no corpo do capítulo, antes de Atividades.
Seção Atividades (bloco final numerado) → NÃO capturar aqui → vai na SEÇÃO ATIVIDADES abaixo.

Use prefixo QI-N (sequência própria do arquivo) e tag [IC]:

**QI-[N]** · [IC]
Enunciado: [texto completo]
Gabarito: [se fornecido pelo livro]
Conceito testado: [conceito central avaliado]
```

---

## ESTRUTURA DO ARQUIVO FINAL

```markdown
## 1. METADADOS
- Matéria: Física
- Unidade:
- Capítulo/Tema:
- Nível de ensino: 9º ano
- Perfil do capítulo:

## 2. CONCEITOS E DEFINIÇÕES
[conceitos em destaque com definição, exemplos e observações]

## 3. FLASHCARDS DO CAPÍTULO
[FC-1 a FC-N, frente e verso]

---
## BLOCO A — CIENTISTAS CITADOS NO MATERIAL
[se aplicável — apenas dados explícitos do texto]

## BLOCO B — FÓRMULAS, LEIS E PRINCÍPIOS
[se aplicável]

## BLOCO C — GRANDEZAS, UNIDADES E SISTEMA INTERNACIONAL
[se aplicável]

## BLOCO D — DADOS FACTUAIS DENSOS
[se aplicável]

## BLOCO E — EXPERIMENTOS E DEMONSTRAÇÕES
[se aplicável]

## BLOCO F — TEXTO COMPLEMENTAR
[se aplicável]

## BLOCO G — QUESTÕES INTERCALADAS
[se aplicável]
```

---

## SEÇÃO ATIVIDADES
[Capture TODAS as questões da seção Atividades (bloco final numerado).
NÃO capturar questões intercaladas — essas vão no BLOCO G acima.]

NÃO CAPTURAR:
- Perguntas retóricas do texto expositivo
- Questões intercaladas ao conteúdo (→ BLOCO G)
- "Questão invertida" (aluno cria a pergunta)

IDENTIFICAÇÃO DE QUESTÕES DE CONCURSO — CRÍTICO:
Se o número vier com nome de banca capture como QC-N. Extraia banca e ano.

NUMERAÇÃO: sequência própria — NUNCA a do livro. Q-N e QC-N independentes.
ANTI-DUPLICATA: mesma questão com e sem banca → apenas QC-N.
ANTI-PARTIÇÃO: itens a) b) c) = UMA questão. Todos no Enunciado:.

TEXTO vs ENUNCIADO:
> Texto: → APENAS fonte primária. Se ausente: OMITA.
Enunciado: → APENAS a pergunta. Nunca vazio.

MÍDIA — CRÍTICO: blocos SEPARADOS antes do Enunciado:.

> Gráfico: reconstrua SEMPRE: título · Eixo X · Eixo Y · valores ·
  segmentos com comportamento. NUNCA [GRÁFICO].
[IMAGEM] irreconstruível (diagrama de circuito, esquema de forças):
  [IMAGEM] (tipo; contexto; o que mostra; por que necessária)

TIPO — um único valor:
  Tem alternativas?                  → múltipla escolha
  Pede cálculo numérico?             → cálculo
  Fonte primária + dissertar?        → análise de fonte
  Associar colunas / tabela?         → associação
  V ou F?                            → V-F
  Nenhuma das anteriores?            → dissertativa
  Gráfico + alternativas             → múltipla escolha
  Gráfico + cálculo                  → cálculo

GABARITO: sempre vazio. NUNCA invente ou infira.

FORMATO:

**Q-[N]** · pág. [X]
[> Texto:] [> Gráfico:] [se houver]
Enunciado: [pergunta com todos os itens]
Alternativas: (dissertativa/cálculo) ou lista
Gabarito:
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

**QC-[N]** · [Banca] · [Ano] · pág. [X]
[> Texto:] [> Gráfico:] [se houver]
Enunciado: [pergunta com todos os itens]
Alternativas: lista
Gabarito:
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

---

EXEMPLOS:

**Q-1** · pág. 22
> Gráfico: Movimento de um carro
> Eixo X: Tempo (s) — 0, 5, 10, 15 · Eixo Y: Velocidade (m/s) — 0, 20, 40
> A→B (0–5s: sobe de 0 a 40 m/s) · B→C (5–10s: 40 m/s constante) · C→D (10–15s: cai a 0)
Enunciado: Em qual intervalo o carro está em movimento uniforme?
Alternativas:
  a) A→B  b) B→C  c) C→D  d) A→D
Gabarito:
Tipo: múltipla escolha
Classificação: fácil

---

## PADRÃO DAS QUESTÕES
- Estilo predominante: [múltipla escolha / dissertativa / cálculo / misto]
- Foco: [memorização / interpretação / aplicação / cálculo]
- Nível de dificuldade médio: [fácil / médio / difícil]
- Tópicos mais cobrados: [lista]
- Total: [N] questões do capítulo + [N] questões de concurso
