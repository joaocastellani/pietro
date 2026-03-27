# PROMPT DE PREPARAÇÃO — GEOGRAFIA (9º ano)

Arquivos de entrada: `geo-[u]-[c].md` + `geo-[u]-[c]-questoes.md`
Arquivo gerado:      `geo-[u]-[c]-prep.md`
Mapa mental gerado:  `mindmap_geo[u][c].html`

---

## INSTRUÇÕES GERAIS

1. Use `project_knowledge_search` para localizar e ler
   `geo-[u]-[c].md` e `geo-[u]-[c]-questoes.md` inteiros
   antes de gerar qualquer conteúdo
2. Todo o conteúdo é gerado de uma vez, sem interação com o aluno
3. Preserve dados numéricos, nomes de países e regiões exatamente
4. Você pode inferir dicas e pegadinhas — não precisa citar o livro
5. Se detectar inconsistência factual, registre na Seção 8
6. Os SVGs da Seção 12 ficam embutidos no próprio `prep.md`

---

## ESTRUTURA DO ARQUIVO DE PREPARAÇÃO

Gere nesta ordem. Seções [CONDICIONAL] só se o conteúdo existir.

---

### SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

**Gerada por último**, após a Seção 12 estar completa.

```
## DIAGRAMAS DISPONÍVEIS — geo-[u]-[c]

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| [nome] | DIAGRAMA: [nome] | [contexto de uso] |

### Mapas via image_search (Seção 4):
- [lista de mapas com termos de busca sugeridos]

### Tabelas markdown (Seção 6):
- [lista das tabelas presentes]

### Nota ao Professor:
Para diagramas: leia o SVG da Seção 12 e passe ao Visualizer.
Para mapas: use image_search com os termos sugeridos na Seção 4.
Tabelas da Seção 6 são apresentadas como markdown no chat.
Se o usuário anexar printscreens de mapas da apostila,
use-os diretamente em vez de fazer image_search.
```

---

### SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — GEOGRAFIA
- Unidade:
- Capítulo:
- Tema:
- Perfil: [descritivo-espacial / analítico-temático /
           histórico-geográfico / misto]
- Mapas principais: [lista dos mapas do capítulo ou "nenhum"]
- Processos/dinâmicas principais: [lista ou "nenhum"]
```

---

### SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

Resumo narrativo organizado por blocos temáticos.
Cada bloco: título em negrito + explicação nível 9º ano +
conexão com exemplos geográficos reais quando possível.

Para blocos com dados espaciais: apresente os dados em contexto
(ex: "O Brasil, com 8,5 milhões de km², é o maior país da
América do Sul e o 5º maior do mundo").

---

### SEÇÃO 3 — PENSADORES E REFERÊNCIAS TEÓRICAS [CONDICIONAL]

Gerar se o capítulo citar geógrafos, cientistas ou teóricos
com contribuição relevante para o conteúdo.

Para cada pensador:
```
### [Nome completo] ([período])
**Área:** [campo]
**Contribuição no capítulo:** [o que o material descreve]
**Conceito associado:** [teoria, modelo ou conceito — se citado]
```

---

### SEÇÃO 4 — MAPAS DO CAPÍTULO [CONDICIONAL]

Gerar se o capítulo apresentar mapas relevantes.
Esta seção orienta o Professor sobre como apresentar cada mapa.

Para cada mapa identificado no material:
```
### MAPA: [título]
**Tipo:** [político / físico / temático / cartograma / climático /
          econômico / demográfico]
