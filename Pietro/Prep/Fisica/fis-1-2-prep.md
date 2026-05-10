## DIAGRAMAS DISPONÍVEIS — fis-1-2

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Classificação das grandezas físicas | DIAGRAMA: classif_grandezas | Bloco "Grandezas Físicas" — Seção 2 |
| Grandezas fundamentais do SI | DIAGRAMA: si_fundamentais | Bloco "SI" — Seção 2 e Seção 5 |
| Notação científica — deslocamento da vírgula | DIAGRAMA: notacao_cientifica | Bloco "Notação Científica" — Seção 2 e C3 |
| Conversões de comprimento | DIAGRAMA: conversoes_comprimento | Bloco "Unidades de Comprimento" — Seção 5.2 |
| Conversões de massa | DIAGRAMA: conversoes_massa | Bloco "Unidades de Massa" — Seção 5.2 |
| Conversões de tempo | DIAGRAMA: conversoes_tempo | Bloco "Unidades de Tempo" — Seção 5.2 |

### Tabelas markdown (Seção 6):
- Tabela 1 — Grandezas Fundamentais do SI (7 grandezas)
- Tabela 2 — Grandezas Derivadas do SI (8 grandezas)
- Tabela 3 — Submúltiplos e Múltiplos do SI (12 prefixos)
- Tabela 4 — Unidades de Medida Corporais Históricas (4 unidades)

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer para renderizar inline.
Tabelas da Seção 6 são apresentadas como markdown no chat.
A Síntese do livro foi fornecida como imagem — Seção 10 gerada com base nela.

---

## SEÇÃO 1 — PERFIL DO CAPÍTULO

# PREPARAÇÃO DE AULA — FÍSICA
- **Unidade:** 1
- **Capítulo:** 2
- **Tema:** Grandezas Físicas
- **Perfil:** misto (descritivo-científico + matemático-operacional)
- **Fórmulas principais:** nenhuma (capítulo conceitual-operacional sem fórmulas algébricas)
- **Cientistas citados:** Galileu Galilei · Isaac Newton (unidade)

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### 🔷 Bloco 1 — O que é medir?
Medir é **comparar algo a um padrão**. Antes da padronização, o ser humano usava partes do próprio corpo como referência: polegada, pé, jarda e palmo. O problema é que essas medidas variavam de pessoa para pessoa. Com o desenvolvimento do comércio e da ciência, tornou-se necessário criar padrões universais — nascendo assim o **Sistema Internacional de Unidades (SI)**, criado em 1960 e obrigatório no Brasil desde 1988.

### 🔷 Bloco 2 — Grandezas Físicas
Toda **característica da matéria ou da energia que pode ser medida** é uma grandeza física. A medida é sempre expressa por um **número seguido de uma unidade**. Exemplos cotidianos: 20 L de água, 1 kg de café, 5 km de distância.

As grandezas físicas se dividem em dois tipos principais:
- **Fundamentais:** independentes, definidas diretamente — comprimento, massa, tempo, corrente elétrica, temperatura termodinâmica, quantidade de matéria e intensidade luminosa.
- **Derivadas:** dependem de grandezas fundamentais — velocidade (comprimento/tempo), volume (comprimento³), força, pressão etc.

### 🔷 Bloco 3 — Escalares vs. Vetoriais
Outra classificação importante:
- **Escalares:** definidas apenas por valor numérico + unidade. Ex.: temperatura (25 °C), massa (70 kg), comprimento (3 m).
- **Vetoriais:** exigem valor numérico + unidade + **direção** + **sentido**. Ex.: força (10 N para a direita), velocidade (60 km/h para o norte). São representadas por letras com seta: $$\vec{F}$$, $$\vec{v}$$.

⚠️ **Distinção importante:** Massa ≠ Peso. A **massa** é escalar (kg); o **peso** é vetorial — força gravitacional com unidade newton (N).

### 🔷 Bloco 4 — Sistema Internacional de Unidades (SI)
O SI define **7 grandezas fundamentais** com suas unidades-padrão:

| Grandeza | Unidade | Símbolo |
|---|---|---|
| Comprimento | metro | m |
| Massa | quilograma | kg |
| Tempo | segundo | s |
| Corrente elétrica | ampere | A |
| Temperatura termodinâmica | kelvin | K |
| Quantidade de matéria | mol | mol |
| Intensidade luminosa | candela | cd |

Atenção à grafia: símbolos derivados de nomes próprios são escritos em **maiúscula** (N, J, W, A, K), mas o **nome da unidade** é escrito em **minúscula** (newton, joule, watt).

Além disso, o SI usa **prefixos** para múltiplos e submúltiplos: de pico (10⁻¹²) a tera (10¹²).

### 🔷 Bloco 5 — Conversões de Unidades
As conversões mais cobradas do capítulo:

**Comprimento:** 1 km = 1 000 m · 1 m = 10 dm · 1 m = 100 cm · 1 m = 1 000 mm

**Massa:** 1 t = 1 000 kg · 1 kg = 1 000 g · 1 g = 1 000 mg

**Tempo:** 1 min = 60 s · 1 h = 3 600 s · 1 dia = 86 400 s

### 🔷 Bloco 6 — Notação Científica e Ordem de Grandeza
Para números muito grandes ou muito pequenos, usamos a **notação científica**:
$$a \times 10^n, \quad \text{onde } 1 \leq a < 10 \text{ e } n \in \mathbb{Z}$$

Regra do deslocamento da vírgula:
- Número **> 10** → vírgula vai para a **esquerda** → **n positivo**
- Número **< 1** → vírgula vai para a **direita** → **n negativo**

Exemplos do livro:
- $$9{,}460{,}800{,}000{,}000{,}000 \text{ m} \rightarrow 9{,}4608 \times 10^{15} \text{ m}$$
- $$0{,}000\,000\,000\,000\,000\,000\,16 \text{ A·s} \rightarrow 1{,}6 \times 10^{-19} \text{ A·s}$$

**Ordem de grandeza:** potência de base 10 mais próxima.
- Se $$a \geq 3{,}16$$ → ordem = $$10^{n+1}$$
- Se $$a < 3{,}16$$ → ordem = $$10^{n}$$
- Exemplo: $$5{,}97 \times 10^{24}$$ kg → como 5,97 > 3,16 → ordem = $$10^{25}$$ kg

### 🔷 Bloco 7 — Grandezas Adimensionais
Quando uma grandeza resulta da **razão entre duas grandezas de mesma unidade**, as unidades se cancelam e o resultado fica **sem unidade**. Exemplos: coeficiente de atrito e índice de refração. Essas grandezas são chamadas de **adimensionais**.

---

## SEÇÃO 3 — CIENTISTAS E HISTÓRIA DA CIÊNCIA

### Galileu Galilei (1564–1642)
**Área:** Física / Astronomia
**Contribuição no capítulo:** Percebeu que o tempo de oscilação de um pêndulo (ida e volta) é constante. Dessa observação surgiu o primeiro método de medição para pequenos intervalos de tempo, como minutos e segundos.
**O que mudou:** Inaugurou a medição precisa de intervalos de tempo com base em fenômenos periódicos regulares.
**Associado a:** Pêndulo como instrumento de medição de tempo.
**Contexto histórico:** Revolução Científica do século XVII.

### Isaac Newton (1643–1727)
**Área:** Física / Matemática
**Contribuição no capítulo:** Citado como referência para a regra de grafia dos símbolos de unidades: o símbolo N (newton, unidade de força) é escrito em maiúscula por derivar do nome do cientista; o nome da unidade, porém, é escrito em minúscula.
**Associado a:** Unidade SI de força: newton (N).

