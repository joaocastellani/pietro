# PROMPT DE CAPTURA — GEOGRAFIA (9º ano) · versão txt
# Uso: input .md consolidado gerado pelo Prompt_de_Transcricao_Geo
# Arquivo gerado: geo-[unidade]-[capitulo].md

---

Tarefa: Organize e estruture o conteúdo do arquivo `.md` anexado,
gerado pelo Prompt de Transcrição de Geografia. O material já foi
extraído das imagens — não há screenshots. Trabalhe exclusivamente
sobre o texto recebido. Não acesse imagens, não tente ver o original.

REGRAS GERAIS:
- Preserve todos os dados exatamente como aparecem no material
- Não resuma, não interprete, não omita dados numéricos, nomes
  de países, regiões, capitais ou indicadores
- Para mapas, gráficos e imagens geográficas: o conteúdo já está
  descrito no `.md` como blocos `> Mapa:`, `> Gráfico:` e
  `> Imagem:` — use essas descrições como fonte. Não tente
  reconstituir além do que está escrito.
- PROIBIDO encerrar o output com perguntas, próximos passos,
  sugestões ou qualquer texto fora dos blocos abaixo.
  O output termina com o último bloco preenchido — nada mais.

REGRA DE OMISSÃO (vale para todos os blocos condicionais):
Se um bloco não tiver dados reais extraídos do material, NÃO o
Inclua. Não escreva "Não aplicável", "Não especificado", "Não
citado" nem variações. Bloco sem dado concreto = bloco ausente
no output. Campo sem dado concreto = campo ausente no bloco.
Exemplos proibidos:
- Bloco E incluído com campos "Não especificado no conteúdo"
- Bloco B com campo "Fonte: —"

BLOCOS DE ATIVIDADES E QUESTÕES: a seção Atividades (bloco final
numerado) vai na SEÇÃO ATIVIDADES ao final deste arquivo.
EXCEÇÃO: questões intercaladas no corpo do capítulo (antes das
Atividades) devem ser capturadas no BLOCO G deste arquivo com
prefixo QI-N e tag [IC].

CAIXAS E SEÇÕES COM TÍTULO PRÓPRIO: todo bloco com título
destacado deve ser capturado — ex: "No contexto", "Veja também
em História", "Saiba mais", caixas de destaque, caixas laterais
informativas. Direcione o conteúdo para o bloco correspondente
(mapa → Bloco A, texto separado → Bloco F, dado → Bloco B,
processo → Bloco D).

SEÇÃO FINAL OPCIONAL — ELEMENTOS PENDENTES:
Se o `.md` recebido contiver seções ELEMENTOS IRRECONSTRUÍVEIS
com itens relevantes para o capítulo (mapas sem legenda, cartogramas
com gradiente indescritível, imagens sem contexto identificável),
liste-os ao final do arquivo:

## ELEMENTOS PENDENTES
- [descrição do elemento] · [localização no capítulo] · [por que é relevante]

---

## 1. METADADOS
- Matéria: Geografia
- Unidade:
- Capítulo/Tema:
- Nível de ensino: 9º ano
- Perfil do capítulo: [escreva EXATAMENTE um:
  descritivo-espacial | analítico-temático |
  histórico-geográfico | misto]

---

## 2. CONCEITOS E DEFINIÇÕES
Para cada conceito presente no capítulo — incluindo termos em
destaque no texto, títulos de processos, nomes de fenômenos,
índices e indicadores, modelos e classificações geográficas,
mesmo que sem definição formal explícita:
- Nome do conceito em destaque
- Definição completa conforme o material (ou descrição funcional
  se não houver definição formal)
- Exemplos dados pelo livro (preserve países, regiões, dados)
- Observações ou ressalvas explícitas no texto

---

## 3. FLASHCARDS DO CAPÍTULO
Regras:
- Mínimo 10 flashcards
- Cobertura obrigatória por bloco — gere ao menos 1 card por:
  · Cada conceito principal da Seção 2
  · Cada região ou país principal do Bloco C
  · Cada processo do Bloco D (causa ou consequência central)
  A cobertura obrigatória tem precedência absoluta — satisfaça
  todos os itens acima antes de aplicar qualquer limite.
  Só após cobrir todos os itens obrigatórios aplica-se o teto
  de 20: se ainda houver itens relevantes além dos obrigatórios,
  selecione os mais importantes até o máximo de 20.
