# PROMPT DE TRANSCRIÇÃO — FÍSICA (9º ano)
# Uso: MyHub.ia · Sonnet · múltiplos screenshots por run
# Output: um bloco por página, para concatenação posterior

---

Tarefa: Transcreva fielmente o conteúdo de cada screenshot anexado.
Este é um passo intermediário de extração — o output será processado
depois por um Prompt de Captura. Não organize, não classifique,
não gere flashcards, não interprete. Apenas extraia.

REGRAS GERAIS:
- Preserve todo texto exatamente como aparece — ortografia, pontuação,
  maiúsculas, negritos, itálicos, números e unidades
- Não resuma, não parafraseie, não omita nada — especialmente
  valores numéricos, símbolos, expoentes e unidades SI
- Preserve a hierarquia visual: identifique o que é título principal,
  subtítulo, corpo de texto, caixa lateral, legenda, rodapé
- Processe cada screenshot na ordem em que foi anexado
- Numere as páginas sequencialmente a partir de 01
- PROIBIDO encerrar com perguntas, sugestões ou qualquer texto
  fora dos blocos abaixo. O output termina com o último bloco.

REGRA DE OMISSÃO:
Se um elemento não puder ser extraído com fidelidade (ex: diagrama
de circuito complexo, esquema de forças sem legenda, fórmula
ilegível), registre na seção ELEMENTOS IRRECONSTRUÍVEIS da página
— nunca invente ou infira valores.

---

COMO TRATAR CADA TIPO DE ELEMENTO:

TEXTO CORRIDO:
Transcreva integralmente, preservando parágrafos separados.
Indique títulos e subtítulos com marcadores markdown (##, ###).
Caixas com título próprio (ex: "Saiba mais", "Para saber mais",
"Você sabia?", "Curiosidade", "Aplicação") → transcreva o título
em negrito e o conteúdo abaixo.

FÓRMULAS E EXPRESSÕES MATEMÁTICAS:
Transcreva em bloco separado com o rótulo > Fórmula:
- Nome ou identificação da fórmula / lei (conforme o material)
- Expressão matemática em notação ASCII clara:
  · Expoentes: use ^ (ex: v² → v^2 · 10³ → 10^3)
  · Frações: use / com parênteses quando necessário (ex: d/t · (a+b)/c)
  · Raiz quadrada: √ ou sqrt()
  · Vetores (se indicados): [vetor F] ou negrito conforme o material
  · Subscrito: use _ (ex: v₀ → v_0 · F_r)
- Para cada variável presente na fórmula:
  · Símbolo exato
  · Nome da grandeza conforme o material
  · Unidade SI conforme o material (se especificada na página)
- Constantes (se apresentadas): símbolo + valor + unidade
- Enunciado verbal da lei (se presente na página — transcreva integralmente)
- Condições de validade (se mencionadas na página)
Nunca invente variáveis, unidades ou condições que não estejam
explicitamente na página.

TABELAS DE DADOS:
Reconstitua em markdown fiel — mesmas colunas, mesmas linhas,
mesmos valores e unidades. Preserve grandezas, símbolos,
valores numéricos com notação científica quando presentes.
Se a tabela continuar na página seguinte, registre:
[TABELA CONTINUA NA PRÓXIMA PÁGINA] ao final da tabela parcial
e [CONTINUAÇÃO DA TABELA DA PÁGINA ANTERIOR] no início da próxima.

GRÁFICOS (posição × tempo, velocidade × tempo, força × distância,
outros gráficos cartesianos):
Descreva em bloco separado com o rótulo > Gráfico:
- Título do gráfico (conforme aparece no material)
- Tipo: [posição-tempo / velocidade-tempo / força-extensão /
  energia / corrente-tensão / outro]
- Eixo X: grandeza + unidade + valores marcados (todos os que
  aparecem explicitamente no gráfico)
- Eixo Y: grandeza + unidade + valores marcados (todos)
- Séries ou segmentos: identifique cada segmento com nome
  (se houver rótulo) e descreva o comportamento:
  ex: "A→B (0 a 5 s): cresce linearmente de 0 a 20 m/s"
      "B→C (5 a 10 s): constante em 20 m/s"
      "C→D (10 a 15 s): decresce linearmente a 0"
- Fonte (se citada)
Nunca substitua por [GRÁFICO] — sempre reconstitua em texto.
Se os valores dos eixos forem ilegíveis → registre em
ELEMENTOS IRRECONSTRUÍVEIS descrevendo o comportamento geral visível.

DIAGRAMAS DE CIRCUITO ELÉTRICO:
Descreva em bloco separado com o rótulo > Diagrama:
- Tipo: [circuito série / paralelo / misto / esquema de forças /
  diagrama de campo / outro]
- Componentes identificáveis e suas posições relativas
  (ex: bateria → resistor 1 → resistor 2 → volta para bateria)
- Valores visíveis nos componentes (tensão, resistência, corrente)
- Legenda (se presente)
- Fonte (se citada)
Se o diagrama for complexo demais para descrição textual fiel →
registre em ELEMENTOS IRRECONSTRUÍVEIS com descrição do que
é identificável e por que não foi possível extrair completamente.

DIAGRAMAS DE FORÇAS E VETORES:
Descreva em bloco separado com o rótulo > Diagrama:
- Tipo: [diagrama de forças / decomposição vetorial / campo
  elétrico / campo magnético / outro]
- Objeto sobre o qual as forças atuam
- Cada força ou vetor: nome + símbolo + sentido/direção descrito
  em palavras (ex: "F_peso: vertical, para baixo")
- Valores indicados (se presentes)
- Legenda (se presente)
Se ilegível ou irreconstruível → registre em ELEMENTOS
IRRECONSTRUÍVEIS com descrição do que é visível.

FOTOGRAFIAS E IMAGENS CIENTÍFICAS:
Descreva em bloco separado com o rótulo > Imagem:
- Tipo (fotografia, ilustração, esquema, imagem de satélite,
  gravura histórica, foto de experimento)
- Fenômeno ou equipamento retratado
- Elementos visíveis relevantes (aparatos, escala, contexto físico)
- Legenda completa conforme o material
- Crédito ou acervo (se citado)
Se não houver legenda e o conteúdo for irrecuperável →
registre em ELEMENTOS IRRECONSTRUÍVEIS.

QUESTÕES E ATIVIDADES:
Transcreva integralmente — enunciado, dados fornecidos,
alternativas, itens. Preserve valores numéricos e unidades.
Não classifique nem resolva.
Preserve a numeração original do livro.
Para questões com gráfico ou diagrama associado:
transcreva o elemento visual no bloco correspondente
(> Gráfico: ou > Diagrama:) imediatamente antes do enunciado
da questão, e na questão escreva:
[Elemento visual: ver > Gráfico: / > Diagrama: desta página]

EXPERIMENTOS E ATIVIDADES PRÁTICAS:
Transcreva integralmente — título, objetivo, materiais,
procedimento em sequência, resultado esperado, conclusão.
Preserve numeração de etapas como aparece no material.

LEGENDAS SOLTAS E CRÉDITOS:
Transcreva na posição em que aparecem na página.

---

FORMATO DE OUTPUT — um bloco por página:

## PÁGINA [NN]

[Conteúdo transcrito da página conforme regras acima]

### ELEMENTOS IRRECONSTRUÍVEIS
[Apenas se houver. Formato:]
- [tipo do elemento] · [localização na página] · [o que é visível] · [por que não foi possível extrair]

---

[próxima página]

---

EXEMPLO DE OUTPUT (estrutura, não conteúdo):

## PÁGINA 01

### Segunda Lei de Newton

A Segunda Lei de Newton estabelece a relação entre a força resultante
aplicada a um corpo, sua massa e a aceleração produzida. Quanto maior
a força aplicada, maior será a aceleração; quanto maior a massa do
corpo, menor será a aceleração para uma mesma força.

> Fórmula: Segunda Lei de Newton
- Expressão: F_r = m × a
- Variáveis:
  · F_r — Força resultante — N (newton)
  · m — Massa — kg (quilograma)
  · a — Aceleração — m/s^2
- Enunciado: "A força resultante que age sobre um corpo é igual ao
  produto de sua massa pela aceleração adquirida."
- Condições de validade: válida para referenciais inerciais

**Saiba mais**
Isaac Newton publicou a obra Princípios Matemáticos da Filosofia
Natural em 1687. As três leis do movimento apresentadas nessa obra
fundamentaram a mecânica clássica por mais de dois séculos...

---

## PÁGINA 02

> Gráfico: Velocidade de um carro em função do tempo
- Tipo: velocidade-tempo
- Eixo X: Tempo (s) — valores: 0, 2, 4, 6, 8, 10
- Eixo Y: Velocidade (m/s) — valores: 0, 10, 20, 30
- Segmentos:
  · A→B (0 a 4 s): cresce linearmente de 0 a 20 m/s
  · B→C (4 a 6 s): constante em 20 m/s
  · C→D (6 a 10 s): decresce linearmente de 20 a 0 m/s
- Fonte: não citada

---

## PÁGINA 03

> Diagrama: Circuito elétrico em série
- Tipo: circuito série
- Componentes: bateria (12 V) → resistor R1 (4 Ω) → resistor R2 (8 Ω) → retorna à bateria
- Valores indicados: bateria = 12 V · R1 = 4 Ω · R2 = 8 Ω
- Legenda: "Figura 3.1 — Circuito com dois resistores em série"

---

## PÁGINA 04

### ELEMENTOS IRRECONSTRUÍVEIS
- Diagrama de forças · centro da página · objeto sobre plano inclinado com vetores de força · vetores sem rótulo e ângulo ilegível — impossível identificar magnitudes e direções com precisão