---

## SEÇÃO 5 — GRANDEZAS E SISTEMA INTERNACIONAL

#### 5.1 — Grandezas do capítulo

| Grandeza | Símbolo | Unidade SI | Símbolo | Tipo |
|---|---|---|---|---|
| Comprimento | — | metro | m | fundamental / escalar |
| Massa | — | quilograma | kg | fundamental / escalar |
| Tempo | — | segundo | s | fundamental / escalar |
| Corrente elétrica | — | ampere | A | fundamental / escalar |
| Temperatura termodinâmica | — | kelvin | K | fundamental / escalar |
| Quantidade de matéria | — | mol | mol | fundamental / escalar |
| Intensidade luminosa | — | candela | cd | fundamental / escalar |
| Velocidade | v⃗ | metro por segundo | m/s | derivada / vetorial |
| Volume | — | metro cúbico | m³ | derivada / escalar |
| Área | — | metro quadrado | m² | derivada / escalar |
| Pressão | — | pascal | Pa | derivada / escalar |
| Força | F⃗ | newton | N | derivada / vetorial |
| Energia | — | joule | J | derivada / escalar |
| Potência | — | watt | W | derivada / escalar |
| Tensão elétrica | — | volt | V | derivada / escalar |

#### 5.2 — Conversões importantes

```
Comprimento: km → m → dm → cm → mm
  1 km = 1 000 m
  1 m  = 10 dm
  1 m  = 100 cm
  1 m  = 1 000 mm
  Exemplo: 2 km = 2 000 m = 2 000 000 mm
  ⚠️ Pegadinha: confundir dm com cm — lembre: 1 m = 10 dm (não 100).

Massa: t → kg → g → mg
  1 t  = 1 000 kg
  1 kg = 1 000 g
  1 g  = 1 000 mg
  Exemplo: 132,4 kg = 132 400 g · 5 300 mg = 5,3 g
  ⚠️ Pegadinha: 1 t ≠ 100 kg. 1 tonelada = 1 000 kg.

Tempo: dias → h → min → s
  1 dia = 24 h
  1 h   = 60 min = 3 600 s
  1 dia = 1 440 min = 86 400 s
  Exemplo: 45 dias = 45 × 24 = 1 080 h
  ⚠️ Pegadinha: não multiplicar dias direto por 3 600 — precisa passar por horas primeiro.
```

#### 5.3 — Notação científica

- **Regra:** $$a \times 10^n$$, onde $$1 \leq a < 10$$ e $$n \in \mathbb{Z}$$
- **Deslocamento da vírgula:**
  - Número > 10 → vírgula para esquerda → n **positivo**
  - Número < 1  → vírgula para direita  → n **negativo**
- **Exemplos do capítulo:**
  - $$9\,460\,800\,000\,000\,000 \text{ m} = 9{,}4608 \times 10^{15} \text{ m}$$ (vírgula desloca 15 casas para esquerda)
  - $$0{,}000\,000\,000\,000\,000\,000\,16 \text{ A·s} = 1{,}6 \times 10^{-19} \text{ A·s}$$ (vírgula desloca 19 casas para direita)
  - $$5\,970\,000\,000\,000\,000\,000\,000\,000 \text{ kg} = 5{,}97 \times 10^{24} \text{ kg}$$ (massa da Terra)
- **Erro clássico:** confundir a direção do deslocamento com o sinal do expoente. Regra mnemônica: **"grande número → expoente grande (positivo)"**.

---

## SEÇÃO 6 — DADOS FACTUAIS DENSOS

### Tabela 1 — Grandezas Fundamentais do SI

| Grandeza fundamental | Unidade de medida | Símbolo da unidade |
|---|---|---|
| Comprimento | metro | m |
| Massa | quilograma | kg |
| Tempo | segundo | s |
| Intensidade de corrente elétrica | ampere | A |
| Temperatura termodinâmica | kelvin | K |
| Quantidade de matéria | mol | mol |
| Intensidade luminosa | candela | cd |

### Tabela 2 — Grandezas Derivadas do SI

| Grandeza derivada | Unidade de medida | Símbolo da unidade |
|---|---|---|
| Velocidade | metros por segundo | m/s |
| Volume | metro cúbico | m³ |
| Área | metro quadrado | m² |
| Pressão | pascal | Pa |
| Força | newton | N |
| Energia | joule | J |
| Potência | watt | W |
| Tensão elétrica | volt | V |

### Tabela 3 — Submúltiplos e Múltiplos do SI

| Fator | Prefixo | Símbolo | Fator | Prefixo | Símbolo |
|---|---|---|---|---|---|
| 10⁻¹² | pico | p | 10¹ | deca | da |
| 10⁻⁹ | nano | n | 10² | hecto | h |
| 10⁻⁶ | micro | μ | 10³ | quilo | k |
| 10⁻³ | mili | m | 10⁶ | mega | M |
| 10⁻² | centi | c | 10⁹ | giga | G |
| 10⁻¹ | deci | d | 10¹² | tera | T |

### Tabela 4 — Unidades de Medida Corporais Históricas

| Unidade | Definição |
|---|---|
| 1 polegada | Medida da base da primeira falange até a ponta da unha do dedo polegar |
| 1 pé | Medida da planta do pé, desde o calcanhar até a ponta do dedo maior |
| 1 jarda | Com o braço esticado lateralmente, da ponta do nariz até a ponta do dedo médio |
| 1 palmo | Medida da palma da mão aberta, da ponta do polegar até a ponta do dedo mínimo |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Símbolo em maiúscula ≠ nome em maiúscula**
Unidades derivadas de nomes próprios têm **símbolo em maiúscula** (N, J, W, A, K), mas o **nome da unidade é escrito em minúscula** (newton, joule, watt, ampere, kelvin). Prova clássica: "A unidade de força no SI é o Newton" — **errado**. O correto é "newton".

💡 **Dica 2 — Massa é escalar; peso é vetorial**
Massa (kg) mede a quantidade de matéria — não muda com a localização. Peso (N) é uma força gravitacional — vetorial, muda conforme o campo gravitacional. Na Lua, seu peso diminui; sua massa permanece igual.

💡 **Dica 3 — Grandeza adimensional não significa "sem física"**
Coeficiente de atrito e índice de refração não têm unidade porque resultam de razões entre grandezas de mesma dimensão — as unidades se cancelam. Isso **não** significa que são menos importantes ou que não podem ser medidos.

💡 **Dica 4 — Notação científica: o "a" deve ser ≥ 1 e < 10**
Erro clássico: escrever 94,608 × 10¹⁴ em vez de 9,4608 × 10¹⁵. O valor de "a" **nunca** pode ser maior ou igual a 10, nem menor que 1. Se errar o "a", o expoente também fica errado.

💡 **Dica 5 — Ordem de grandeza: o corte é em √10 ≈ 3,16**
Esse valor não é arbitrário: é a raiz quadrada de 10, que representa o ponto médio entre 10⁰ e 10¹ em escala logarítmica. Se a ≥ 3,16 → arredonda para cima (10ⁿ⁺¹); se a < 3,16 → mantém (10ⁿ).

💡 **Dica 6 — dm é frequentemente esquecido nas conversões**
Na cadeia km → m → **dm** → cm → mm, o decímetro (dm) aparece pouco no cotidiano mas cai em provas de conversão: **1 m = 10 dm** (não 100 dm). Confundir dm com cm é o erro mais comum.

