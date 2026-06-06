# PROMPT DE CAPTURA — FÍSICA (9º ano) · versão txt
# Uso: input .md consolidado gerado pelo Prompt_de_Transcricao_Fis
# Arquivo gerado: fis-[unidade]-[capitulo].md

---

Tarefa: Organize e estruture o conteúdo do arquivo `.md` anexado,
gerado pelo Prompt de Transcrição de Física. O material já foi
extraído das imagens — não há screenshots. Trabalhe exclusivamente
sobre o texto recebido. Não acesse imagens, não tente ver o original.

REGRAS GERAIS:
- Preserve todos os dados exatamente como aparecem no material
- Não resuma, não interprete, não omita dados numéricos, símbolos,
  expoentes ou unidades
- Para fórmulas: use os campos já descritos nos blocos `> Fórmula:`
  — preserve expressão, variáveis e unidades exatamente como
  transcritos. Não tente completar variáveis não presentes no `.md`.
- Para gráficos, diagramas e imagens: o conteúdo já está descrito
  nos blocos `> Gráfico:`, `> Diagrama:` e `> Imagem:` — use essas
  descrições como fonte. Não tente reconstituir além do que está escrito.
- PROIBIDO encerrar o output com perguntas, próximos passos,
  sugestões ou qualquer texto fora dos blocos abaixo.
  O output termina com o último bloco preenchido — nada mais.

REGRA DE OMISSÃO (vale para todos os blocos condicionais):
Se um bloco não tiver dados reais extraídos do material, NÃO o
inclua. Não escreva "Não aplicável", "Não especificado", "Não
citado" nem variações. Bloco sem dado concreto = bloco ausente
no output. Campo sem dado concreto = campo ausente no bloco.
Exemplos proibidos:
- Bloco E incluído com campos "Não especificado no conteúdo"
- Bloco B com campo "Unidade SI: —"

BLOCOS DE ATIVIDADES E QUESTÕES: a seção Atividades (bloco final
numerado) vai na SEÇÃO ATIVIDADES ao final deste arquivo.
EXCEÇÃO: questões intercaladas no corpo do capítulo (antes das
Atividades) devem ser capturadas no BLOCO G deste arquivo com
prefixo QI-N e tag [IC].

CAIXAS E SEÇÕES COM TÍTULO PRÓPRIO: todo bloco com título
destacado deve ser capturado — ex: "Saiba mais", "Para saber mais",
"Você sabia?", "Curiosidade", "Aplicação", "Veja também".
Direcione o conteúdo para o bloco correspondente
(fórmula → Bloco B, dado → Bloco D, experimento → Bloco E,
texto complementar → Bloco F, conceito → Seção 2).

SEÇÃO FINAL OPCIONAL — ELEMENTOS PENDENTES:
Se o `.md` recebido contiver seções ELEMENTOS IRRECONSTRUÍVEIS
com itens relevantes para o capítulo (diagramas de circuito
sem legenda, esquemas de forças sem valores, gráficos com
eixos ilegíveis), liste-os ao final do arquivo:

## ELEMENTOS PENDENTES
- [descrição do elemento] · [localização no capítulo] · [por que é relevante]

---

## 1. METADADOS
- Matéria: Física
- Unidade:
- Capítulo/Tema:
- Nível de ensino: 9º ano
- Perfil do capítulo: [escreva EXATAMENTE um:
  histórico-conceitual | matemático-operacional |
  descritivo-científico | misto]

---

## 2. CONCEITOS E DEFINIÇÕES
Para cada conceito presente no capítulo — incluindo termos em
destaque no texto, nomes de leis, fenômenos físicos e
grandezas definidas, mesmo que sem definição formal explícita:
- Nome do conceito em destaque
- Definição completa conforme o material (ou descrição funcional
  se não houver definição formal)
- Exemplos dados pelo livro (preserve números, unidades e contextos)
- Observações ou ressalvas explícitas no texto

---

## 3. FLASHCARDS DO CAPÍTULO
Regras:
- Mínimo 10 flashcards
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
- Alterne sentidos: conceito→definição, fórmula→variáveis,
  cientista→contribuição, grandeza→unidade, causa→efeito
- Para fórmulas: frente = expressão, verso = nome + variáveis + unidades
- Para cientistas: frente = nome, verso = contribuição principal
- NÃO crie flashcard de questão de exercício
- Se não souber a resposta do verso com base no `.md`, omita o card

FORMATO OBRIGATÓRIO — 3 linhas por card, linha em branco entre cards:

**FC-1**
🔵 Frente: Qual é a expressão da Segunda Lei de Newton?
🟢 Verso: F_r = m × a, onde F_r é a força resultante (N), m é a massa (kg) e a é a aceleração (m/s²).

**FC-2**
🔵 Frente: Quem foi Isaac Newton e qual foi sua principal contribuição para a Física?
🟢 Verso: Físico e matemático inglês (1643–1727) que formulou as três leis do movimento e a Lei da Gravitação Universal, fundamentos da mecânica clássica.

---

## BLOCO A — CIENTISTAS CITADOS NO MATERIAL
[Execute se o `.md` recebido citar cientistas, físicos, matemáticos
ou exploradores científicos com papel no conteúdo do capítulo.
NÃO inclua fotógrafos, artistas ou nomes que apareçam
exclusivamente como crédito de imagem ou acervo.]

Para cada cientista, capture APENAS o que está explicitamente
descrito no `.md` recebido — não infira, não complemente
com conhecimento externo:
- Nome completo
- Contribuição descrita no texto (palavras do material)
- Instrumento, obra ou experimento associado (se citado no `.md`)

---

## BLOCO B — FÓRMULAS, LEIS E PRINCÍPIOS
[Execute se o `.md` recebido contiver blocos `> Fórmula:` com
expressões matemáticas ou leis físicas.]

Para cada fórmula ou lei, use os campos já descritos no bloco
`> Fórmula:` da transcrição:
- Nome da lei ou grandeza
- Expressão matemática exata (preserve símbolos e expoentes
  conforme transcritos — ex: F_r = m × a · v^2 · 10^3)
- Para cada variável descrita no `.md`:
  · Símbolo exato
  · Nome da grandeza
  · Unidade SI (apenas se presente no `.md` — não inferir)
- Constantes (se descritas no `.md`): símbolo + valor + unidade
- Enunciado completo da lei (se transcrito no `.md`)
- Condições de validade (se descritas no `.md`)

PROIBIDO completar variáveis, unidades ou condições que não
estejam explicitamente no `.md` recebido.

---

## BLOCO C — GRANDEZAS, UNIDADES E SISTEMA INTERNACIONAL
[Execute se o `.md` recebido abordar o SI, conversões de unidades
ou notação científica.]

#### C1 — Grandezas fundamentais e derivadas
Para cada grandeza citada no `.md`:
- Nome da grandeza
- Símbolo
- Unidade SI + símbolo da unidade
- Tipo: [fundamental / derivada / adimensional / vetorial / escalar]
- Grandezas fundamentais das quais deriva (se descrito no `.md`)

#### C2 — Conversões de unidades
Para cada conversão presente no `.md`:
- Grandeza convertida
- Fator de conversão exato conforme o material
- Exemplo de aplicação (preserve os números do `.md`)

#### C3 — Notação científica e ordens de grandeza
[Execute se o `.md` abordar notação científica]
- Regra da notação científica conforme o material (a × 10^n)
- Exemplos resolvidos presentes no `.md` (preserve os números)
- Regra de ordem de grandeza (se descrita no `.md`)

---

## BLOCO D — DADOS FACTUAIS DENSOS
[Execute se o `.md` recebido contiver tabelas markdown com linhas
e colunas explícitas.]

CHECAGEM OBRIGATÓRIA — responda internamente antes de executar:
"Existe uma tabela em markdown no `.md` recebido, com linhas e
colunas explícitas, que eu possa copiar célula a célula sem
inferir nenhum valor?"
→ Não → omita o bloco inteiro, sem exceção
→ Sim → copie célula a célula, sem adicionar nada

PROIBIDO reconstituir tabela a partir de:
- Texto corrido ou parágrafos expositivos
- Descrições de blocos `> Gráfico:` ou `> Diagrama:`
- Alternativas ou enunciados de questões
- Qualquer fonte que não seja tabela markdown com linhas e
  colunas literalmente presentes no `.md` recebido

Para cada conjunto de dados:
- Título ou tema dos dados
- Organize em tabela fiel ao material
- Preserve todos os valores numéricos com unidades exatas
- Não omita nenhum item da lista ou tabela original

---

## BLOCO E — EXPERIMENTOS E DEMONSTRAÇÕES
[Execute se o `.md` recebido descrever experimentos,
demonstrações ou procedimentos investigativos com etapas
identificáveis.]

Para cada experimento:
- Nome ou título (se presente no `.md`)
- Objetivo
- Materiais citados
- Procedimento (em sequência ordenada, conforme o `.md`)
- Resultado observado
- Conclusão apresentada pelo material
- Cientista associado (se citado no `.md`)

---

