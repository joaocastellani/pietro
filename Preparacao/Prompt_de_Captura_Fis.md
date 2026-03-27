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
- BLOCOS DE ATIVIDADES E QUESTÕES: se o capítulo incluir seções
  de atividades ou questões para o aluno, NÃO os capture neste
  arquivo. Questões vão no arquivo separado fis-[u]-[c]-questoes.md.
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
```