---

## SEÇÃO 8 — ALERTAS DE INCONSISTÊNCIA

```
# GAPS — fis-1-2
# Gerado automaticamente pelo Prompt de Preparação

## INFERÊNCIAS USADAS NO PREP

| Seção | Campo | Valor inferido | Fonte da inferência |
|-------|-------|---------------|---------------------|
| Seção 5.2 | 1 m = 10 dm | Não constava no fis-1-2.md; foi capturado nas imagens fornecidas ("1 m = 10 dm") | Imagem da apostila anexada |
| Seção 3 / Galileu | Datas de vida (1564–1642) | Constam no fis-1-1.md do mesmo projeto | Arquivo fis-1-1.md |

## DADOS AUSENTES — AÇÃO NECESSÁRIA

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| Seção 11 / todas as Q e QC | Gabaritos | Não fornecidos no material | Verificar gabaritos no livro do professor |
| Seção 6 / Tabela 4 | Ilustrações das unidades corporais | Imagens com figuras humanas — não reconstituíveis em texto | Usar imagem da apostila diretamente na aula |
```

⚠️ **DADO ATUALIZADO — Conversões de comprimento**
- Dado no fis-1-2.md: `1 m = 1 000 000 μm` e lista sem dm
- Dado nas imagens fornecidas: `1 km = 1 000 m · 1 m = 10 dm · 1 m = 100 cm · 1 m = 1 000 mm`
- **Ação:** o decímetro (dm) consta nas imagens do livro mas não foi capturado no fis-1-2.md. O prep usa a versão das imagens, que é mais completa. Recomenda-se atualizar o fis-1-2.md adicionando `1 m = 10 dm` às equivalências de comprimento.

⚠️ **VISUAL AUSENTE — Termômetro infravermelho**
- O texto menciona o termômetro infravermelho e seu funcionamento (medição por radiação infravermelha)
- Sugestão: image_search "termômetro infravermelho funcionamento radiação"
- Ação: usar image_search na aula para contextualizar o instrumento de medição

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

- **Grandeza Física**
  - Definição: `______` → *(Toda característica da matéria e da energia que pode ser medida)*
  - Exemplo: `______` → *(20 litros de água / 1 kg de café / 5 km de distância)*

- **Grandezas Fundamentais**
  - Definição: `______` → *(Grandezas independentes que podem ser definidas diretamente e formam as bases para outras grandezas)*
  - Quantidade no SI: `______` → *(7 grandezas)*

- **Grandezas Derivadas**
  - Definição: `______` → *(Definidas com base em relações entre as grandezas fundamentais)*
  - Exemplo: velocidade deriva de `______` → *(comprimento e tempo)*

- **Grandezas Escalares**
  - Definição: `______` → *(Representadas somente pelo valor numérico e sua unidade; não precisam de direção ou sentido)*

- **Grandezas Vetoriais**
  - Definição: `______` → *(Representadas pela intensidade, unidade correspondente, direção e sentido)*
  - Exemplo: `______` → *(Força, velocidade)*

- **Notação Científica**
  - Forma: `______` → *(a × 10ⁿ, onde 1 ≤ a < 10)*
  - Número grande → vírgula para `______` → expoente `______` → *(esquerda / positivo)*

- **Ordem de Grandeza**
  - Corte: se a ≥ `______` → ordem = 10ⁿ⁺¹ → *(3,16)*

- **Grandeza Adimensional**
  - O que é: `______` → *(Grandeza sem unidade; resulta da razão entre grandezas de mesma dimensão)*
  - Exemplos: `______` → *(Coeficiente de atrito e índice de refração)*

---

#### Bloco 2 — Fórmulas
*(Capítulo não apresenta fórmulas algébricas — bloco omitido)*

---

#### Bloco 3 — Lacunas para Warm-Up

1. Medir uma grandeza física é compará-la a uma `______`, verificando quantas vezes essa grandeza contém essa referência.
*(resposta: unidade de medida adotada como padrão)*

2. As grandezas `______` são independentes e formam as bases para outras grandezas físicas, como o comprimento, a massa e o tempo.
*(resposta: fundamentais)*

3. A velocidade é um exemplo de grandeza `______`, pois deriva das grandezas comprimento e tempo.
*(resposta: derivada)*

4. Uma grandeza `______` é definida apenas por seu valor numérico e sua unidade, como a temperatura e a massa.
*(resposta: escalar)*

5. Uma grandeza `______` exige, além do valor numérico e da unidade, a definição de sua direção e seu sentido.
*(resposta: vetorial)*

6. O Sistema Internacional de Unidades foi criado em `______` e adotado pelo Brasil em `______`, tornando-se obrigatório em `______`.
*(resposta: 1960 / 1962 / 1988)*

7. Na notação científica, o número 9 460 800 000 000 000 m é escrito como `______`.
*(resposta: 9,4608 × 10¹⁵ m)*

8. A massa da Terra é 5,97 × 10²⁴ kg. Como 5,97 `______` 3,16, a ordem de grandeza é `______`.
*(resposta: > / 10²⁵ kg)*

---

#### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Definição de grandeza física | `______` → *Característica da matéria/energia que pode ser medida* |
| Grandeza fundamental vs. derivada | `______` → *Fundamental: independente · Derivada: combinação de fundamentais* |
| Grandeza escalar vs. vetorial | `______` → *Escalar: valor + unidade · Vetorial: valor + unidade + direção + sentido* |
| 7 grandezas fundamentais do SI | `______` → *Comprimento · Massa · Tempo · Corrente · Temperatura · Matéria · Luminosa* |
| Notação científica — forma geral | `______` → *a × 10ⁿ, com 1 ≤ a < 10* |
| Ordem de grandeza — regra do corte | `______` → *a ≥ 3,16 → 10ⁿ⁺¹ · a < 3,16 → 10ⁿ* |
| 1 dia em segundos | `______` → *86 400 s* |
| Massa ≠ Peso (unidades) | `______` → *Massa: kg (escalar) · Peso: N (vetorial)* |
| Grandeza adimensional — exemplos | `______` → *Coeficiente de atrito · Índice de refração* |
| ⚠️ Pegadinha — símbolo de unidade | N de newton: maiúscula ou minúscula? → *Símbolo: N (maiúscula) · Nome: newton (minúscula)* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

### Síntese do Livro — GRANDEZAS FÍSICAS

**Parte 1 — Classificação das grandezas:**

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| Nó raiz | "Grandezas físicas" | *(dado completo)* |
| Ramo 1 | "Grandezas fundamentais — Formam as bases para outras grandezas e podem ser definidas diretamente" | *(dado completo)* |
| Ramo 2 — lacuna | *(caixa em branco)* | `______` → *Grandezas escalares* |
| Descrição Ramo 2 | "Representadas somente pelo seu valor numérico e pela sua unidade" | *(dado completo — leva à resposta)* |
| Ramo 3 | "Grandezas derivadas — Derivam de relações entre as grandezas fundamentais" | *(dado completo)* |
| Ramo 4 — lacuna | *(caixa em branco)* | `______` → *Grandezas vetoriais* |
| Descrição Ramo 4 | "Representadas pela sua intensidade, unidade correspondente, direção e sentido" | *(dado completo — leva à resposta)* |

