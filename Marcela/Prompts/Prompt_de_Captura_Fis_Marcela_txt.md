# PROMPT DE CAPTURA — FÍSICA (Ensino Superior — Biologia) · versão PDF nativo
# Uso: PDF do capítulo anexado diretamente (texto nativo, não escaneado)
# Arquivo gerado: fis-[unidade]-[capitulo].md

Base: adaptado do `Prompt_de_Captura_Fis_txt.md` do Pietro. Diferença
principal: o Pietro parte de uma *transcrição* já gerada a partir de
screenshots (Prompt de Transcrição). O material da Marcela já é um
PDF de texto nativo (apostila/capítulo digitado) — **não há etapa de
Transcrição**. Anexe o PDF do capítulo diretamente nesta conversa e
trabalhe sobre o texto e as figuras dele.

---

Tarefa: organize e estruture o conteúdo do PDF anexado (capítulo de
Mecânica) neste formato. Preserve fórmulas, gráficos e tabelas
exatamente como aparecem no original.

REGRAS GERAIS:
- Preserve todos os dados exatamente como aparecem no material
- Não resuma, não interprete, não omita dados numéricos, símbolos,
  expoentes ou unidades
- Para fórmulas: preserve expressão, variáveis e unidades exatamente
  como aparecem no PDF
- Para gráficos e figuras (ex.: Fig. 23, Fig. 24, diagramas de
  vetores): descreva em bloco `> Gráfico:` ou `> Diagrama:` com
  eixos, valores marcados e o comportamento da curva/forma —
  reconstrua o que for possível ler diretamente da figura
- PROIBIDO encerrar o output com perguntas, próximos passos,
  sugestões ou qualquer texto fora dos blocos abaixo.
  O output termina com o último bloco preenchido — nada mais.

REGRA DE OMISSÃO (vale para todos os blocos condicionais):
Se um bloco não tiver dados reais extraídos do material, NÃO o
inclua. Não escreva "Não aplicável", "Não especificado", "Não
citado" nem variações. Bloco sem dado concreto = bloco ausente
no output. Campo sem dado concreto = campo ausente no bloco.

GABARITO — DIFERENÇA IMPORTANTE em relação ao material do Pietro:
o livro da Marcela **traz o gabarito impresso** nos "Exercícios
Propostos" (campo "R." logo após cada exercício). Sempre que o
gabarito estiver presente no PDF, copie-o exatamente no campo
Gabarito: da questão. Só deixe o campo vazio se o livro realmente
não trouxer resposta para aquele exercício específico.

BLOCOS DE ATIVIDADES E QUESTÕES: a seção "Exercícios Propostos"
(bloco final de cada parte) vai na SEÇÃO ATIVIDADES ao final deste
arquivo. Questões resolvidas dentro do corpo do texto (ex.:
"Exemplo 1", "Exemplo 2" com solução completa) vão no BLOCO B
(fórmulas) ou na Seção 2 como exemplo do conceito — não são
"atividades" porque já vêm resolvidas pelo autor.

CAIXAS E SEÇÕES COM TÍTULO PRÓPRIO: todo bloco com título
destacado deve ser capturado — ex: "Procedimento Experimental",
"Análise Gráfica", "Exemplo N".

---

## 1. METADADOS
- Matéria: Física
- Unidade: [número do capítulo do material — ex: 2]
- Capítulo/Tema: [número da parte — ex: 1 para "Parte 1", 2 para "Parte 2"]
- Nível de ensino: Ensino Superior — Física Geral (curso de Biologia)
- Perfil do capítulo: [escreva EXATAMENTE um:
  conceitual | matemático-operacional | misto]

---

## 2. CONCEITOS E DEFINIÇÕES
Para cada conceito presente no capítulo — incluindo termos em
destaque no texto, nomes de leis, grandezas definidas, mesmo que
sem definição formal explícita:
- Nome do conceito em destaque
- Definição completa conforme o material
- Exemplos dados pelo livro, incluindo exemplos resolvidos
  ("Exemplo 1", "Exemplo 2" etc. com o desenvolvimento completo)
- Observações ou ressalvas explícitas no texto (ex.: distinção
  entre movimento uniforme e uniformemente variado)

---

## 3. FLASHCARDS DO CAPÍTULO
Regras:
- Mínimo 10 flashcards
- Cobertura obrigatória por bloco — gere ao menos 1 card por:
  · Cada conceito principal da Seção 2
  · Cada fórmula ou lei do Bloco B
  · Cada grandeza principal do Bloco C
  A cobertura obrigatória tem precedência absoluta — satisfaça
  todos os itens acima antes de aplicar qualquer limite.
  Só após cobrir todos os itens obrigatórios aplica-se o teto
  de 20: se ainda houver itens relevantes além dos obrigatórios,
  selecione os mais importantes até o máximo de 20.
- Alterne sentidos: conceito→definição, fórmula→variáveis,
  grandeza→unidade, causa→efeito
- Para fórmulas: frente = expressão, verso = nome + variáveis + unidades
- NÃO crie flashcard de questão de exercício
- Se não souber a resposta do verso com base no PDF, omita o card

FORMATO OBRIGATÓRIO — 3 linhas por card, linha em branco entre cards:

**FC-1**
🔵 Frente: Qual é a equação da posição no Movimento Uniformemente Variado (MUV)?
🟢 Verso: S = S₀ + v₀·t + ½·a·t², onde S₀ é a posição inicial, v₀ a velocidade inicial, a a aceleração e t o tempo.

**FC-2**
🔵 Frente: O que caracteriza uma grandeza vetorial?
🟢 Verso: Tem módulo (intensidade), direção e sentido — ex.: força, velocidade, aceleração. Diferente de grandeza escalar, que é só número + unidade.