**O que mostra:** [descrição em 1–2 linhas]
**Dados da legenda:** [elementos e significados]
**Dados capturados:** [países, regiões, valores identificados]
**Termos para image_search:** "[termos específicos]"
**Quando usar na aula:** [momento da Etapa 1]
**Pegadinha:** [erro de leitura ou interpretação mais comum]
```

---

### SEÇÃO 5 — PROCESSOS E DINÂMICAS GEOGRÁFICAS [CONDICIONAL]

Gerar se o capítulo apresentar processos espaciais ou dinâmicas
com etapas ou relações de causa e consequência.

Para cada processo:
```
### [Nome do processo]
**Causas:** [fatores descritos no material]
**Dinâmica:** [como o processo ocorre]
**Consequências:** [impactos descritos]
**Exemplos geográficos:** [países, regiões, dados do material]
**Indicadores:** [métricas associadas — se citadas]
💡 **Pegadinha:** [confusão mais comum sobre este processo]
```

---

### SEÇÃO 6 — DADOS GEOGRÁFICOS DENSOS [CONDICIONAL]

Gerar se o capítulo apresentar conjuntos de dados estruturados.
Usar **tabelas markdown** — não SVG para dados tabulares.
Adicionar coluna "⚠️ Pegadinha" quando relevante.

REGRAS CRÍTICAS para tabelas:
- Se um dado não foi capturado no material, NÃO deixe célula
  vazia sem explicação e NÃO escreva meta-comentários como
  "(não listados no material)". Em vez disso:
  1. Gere um alerta na SEÇÃO 8 com o formato:
     ⚠️ DADO AUSENTE — [tabela/campo]
     Campo: [qual célula está incompleta]
     Motivo: [não capturado / imagem não processada]
     Ação: adicionar ao arquivo geo-[u]-[c].md e reprocessar
     o prep antes de disponibilizar ao aluno
  2. Na tabela, marque a célula com "⚠️ ver Seção 8"
- Se o material citar um GRUPO (ex: países nórdicos, países
  balcânicos, países do G7), liste SEMPRE os membros do grupo
  em coluna própria ou em nota abaixo da tabela. Se os membros
  não estiverem no material, gere alerta na Seção 8.

Tipos de tabela esperados em Geografia do 9º ano:
- Países com área, população, capital, IDH, PIB
- Regiões com características físicas e humanas + países membros
- Indicadores socioeconômicos comparativos
- Dados climáticos (temperaturas, precipitação por região)
- Fusos horários e coordenadas geográficas

---

### SEÇÃO 7 — DICAS DE OURO

4–6 dicas inferidas do conteúdo. Foco em: pegadinhas de prova,
confusões de localização, erros de leitura de mapa, dados
frequentemente invertidos.

Temas prioritários para Geografia:
- Confusão entre países limítrofes
- Inversão de dados (PIB vs. IDH, área vs. população)
- Leitura incorreta de legenda de mapa
- Confusão entre processos opostos (urbanização vs. êxodo rural)
- Coordenadas e hemisférios
- Escalas cartográficas

```
💡 **Dica [N] — [título curto]**
[explicação com exemplo geográfico concreto]
```

---

### SEÇÃO 8 — ALERTAS DE INCONSISTÊNCIA [CONDICIONAL]
**ARQUIVO DE GAPS — gerar quando houver inferências ou ausências:**

Formato do arquivo `[mat]-[u]-[c]-gaps.md`:

```markdown
# GAPS — [mat]-[u]-[c]
# Gerado automaticamente pelo Prompt de Preparação

## INFERÊNCIAS USADAS NO PREP
Dados não capturados no material mas inferidos com conhecimento
geral. Verificar com o material original antes de disponibilizar
ao aluno.

| Seção | Campo | Valor inferido | Fonte da inferência |
|-------|-------|---------------|---------------------|
| [seção] | [campo] | [valor usado no prep] | [base da inferência] |

## DADOS AUSENTES — AÇÃO NECESSÁRIA
Dados que não puderam ser inferidos. Adicionar ao material
antes de disponibilizar o prep ao aluno.

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| [seção] | [campo] | [motivo] | [ação concreta] |
```



Gerar se detectar erros factuais no material capturado.
Em Geografia: verificar dados desatualizados (população, PIB,
fronteiras), capitais incorretas, coordenadas erradas.

```
⚠️ ALERTA — [país, região ou dado]
- Dado no material: "[texto exato do arquivo .md]"
- Problema: [descrição do erro ou desatualização]
- Dado correto: [informação atualizada]
- Impacto na aula: [o que o Professor deve fazer]
```

---

### SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

```
- **[Conceito]**
  - Definição: `______` ([resposta esperada])
  - Exemplo: `______` ([país ou região do material])
```

#### Bloco 2 — Dados e Localizações [se houver]

```
- **[País ou região]**
  - Capital: `______` ([resposta])
  - Dado principal: `______` ([valor + unidade])
