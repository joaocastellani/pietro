# PROMPT DE TRANSCRIÇÃO — INGLÊS (9º ano)
# Uso: MyHub.ia · Sonnet · múltiplos screenshots por run
# Output: um bloco por página, para concatenação posterior

---

Tarefa: Transcreva fielmente o conteúdo de cada screenshot anexado.
Este é um passo intermediário de extração — o output será processado
depois por um Prompt de Captura. Não organize, não classifique,
não gere flashcards, não interprete. Apenas extraia.

REGRAS GERAIS:
- Preserve todo texto exatamente como aparece — ortografia, pontuação,
  maiúsculas, negritos, itálicos, aspas e numeração
- Não resuma, não parafraseie, não omita nada
- Preserve a hierarquia visual: identifique o que é título de seção,
  subtítulo, corpo de texto, caixa destacada, legenda, rodapé
- Textos em inglês devem ser transcritos em inglês — não traduzir
- Processe cada screenshot na ordem em que foi anexado
- Numere as páginas sequencialmente a partir de 01
- PROIBIDO encerrar com perguntas, sugestões ou qualquer texto
  fora dos blocos abaixo. O output termina com o último bloco.

REGRA DE OMISSÃO:
Se um elemento não puder ser extraído com fidelidade (ex: texto
ilegível, imagem sem legenda, balão cortado), registre na seção
ELEMENTOS IRRECONSTRUÍVEIS da página — nunca invente ou complete
com conhecimento próprio.

---

COMO TRATAR CADA TIPO DE ELEMENTO:

TÍTULO DE SEÇÃO E SUBSEÇÃO:
Identifique os títulos de seção do livro e transcreva em negrito
com marcador markdown correspondente (##, ###).
Títulos comuns (não limitado a):
"Reading Time", "Before reading", "Reading", "After reading",
"Vocabulary Time", "Glossary", "Take a tip!", "Now I know — Glossary",
"Language Tools", "Focus on the language",
"Listening Time", "Before listening", "After listening",
"Speaking Time", "Before speaking", "After speaking",
"Writing Time", "Before writing", "Focus on the genre",
"Writing", "After writing",
"Now I Know", "Summary"
Seções com título temático próprio (ex: "Can English build bridges
between people and art?") também devem ser identificadas como
título e transcritas.

TEXTO CORRIDO (expositivo ou instrucional):
Transcreva integralmente, preservando parágrafos separados.
Inclua instruções ao aluno exatamente como aparecem no material
(ex: "Read the text and answer the questions.", "Look at the picture.").

TEXTOS DE LEITURA (reading texts, artigos, diálogos, letras de música,
histórias, entrevistas, infográficos):
Transcreva com o rótulo > Texto:
- Título: (conforme o material; "Sem título" se ausente)
- Autor: (conforme legenda; omitir se ausente)
- Fonte: (veículo, editora, ano — conforme o material; omitir se ausente)
- Gênero: (article / dialogue / song / interview / story /
           comic strip / infographic / letter / other)
- Texto integral: preserve parágrafos, estrofes (se poema),
  legendas internas, falas de balões (se quadrinhos), créditos
  de imagem associados ao texto
Se parcialmente ilegível: transcreva o legível e marque
[ilegível] no trecho faltante.

TABELAS GRAMATICAIS E QUADROS DE LÍNGUA:
Reconstitua em markdown fiel — mesmas colunas, mesmas linhas,
mesmos exemplos e observações. Preserve o inglês exatamente.
Exemplos de tabelas comuns: conjugação verbal, formas afirmativa /
negativa / interrogativa, pronomes, conectivos, estrutura de gênero.
Se a tabela continuar na página seguinte, registre:
[TABELA CONTINUA NA PRÓXIMA PÁGINA] ao final da tabela parcial
e [CONTINUAÇÃO DA TABELA DA PÁGINA ANTERIOR] no início da próxima.

CAIXAS DE VOCABULÁRIO E GLOSSÁRIO:
Transcreva cada entrada exatamente:
- [palavra ou expressão em inglês]: [definição ou tradução conforme o livro]
Caixas "Take a tip!" e equivalentes → transcreva o título em negrito
e o conteúdo abaixo.
Caixas de vocabulário embutidas no texto (word boxes, highlighted
vocabulary) → transcreva na posição em que aparecem.

QUESTÕES E ATIVIDADES:
Transcreva integralmente — enunciado em inglês, alternativas, itens.
Preserve a numeração original do livro.
Para questões de múltipla escolha: transcreva cada alternativa
identificada com a letra original (a, b, c, d / A, B, C, D).
Para questões de lacuna: preserve os underlines como `______`.
Para questões com texto-base associado: transcreva o texto-base
com o rótulo > Texto: (acima) e na questão escreva apenas:
[Texto-base: ver > Texto: da mesma página]
Ícones de marcador (quadrado, círculo, seta, traço) usados como
bullet antes de perguntas → substitua por `—`.

FOTOGRAFIAS E ILUSTRAÇÕES:
Descreva em bloco separado com o rótulo > Imagem:
- Tipo: (fotografia, ilustração, obra de arte, infográfico, mapa)
- Contexto: (identificável pela legenda ou pelo tema do capítulo)
- Elementos visíveis relevantes: (pessoas, cenário, objetos, símbolos)
- Legenda completa conforme o material
- Crédito ou acervo (se citado)
Se não houver legenda e o conteúdo for irrecuperável →
registre em ELEMENTOS IRRECONSTRUÍVEIS.

SUMMARY (mapa mental de lacunas):
Descreva em bloco separado com o rótulo > Summary:
- Tema central (nó central do mapa mental)
- Categorias ou ramos visíveis (nós secundários)
- Textos já preenchidos pelo livro (transcreva exatamente)
- Lacunas a completar: represente cada linha em branco como `______`
  na posição correspondente no esquema
- Estrutura do mapa (descreva a disposição visual dos nós)
Se o Summary for parcialmente ilegível → transcreva o legível
e marque [ilegível] nas partes não identificáveis.

LEGENDAS SOLTAS E CRÉDITOS:
Transcreva na posição em que aparecem na página.

NUMERAÇÃO DE PÁGINA:
Sempre que visível, registre o número da página ao final do bloco
como: *[Página X do livro]*

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

## Unit 3 — Can music change the world?

**Objectives**
— Understand the main idea of a song
— Use modal verbs: must / should / can
— Write a persuasive text

---

## PÁGINA 02

## Reading Time

### Before reading
1. Look at the picture and answer the questions.
a) What kind of music do you like?
b) Do you think music can change people's lives? Why?