## BLOCO F — TEXTO COMPLEMENTAR
[Execute SOMENTE se o `.md` recebido contiver texto de leitura
SEPARADO do conteúdo expositivo principal — como seção "Saiba
mais", "Para saber mais", reportagem, artigo adaptado ou
excerto de contextualização.
NÃO capture aqui o conteúdo expositivo normal do capítulo —
esse vai nas Seções 2 e Blocos A–E.
NÃO capture afirmativas de questões como fatos.
NÃO capture trechos cujo conteúdo já está no corpo expositivo
do capítulo — se a fonte for o próprio livro didático, não é
texto complementar.
Critério prático: o texto do Bloco F deve ter título próprio
destacado, ser de fonte externa ou estar claramente separado
do texto principal do capítulo. Se a fonte não estiver citada
no `.md`, omita o campo — nunca preencha com "Não especificada".]

- Título do texto | Tema central
- Dados, valores e fatos relevantes (preserve números, datas,
  nomes e unidades conforme o `.md`)
- Conceitos físicos presentes ou exemplificados
- Fonte (se citada no `.md`)

---

## BLOCO G — QUESTÕES INTERCALADAS
[Se houver questões autônomas inseridas no corpo do capítulo,
antes da seção Atividades. Sinais: número ou caixa destacada
com título "Pratique"/"Resolva"/"Verifique"/"Atividade" dentro
do fluxo expositivo — não no bloco final de Atividades.]

DISTINÇÃO — CRÍTICO:
Questão intercalada = aparece no corpo do capítulo, antes de Atividades.
Seção Atividades (bloco final numerado) → NÃO capturar aqui → vai na SEÇÃO ATIVIDADES abaixo.

Use prefixo QI-N (sequência própria do arquivo) e tag [IC]:

**QI-[N]** · [IC]
Enunciado: [texto completo com dados e valores]
Gabarito: [se fornecido pelo livro]
Conceito testado: [conceito central avaliado]

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
> Texto: → APENAS fonte primária (excerto com autoria explícita).
  Se ausente: OMITA.
Enunciado: → APENAS a pergunta. Nunca vazio.
Preserve todos os dados numéricos, unidades e condições do enunciado.

MÍDIA — CRÍTICO: blocos SEPARADOS antes do Enunciado:. Omitir se vazio.
Use a descrição já presente no `.md` recebido para cada bloco:

> Gráfico: use a descrição do bloco `> Gráfico:` correspondente.
  Nunca substitua por [GRÁFICO] se a descrição estiver disponível.
> Diagrama: use a descrição do bloco `> Diagrama:` correspondente.
  Se marcado como [IRRECONSTRUÍVEL] na transcrição: [IMAGEM].
> Imagem: use a descrição do bloco `> Imagem:` correspondente.
  Se marcado como [IRRECONSTRUÍVEL] na transcrição: [IMAGEM].
[IMAGEM] irreconstruível:
  [IMAGEM] (tipo; contexto físico; o que mostra; por que necessária)

TIPO — um único valor:
  Tem alternativas?                  → múltipla escolha
  Afirmações I II III + alternativas? → múltipla escolha
  Pede cálculo numérico?             → cálculo
  Fonte primária + dissertar?        → análise de fonte
  Associar colunas / tabela?         → associação
  V ou F?                            → V-F
  Análise de gráfico + alternativas  → múltipla escolha
  Análise de gráfico + cálculo       → cálculo
  Diagrama + alternativas            → múltipla escolha
  Nenhuma das anteriores?            → dissertativa

GABARITO: sempre vazio. NUNCA invente ou infira.

FORMATO — inclua APENAS campos com conteúdo real:

**Q-[N]** · pág. [X]
[> Texto:] [> Gráfico:] [> Diagrama:] [> Imagem:] [se houver]
[[IMAGEM] se necessário]
Enunciado: [pergunta com todos os itens e dados numéricos]
Alternativas: (dissertativa/cálculo) ou lista
Gabarito:
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

**QC-[N]** · [Banca] · [Ano] · pág. [X]
[> Texto:] [> Gráfico:] [> Diagrama:] [> Imagem:] [se houver]
[[IMAGEM] se necessário]
Enunciado: [pergunta com todos os itens e dados numéricos]
Alternativas: lista
Gabarito:
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

---

## PADRÃO DAS QUESTÕES
- Estilo predominante: [múltipla escolha / dissertativa / cálculo / misto]
- Foco: [memorização / interpretação / aplicação / cálculo]
- Nível de dificuldade médio: [fácil / médio / difícil]
- Tópicos mais cobrados: [lista]
- Total: [N] questões do capítulo + [N] questões de concurso
