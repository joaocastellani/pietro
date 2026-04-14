# PROMPT DE PREPARAÇÃO — HISTÓRIA (9º ano)

Arquivos de entrada: `his-[u]-[c].md` + `his-[u]-[c]-questoes.md`
Arquivo gerado:      `his-[u]-[c]-prep.md`
Mapa mental gerado:  `mindmap_his[u][c].html`

---

## INSTRUÇÕES GERAIS

1. Use `project_knowledge_search` para localizar e ler
   `his-[u]-[c].md` e `his-[u]-[c]-questoes.md` inteiros
   antes de gerar qualquer conteúdo
2. Todo o conteúdo é gerado de uma vez, sem interação com o aluno
3. Preserve datas, nomes de personagens e países exatamente
   como aparecem no material capturado
4. Você pode inferir dicas e pegadinhas — não precisa citar o livro
5. Se detectar inconsistência factual, registre na Seção 8
6. Os SVGs da Seção 12 ficam embutidos no próprio `prep.md`

---

## PERFIS DE CAPÍTULO

História no 9º ano tem quatro perfis:

| Perfil | Características | Exemplos |
|--------|----------------|---------|
| Histórico-conceitual | Conceitos, teorias e correntes de pensamento histórico | Iluminismo, Liberalismo, Socialismo |
| Histórico-narrativo | Sequência de eventos, personagens e transformações | Revolução Francesa, I Guerra Mundial |
| Analítico-temático | Processos, estruturas e relações de longa duração | Imperialismo, Industrialização, Globalização |
| Misto | Combinação dos perfis acima | — |

---

## ESTRUTURA DO ARQUIVO DE PREPARAÇÃO

Gere nesta ordem. Seções [CONDICIONAL] só se o conteúdo existir.

---

### SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

**Gerada por último**, após a Seção 12 estar completa.

```
## DIAGRAMAS DISPONÍVEIS — his-[u]-[c]

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| [nome] | DIAGRAMA: [nome] | [contexto de uso] |

### Tabelas markdown (Seção 6):
- [lista das tabelas presentes]

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.
Se o usuário anexar printscreens de mapas históricos da apostila,
use-os diretamente em vez de fazer image_search.
```

---

### SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — HISTÓRIA
- Unidade:
- Capítulo:
- Tema:
- Perfil: [histórico-conceitual / histórico-narrativo /
           analítico-temático / misto]