**Parte 2 — Sistema Internacional de Unidades:**

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| Nó central | "Sistema Internacional de Unidades" | *(dado completo)* |
| Grandeza com unidade metro (m) — lacuna | metro (m) | `______` → *Comprimento* |
| Grandeza Tempo | "Tempo" | *(dado completo)* |
| Unidade do Tempo | "segundo (s)" | *(dado completo)* |
| Grandeza com unidade mol — lacuna | mol (mol) | `______` → *Quantidade de matéria* |
| Grandeza Massa | "Massa" | *(dado completo)* |
| Unidade da Massa | "quilograma (kg)" | *(dado completo)* |
| Grandeza Temperatura termodinâmica | "Temperatura termodinâmica" | *(dado completo)* |
| Unidade da Temperatura | "kelvin (K)" | *(dado completo)* |
| Grandeza com unidade candela (cd) — lacuna | candela (cd) | `______` → *Intensidade luminosa* |

**Parte 3 — Notação científica:**

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| Exemplo positivo — número original | "9 460 800 000 000 000,0" | *(dado completo)* |
| Exemplo positivo — deslocamento | "A vírgula é deslocada 15 casas para a esquerda" | *(dado completo)* |
| Exemplo positivo — resultado | "9,4608 · 10¹⁵" | *(dado completo)* |
| Exemplo positivo — sinal da potência | `______` | `______` → *Potência +* |
| Exemplo negativo — número original | "0,000000000000000000016" | *(dado completo)* |
| Exemplo negativo — deslocamento | "A vírgula é deslocada 19 casas para a direita" | *(dado completo)* |
| Exemplo negativo — resultado | "1,6 · 10⁻¹⁹" | *(dado completo)* |
| Exemplo negativo — sinal da potência | `______` | `______` → *Potência −* |

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| Q-1 | Classificar 3 grandezas: fundamental ou derivada (água, café, distância) | Dis | F | AT | a) derivada (volume) · b) fundamental (massa) · c) fundamental (comprimento) | — |
| Q-2 | V ou F — 5 afirmativas sobre escalares, fundamentais, vetoriais, derivadas, força/aceleração | V-F | M | AT | a)V · b)V · c)V · d)F · e)V | — |
| Q-3 | Por que é importante realizar medições? | Dis | F | AT | (aberta) | — |
| Q-4 | Converter períodos em horas: 45 dias; 5 meses; 2 anos | Cálculo | F | AT | a)1 080 h · b)3 600 h · c)17 520 h | — |
| Q-5 | Converter massas para gramas: 22 kg; 132,4 kg; 5 300 mg; 3 t | Cálculo | F | AT | a)22 000 g · b)132 400 g · c)5,3 g · d)3 000 000 g | — |
| Q-6 | Converter para milímetros: 32 cm; 2 km; 5 m | Cálculo | F | AT | a)320 mm · b)2 000 000 mm · c)5 000 mm | — |
| Q-7 | Diferença fundamental/derivada + listar 7 grandezas do SI | Dis | M | AT | (ver resolução abaixo) | — |
| Q-8 | Livro 300 folhas: espessura de 1 folha (3 cm total) + massa total | Cálculo | M | AT | a)0,1 mm · b)390,4 g | ⚠️ ver resolução |
| Q-9 | Converter: 900 m→km; 16,5 h→min; 0,6 kg→g; 54,2 t→kg; 54 dias→h | Cálculo | F | AT | a)0,9 km · b)990 min · c)600 g · d)54 200 kg · e)1 296 h | — |
| Q-10 | 2,5 milhões de anos-luz em notação científica | Cálculo | M | AT | 2,5 × 10⁶ anos-luz | — |
| Q-11 | Notação científica: 5 valores (800 m; 0,000074 m; 58×10¹⁵ kg; 1,6×10⁻¹⁹; 0,0008 km) | Cálculo | M | AT | a)8×10² m · b)7,4×10⁻⁵ m · c)5,8×10¹⁶ kg · d)1,6×10⁻¹⁹ A·s · e)8×10⁻⁴ km | — |
| Q-12 | Operações com notação científica em unidades SI | Cálculo | D | AT | ⚠️ ver resolução | ⚠️ |
| Q-13 | Sonda New Horizons — 5 bilhões de km em notação científica | Cálculo | M | AT | 5 × 10⁹ km = 5 × 10¹² m | — |
| Q-14 | Água da Terra: caminhões-pipa para Marte — notação científica | Cálculo | D | AT | ⚠️ ver resolução | — |
| QC-1 | UFPR 2024 — unidade de tempo no SI | MC | F | AT | c) s (segundo) | — |
| QC-2 | UFPR 2021 — unidade básica de comprimento no SI | MC | F | AT | b) o metro | — |
| QC-3 | Engenheiro — 4,5 km em metros e centímetros | Cálculo | F | AT | 4 500 m · 450 000 cm | — |
| QC-4 | Mackenzie 2020 — 50 mph em m/s | MC | M | AT | a) 22 m/s | — |
| QC-5 | Udesc — apenas unidades fundamentais do SI | MC | M | AT | e) Metro, segundo, quilograma | — |
| QC-6 | Unifesp — grandezas adimensionais | MC | M | AT | a) razão entre grandezas de mesma dimensão | — |
| QC-7 | UFPR 2022 — ordem de grandeza da espessura do celular | MC | M | AT | c) 10⁻² m | — |
| QC-8 | UTFPR — 30 mg em notação científica na unidade SI (kg) | MC | M | AT | ⚠️ ver resolução | ⚠️ |
| QC-9 | Famerp-SP 2024 — altitude 13,12 km em pés | MC | M | AT | c) 30,5 cm | — |
| QC-10 | Uesb-BA — ordem de grandeza de átomos de urânio em 5 g | MC | D | AT | b) 10²³ | — |

---

**Resoluções desenvolvidas:**

**Q-4:**
- a) 45 × 24 = **1 080 h**
- b) 5 × 30 × 24 = **3 600 h**
- c) 2 × 365 × 24 = **17 520 h**

**Q-5:**
- a) 22 × 1 000 = **22 000 g**
- b) 132,4 × 1 000 = **132 400 g**
- c) 5 300 ÷ 1 000 = **5,3 g**
- d) 3 × 1 000 × 1 000 = **3 000 000 g**

**Q-6:**
- a) 32 × 10 = **320 mm**
- b) 2 × 1 000 × 1 000 = **2 000 000 mm**
- c) 5 × 1 000 = **5 000 mm**

**Q-8:**
- a) Espessura total = 3 cm = 30 mm. Folhas = 300. Espessura por folha = 30 ÷ 300 = **0,1 mm**
- b) Capa e contracapa: 2 × 15,2 = 30,4 g. Demais folhas: (300 − 2) × 1,2 = 298 × 1,2 = 357,6 g. Total: 30,4 + 357,6 = **388 g**
  *(Observação: se o livro tem 300 folhas incluindo capa e contracapa, então há 298 folhas internas)*

**Q-9:**
- a) 900 ÷ 1 000 = **0,9 km**
- b) 16,5 × 60 = **990 min**
- c) 0,6 × 1 000 = **600 g**
- d) 54,2 × 1 000 = **54 200 kg**
- e) 54 × 24 = **1 296 h**

**Q-12:**
- a) Converter: 1,0 × 10⁴ mm = 1,0 × 10⁴ × 10⁻³ m = 1,0 × 10¹ m = 10 m. Então: 10 m × 1,0 × 10⁶ m = **1,0 × 10⁷ m²** *(área)*
- b) Converter: 1,0 × 10⁶ g = 1,0 × 10³ kg. Então: 1,0 × 10⁻²⁵ kg + 1 000 kg ≈ **1,0 × 10³ kg** *(o primeiro termo é desprezível)*