- Cubra conceitos, localizações, dados e relações espaciais
- Alterne sentidos: conceito→definição, país→capital,
  região→característica, dado→país/região, causa→consequência
- NÃO crie flashcard de questão de exercício
- Se não souber a resposta do verso, omita o card inteiro
- NÃO escreva "Frente:" duas vezes na mesma linha

FORMATO OBRIGATÓRIO — 3 linhas por card, linha em branco entre cards:

**FC-1**
🔵 Frente: O que é densidade demográfica?
🟢 Verso: Relação entre o número de habitantes e a área do território, expressa em hab/km².

**FC-2**
🔵 Frente: Qual é a capital da Alemanha?
🟢 Verso: Berlim.

---

## BLOCO A — MAPAS E REPRESENTAÇÕES CARTOGRÁFICAS
[Execute se o `.md` recebido contiver blocos `> Mapa:` com
dados cartográficos — políticos, físicos, temáticos, cartogramas,
climáticos, econômicos ou demográficos.]

Para cada mapa, use os campos já descritos no bloco `> Mapa:`:
- Título do mapa (conforme o material)
- Tipo: [político / físico / temático / cartograma / climático /
  econômico / demográfico / outro]
- Escala (se descrita)
- Legenda: todos os elementos e valores descritos
- Países/regiões/territórios identificados
- Dados visíveis nos rótulos (se descritos)
- Fonte (se citada)
- Contexto de uso: o que o mapa ilustra no capítulo

---

## BLOCO B — DADOS GEOGRÁFICOS ESTRUTURADOS
[Execute se o `.md` recebido contiver tabelas markdown com linhas
e colunas explícitas, ou blocos `> Gráfico:` com valores de
eixos ou rótulos explicitamente marcados.]

CHECAGEM OBRIGATÓRIA — responda internamente antes de executar:
"Existe uma tabela em markdown no `.md` recebido, com linhas e
colunas explícitas, que eu possa copiar célula a célula sem
Inferir nenhum valor?"
→ Não → omita a parte de tabelas, sem exceção
→ Sim → copie célula a célula, sem adicionar nada

Para gráficos com valores explícitos nos eixos ou rótulos:
- Capture eixos (grandeza + unidade) e valores marcados
- Capture apenas o que está literalmente descrito no `.md`
- Nunca interpole ou estime valores entre os marcados

PROIBIDO reconstituir tabela a partir de:
- Texto corrido ou parágrafos expositivos
- Descrições de blocos `> Gráfico:` sem valores explícitos
- Descrições de blocos `> Mapa:` ou `> Imagem:`
- Alternativas ou enunciados de questões
- Qualquer fonte que não seja tabela markdown com linhas e
  colunas literalmente presentes no `.md` recebido

Para cada conjunto de dados:
- Título ou tema dos dados
- Organize em tabela fiel ao material
- Preserve todos os valores numéricos com unidades exatas
  (populações, áreas, IDH, PIB, percentuais)
- Não omita nenhum país, região ou item da lista original

---

## BLOCO C — REGIÕES, PAÍSES E LOCALIZAÇÕES
[Execute se o capítulo trabalhar com localização, divisão
regional ou caracterização de países e territórios.]

Para cada região ou país tratado:
- Nome oficial e outros nomes citados
- Localização: continente, hemisférios, coordenadas (se citadas)
- Países limítrofes ou países membros (se aplicável)
- Características físicas principais (relevo, clima, hidrografia)
- Características humanas principais (população, economia, IDH)
- Dados numéricos exatos conforme o material

---

## BLOCO D — PROCESSOS E DINÂMICAS GEOGRÁFICAS
[Execute se o capítulo descrever processos espaciais,
dinâmicas populacionais, fluxos migratórios, processos
físicos (erosão, desertificação, urbanização) ou
transformações territoriais com etapas identificáveis.]

Para cada processo:
- Nome do processo
- Causas descritas no material
- Etapas ou fases (se apresentadas)
- Consequências descritas
- Exemplos geográficos citados (preserve países e dados)
- Indicadores associados (se citados)

---