- Período histórico: [ex: séc. XIX / Entreguerras / Guerra Fria]
- Personagens principais: [lista ou "nenhum"]
- Processos principais: [lista ou "nenhum"]
```

---

### SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

Resumo narrativo organizado por blocos temáticos.
Cada bloco: título em negrito + explicação nível 9º ano +
conexão com exemplos históricos reais do material.

Para blocos narrativos: apresente os eventos em ordem
cronológica, destacando causas, personagens e consequências.

Para blocos analítico-temáticos: apresente o processo com
suas etapas, seus agentes históricos e suas consequências
estruturais.

Para blocos conceituais: apresente a ideia, sua origem
histórica e seus defensores principais.

---

### SEÇÃO 3 — PERSONAGENS E PENSADORES [CONDICIONAL]

Gerar se o capítulo citar personagens ou intelectuais com
papel relevante na narrativa histórica.

Para cada personagem:
```
### [Nome completo] ([período ou datas — se citadas])
**Origem:** [país ou região]
**Papel histórico:** [o que o material descreve]
**Ações ou decisões relevantes:** [conforme o material]
**Associado a:** [evento, movimento ou obra — se citado]
💡 **Pegadinha:** [confusão mais comum sobre este personagem]
```

---

### SEÇÃO 4 — CRONOLOGIA DO CAPÍTULO [CONDICIONAL]

Gerar se o capítulo apresentar sequência de eventos datados.

```
| Data | Evento | Local | Consequência imediata |
|------|--------|-------|----------------------|
| [data] | [evento] | [país/região] | [consequência] |
```

Regras:
- Preserve datas exatas conforme o material
- Se o material citar apenas décadas ou séculos, use esse nível
- Inclua todos os eventos mencionados no material — não filtre

---

### SEÇÃO 5 — CAUSAS E CONSEQUÊNCIAS [CONDICIONAL]

Gerar se o capítulo apresentar análise de processos históricos
com causas e consequências identificáveis.

Para cada processo:
```
### [Nome do processo ou evento]
**Causas estruturais:** [fatores de longa duração]
**Causas imediatas:** [fatores precipitantes]
**Desenvolvimento:** [como ocorreu — etapas se aplicável]
**Consequências de curto prazo:** [efeitos imediatos]
**Consequências de longo prazo:** [transformações duradouras]
**Países/regiões afetados:** [com dados quando citados]
💡 **Pegadinha:** [confusão mais comum sobre este processo]
```

---

### SEÇÃO 6 — DADOS HISTÓRICOS DENSOS [CONDICIONAL]

Gerar se o capítulo apresentar conjuntos de dados estruturados.
Usar **tabelas markdown** — não SVG para dados tabulares.
Adicionar coluna "⚠️ Pegadinha" quando relevante.

REGRAS CRÍTICAS para tabelas:
- Se um dado não foi capturado no material, NÃO deixe célula
  vazia sem explicação. Em vez disso:
  1. Gere um alerta na SEÇÃO 8 com o formato:
     ⚠️ DADO AUSENTE — [tabela/campo]
     Campo: [qual célula está incompleta]
     Motivo: [não capturado / imagem não processada]
     Ação: adicionar ao arquivo his-[u]-[c].md e reprocessar
  2. Na tabela, marque a célula com "⚠️ ver Seção 8"
- Célula com dado inferido → marcar "⚠️ inferido" +
  registrar no gaps.md

Tipos de tabela esperados em História do 9º ano:
- Cronologias comparativas (eventos por país/período)
- Causas vs. consequências de eventos
- Comparação de regimes políticos ou sistemas econômicos
- Líderes e seus países/períodos
- Tratados e acordos com partes e termos principais

---

### SEÇÃO 7 — DICAS DE OURO

4–6 dicas inferidas do conteúdo. Foco em: pegadinhas de prova,
confusões de data, inversões de causa/consequência, personagens
com papéis parecidos, eventos com nomes similares.

Temas prioritários para História:
- Confusão entre eventos cronologicamente próximos
- Inversão de causas e consequências
- Confusão entre personagens com papéis semelhantes
- Datas e tratados frequentemente trocados
- Confusão entre movimentos ideológicos (liberalismo vs.
  socialismo, fascismo vs. nazismo, etc.)
- Distinção entre guerras, revoluções e golpes de Estado

```
💡 **Dica [N] — [título curto]**
[explicação com exemplo histórico concreto]
```

---

### SEÇÃO 8 — ALERTAS DE INCONSISTÊNCIA [CONDICIONAL]

**ARQUIVO DE GAPS — gerar quando houver inferências ou ausências:**

Formato do arquivo `his-[u]-[c]-gaps.md`:

```markdown
# GAPS — his-[u]-[c]
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
|-------|-------|-------------------|--------------------|
| [seção] | [campo] | [motivo] | [ação concreta] |
```

Gerar também para inconsistências factuais:
```
⚠️ ALERTA — [evento, personagem ou dado]
- Dado no material: "[texto exato do arquivo .md]"
- Problema: [descrição do erro ou imprecisão]
- Dado correto: [informação correta]
- Impacto na aula: [o que o Professor deve fazer]
```

**Fragmentos truncados — verificar no material capturado:**
Se o `.md` contiver texto interrompido no meio de uma frase
(ex: "formação dos ;", "como resultado da —", texto que termina
sem completar o sentido), gerar alerta:
```
⚠️ FRAGMENTO TRUNCADO — [seção/bloco do .md]
- Texto: "[trecho exato como aparece no arquivo]"
- Problema: texto interrompido — conteúdo ausente
- Ação: reler o material original e completar a captura
  antes de disponibilizar o prep ao aluno
```
NÃO inferir o conteúdo ausente de fragmentos truncados —
registrar o alerta e deixar a célula/campo como "⚠️ ver Seção 8".

---

### SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

```
- **[Conceito]**
  - Definição: `______` ([resposta esperada])
  - Exemplo histórico: `______` ([evento ou personagem do material])
```

#### Bloco 2 — Cronologia e Personagens [se houver]

```
- **[Evento]**
  - Data: `______` ([resposta])
  - Local: `______` ([país ou região])
  - Consequência principal: `______` ([resposta])