**QC-4 (Mackenzie 2020):**
50 mph × 1,6 km/h = 80 km/h. Converter: 80 ÷ 3,6 ≈ **22 m/s** → **a)**

**QC-8 (UTFPR):**
30 mg → converter para kg: 30 mg = 30 × 10⁻³ g = 30 × 10⁻⁶ kg = 3,0 × 10⁻⁵ kg → **a) 3,0 · 10⁻⁵**

**QC-9 (Famerp-SP 2024):**
13,12 km = 13 120 m. Convertendo para pés, 1 pé ≈ 0,305 m: 13 120 ÷ 0,305 ≈ 43 016 pés. A questão pede a equivalência de 1 pé ≈ **30,5 cm** → **c)**

**QC-10 (Uesb-BA):**
5,0 g = 5,0 × 10⁻³ kg. Número de átomos = (5,0 × 10⁻³) ÷ (4,0 × 10⁻²⁵) = 1,25 × 10²². Como 1,25 < 3,16 → ordem de grandeza = **10²²** → **c)**

⚠️ **Nota:** as alternativas do QC-8 no material apresentam duplicação ("3,0 · 10⁻⁵" aparece duas vezes — nas alíneas a e d). Verificar gabarito oficial.

---

#### Bloco B — Questões modelo originais

---

**QM-1** · múltipla escolha · médio · inspirada em: Q-2

Em uma aula de Física, a professora escreveu no quadro quatro afirmações sobre grandezas físicas. Assinale a alternativa que contém **apenas afirmações verdadeiras**:

I. A temperatura é uma grandeza escalar, pois é definida apenas por um valor numérico e sua unidade.
II. A aceleração é uma grandeza vetorial, pois necessita de direção e sentido para ser completamente definida.
III. O volume de uma garrafa é uma grandeza fundamental, pois é facilmente medida com instrumentos.
IV. A força é uma grandeza escalar, expressa em newton (N).

a) I e II apenas
b) I, II e III
c) II e IV apenas
d) I, II e IV

✅ **Gabarito:** a)
📝 **Resolução:**
- I → **V**: temperatura é escalar ✓
- II → **V**: aceleração é vetorial ✓
- III → **F**: volume é derivada (não fundamental)
- IV → **F**: força é **vetorial**, não escalar
⚠️ **Professor:** referência de estilo — crie variações originais, nunca reproduza diretamente.

---

**QM-2** · múltipla escolha · médio · inspirada em: QC-5

Considere as grandezas e unidades listadas abaixo:

I. Comprimento — metro (m)
II. Velocidade — metro por segundo (m/s)
III. Temperatura termodinâmica — kelvin (K)
IV. Força — newton (N)
V. Quantidade de matéria — mol (mol)

Assinale a alternativa que contém **apenas grandezas fundamentais do SI**:

a) I, II e III
b) I, III e V
c) II, IV e V
d) I, IV e V

✅ **Gabarito:** b)
📝 **Resolução:**
- I → fundamental ✓
- II → **derivada** (comprimento/tempo)
- III → fundamental ✓
- IV → **derivada** (massa × comprimento / tempo²)
- V → fundamental ✓
⚠️ **Professor:** referência de estilo — crie variações originais, nunca reproduza diretamente.

---

**QM-3** · dissertativa · médio · inspirada em: Q-3 e Q-7

Antes da criação do Sistema Internacional de Unidades, diferentes regiões do mundo utilizavam padrões de medida distintos, como polegadas, pés e jardas. Com base no que você estudou:

a) Explique por que a padronização das unidades de medida é fundamental para a ciência e para o comércio global.
b) Qual é a diferença entre uma grandeza fundamental e uma grandeza derivada? Dê um exemplo de cada uma com sua respectiva unidade no SI.

✅ **Gabarito esperado:**
a) Sem padronização, uma mesma medida teria valores diferentes dependendo da região ou da pessoa que mede (ex.: o tamanho de um "pé" varia de pessoa para pessoa). A padronização permite que experimentos científicos sejam reproduzidos e verificados em qualquer lugar do mundo, e que produtos comerciais sejam descritos de forma universal.

b) Fundamental: independente, definida diretamente — ex.: comprimento (metro, m). Derivada: obtida a partir de combinações de grandezas fundamentais — ex.: velocidade (metro por segundo, m/s), que deriva de comprimento e tempo.
⚠️ **Professor:** referência de estilo — crie variações originais, nunca reproduza diretamente.

---

**QM-4** · múltipla escolha estilo concurso · difícil · inspirada em: QC-6 e QC-10

*(Estilo somatório)*

Sobre grandezas físicas, notação científica e Sistema Internacional de Unidades, avalie as afirmativas:

- **01.** O índice de refração da luz em um meio é uma grandeza adimensional porque resulta da razão entre duas velocidades — grandezas de mesma dimensão.
- **02.** A unidade de medida de força no SI é o quilograma (kg), que é uma grandeza fundamental.
- **04.** A massa de 5,97 × 10²⁴ kg possui ordem de grandeza 10²⁵ kg, pois 5,97 > 3,16.
- **08.** Em notação científica, o número 0,00045 m é representado como 4,5 × 10⁻⁴ m.
- **16.** Uma grandeza vetorial pode ser completamente descrita apenas por seu valor numérico e sua unidade de medida.

a) 05   b) 13   c) 17   d) 09

✅ **Gabarito:** b) 13
📝 **Resolução:**
- 01 → **V** ✓ (razão entre velocidades cancela a unidade)
- 02 → **F** (força: newton, N — grandeza derivada)
- 04 → **V** ✓ (5,97 > 3,16 → 10²⁵ kg)
- 08 → **V** ✓ (vírgula 4 casas para direita → 10⁻⁴)
- 16 → **F** (vetorial precisa de direção e sentido)
- Soma: 01 + 04 + 08 = **13**
⚠️ **Professor:** referência de estilo — crie variações originais, nunca reproduza diretamente.

---

**QM-5** · cálculo · médio-difícil · inspirada em: Q-8 e Q-12

Uma embalagem de medicamento informa que cada comprimido contém 500 mg do princípio ativo. Uma caixa contém 30 comprimidos.

a) Qual é a massa total do princípio ativo na caixa, em gramas?
b) Expresse essa massa em quilogramas, em notação científica.
c) Qual é a ordem de grandeza dessa massa em quilogramas?

✅ **Gabarito:**
a) 30 × 500 mg = 15 000 mg = **15 g**
b) 15 g = 0,015 kg = **1,5 × 10⁻² kg**
c) 1,5 < 3,16 → ordem de grandeza = **10⁻²**
📝 **Resolução detalhada:**
- a) Multiplicar: 30 × 500 = 15 000 mg; converter: 15 000 ÷ 1 000 = 15 g
- b) 15 g ÷ 1 000 = 0,015 kg = 1,5 × 10⁻² kg (vírgula 2 casas para direita → expoente −2)
- c) Como a = 1,5 e 1,5 < 3,16 → potência não sobe → ordem = 10⁻²
⚠️ **Professor:** referência de estilo — crie variações originais, nunca reproduza diretamente.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: classif_grandezas
Mapa de classificação das grandezas físicas: fundamental/derivada e escalar/vetorial.