```

#### Bloco 3 — Lacunas para Warm-Up

6–8 lacunas cobrindo obrigatoriamente:
- Pelo menos 1 por conceito principal do resumo (Seção 2)
- Pelo menos 1 por **categoria/tipo** das tabelas da Seção 6
- Pelo menos 1 de localização ou dado geográfico específico
- Pelo menos 1 baseada na Síntese do livro (se imagem fornecida)
- Pelo menos 1 de aplicação contextual (situação geográfica real)

REGRA CRÍTICA — lacunas:
- Gere lacuna APENAS para termos e dados explicitamente presentes
  no material capturado. Nunca crie lacuna cuja resposta exige
  inferência ou conhecimento externo ao material.
- Se um grupo é citado (ex: "países nórdicos"), a lacuna pode
  pedir o NOME do grupo — mas nunca pedir seus membros se eles
  não foram listados no material capturado.

```
N. [enunciado com `______` marcando a lacuna]
*(resposta: [resposta esperada])*
```

---

### SEÇÃO 10 — SÍNTESE DO LIVRO [CONDICIONAL]

**Só gerada se imagem da Síntese for anexada.**

```
### Síntese do Livro — [TEMA CENTRAL]

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| [posição no esquema] | [texto dado] | [resposta] |
```

Se não houver imagem: escreva
"Seção 10 não gerada — anexe a imagem da Síntese para incluir."

---

### SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

**Fonte exclusiva:** `geo-[u]-[c]-questoes.md`
Se não disponível: "Seção 11 não gerada — adicione o arquivo ao KB."

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Gabarito | Obs. |
|---|---|---|---|---|---|
| Q-N | [1 linha] | [MC/Dis/Mapa/VF/Assoc] | [F/M/D] | [resposta + justificativa] | [— ou ⚠️] |

Legenda: MC = múltipla escolha · Dis = dissertativa ·
Mapa = análise de mapa · VF = V-F · Assoc = associação

Regras:
- Infira gabaritos usando o conteúdo do `.md`
- Para questões de mapa: indique o que se observa no mapa
  que leva à resposta correta
- Marque ⚠️ para: dado desatualizado, mapa não capturado,
  enunciado ambíguo, erro já registrado na Seção 8

#### Bloco B — Questões modelo originais

5 questões originais inspiradas no estilo do `questoes.md`.
NÃO copiar nem parafrasear — criar contextos novos.

Distribuição:
- 2 múltipla escolha (médio)
- 1 dissertativa (médio)
- 1 análise de mapa ou gráfico estilo concurso (difícil)
- 1 localização ou dado geográfico (médio-difícil)

```
**QM-[N]** · [tipo] · [dificuldade] · inspirada em: [Q-N]

[enunciado completo]

a) [alt]  b) [alt]  c) [alt]  d) [alt]