```

#### Bloco 3 — Lacunas para Warm-Up

6–8 lacunas cobrindo obrigatoriamente:
- Pelo menos 1 por conceito principal do resumo (Seção 2)
- Pelo menos 1 de data ou personagem (Seção 4 ou Seção 3)
- Pelo menos 1 de causa ou consequência (Seção 5)
- Pelo menos 1 por categoria das tabelas da Seção 6
- Pelo menos 1 de aplicação contextual (situação histórica real)

REGRA CRÍTICA — lacunas:
- Gere lacuna APENAS para termos e dados explicitamente presentes
  no material capturado. Nunca crie lacuna cuja resposta exige
  inferência ou conhecimento externo ao material.

```
N. [enunciado com `______` marcando a lacuna]
*(resposta: [resposta esperada])*
```

#### Bloco 4 — Tabela Síntese

Tabela markdown obrigatória (6–10 linhas). Cobre conceitos
principais, fórmulas-chave, pelo menos 1 aplicação prática e
1 pegadinha/alerta. Formato exato:

```
| Conceito | Lacuna — resposta esperada |
|---|---|
| [conceito 1] | `______` → *[resposta]* |
| [conceito 2] | `______` → *[resposta]* |
| [fórmula ou dado] | `______` → *[resposta]* |
| [aplicação prática] | `______` → *[resposta]* |
| [pegadinha ou alerta] | `______` → *[resposta]* |
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

**Fontes:**
- `his-[u]-[c]-questoes.md` → Bloco Atividades (Origem: AT)
- BLOCO G (QI-N) do `his-[u]-[c].md` → Questões Intercaladas (Origem: IC)

Se `questoes.md` não disponível: "Seção 11 parcial — apenas questões intercaladas."
Se não disponível: "Seção 11 não gerada — adicione o arquivo ao KB."

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| Q-N | [1 linha] | [MC/Dis/Fonte/Mapa/VF/Assoc/Cron] | [F/M/D] | [resposta + justificativa] | [— ou ⚠️] |

Legenda: MC = múltipla escolha · Dis = dissertativa ·
Fonte = análise de fonte primária · Mapa = análise de mapa ·
VF = V-F · Assoc = associação · Cron = cronologia

Regras:
- Infira gabaritos usando o conteúdo do `.md`
- Para questões de fonte primária: indique o elemento do
  documento que leva à resposta correta
- Marque ⚠️ para: dado desatualizado, imagem não capturada,
  enunciado ambíguo, erro já registrado na Seção 8

#### Bloco B — Questões modelo originais

5 questões originais inspiradas no estilo do `questoes.md`.
NÃO copiar nem parafrasear — criar contextos novos.

Distribuição:
- 2 múltipla escolha (médio)
- 1 análise de fonte primária com trecho histórico (médio)
- 1 questão de causa-consequência (médio-difícil)
- 1 dissertativa aprofundada (difícil)

```
**QM-[N]** · [tipo] · [dificuldade] · inspirada em: [Q-N]

[enunciado completo]

a) [alt]  b) [alt]  c) [alt]  d) [alt]

✅ Gabarito: [letra ou resposta]
📝 Resolução: [desenvolvimento ou justificativa]
⚠️ Professor: referência de estilo — crie variações originais,
   nunca reproduza diretamente.
```

---

### SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

Os SVGs ficam embutidos no próprio prep.md.

**Formato de cada diagrama:**
```
### DIAGRAMA: [nome]
[descrição em 1 linha]

<svg width="100%" viewBox="0 0 680 H">
...código SVG completo...
</svg>
```

**Regras obrigatórias para todos os SVGs:**
- `width="100%"` e `viewBox="0 0 680 H"` — não alterar o 680
- Classes do Visualizer para nós: `c-purple`, `c-teal`, `c-amber`,
  `c-coral`, `c-gray`, `c-green`
- Classes de texto: `class="t"` (14px), `class="ts"` (12px),
  `class="th"` (14px bold)
- Alertas/pegadinhas: `c-coral`
- Sem gradientes, sem emojis, sem texto rotacionado
- Dark mode automático via classes — nunca hardcode hex para texto
- Incluir `<defs>` com marker de seta em cada SVG:
  ```
  <defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
  markerWidth="6" markerHeight="6" orient="auto-start-reverse">
  <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
  stroke-width="1.5" stroke-linecap="round"
  stroke-linejoin="round"/></marker></defs>
  ```
  ⚠️ OBRIGATÓRIO em todos os SVGs, mesmo nos que não usam setas.

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