```svg
<svg width="100%" viewBox="0 0 680 360">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
stroke-width="1.5" stroke-linecap="round"
stroke-linejoin="round"/></marker></defs>
<style>
  .c-purple{fill:#7c3aed}.c-teal{fill:#0d9488}.c-amber{fill:#d97706}
  .c-coral{fill:#e11d48}.c-gray{fill:#6b7280}
  .t{font-size:14px;font-family:sans-serif;fill:#1f2937}
  .ts{font-size:12px;font-family:sans-serif;fill:#4b5563}
  .th{font-size:13px;font-weight:bold;font-family:sans-serif;fill:#fff}
  @media(prefers-color-scheme:dark){.t{fill:#f3f4f6}.ts{fill:#d1d5db}}
</style>

<!-- Raiz -->
<rect x="215" y="10" width="250" height="44" rx="8" class="c-purple"/>
<text x="340" y="32" text-anchor="middle" dominant-baseline="central" class="th">Grandezas Físicas</text>

<!-- Setas raiz -->
<line x1="270" y1="54" x2="130" y2="100" stroke="#9ca3af" stroke-width="1.5" marker-end="url(#arrow)"/>
<line x1="340" y1="54" x2="340" y2="100" stroke="#9ca3af" stroke-width="1.5" marker-end="url(#arrow)"/>
<line x1="410" y1="54" x2="480" y2="100" stroke="#9ca3af" stroke-width="1.5" marker-end="url(#arrow)"/>
<line x1="440" y1="54" x2="580" y2="100" stroke="#9ca3af" stroke-width="1.5" marker-end="url(#arrow)"/>

<!-- Nó 1: Fundamental -->
<rect x="40" y="100" width="160" height="58" rx="6" class="c-teal"/>
<text x="120" y="120" text-anchor="middle" dominant-baseline="central" class="th">Fundamental</text>
<text x="120" y="140" text-anchor="middle" dominant-baseline="central" class="th">7 no SI</text>
<text x="120" y="172" text-anchor="middle" class="ts">Independente;</text>
<text x="120" y="186" text-anchor="middle" class="ts">definida diretamente</text>

<!-- Nó 2: Derivada -->
<rect x="258" y="100" width="160" height="58" rx="6" class="c-teal"/>
<text x="338" y="120" text-anchor="middle" dominant-baseline="central" class="th">Derivada</text>
<text x="338" y="140" text-anchor="middle" dominant-baseline="central" class="th">(Composta)</text>
<text x="338" y="172" text-anchor="middle" class="ts">Combina grandezas</text>
<text x="338" y="186" text-anchor="middle" class="ts">fundamentais</text>

<!-- Nó 3: Escalar -->
<rect x="430" y="100" width="110" height="58" rx="6" class="c-amber"/>
<text x="485" y="120" text-anchor="middle" dominant-baseline="central" class="th">Escalar</text>
<text x="485" y="140" text-anchor="middle" dominant-baseline="central" class="th"> </text>
<text x="485" y="172" text-anchor="middle" class="ts">Valor + unidade</text>
<text x="485" y="186" text-anchor="middle" class="ts">Ex.: massa, temp.</text>

<!-- Nó 4: Vetorial -->
<rect x="550" y="100" width="120" height="58" rx="6" class="c-amber"/>
<text x="610" y="120" text-anchor="middle" dominant-baseline="central" class="th">Vetorial</text>
<text x="610" y="140" text-anchor="middle" dominant-baseline="central" class="th"> </text>
<text x="610" y="172" text-anchor="middle" class="ts">Valor + unidade</text>
<text x="610" y="186" text-anchor="middle" class="ts">+ direção + sentido</text>

<!-- Exemplos fundamentais -->
<rect x="10" y="220" width="180" height="58" rx="5" class="c-gray"/>
<text x="100" y="240" text-anchor="middle" dominant-baseline="central" class="th">Ex. Fundamentais:</text>
<text x="100" y="260" text-anchor="middle" dominant-baseline="central" class="th">m · kg · s · A · K · mol · cd</text>
<line x1="120" y1="158" x2="100" y2="220" stroke="#6b7280" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- Exemplos derivadas -->
<rect x="220" y="220" width="190" height="58" rx="5" class="c-gray"/>
<text x="315" y="240" text-anchor="middle" dominant-baseline="central" class="th">Ex. Derivadas:</text>
<text x="315" y="260" text-anchor="middle" dominant-baseline="central" class="th">velocidade · força · volume</text>
<line x1="338" y1="158" x2="315" y2="220" stroke="#6b7280" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- Alerta massa x peso -->
<rect x="420" y="220" width="250" height="58" rx="5" class="c-coral"/>
<text x="545" y="240" text-anchor="middle" dominant-baseline="central" class="th">⚠ Massa ≠ Peso</text>
<text x="545" y="260" text-anchor="middle" dominant-baseline="central" class="th">Massa: kg (escalar) · Peso: N (vetorial)</text>
<line x1="485" y1="158" x2="500" y2="220" stroke="#e11d48" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- Legenda rótulo classificação -->
<rect x="10" y="300" width="14" height="14" rx="2" class="c-teal"/>
<text x="30" y="311" class="ts" dominant-baseline="central">Classificação 1: Fundamental / Derivada</text>
<rect x="310" y="300" width="14" height="14" rx="2" class="c-amber"/>
<text x="330" y="311" class="ts" dominant-baseline="central">Classificação 2: Escalar / Vetorial</text>
</svg>
```

---

### DIAGRAMA: notacao_cientifica
Regra de notação científica com os dois exemplos do livro e a distinção positivo/negativo.

```svg
<svg width="100%" viewBox="0 0 680 310">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
stroke-width="1.5" stroke-linecap="round"
stroke-linejoin="round"/></marker></defs>
<style>
  .c-purple{fill:#7c3aed}.c-teal{fill:#0d9488}.c-amber{fill:#d97706}
  .c-coral{fill:#e11d48}.c-gray{fill:#6b7280}
  .t{font-size:14px;font-family:sans-serif;fill:#1f2937}
  .ts{font-size:12px;font-family:sans-serif;fill:#4b5563}
  .th{font-size:13px;font-weight:bold;font-family:sans-serif;fill:#fff}
  @media(prefers-color-scheme:dark){.t{fill:#f3f4f6}.ts{fill:#d1d5db}}
</style>

<!-- Título / forma geral -->
<rect x="190" y="10" width="300" height="44" rx="8" class="c-purple"/>
<text x="340" y="32" text-anchor="middle" dominant-baseline="central" class="th">Notação Científica: a × 10ⁿ</text>

<text x="340" y="70" text-anchor="middle" class="ts">1 ≤ a &lt; 10  ·  n é inteiro</text>

<!-- --- EXEMPLO POSITIVO --- -->
<!-- Caixa número original -->
<rect x="10" y="90" width="200" height="44" rx="5" class="c-gray"/>
<text x="110" y="112" text-anchor="middle" dominant-baseline="central" class="th">9 460 800 000 000 000</text>

<!-- Seta -->
<line x1="210" y1="112" x2="248" y2="112" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="229" y="105" text-anchor="middle" class="ts">15 casas</text>
<text x="229" y="118" text-anchor="middle" class="ts">← esquerda</text>

<!-- Resultado -->
<rect x="250" y="90" width="160" height="44" rx="5" class="c-teal"/>
<text x="330" y="112" text-anchor="middle" dominant-baseline="central" class="th">9,4608 × 10¹⁵ m</text>

<!-- Seta resultado -->
<line x1="410" y1="112" x2="448" y2="112" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>

<!-- Potência positiva -->
<rect x="450" y="90" width="220" height="44" rx="5" class="c-teal"/>
<text x="560" y="104" text-anchor="middle" dominant-baseline="central" class="th">Potência POSITIVA</text>
<text x="560" y="122" text-anchor="middle" dominant-baseline="central" class="th">número grande (&gt; 10)</text>

<!-- --- EXEMPLO NEGATIVO --- -->
<rect x="10" y="170" width="200" height="44" rx="5" class="c-gray"/>
<text x="110" y="192" text-anchor="middle" dominant-baseline="central" class="th">0,000...000016</text>

<line x1="210" y1="192" x2="248" y2="192" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="229" y="185" text-anchor="middle" class="ts">19 casas</text>
<text x="229" y="198" text-anchor="middle" class="ts">→ direita</text>

<rect x="250" y="170" width="160" height="44" rx="5" class="c-coral"/>
<text x="330" y="192" text-anchor="middle" dominant-baseline="central" class="th">1,6 × 10⁻¹⁹ A·s</text>

<line x1="410" y1="192" x2="448" y2="192" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>

<rect x="450" y="170" width="220" height="44" rx="5" class="c-coral"/>
<text x="560" y="184" text-anchor="middle" dominant-baseline="central" class="th">Potência NEGATIVA</text>
<text x="560" y="202" text-anchor="middle" dominant-baseline="central" class="th">número pequeno (&lt; 1)</text>

<!-- Alerta ordem de grandeza -->
<rect x="10" y="240" width="660" height="58" rx="6" class="c-amber"/>
<text x="340" y="258" text-anchor="middle" dominant-baseline="central" class="th">Ordem de grandeza: a ≥ 3,16 → potência sobe (10ⁿ⁺¹) · a &lt; 3,16 → potência mantém (10ⁿ)</text>
<text x="340" y="278" text-anchor="middle" dominant-baseline="central" class="th">Ex.: 5,97 × 10²⁴ kg → 5,97 &gt; 3,16 → ordem = 10²⁵ kg</text>
</svg>
```

