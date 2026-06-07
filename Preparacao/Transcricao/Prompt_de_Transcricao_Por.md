# PROMPT DE TRANSCRIÇÃO — PORTUGUÊS (9º ano)
# Uso: MyHub.ia · Sonnet · múltiplos screenshots por run
# Output: um bloco por página, para concatenação posterior

---

Tarefa: Transcreva fielmente o conteúdo de cada screenshot anexado.
Este é um passo intermediário de extração — o output será processado
depois por um Prompt de Captura. Não organize, não classifique,
não gere flashcards, não interprete. Apenas extraia.

REGRAS GERAIS:
- Preserve todo texto exatamente como aparece — ortografia, pontuação,
  maiúsculas, negritos, itálicos, aspas, travessões e numeração
- Não resuma, não parafraseie, não omita nada
- Preserve a hierarquia visual: identifique o que é título principal,
  subtítulo, corpo de texto, caixa lateral, legenda, rodapé
- Para textos literários (poemas, crônicas, contos): preserve
  a diagramação — quebras de verso, estrofes, parágrafos e
  qualquer formatação visual intencional
- Processe cada screenshot na ordem em que foi anexado
- Numere as páginas sequencialmente a partir de 01
- PROIBIDO encerrar com perguntas, sugestões ou qualquer texto
  fora dos blocos abaixo. O output termina com o último bloco.

REGRA DE OMISSÃO:
Se um elemento não puder ser extraído com fidelidade (ex: texto
ilegível, tirinha com balão cortado, imagem sem legenda), registre
na seção ELEMENTOS IRRECONSTRUÍVEIS da página — nunca invente
ou complete com conhecimento próprio.

---

COMO TRATAR CADA TIPO DE ELEMENTO:

TEXTO CORRIDO (explicativo, expositivo):
Transcreva integralmente, preservando parágrafos separados.
Indique títulos e subtítulos com marcadores markdown (##, ###).
Caixas com título próprio (ex: "Saiba mais", "Para saber mais",
"Você sabia?", "Língua viva", "Vocabulário", "Dica", "Atenção",
"Veja também em História / Geografia", "Intertextualizando",
"Alternando o gênero") → transcreva o título em negrito e
o conteúdo abaixo.

TEXTOS LITERÁRIOS E TEXTOS-BASE:
Transcreva integralmente com o rótulo > Texto:
- Título conforme aparece no material (ou "Sem título" se ausente)
- Autor conforme aparece na legenda
- Fonte / veículo / editora / ano conforme aparece no material
- Texto integral: preserve quebras de verso, estrofes, parágrafos,
  diálogos, travessões e formatação visual (negritos, itálicos)
- Gênero textual (identifique: poema, crônica, conto, notícia,
  artigo de opinião, carta, anúncio, outro)
Nunca parafrasear — transcreva palavra a palavra.
Se parcialmente ilegível: transcreva o legível e marque
[ilegível] no trecho faltante.

TIRINHAS E HISTÓRIAS EM QUADRINHOS:
Descreva em bloco separado com o rótulo > Tirinha:
- Título da tirinha e autor / série (conforme legenda)
- Número de quadros
- Para cada quadro, em ordem:
  · Personagens presentes e ação ou postura visível
  · Balões de fala na sequência: [Personagem]: "texto do balão"
  · Balão de pensamento: [Personagem pensa]: "texto"
  · Narrador (se houver caixa de texto fora dos balões): Narrador: "texto"
  · Elemento visual relevante para o humor ou sentido (ex:
    expressão facial, objeto, símbolo, onomatopeia)
- Legenda e crédito abaixo da tirinha (conforme o material)
Se algum balão estiver ilegível ou cortado: registre [ilegível]
no lugar do texto e registre em ELEMENTOS IRRECONSTRUÍVEIS.

CHARGES E CARTUNS:
Descreva em bloco separado com o rótulo > Charge:
- Autor e data (conforme legenda)
- Cenário e personagens identificáveis (por nome ou por tipo)
- Falas ou legendas visíveis (transcreva exatamente)
- Elemento visual central que compõe a crítica ou o humor
- Legenda ou crédito abaixo da imagem (conforme o material)
Se ilegível ou sem legenda → registre em ELEMENTOS IRRECONSTRUÍVEIS
com descrição do que é visível.

FOTOGRAFIAS E ILUSTRAÇÕES:
Descreva em bloco separado com o rótulo > Imagem:
- Tipo (fotografia, ilustração, gravura, reprodução de obra de arte)
- Contexto identificável pela legenda ou pelo capítulo
- Elementos visíveis relevantes (pessoas, cenário, objetos, ações)
- Legenda completa conforme o material
- Crédito ou acervo (se citado)
Se não houver legenda e o conteúdo for irrecuperável →
registre em ELEMENTOS IRRECONSTRUÍVEIS.

TABELAS E QUADROS GRAMATICAIS:
Reconstitua em markdown fiel — mesmas colunas, mesmas linhas,
mesmos valores e exemplos. Preserve conjugações, classificações,
pronomes, prefixos, sufixos e demais dados com exatidão.
Se a tabela continuar na página seguinte, registre:
[TABELA CONTINUA NA PRÓXIMA PÁGINA] ao final da tabela parcial
e [CONTINUAÇÃO DA TABELA DA PÁGINA ANTERIOR] no início da próxima.

GRÁFICOS E INFOGRÁFICOS:
Descreva em bloco separado com o rótulo > Gráfico:
- Título
- Tipo (barras, linha, pizza, infográfico, etc.)
- Eixo X: label e valores
- Eixo Y: label e valores
- Séries ou categorias: nome e valores explícitos
- Fonte (se citada)
Nunca substitua por [GRÁFICO] — sempre reconstitua em texto.

QUESTÕES E ATIVIDADES:
Transcreva integralmente — enunciado, alternativas, itens.
Não classifique nem atribua gabarito.
Preserve a numeração original do livro.
Ícones de marcador (quadrado, círculo, seta, traço) usados como
bullet antes de perguntas reflexivas → substitua por `—`.
Para questões com texto-base associado: registre o texto-base
na seção TEXTOS LITERÁRIOS acima e na questão escreva apenas:
[Texto-base: ver > Texto: da mesma página]

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

### Interpretação de texto

> Texto:
- Título: A hora da estrela
- Autor: Clarice Lispector
- Fonte: Editora Rocco, 1977
- Gênero: conto (excerto)

Ela era tão ingênua que às vezes sorria para os outros na rua.
Ninguém lhe sorria de volta, o que às vezes a magoava. Mas ela
logo esquecia, pois tinha outras coisas mais urgentes em que pensar,
como o problema de arranjar sustento...

**Para saber mais**
Clarice Lispector (1920–1977) é considerada uma das maiores
escritoras brasileiras do século XX. Seu estilo é marcado por...

---

## PÁGINA 02

### Gramática — Período composto por subordinação

As orações subordinadas estabelecem uma relação de dependência
sintática com a oração principal. Elas se classificam em:

| Classificação | Função sintática | Conjunção típica |
|---|---|---|
| Substantiva subjetiva | Sujeito da oração principal | que |
| Substantiva objetiva direta | Objeto direto | que |
| Substantiva predicativa | Predicativo do sujeito | que |

---

## PÁGINA 03

> Tirinha: Mafalda — Quino
- 3 quadros
- Quadro 1: Mafalda sentada à mesa com um livro aberto. Mafalda: "Por que será que as pessoas leem tão pouco?"
- Quadro 2: Mafalda olha para o lado, pensativa.
- Quadro 3: Mafalda conclui, olhando para o livro. Mafalda: "Talvez porque as letras não façam barulho."
- Fonte: © Quino / Toda Mafalda, Martins Fontes

---

## PÁGINA 04

### ELEMENTOS IRRECONSTRUÍVEIS
- Tirinha · canto inferior esquerdo · balão de fala parcialmente cortado na margem direita do screenshot · texto do último balão ilegível
