# PROMPT DE TRANSCRIÇÃO — HISTÓRIA (9º ano)
# Uso: MyHub.ia · Sonnet · múltiplos screenshots por run
# Output: um bloco por página, para concatenação posterior

---

Tarefa: Transcreva fielmente o conteúdo de cada screenshot anexado.
Este é um passo intermediário de extração — o output será processado
depois por um Prompt de Captura. Não organize, não classifique,
não gere flashcards, não interprete. Apenas extraia.

REGRAS GERAIS:
- Preserve todo texto exatamente como aparece — ortografia, pontuação,
  maiúsculas, negritos, itálicos, números
- Não resuma, não parafraseie, não omita nada
- Preserve a hierarquia visual: identifique o que é título principal,
  subtítulo, corpo de texto, caixa lateral, legenda, rodapé
- Processe cada screenshot na ordem em que foi anexado
- Numere as páginas sequencialmente a partir de 01
- PROIBIDO encerrar com perguntas, sugestões ou qualquer texto
  fora dos blocos abaixo. O output termina com o último bloco.

REGRA DE OMISSÃO:
Se um elemento não puder ser extraído com fidelidade (ex: texto
ilegível, imagem sem legenda), registre na seção ELEMENTOS
IRRECONSTRUÍVEIS da página — nunca invente ou infira conteúdo.

---

COMO TRATAR CADA TIPO DE ELEMENTO:

TEXTO CORRIDO:
Transcreva integralmente, preservando parágrafos separados.
Indique títulos e subtítulos com marcadores markdown (##, ###).
Caixas com título próprio (ex: "Para saber mais", "Saiba mais",
"Veja também") → transcreva o título em negrito e o conteúdo abaixo.

TABELAS:
Reconstitua em markdown fiel — mesmas colunas, mesmas linhas,
mesmos valores. Preserve unidades, percentuais e datas exatas.
Se a tabela continuar na página seguinte, registre:
[TABELA CONTINUA NA PRÓXIMA PÁGINA] ao final da tabela parcial
e [CONTINUAÇÃO DA TABELA DA PÁGINA ANTERIOR] no início da próxima.

MAPAS HISTÓRICOS:
Descreva em bloco separado com o rótulo > Mapa:
- Título do mapa (conforme aparece no material)
- Período histórico representado
- Legenda: liste todos os elementos visíveis (cores, símbolos, hachuras)
- Territórios, rotas, fronteiras ou zonas identificáveis pelo nome
- Fonte (se citada)
Se ilegível ou sem legenda identificável → registre em
ELEMENTOS IRRECONSTRUÍVEIS com descrição do que é visível.

GRÁFICOS E INFOGRÁFICOS:
Descreva em bloco separado com o rótulo > Gráfico:
- Título
- Tipo (barras, linha, pizza, etc.)
- Eixo X: label e valores
- Eixo Y: label e valores
- Séries: nome e comportamento (ex: "sobe de X para Y entre A e B")
- Fonte (se citada)
Nunca substitua por [GRÁFICO] — sempre reconstitua em texto.

FOTOGRAFIAS E GRAVURAS HISTÓRICAS:
Descreva em bloco separado com o rótulo > Imagem:
- Tipo (fotografia, gravura, pintura, cartaz, caricatura)
- Contexto histórico identificável pela legenda ou pelo capítulo
- Elementos visíveis relevantes (pessoas, cenário, símbolos, ações)
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

### A Primeira Guerra Mundial

O conflito que ficou conhecido como Primeira Guerra Mundial teve início
em julho de 1914, após o assassinato do arquiduque Francisco Ferdinando...

**Para saber mais**
A expressão "guerra total" foi cunhada para descrever conflitos em que...

> Mapa: Frentes de batalha na Europa (1914–1918)
- Período: 1914 a 1918
- Legenda: linha vermelha = Frente Ocidental · linha azul = Frente Oriental
  · área hachurada = territórios ocupados pela Alemanha
- Territórios identificados: França, Bélgica, Alemanha, Império Austro-Húngaro
- Fonte: não citada

---

## PÁGINA 02

### ELEMENTOS IRRECONSTRUÍVEIS
- Fotografia · canto inferior direito · homens em trincheira, sem legenda · legenda ausente e contexto não identificável pelo texto da página