---

### DIAGRAMA: si_fundamentais
As 7 grandezas fundamentais do SI organizadas em torno do nó central.

```svg
<svg width="100%" viewBox="0 0 680 380">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
stroke-width="1.5" stroke-linecap="round"
stroke-linejoin="round"/></marker></defs>
<style>
  .c-purple{fill:#7c3aed}.c-teal{fill:#0d9488}.c-amber{fill:#d97706}
  .c-coral{fill:#e11d48}.c-gray{fill:#6b7280}
  .t{font-size:14px;font-family:sans-serif;fill:#1f2937}
  .ts{font-size:12px;font-family:sans-serif;fill:#4b5563}
  .th{font-size:13px;font-weight:bold;font-family:sans-serif;fill:#fff}
  @media(prefers-color-scheme:dark){.t{fill:#f3f4f6}.ts{fill:#d1d5db}}
</style>

<!-- Nó central -->
<rect x="230" y="158" width="220" height="44" rx="8" class="c-purple"/>
<text x="340" y="180" text-anchor="middle" dominant-baseline="central" class="th">SI — 7 Grandezas Fundamentais</text>

<!-- 1 Comprimento -->
<rect x="10" y="10" width="150" height="58" rx="6" class="c-teal"/>
<text x="85" y="30" text-anchor="middle" dominant-baseline="central" class="th">Comprimento</text>
<text x="85" y="50" text-anchor="middle" dominant-baseline="central" class="th">metro (m)</text>
<line x1="160" y1="39" x2="230" y2="168" stroke="#9ca3af" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- 2 Massa -->
<rect x="10" y="100" width="150" height="58" rx="6" class="c-teal"/>
<text x="85" y="120" text-anchor="middle" dominant-baseline="central" class="th">Massa</text>
<text x="85" y="140" text-anchor="middle" dominant-baseline="central" class="th">quilograma (kg)</text>
<line x1="160" y1="129" x2="230" y2="176" stroke="#9ca3af" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- 3 Tempo -->
<rect x="10" y="190" width="150" height="58" rx="6" class="c-teal"/>
<text x="85" y="210" text-anchor="middle" dominant-baseline="central" class="th">Tempo</text>
<text x="85" y="230" text-anchor="middle" dominant-baseline="central" class="th">segundo (s)</text>
<line x1="160" y1="200" x2="230" y2="188" stroke="#9ca3af" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- 4 Corrente elétrica -->
<rect x="10" y="280" width="150" height="58" rx="6" class="c-teal"/>
<text x="85" y="298" text-anchor="middle" dominant-baseline="central" class="th">Corrente elétrica</text>
<text x="85" y="318" text-anchor="middle" dominant-baseline="central" class="th">ampere (A)</text>
<line x1="160" y1="290" x2="230" y2="196" stroke="#9ca3af" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- 5 Temperatura termodinâmica -->
<rect x="520" y="10" width="150" height="58" rx="6" class="c-amber"/>
<text x="595" y="28" text-anchor="middle" dominant-baseline="central" class="th">Temperatura</text>
<text x="595" y="48" text-anchor="middle" dominant-baseline="central" class="th">kelvin (K)</text>
<line x1="520" y1="39" x2="450" y2="168" stroke="#9ca3af" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- 6 Quantidade de matéria -->
<rect x="520" y="100" width="150" height="58" rx="6" class="c-amber"/>
<text x="595" y="118" text-anchor="middle" dominant-baseline="central" class="th">Qtd. de matéria</text>
<text x="595" y="138" text-anchor="middle" dominant-baseline="central" class="th">mol (mol)</text>
<line x1="520" y1="129" x2="450" y2="176" stroke="#9ca3af" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- 7 Intensidade luminosa -->
<rect x="520" y="190" width="150" height="58" rx="6" class="c-amber"/>
<text x="595" y="208" text-anchor="middle" dominant-baseline="central" class="th">Int. luminosa</text>
<text x="595" y="228" text-anchor="middle" dominant-baseline="central" class="th">candela (cd)</text>
<line x1="520" y1="210" x2="450" y2="190" stroke="#9ca3af" stroke-width="1.2" marker-end="url(#arrow)"/>

<!-- Alerta -->
<rect x="170" y="320" width="340" height="44" rx="6" class="c-coral"/>
<text x="340" y="334" text-anchor="middle" dominant-baseline="central" class="th">⚠ Símbolo derivado de nome próprio → MAIÚSCULA</text>
<text x="340" y="352" text-anchor="middle" dominant-baseline="central" class="th">Nome da unidade → minúscula (ex.: newton, kelvin)</text>
</svg>
```

---

### DIAGRAMA: conversoes_comprimento
Cadeia de conversões de comprimento com fatores explícitos.