**Histórico-conceitual → DIAGRAMA: mapa_conceitual_[tema]**
Mapa de conceitos e correntes de pensamento.
Conceito central (c-purple) → correntes ou desdobramentos
(c-teal) → pensadores ou exemplos históricos (c-gray).
Ex: Iluminismo → Liberalismo / Enciclopedismo / Separação de
poderes → Locke / Voltaire / Montesquieu.

**Histórico-narrativo → DIAGRAMA: timeline**
Linha do tempo dos eventos do capítulo.
Eixo horizontal = tempo. Nós alternados acima/abaixo.
Cores por relevância ou fase:
  c-purple (eventos políticos) ·
  c-teal (eventos econômicos/sociais) ·
  c-amber (acordos e tratados) ·
  c-coral (conflitos e crises)
Texto do nó: data + nome curto do evento (th).
Texto fora do nó: consequência principal (ts).

**Analítico-temático → DIAGRAMA: fluxo_[processo]**
Fluxo de processo histórico ou relação de causa-consequência.
Ex: acumulação de capital → industrialização → urbanização
→ questão social.
Causas (c-teal) → processo (c-green) → consequências (c-amber)
→ crises ou rupturas (c-coral).

**Misto → regra de priorização (não gerar tudo automaticamente)**
Avalie quantos elementos reais existem por perfil no material:
- Se um perfil tem ≥ 4 eventos/conceitos/processos → gerar seu diagrama
- Se um perfil tem < 4 elementos → incorporar no diagrama do perfil dominante
  como nós secundários, em vez de criar SVG separado ralo
- Máximo 2 SVGs por capítulo misto
- Perfil dominante = o que concentra mais conteúdo no material capturado

Exemplo: capítulo com 5 eventos datados (narrativo) + 2 conceitos (conceitual)
→ gerar timeline com os 5 eventos + incorporar os 2 conceitos como nós
  de contexto na timeline; NÃO gerar mapa_conceitual separado com 2 nós.

---

## EXECUÇÃO

1. Leia `his-[u]-[c].md` e `his-[u]-[c]-questoes.md` inteiros
2. Verifique se imagem da Síntese foi anexada:
   - ✅ Sim: gere todas as seções incluindo a 10
   - ⬜ Não: gere seções 0–9, 11, 12; indique que Seção 10
     pode ser adicionada depois com a imagem
3. Gere Seções 1–11 (conteúdo textual)
4. Gere Seção 12 (SVGs embutidos no prep)
5. Gere Seção 0 (índice) e posicione no início do arquivo
6. Salve em `/mnt/user-data/outputs/his-[u]-[c]-prep.md`
7. Apresente com `present_files`
8. Gere o Mapa Mental HTML (ver seção abaixo)
9. Salve em `/mnt/user-data/outputs/mindmap_his[u][c].html`
10. Apresente com `present_files`
11. Informe:
    "✅ Preparação concluída!
    - `his-[u]-[c]-prep.md` → adicionar ao knowledge base
    - `mindmap_his[u][c].html` → adicionar ao knowledge base"

---

## GERAÇÃO DO MAPA MENTAL HTML

Arquivo HTML com mapa mental completo. Todos os cards iniciam
em verde escuro "Não testado".

**a) HEADER** — fundo #3D1A24:
- "História · Unidade X · Capítulo Y · 9º ano"
- Título do capítulo (32px bold)
- "Mapa Mental — gerado na preparação"
- Legenda: verde=Dominado · vermelho=Reforçar · verde escuro=Não testado

**b) PÍLULA CENTRAL** — tema, fundo #3D1A24

**c) GRID DE CARDS** — um por tópico, todos cor primária:
- Faixa lateral 3px · número em círculo · título em negrito
- Bullets com conteúdo · badge "Não testado"
- Para cronologias: linha do tempo compacta com datas e eventos
- Para personagens: nome → papel histórico → evento associado
- Para causas/consequências: setas visuais → →
- Para conceitos: definição + exemplo histórico

**d) DICAS DE OURO** — fundo #FFF0F3, borda #3D1A24,
dicas da Seção 7, badge cor primária numerado

**CSS obrigatório:**
- Fonte: 'Inter' (Google Fonts) · Fundo: #F4F2EE
- Cards: bg #ffffff · border-radius 14px ·
  box-shadow 0 2px 8px rgba(0,0,0,0.07)
- Grid: 3 colunas · font-size mínimo 13px · header 32px bold
- Cor primária: #3D1A24 (bordô escuro de História)