## BLOCO E — EXPERIMENTOS, SAÍDAS DE CAMPO E ATIVIDADES PRÁTICAS
[Execute SOMENTE se houver atividade prática com procedimento
identificável. Descrição genérica de fenômeno não ativa este bloco.]

- Nome ou título | Objetivo
- Materiais ou recursos | Procedimento em sequência
- Resultado esperado | Conceito geográfico associado

---

## BLOCO F — TEXTO COMPLEMENTAR
[Execute SOMENTE se o capítulo incluir texto de leitura SEPARADO
do conteúdo expositivo principal — como reportagem, artigo
adaptado, excerto de autor externo ou seção "No contexto".
NÃO capture aqui o conteúdo expositivo normal do capítulo —
esse vai nas Seções 2, Bloco C e Bloco D.
NÃO capture afirmativas de questões como fatos.
NÃO capture trechos cujo conteúdo já está no corpo expositivo
do capítulo — se a fonte for o próprio livro didático, não é
texto complementar.
Critério prático: o texto do Bloco F deve ter título próprio
destacado, ser de fonte externa, ou estar claramente separado
do texto principal do capítulo. Se a fonte não estiver citada,
omita o campo — nunca preencha com "Não especificada".]

- Título | Tema central
- Dados e fatos relevantes (preserve números, países, datas)
- Conceitos geográficos presentes
- Fonte (se citada)

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
Enunciado: [texto completo]
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
> Texto: → APENAS fonte primária (tabela de dados com autoria,
  excerto de relatório ou documento com citação explícita).
  Se ausente: OMITA.
  ATENÇÃO: artigo jornalístico, texto de divulgação ou trecho
  de livro didático NÃO são fonte primária → use apenas como
  contexto do Enunciado, não como bloco > Texto:.
Enunciado: → APENAS a pergunta. Nunca vazio.

MÍDIA — CRÍTICO: blocos SEPARADOS antes do Enunciado:. Omitir se vazio.
Use a descrição já presente no `.md` recebido para cada bloco:

> Mapa: use a descrição do bloco `> Mapa:` correspondente.
  Se marcado como [IRRECONSTRUÍVEL] na transcrição: [IMAGEM].
> Gráfico: use a descrição do bloco `> Gráfico:` correspondente.
  Nunca substitua por [GRÁFICO] se a descrição estiver disponível.
> Imagem: use a descrição do bloco `> Imagem:` correspondente.
  Se marcado como [IRRECONSTRUÍVEL] na transcrição: [IMAGEM].
[IMAGEM] irreconstruível:
  [IMAGEM] (tipo; contexto geográfico; o que mostra; por que necessária)

TIPO — um único valor:
  Tem alternativas?                             → múltipla escolha
  Afirmações I II III + alternativas?          → múltipla escolha
  V ou F?                                       → V-F
  Pede cálculo ou conversão de dado?           → cálculo
  Pede dissertar/justificar processo?          → dissertativa
  Análise de mapa ou cartograma?               → análise de mapa
  Análise de gráfico ou dado estatístico?      → análise de dados
  Associar colunas / completar tabela?         → associação
  Mapa + alternativas                          → múltipla escolha
  Gráfico + alternativas                       → múltipla escolha
  Mapa + dissertar                             → análise de mapa

GABARITO: sempre vazio. NUNCA invente ou infira.

FORMATO — inclua APENAS campos com conteúdo real:

**Q-[N]** · pág. [X]
[> Texto:] [> Mapa:] [> Gráfico:] [> Imagem:] [se houver]
Enunciado: [pergunta com todos os itens]
Alternativas: (dissertativa/cálculo/análise) ou lista
Gabarito:
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

**QC-[N]** · [Banca] · [Ano] · pág. [X]
[> Texto:] [> Mapa:] [> Gráfico:] [> Imagem:] [se houver]
Enunciado: [pergunta com todos os itens]
Alternativas: lista
Gabarito:
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

---

## PADRÃO DAS QUESTÕES
- Estilo predominante: [múltipla escolha / dissertativa / análise de mapa / misto]
- Foco: [localização / dados estatísticos / processos geográficos / análise de mapa / aplicação]
- Nível de dificuldade médio: [fácil / médio / difícil]
- Tópicos mais cobrados: [lista]
- Total: [N] questões do capítulo + [N] questões de concurso
