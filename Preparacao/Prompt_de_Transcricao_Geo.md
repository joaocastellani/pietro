# PROMPT DE TRANSCRIÇÃO — GEOGRAFIA (9º ano)
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
- Não resuma, não parafraseie, não omita nada
- Preserve a hierarquia visual: identifique o que é título principal,
  subtítulo, corpo de texto, caixa lateral, legenda, rodapé
- Processe cada screenshot na ordem em que foi anexado
- Numere as páginas sequencialmente a partir de 01
- PROIBIDO encerrar com perguntas, sugestões ou qualquer texto
  fora dos blocos abaixo. O output termina com o último bloco.

REGRA DE OMISSÃO:
Se um elemento não puder ser extraído com fidelidade (ex: texto
ilegível, mapa sem legenda visível, cartograma com gradiente de
cor contínuo sem intervalos definidos), registre na seção
ELEMENTOS IRRECONSTRUÍVEIS da página — nunca invente ou infira.

---

COMO TRATAR CADA TIPO DE ELEMENTO:

TEXTO CORRIDO:
Transcreva integralmente, preservando parágrafos separados.
Indique títulos e subtítulos com marcadores markdown (##, ###).
Caixas com título próprio (ex: "No contexto", "Saiba mais",
"Veja também em História") → transcreva o título em negrito
e o conteúdo abaixo.

TABELAS:
Reconstitua em markdown fiel — mesmas colunas, mesmas linhas,
mesmos valores. Preserve unidades, percentuais e dados exatos.
Se a tabela continuar na página seguinte, registre:
[TABELA CONTINUA NA PRÓXIMA PÁGINA] ao final da tabela parcial
e [CONTINUAÇÃO DA TABELA DA PÁGINA ANTERIOR] no início da próxima.

MAPAS GEOGRÁFICOS:
Descreva em bloco separado com o rótulo > Mapa:
- Título do mapa (conforme aparece no material)
- Tipo: [político / físico / temático / cartograma / climático /
  econômico / demográfico / outro]
- Escala (se presente): valor exato conforme o material
- Legenda: liste TODOS os elementos visíveis com valores exatos
  (cores, símbolos, hachuras, intervalos numéricos)
  Ex: "> 50 milhões (vermelho escuro) · 10–50 milhões (laranja)
  · < 10 milhões (amarelo)"
- Países, regiões, capitais ou territórios identificáveis pelo nome
- Dados visíveis diretamente sobre o mapa (valores em rótulos)
- Fonte (se citada)
Se a legenda for ilegível ou o gradiente de cor for contínuo
sem intervalos discretos definidos → registre em
ELEMENTOS IRRECONSTRUÍVEIS com descrição do que é visível
e do que impede a extração.

GRÁFICOS E INFOGRÁFICOS:
Descreva em bloco separado com o rótulo > Gráfico:
- Título
- Tipo (barras, linha, pizza, pirâmide etária, dispersão, etc.)
- Eixo X: label e valores
- Eixo Y: label e valores
- Séries: nome e comportamento (ex: "sobe de X para Y entre A e B")
- Fonte (se citada)
Nunca substitua por [GRÁFICO] — sempre reconstitua em texto.

FOTOGRAFIAS E IMAGENS GEOGRÁFICAS:
Descreva em bloco separado com o rótulo > Imagem:
- Tipo (fotografia, imagem de satélite, gravura, ilustração)
- Contexto geográfico identificável pela legenda ou pelo capítulo
  (ex: paisagem urbana, relevo, vegetação, fenômeno climático,
  atividade econômica, infraestrutura)
- Elementos visíveis relevantes (formações geográficas, estruturas,
  atividades humanas, indicadores de escala ou localização)
- Legenda completa conforme o material
- Crédito ou acervo (se citado)
Se não houver legenda e o conteúdo for irrecuperável →
registre em ELEMENTOS IRRECONSTRUÍVEIS.

QUESTÕES E ATIVIDADES:
Transcreva integralmente — enunciado, alternativas, itens.
Não classifique nem atribua gabarito.
Preserve a numeração original do livro.
Ícones de marcador (quadrado, círculo, seta, traço) usados como
bullet antes de perguntas reflexivas → substitua por `—`.

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

### A Europa Ocidental

A Europa Ocidental é uma das regiões mais desenvolvidas do mundo,
com elevados índices de IDH e alta densidade demográfica. Os países
que compõem essa região incluem França, Alemanha, Itália e Espanha...

**No contexto**
A União Europeia, criada em 1993 pelo Tratado de Maastricht,
reúne atualmente 27 países-membros. Sua sede institucional está
em Bruxelas, na Bélgica...

> Mapa: Densidade demográfica da Europa (2020)
- Tipo: cartograma
- Escala: não citada
- Legenda: > 200 hab/km² (vermelho escuro) · 100–200 hab/km² (vermelho)
  · 50–100 hab/km² (laranja) · < 50 hab/km² (amarelo)
- Países identificados: França, Alemanha, Países Baixos, Polônia, Itália, Espanha
- Fonte: ONU, 2020

---

## PÁGINA 02

### ELEMENTOS IRRECONSTRUÍVEIS
- Cartograma · centro da página · gradiente de cores representando IDH por país europeu · escala de cores contínua sem valores discretos definidos — impossível descrever intervalos com precisão