```svg
<svg width="100%" viewBox="0 0 680 160">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
stroke-width="1.5" stroke-linecap="round"
stroke-linejoin="round"/></marker></defs>
<style>
  .c-purple{fill:#7c3aed}.c-teal{fill:#0d9488}.c-amber{fill:#d97706}
  .c-coral{fill:#e11d48}.c-gray{fill:#6b7280}
  .t{font-size:14px;font-family:sans-serif;fill:#1f2937}
  .ts{font-size:12px;font-family:sans-serif;fill:#4b5563}
  .th{font-size:13px;font-weight:bold;font-family:sans-serif;fill:#fff}
  @media(prefers-color-scheme:dark){.t{fill:#f3f4f6}.ts{fill:#d1d5db}}
</style>

<!-- km -->
<rect x="10" y="50" width="80" height="44" rx="6" class="c-purple"/>
<text x="50" y="72" text-anchor="middle" dominant-baseline="central" class="th">km</text>

<line x1="90" y1="72" x2="128" y2="72" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="109" y="62" text-anchor="middle" class="ts">× 1 000</text>
<line x1="128" y1="82" x2="90" y2="82" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="109" y="95" text-anchor="middle" class="ts">÷ 1 000</text>

<!-- m -->
<rect x="130" y="50" width="80" height="44" rx="6" class="c-teal"/>
<text x="170" y="72" text-anchor="middle" dominant-baseline="central" class="th">m</text>

<line x1="210" y1="72" x2="248" y2="72" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="229" y="62" text-anchor="middle" class="ts">× 10</text>
<line x1="248" y1="82" x2="210" y2="82" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="229" y="95" text-anchor="middle" class="ts">÷ 10</text>

<!-- dm -->
<rect x="250" y="50" width="80" height="44" rx="6" class="c-teal"/>
<text x="290" y="72" text-anchor="middle" dominant-baseline="central" class="th">dm</text>

<line x1="330" y1="72" x2="368" y2="72" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="349" y="62" text-anchor="middle" class="ts">× 10</text>
<line x1="368" y1="82" x2="330" y2="82" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="349" y="95" text-anchor="middle" class="ts">÷ 10</text>

<!-- cm -->
<rect x="370" y="50" width="80" height="44" rx="6" class="c-amber"/>
<text x="410" y="72" text-anchor="middle" dominant-baseline="central" class="th">cm</text>

<line x1="450" y1="72" x2="488" y2="72" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="469" y="62" text-anchor="middle" class="ts">× 10</text>
<line x1="488" y1="82" x2="450" y2="82" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="469" y="95" text-anchor="middle" class="ts">÷ 10</text>

<!-- mm -->
<rect x="490" y="50" width="80" height="44" rx="6" class="c-amber"/>
<text x="530" y="72" text-anchor="middle" dominant-baseline="central" class="th">mm</text>

<!-- Alerta dm -->
<rect x="220" y="115" width="240" height="36" rx="5" class="c-coral"/>
<text x="340" y="133" text-anchor="middle" dominant-baseline="central" class="th">⚠ 1 m = 10 dm (não 100 dm!)</text>
</svg>
```

---

### DIAGRAMA: conversoes_massa
Cadeia de conversões de massa.

```svg
<svg width="100%" viewBox="0 0 680 130">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
stroke-width="1.5" stroke-linecap="round"
stroke-linejoin="round"/></marker></defs>
<style>
  .c-purple{fill:#7c3aed}.c-teal{fill:#0d9488}.c-amber{fill:#d97706}
  .c-coral{fill:#e11d48}.c-gray{fill:#6b7280}
  .th{font-size:13px;font-weight:bold;font-family:sans-serif;fill:#fff}
  .ts{font-size:12px;font-family:sans-serif;fill:#4b5563}
  @media(prefers-color-scheme:dark){.ts{fill:#d1d5db}}
</style>

<!-- t -->
<rect x="40" y="30" width="100" height="44" rx="6" class="c-purple"/>
<text x="90" y="52" text-anchor="middle" dominant-baseline="central" class="th">tonelada (t)</text>

<line x1="140" y1="52" x2="188" y2="52" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="164" y="42" text-anchor="middle" class="ts">× 1 000</text>
<line x1="188" y1="62" x2="140" y2="62" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="164" y="76" text-anchor="middle" class="ts">÷ 1 000</text>

<!-- kg -->
<rect x="190" y="30" width="140" height="44" rx="6" class="c-teal"/>
<text x="260" y="52" text-anchor="middle" dominant-baseline="central" class="th">quilograma (kg)</text>

<line x1="330" y1="52" x2="378" y2="52" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="354" y="42" text-anchor="middle" class="ts">× 1 000</text>
<line x1="378" y1="62" x2="330" y2="62" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="354" y="76" text-anchor="middle" class="ts">÷ 1 000</text>

<!-- g -->
<rect x="380" y="30" width="100" height="44" rx="6" class="c-amber"/>
<text x="430" y="52" text-anchor="middle" dominant-baseline="central" class="th">grama (g)</text>

<line x1="480" y1="52" x2="528" y2="52" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="504" y="42" text-anchor="middle" class="ts">× 1 000</text>
<line x1="528" y1="62" x2="480" y2="62" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="504" y="76" text-anchor="middle" class="ts">÷ 1 000</text>

<!-- mg -->
<rect x="530" y="30" width="130" height="44" rx="6" class="c-amber"/>
<text x="595" y="52" text-anchor="middle" dominant-baseline="central" class="th">miligrama (mg)</text>

<!-- Alerta -->
<rect x="160" y="90" width="200" height="30" rx="4" class="c-coral"/>
<text x="260" y="105" text-anchor="middle" dominant-baseline="central" class="th">⚠ 1 t = 1 000 kg (não 100 kg)</text>
</svg>
```

---

### DIAGRAMA: conversoes_tempo
Cadeia de conversões de tempo.

```svg
<svg width="100%" viewBox="0 0 680 130">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
stroke-width="1.5" stroke-linecap="round"
stroke-linejoin="round"/></marker></defs>
<style>
  .c-purple{fill:#7c3aed}.c-teal{fill:#0d9488}.c-amber{fill:#d97706}
  .c-coral{fill:#e11d48}.c-gray{fill:#6b7280}
  .th{font-size:13px;font-weight:bold;font-family:sans-serif;fill:#fff}
  .ts{font-size:12px;font-family:sans-serif;fill:#4b5563}
  @media(prefers-color-scheme:dark){.ts{fill:#d1d5db}}
</style>

<!-- dia -->
<rect x="10" y="30" width="100" height="44" rx="6" class="c-purple"/>
<text x="60" y="52" text-anchor="middle" dominant-baseline="central" class="th">dia</text>

<line x1="110" y1="52" x2="148" y2="52" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="129" y="42" text-anchor="middle" class="ts">× 24</text>
<line x1="148" y1="62" x2="110" y2="62" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="129" y="76" text-anchor="middle" class="ts">÷ 24</text>

<!-- h -->
<rect x="150" y="30" width="100" height="44" rx="6" class="c-teal"/>
<text x="200" y="52" text-anchor="middle" dominant-baseline="central" class="th">hora (h)</text>

<line x1="250" y1="52" x2="298" y2="52" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="274" y="42" text-anchor="middle" class="ts">× 60</text>
<line x1="298" y1="62" x2="250" y2="62" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="274" y="76" text-anchor="middle" class="ts">÷ 60</text>

<!-- min -->
<rect x="300" y="30" width="110" height="44" rx="6" class="c-teal"/>
<text x="355" y="52" text-anchor="middle" dominant-baseline="central" class="th">minuto (min)</text>

<line x1="410" y1="52" x2="458" y2="52" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="434" y="42" text-anchor="middle" class="ts">× 60</text>
<line x1="458" y1="62" x2="410" y2="62" stroke="#9ca3af" stroke-width="2" marker-end="url(#arrow)"/>
<text x="434" y="76" text-anchor="middle" class="ts">÷ 60</text>

<!-- s -->
<rect x="460" y="30" width="130" height="44" rx="6" class="c-amber"/>
<text x="525" y="52" text-anchor="middle" dominant-baseline="central" class="th">segundo (s)</text>

<!-- Alerta -->
<rect x="120" y="90" width="310" height="30" rx="4" class="c-coral"/>
<text x="275" y="105" text-anchor="middle" dominant-baseline="central" class="th">⚠ 1 dia = 86 400 s (não multiplicar dias × 3 600)</text>
</svg>
```