### Reading

> Texto:
- Título: Music as a Tool for Change
- Autor: não citado
- Fonte: Adapted from Time for Kids, 2019
- Gênero: article
- Texto integral:
Music has always been a powerful force in society. From protest
songs of the 1960s to today's social media anthems, musicians
have used their voices to fight for justice and equality...
[continua]

*[Página 48 do livro]*

---

## PÁGINA 03

## Language Tools

### Focus on the language — Modal verbs: must / should / can

Modal verbs are used to express obligation, advice, and ability.
They are followed by the base form of the verb.

| Modal | Use | Example |
|---|---|---|
| must | strong obligation / necessity | You **must** wear a seatbelt. |
| should | advice / recommendation | You **should** study more. |
| can | ability / possibility | She **can** speak three languages. |

**Note:** "Must" and "should" are not usually used in questions
in the same way as regular auxiliaries. Use "Do I have to...?"
for strong obligation in questions.

---

## PÁGINA 04

## Vocabulary Time

### Glossary
- **anthem**: a song adopted as an official song by a group of people
- **protest**: an expression of disagreement with something

### Take a tip!
"Must" vs. "have to": both express obligation, but "must" comes
from the speaker's own feelings, while "have to" comes from
external rules. Example: "I must study." (I want to.) vs.
"I have to study." (My teacher said so.)

---

## PÁGINA 05

## Writing Time

### Focus on the genre — Persuasive text

A persuasive text tries to convince the reader to agree with
a point of view. It includes:
- A clear opinion or thesis
- Supporting arguments
- Examples and evidence
- A conclusion that reinforces the main idea

**Example present in the material:** "Why Everyone Should Listen to Music"

### Writing
Write a short persuasive text (8–10 lines) about the power of music.
Use modal verbs to express your opinions.

---

## PÁGINA 06

## Now I Know

1. Read the sentences and choose the correct modal verb.
a) You ______ exercise regularly. It's very important. (must / can)
b) She ______ play the guitar really well. (must / can)
c) We ______ be more careful with the environment. (should / must)

## Summary

> Summary:
- Tema central: Unit 3 — Music
- Ramos visíveis: Reading | Language | Vocabulary | Writing
- Textos dados pelo livro:
  · Reading: "Music as a Tool for Change" (article)
  · Language: Modal verbs — must / should / can
- Lacunas: Reading — genre: ______  ·  Language — use of "must": ______
  ·  Vocabulary — definition of "anthem": ______
- Estrutura: mapa radial com tema central no centro e 4 ramos

*[Página 56 do livro]*

---

## PÁGINA 07

### ELEMENTOS IRRECONSTRUÍVEIS
- Fotografia · canto superior direito · jovens tocando instrumentos, sem legenda · crédito ausente e contexto não identificável com certeza pelo texto da página