✅ Gabarito: [letra ou resposta]
📝 Resolução: [desenvolvimento ou justificativa]
⚠️ Professor: referência de estilo — crie variações originais.
```

---

### SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

Os SVGs ficam embutidos no próprio prep.md.
**Nota:** mapas geográficos reais NÃO são gerados como SVG —
use image_search na aula (Seção 4). SVGs são para hierarquias,
fluxos e esquemas conceituais.

**Formato de cada diagrama:**
```
### DIAGRAMA: [nome]
[descrição em 1 linha]
<svg width="100%" viewBox="0 0 680 H">...</svg>
```

**Regras obrigatórias:** width="100%", viewBox="0 0 680 H",
classes c-purple/c-teal/c-amber/c-coral/c-gray/c-green,
text classes t/ts/th, sem gradientes, sem emojis,
dark mode automático, incluir defs com marker de seta.

**Regras anti-sobreposição — verificar ANTES de posicionar cada elemento:**

Regra 1 — Packing de caixas numa mesma linha:
  `soma(larguras) + (n-1) × gap ≥ espaço_disponível → ERRO`
  Calcule explicitamente antes de atribuir coordenadas x.
  Espaço disponível = x_final − x_inicial (ex: x=40 a x=640 = 600px).
  Gap mínimo entre caixas: 8px.

Regra 2 — Texto dentro da caixa:
  `caracteres_do_texto_mais_longo × 7 + 24 ≤ largura_da_caixa`
  Se não couber: distribuir o texto em 2 linhas com palavras inteiras.
  NUNCA quebrar uma palavra no meio para forçá-la a caber.

Regra 3 — Altura mínima por número de linhas de conteúdo:
  1 linha de conteúdo → h = 44px
  2 linhas de conteúdo → h = 58px
  3 linhas de conteúdo → h = 72px
  Usar `dominant-baseline="central"` em todos os `<text>`.
  Linha 1: y = topo_caixa + 20px · Linha 2: y = topo_caixa + 38px · Linha 3: y = topo_caixa + 56px

Regra 4 — viewBox height:
  Calcular y_máximo = borda inferior do elemento mais baixo.
  Definir H = y_máximo + 40.
  Nunca fixar H sem verificar o elemento mais baixo.

**Por perfil do capítulo:**

**Descritivo-espacial → DIAGRAMA: hierarquia_[tema]**
Hierarquia regional ou de classificação geográfica.
Ex: continentes → países → regiões · tipos de clima →
subtipos → exemplos de localização.
Nó raiz (c-green) → níveis intermediários (c-teal) →
exemplos (c-gray).
NÃO usar SVG para tabelas de dados — usar markdown na Seção 6.
NÃO usar SVG para mapas — usar image_search na Seção 4.

**Analítico-temático → DIAGRAMA: fluxo_[processo]**
Fluxo de processo geográfico ou relação de causa-consequência.
Ex: industrialização → urbanização → metropolização.
Causas (c-teal) → processo (c-green) → consequências (c-amber)
→ problemas (c-coral).

**Histórico-geográfico → DIAGRAMA: timeline**
Linha do tempo de eventos ou transformações territoriais.
Eixo horizontal = tempo, nós coloridos por período/relevância.

**Misto → gerar os diagramas de todos os perfis presentes.**

---

## EXECUÇÃO

1. Leia `geo-[u]-[c].md` e `geo-[u]-[c]-questoes.md` inteiros
2. Verifique se imagem da Síntese foi anexada:
   - ✅ Sim: gere todas as seções incluindo a 10
   - ⬜ Não: gere seções 0–9, 11, 12; indique que Seção 10
     pode ser adicionada depois com a imagem
3. Gere Seções 1–11 (conteúdo textual)
4. Gere Seção 12 (SVGs embutidos no prep)
5. Gere Seção 0 (índice) e posicione no início do arquivo
6. Salve em `/mnt/user-data/outputs/geo-[u]-[c]-prep.md`
7. Apresente com `present_files`
8. Gere o Mapa Mental HTML (ver seção abaixo)
9. Salve em `/mnt/user-data/outputs/mindmap_geo[u][c].html`
10. Apresente com `present_files`
11. Informe:
    "✅ Preparação concluída!
    - `geo-[u]-[c]-prep.md` → adicionar ao knowledge base
    - `mindmap_geo[u][c].html` → adicionar ao knowledge base"

---

## GERAÇÃO DO MAPA MENTAL HTML

Arquivo HTML com mapa mental completo. Todos os cards iniciam
em verde escuro "Não testado".

**a) HEADER** — fundo #2D6A4F:
- "Geografia · Unidade X · Capítulo Y · 9º ano"
- Título do capítulo (32px bold)
- "Mapa Mental — gerado na preparação"
- Legenda: verde=Dominado · vermelho=Reforçar · verde escuro=Não testado

**b) PÍLULA CENTRAL** — tema, fundo #2D6A4F

**c) GRID DE CARDS** — um por tópico, todos verde escuro:
- Faixa lateral 3px · número em círculo · título em negrito
- Bullets com conteúdo · badge "Não testado"
- Para dados geográficos: tabela compacta com valores
- Para mapas: indicação do mapa e termos de busca

**d) DICAS DE OURO** — fundo #F0FAF4, borda #2D6A4F,
dicas da Seção 7, badge verde escuro numerado

**CSS obrigatório:**
- Fonte: 'Inter' (Google Fonts) · Fundo: #F4F2EE
- Cards: bg #ffffff · border-radius 14px ·
  box-shadow 0 2px 8px rgba(0,0,0,0.07)
- Grid: 3 colunas · font-size mínimo 13px · header 32px bold
- Cor primária: #2D6A4F (verde escuro de Geografia)