---

## BLOCO B — FÓRMULAS, LEIS E PRINCÍPIOS
[Execute se o PDF contiver expressões matemáticas ou leis físicas.]

Para cada fórmula ou lei:
- Nome da lei ou grandeza
- Expressão matemática exata (preserve símbolos e expoentes
  conforme o PDF — ex: S = S₀ + v₀·t + ½·a·t²)
- Para cada variável:
  · Símbolo exato
  · Nome da grandeza
  · Unidade SI (apenas se presente no PDF — não inferir)
- Enunciado completo da lei (se apresentado no texto)
- Condições de validade (se descritas no PDF — ex: aceleração constante)
- Exemplo resolvido associado, com o desenvolvimento completo
  (preserve os números exatamente como no PDF)

PROIBIDO completar variáveis, unidades ou condições que não
estejam explicitamente no PDF.

---

## BLOCO C — GRANDEZAS, UNIDADES E SISTEMA INTERNACIONAL
[Execute se o PDF abordar o SI, vetores, conversões de unidades
ou notação científica.]

#### C1 — Grandezas fundamentais e derivadas
Para cada grandeza citada:
- Nome da grandeza
- Símbolo
- Unidade SI + símbolo da unidade
- Tipo: [escalar / vetorial]
- Exemplos dados pelo livro para essa categoria

#### C2 — Conversões de unidades
Para cada conversão presente no PDF:
- Grandeza convertida
- Fator de conversão exato conforme o material
- Exemplo de aplicação (preserve os números do PDF)

---

## BLOCO D — DADOS FACTUAIS DENSOS
[Execute se o PDF contiver tabelas com linhas e colunas explícitas
— ex: "Tabela 2. Valores de tempo e distância."]

CHECAGEM OBRIGATÓRIA — responda internamente antes de executar:
"Existe uma tabela no PDF, com linhas e colunas explícitas, que eu
possa copiar célula a célula sem inferir nenhum valor?"
→ Não → omita o bloco inteiro, sem exceção
→ Sim → copie célula a célula, sem adicionar nada

Para cada tabela:
- Título ou tema dos dados (ex: "Tabela 2. Valores de tempo e distância")
- Organize em tabela markdown fiel ao material
- Preserve todos os valores numéricos com unidades exatas
- Não omita nenhum item da lista ou tabela original

---

## BLOCO E — GRÁFICOS E FIGURAS
[Execute se o PDF contiver gráficos (ex: Fig. 23 S×t, Fig. 24 v×t)
ou diagramas de vetores (ex: Fig. 2-1 a Fig. 2-5).]

Para cada gráfico:
- Número e legenda da figura conforme o PDF
- Tipo de gráfico (S×t, v×t, a×t, diagrama de vetores)
- Eixos: grandeza + unidade de cada eixo
- Valores marcados nos eixos
- Forma da curva (reta / parábola / segmentos) e o que ela
  representa fisicamente (ex.: "reta em v×t → velocidade
  proporcional ao tempo, movimento uniformemente acelerado")
- Pontos ou valores notáveis destacados no gráfico (ex.: variação
  Δv, Δt indicada na figura)

Para cada diagrama de vetores:
- Vetores envolvidos (nomes/símbolos, ex: v₁, v₂)
- Operação ilustrada (soma com mesmo sentido, sentidos opostos,
  vetores ortogonais / regra do paralelogramo)
- Resultado da operação conforme mostrado na figura

---

## BLOCO G — QUESTÕES INTERCALADAS
[Se houver questões autônomas inseridas no corpo do capítulo, fora
da seção "Exercícios Propostos" — normalmente não há neste material,
mas verifique.]

Use prefixo QI-N (sequência própria do arquivo) e tag [IC]:

**QI-[N]** · [IC]
Enunciado: [texto completo com dados e valores]
Gabarito: [se fornecido pelo livro]
Conceito testado: [conceito central avaliado]

---

## SEÇÃO ATIVIDADES
[Capture TODAS as questões da seção "Exercícios Propostos" de
cada parte do capítulo.]

NUMERAÇÃO: sequência própria — NUNCA a do livro. Q-N própria do arquivo.

TEXTO vs ENUNCIADO:
Enunciado: → a pergunta completa, com todos os dados numéricos e
  unidades exatamente como no PDF.

MÍDIA: se o exercício referenciar uma figura do capítulo (ex.: "Fig.
2-9, das calhas"), inclua um bloco `> Figura:` com a descrição antes
do Enunciado:.

TIPO — um único valor:
  Pede cálculo numérico?             → cálculo
  Pede dissertar/justificar?         → dissertativa
  Tem alternativas?                  → múltipla escolha
  Nenhuma das anteriores?            → dissertativa

GABARITO: copie o valor exato do campo "R." do livro quando presente
(ex: "R. 5,00 m/s²"). Deixe vazio apenas se o livro não trouxer
resposta para aquele exercício.

FORMATO — inclua APENAS campos com conteúdo real:

**Q-[N]** · pág. [X]
[> Figura:] [se houver]
Enunciado: [pergunta completa com todos os dados numéricos]
Alternativas: (cálculo/dissertativa) ou lista
Gabarito: [valor do livro, se houver]
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

---

## PADRÃO DAS QUESTÕES
- Estilo predominante: [cálculo / dissertativa / misto]
- Foco: [aplicação de fórmula / interpretação de gráfico / conceitual]
- Nível de dificuldade médio: [fácil / médio / difícil]
- Tópicos mais cobrados: [lista]
- Total: [N] questões da(s) parte(s) do capítulo
