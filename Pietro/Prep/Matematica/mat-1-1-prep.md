## DIAGRAMAS DISPONÍVEIS — mat-1-1

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Hierarquia de conjuntos | DIAGRAMA: conjuntos | Ao apresentar Bloco 2 — os cinco conjuntos numéricos |
| Reta numérica real | DIAGRAMA: reta_numerica | Ao apresentar Bloco 4 — representação na reta real |
| Fórmulas principais | DIAGRAMA: formulas | Ao apresentar Bloco 2 — definição formal de racional e real |

### Tabelas markdown (Seção 6):
- Tabela 1: cinco conjuntos com notação, definição e exemplos
- Tabela 2: classificação de números específicos por conjunto (N/Z/Q/I/R)

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.
Para image_search: use "código de barras sistema binário matemática" ao apresentar o Bloco G.

---

## SEÇÃO 1 — METADADOS

# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 1
- Tema: Números reais
- Perfil: álgebra
- Fórmulas principais: Q = {a/b | a ∈ Z, b ∈ Z, b ≠ 0} · R = Q ∪ I
- Matemáticos citados: nenhum

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### Bloco 1 — Por que organizar os números em conjuntos?

Os números estão presentes em todo o nosso cotidiano — em preços, temperaturas, distâncias, populações. Para organizar essa diversidade, a matemática agrupa os números em **conjuntos numéricos**, cada um com características próprias. Conhecer esses conjuntos é fundamental para entender qual tipo de número está sendo usado em cada situação e quais operações são possíveis.

### Bloco 2 — Os cinco conjuntos numéricos

**Números naturais (N)** são os números que usamos para contar e o zero: {0, 1, 2, 3, 4, ...}. São sempre inteiros e não negativos. Exemplos do livro: 0; 4/2 (= 2); √100 (= 10); 294.

**Números inteiros (Z)** reúnem os naturais e seus opostos (negativos): {..., −3, −2, −1, 0, 1, 2, 3, ...}. Todo natural é inteiro, mas nem todo inteiro é natural. Exemplos do livro: −326; −12; −√100 (= −10); 0; 294.

**Números racionais (Q)** são todos os que podem ser escritos como fração a/b, com a e b inteiros e b ≠ 0. Sua representação decimal é sempre **exata** (ex: 3/4 = 0,75) ou **dízima periódica** (ex: 4/3 = 1,333... = 1,3̄). Exemplos do livro: −1,75; −1/2; 0; 3/4; 1½; 1,3̄; 12,64; 294.

**Números irracionais (I)** são os que **não podem** ser escritos como fração. Sua representação decimal é **infinita e não periódica** — os dígitos nunca se repetem em padrão. Exemplos do livro: √2/2; √7; π ≈ 3,14159...; √12.

**Números reais (R)** formam o conjunto mais amplo: a união de racionais e irracionais. R = Q ∪ I. Todo número real pode ser representado como um ponto na reta numérica.

### Bloco 3 — Relação de inclusão entre os conjuntos

Os conjuntos se encaixam como bonecas russas: N ⊂ Z ⊂ Q ⊂ R, e I ⊂ R. Isso significa que todo natural é inteiro, todo inteiro é racional, todo racional é real. Os irracionais, por sua vez, não pertencem a N, Z ou Q — só a R.

O diagrama de Venn do livro mostra N e Z dentro de Q, com I separado, ambos dentro do grande conjunto R.

### Bloco 4 — Representação na reta real

A **reta real** é uma reta em que cada ponto corresponde exatamente a um número real — e vice-versa. Números racionais e irracionais têm posição na reta. Para localizar irracionais, usa-se uma aproximação decimal:
- √2 ≅ 1,4 → localizado entre 1 e 2
- −√3 ≅ −1,7 → localizado entre −2 e −1
- π ≅ 3,14159... → logo após o 3

### Bloco 5 — Aplicação real: código de barras e o sistema binário

O capítulo apresenta como aplicação o código de barras. As listras representam zeros e uns (código binário). Um código é dividido em 95 partes, agrupadas em 15 seções. O computador lê cada coluna como 0 (branco) ou 1 (preto), gerando um número de 95 dígitos. Um dígito verificador ao final valida o scan por meio de um cálculo matemático.

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Definição formal de número racional

**Expressão:** Q = {a/b | a ∈ Z, b ∈ Z, b ≠ 0}

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| a | numerador | número inteiro |
| b | denominador | número inteiro |
| b ≠ 0 | condição obrigatória | restrição |

**Válida quando:** b é diferente de zero.
**Caso especial:** quando b = 1, o resultado é o próprio inteiro a (ex: 5/1 = 5 ∈ Z ⊂ Q).
💡 **Pegadinha:** √4 = 2 é racional (é inteiro!). Nem toda raiz quadrada é irracional — só as que não resultam em inteiro.

### Composição do conjunto real

**Expressão:** R = Q ∪ I

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| R | conjunto dos números reais | conjunto |
| Q | conjunto dos números racionais | subconjunto de R |
| I | conjunto dos números irracionais | subconjunto de R |
| ∪ | operação de união | operador de conjunto |

💡 **Pegadinha:** Q e I são **disjuntos** — nenhum número pode ser racional e irracional ao mesmo tempo.

### Relação de inclusão

**Expressão:** N ⊂ Z ⊂ Q ⊂ R e I ⊂ R

💡 **Pegadinha:** a inclusão é em cadeia — se N ⊂ Z e Z ⊂ Q, então N ⊂ Q também. Todo natural é racional.

### Aproximações de irracionais na reta real

**Expressão:** −√3 ≅ −1,7 · √2 ≅ 1,4

💡 **Pegadinha:** √2 não é 1,5 — está mais próximo de 1,4. Alunos frequentemente colocam √2 na metade entre 1 e 2, o que está errado.

---

## SEÇÃO 5 — REPRESENTAÇÕES E SISTEMAS

### Diagrama de Venn dos conjuntos numéricos

- **Nome:** Diagrama de Venn
- **Definição:** representação visual das relações de inclusão entre conjuntos
- **Elementos:** N (círculo menor), Z (envolve N), Q (envolve Z), I (separado de Q), R (envolve Q e I)
- **Regra de leitura:** estar dentro de outro conjunto = ser subconjunto dele
- **Relações:** N ⊂ Z ⊂ Q ⊂ R; I ⊂ R; Q ∩ I = ∅ (conjuntos disjuntos)

### Reta real

- **Nome:** Reta real (ou reta numérica)
- **Definição:** reta em que cada ponto corresponde exatamente a um número real
- **Elementos:** origem (0), direção positiva (direita), direção negativa (esquerda), pontos marcados
- **Regra de construção:** inteiros em posições igualmente espaçadas; irracionais localizados por aproximação decimal
- **Exemplos do material:** −2; −1,5; −√3 (≅ −1,7); −1; −1/2; 0; 1/2; 1; √2 (≅ 1,4); 1,5; 5/2; 3; π (≅ 3,14)

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

| Conjunto | Notação | Definição resumida | Exemplos do livro |
|----------|---------|-------------------|-------------------|
| Naturais | N | Números para contar e o zero | {0; 2; 10; 294} |
| Inteiros | Z | Naturais e seus opostos | {−326; −10; 0; 2; 294} |
| Racionais | Q | Fração a/b (b≠0); decimal exato ou periódico | {−1,75; −1/2; 0; 3/4; 1,3̄; 294} |
| Irracionais | I | Decimal infinito e não periódico | {√2/2; √7; π; √12} |
| Reais | R | União de Q e I | Todos os números |

| Número | N | Z | Q | I | R |
|--------|---|---|---|---|---|
| 0 | ✓ | ✓ | ✓ | — | ✓ |
| −12 | — | ✓ | ✓ | — | ✓ |
| 3/4 | — | — | ✓ | — | ✓ |
| 1,3̄ | — | — | ✓ | — | ✓ |
| √100 = 10 | ✓ | ✓ | ✓ | — | ✓ |
| √7 | — | — | — | ✓ | ✓ |
| π | — | — | — | ✓ | ✓ |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Raiz quadrada nem sempre é irracional**
√4 = 2 (natural!), √9 = 3, √100 = 10. Só é irracional se não resultar em número inteiro. Teste: se √n é inteiro, n é quadrado perfeito.

💡 **Dica 2 — Dízima periódica é racional, não irracional**
0,333... = 1/3 ∈ Q. 0,142857142857... = 1/7 ∈ Q. A periodicidade garante que existe fração equivalente. Irracional = sem periodicidade alguma.

💡 **Dica 3 — Todo inteiro negativo NÃO é natural**
−5 ∈ Z, mas −5 ∉ N. Naturais são só os não-negativos. Pietro errou: "a diferença de dois naturais é sempre inteira" — 3 − 5 = −2, que é inteiro mas não natural.

💡 **Dica 4 — Q e I são disjuntos**
Um número não pode ser racional E irracional ao mesmo tempo. Se souber que é racional, já sabe que não é irracional — e vice-versa. R = Q ∪ I e Q ∩ I = ∅.

💡 **Dica 5 — Posição de irracionais na reta**
√2 ≅ 1,4 (não 1,5!). √3 ≅ 1,7. Use que √1 = 1 e √4 = 2 como âncoras: √2 e √3 estão entre 1 e 2, com √2 mais perto de 1 e √3 mais perto de 2.

💡 **Dica 6 — Massa corporal não é irracional**
A questão do Professor Thiago: "representar nossa massa por um número irracional" está errada. Medidas do cotidiano (massa, preço, saldo) são expressas por racionais — decimais finitos ou aproximações racionais.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

#### Bloco A — Lacunas de dados

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| Metadados | Unidade | Não aparecia no cabeçalho das páginas capturadas | Confirmar que é Unidade 1 no índice do livro |
| QC-1 | Enunciado original | ARIA capturou incorretamente como "1 − 2/3" | Corrigido para "1 + 1/(1 − 2/3)" conforme screenshot |

#### Bloco B — Inconsistências factuais

Nenhuma inconsistência factual detectada no material. O capítulo apresenta definições padrão e corretas dos conjuntos numéricos.

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

- **Números naturais (N)**
  - Definição: `______` (números que usamos para contar e o zero)
  - Notação: `______` (N)

- **Números inteiros (Z)**
  - Definição: `______` (naturais e seus opostos — incluindo negativos)
  - Notação: `______` (Z)

- **Números racionais (Q)**
  - Definição: `______` (podem ser escritos como fração a/b, b ≠ 0)
  - Representação decimal: `______` (exata ou dízima periódica)

- **Números irracionais (I)**
  - Definição: `______` (decimal infinito e não periódico)
  - Exemplo canônico: `______` (π ≈ 3,14159...)

- **Números reais (R)**
  - Composição: `______` (união de Q e I)
  - Expressão simbólica: `______` (R = Q ∪ I)

#### Bloco 2 — Fórmulas e Propriedades

- **Definição formal de racional**
  - Expressão: `______` (Q = {a/b | a ∈ Z, b ∈ Z, b ≠ 0})
  - Condição obrigatória: `______` (b ≠ 0)

- **Relação de inclusão**
  - Expressão: `______` (N ⊂ Z ⊂ Q ⊂ R e I ⊂ R)

- **Aproximações na reta real**
  - √2 ≅ `______` (1,4)
  - −√3 ≅ `______` (−1,7)

#### Bloco 3 — Lacunas para Warm-Up

1. Os conjuntos numéricos têm por objetivo `______` os números.
*(resposta: organizar todos os números, separando-os em conjuntos)*

2. Um número racional pode ter representação decimal `______` ou `______`.
*(resposta: exata / dízima periódica)*

3. O número π pertence ao conjunto `______` porque sua representação decimal é `______`.
*(resposta: I (irracionais) / infinita e não periódica)*

4. Complete: N ⊂ `______` ⊂ `______` ⊂ R e `______` ⊂ R.
*(resposta: Z / Q / I)*

5. O conjunto dos números reais é formado pela `______` dos conjuntos Q e I.
*(resposta: união — R = Q ∪ I)*

6. √100 pertence aos conjuntos `______` porque √100 = `______`.
*(resposta: N, Z, Q e R / 10)*

7. Na reta real, √2 está localizado entre `______` e `______`, com valor aproximado `______`.
*(resposta: 1 / 2 / 1,4)*

8. O código de barras usa o sistema `______`, que representa informações como sequências de `______` e `______`.
*(resposta: binário / zeros / uns)*

#### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Conjunto N (naturais) | Números usados para contar e o zero: `______` → {0, 1, 2, 3, ...} |
| Conjunto Z (inteiros) | Naturais e seus opostos: `______` → {..., −2, −1, 0, 1, 2, ...} |
| Conjunto Q (racionais) | Escritos como fração a/b, b ≠ 0 — decimal `______` ou `______` → exata; dízima periódica |
| Conjunto I (irracionais) | Decimal `______` e `______` → infinito; não periódico |
| Conjunto R (reais) | União de Q e I: `______` → R = Q ∪ I |
| Relação de inclusão | `______` ⊂ `______` ⊂ `______` ⊂ R → N ⊂ Z ⊂ Q ⊂ R |
| Definição formal de Q | Q = {a/b \| a ∈ Z, b ∈ Z, b `______`} → b ≠ 0 |
| Aproximação de √2 na reta real | √2 ≅ `______`, entre os inteiros `______` e `______` → 1,4; 1; 2 |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

### Síntese do Livro — Conjuntos Numéricos

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| Caixa superior esquerda | Números naturais (N) — São os números que usamos para contar (0, 1, 2, 3, 4, ...) | — (já preenchido) |
| Caixa superior direita | Números inteiros (Z) — Correspondem aos números naturais e seus opostos: números negativos (..., −3, −2, −1, 0, 1, 2, 3, 4, ...) | — (já preenchido) |
| Caixa central esquerda | Números racionais (Q) — São todos os números que podem ser escritos como uma razão de dois números inteiros. Representação: decimal exata ou dízima periódica. Ex: 3/4 = 0,75; 4/3 = 1,333... = 1,3̄ | — (já preenchido) |
| Caixa central direita | Números irracionais (I) — São todos os números que não podem ser escritos na forma de fração. Decimal infinita e não periódica. | — (já preenchido) |
| Pílula central | Conjuntos numéricos | — (já preenchido) |
| Caixa inferior — título | Números reais (R) | — (já preenchido) |
| Caixa inferior — definição | `______` | A união dos números racionais e irracionais forma o conjunto dos números reais |
| Diagrama de Venn interno | N dentro de Z, Z dentro de Q, I separado, R envolvendo tudo | — (visual — não há lacuna textual) |
| Nota abaixo do diagrama | `______` | Todo número real pode ser representado na reta numérica (inclusive os números naturais, inteiros e racionais) |
| Reta numérica | −√5; 0,75; 1,333...; e; π marcados entre −3 e 3 | — (visual) |

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Gabarito | Obs. |
|---|---|---|---|---|---|
| Q-1 | Classificar 16 números em N, Z, Q, I, R | Dis | F | N: 234, 2, 11, 4, 1, 0, 15, 49, 18 · Z: acrescenta −7, −1, −2, −28 · Q: acrescenta −2,8; 0,2; 3,45 · I: nenhum · R: todos | — |
| Q-2 | Qual aluno errou frase sobre conjuntos? | MC | F | a) Vinícius — divisão de inteiros não é sempre inteira (ex: 1÷2 = 0,5 ∈ Q) | — |
| Q-3 | Quais afirmações sobre conjuntos são verdadeiras? | MC | M | b) II e III — II: existem inteiros não naturais (ex: −1) ✓ · III: existem reais não racionais (ex: √2) ✓ | — |
| Q-4 | Qual frase do professor Thiago está incorreta? | Dis | M | IV — massa corporal é expressa por racional (decimal finito ou aproximação), não por irracional | — |
| QC-1 | Valor de 1 + 1/(1 − 2/3) | MC | M | e) 4 — 1 − 2/3 = 1/3; 1/(1/3) = 3; 1 + 3 = 4 | OBMEP |
| Q-5 | (0,6666...)² = ? | MC | M | e) 0,4444... — 0,6̄ = 2/3; (2/3)² = 4/9 = 0,4̄ | — |
| QC-2 | Afirmações sobre a e b irracionais | MC | M | c) somente I e III são verdadeiras — I: √2 × √2 = 2 (racional!) ✗ · II: √2 + (−√2) = 0 (racional!) ✗ · III: a − b pode ser racional ✓ | Fatec-SP |
| Q-6 | Calcular 4 operações com decimais/frações | Cal | F | a) 3,0 · b) −0,17 · c) 3,6 · d) 0,9375 | — |
| Q-7 | Valor de 1/4 + 0,222... | Cal | M | 0,222... = 2/9; 1/4 + 2/9 = 9/36 + 8/36 = 17/36 ≅ 0,472... | — |
| Q-8 | a·b·c com a=4, b=1, c=3 | MC | F | b) natural, cujo módulo é igual a 8 — 4×1×3 = 12? ⚠️ ver alerta abaixo | ⚠️ |
| QC-3 | 0,999... é igual a? | MC | M | a) R é igual a 1 — 0,999... = 9/9 = 1 (dízima periódica de razão 9) | Vunesp |
| Q-9 | João vs Tomás: quem comeu mais bolo? | MC | F | d) Os dois comeram a mesma quantidade — metade da terça parte = 1/2 × 1/3 = 1/6; terça parte da metade = 1/3 × 1/2 = 1/6 | — |
| Q-10 | 0,5² > ou < 1,40 − 0,89? | Cal | F | 0,5² = 0,25; 1,40 − 0,89 = 0,51; portanto 0,25 < 0,51 | — |
| Q-11 | 5,444... − 2,777... | Cal | M | 5,4̄ = 49/9; 2,7̄ = 25/9; 49/9 − 25/9 = 24/9 = 8/3 = 2,6̄ | — |
| QC-4 | Quadriculado 2×2 com produtos L1=6, L2=8, C1=4, C2=12 | MC | D | c) 13 — os 4 números são 1, 4, 3, 2 (ou combinações); soma = 1+4+3+2 = 10? ⚠️ ver figura | ⚠️ Canguru 2024 |
| QC-5 | Próximo número na sequência com símbolos | MC | D | ver resolução abaixo | Canguru 2023 |
| Q-12 | Localizar 3⅛; 1,5; −3/2; −2,2 nas letras da reta | MC | M | d) F, E, B e D — 3⅛ = 3,125 → F (entre 3 e +∞) · 1,5 → E (entre 1 e 2) · −3/2 = −1,5 → B (entre −2 e −1) · −2,2 → D (entre −3 e −2) | — |
| Q-13 | Dispor √2; 11/4; 3,1; −1/5; −1,5 na reta real | Const | F | √2≅1,4 · 11/4=2,75 · 3,1 · −1/5=−0,2 · −1,5 — da esquerda: −1,5; −0,2; √2; 2,75; 3,1 | — |

⚠️ **Q-8 — Alerta:** a expressão é `a·b·c` com a=4, b=1, c=3, resultando em 4×1×3 = 12, não 8. A alternativa b) diz "módulo igual a 8" — possível erro de digitação no livro (talvez a expressão original seja diferente). O tutor deve apresentar a questão e deixar o aluno calcular, alertando que pode haver inconsistência.

⚠️ **QC-4 — Alerta:** os 4 números inteiros positivos diferentes cujos produtos por linha/coluna são L1=6, L2=8, C1=4, C2=12: tentativa 1×6, 4×3 → L1=1×6=6✓, L2=4×3=12≠8. Tentativa 2×3, 1×8 → não fecha. Tentativa 1×6, 2×4 → L1=6✓, L2=8✓, C1=1×2=2≠4. Tentativa 2×3, 4×2 → L1=6✓, L2=8✓, C1=2×4=8≠4. Tentativa 3×2, 4×2: repetição. Correto: 1, 6, 4, 2 → L1=1×6=6✓, L2=4×2=8✓, C1=1×4=4✓, C2=6×2=12✓ — soma = 1+6+4+2 = 13 ✓ → alternativa c).

**QC-5 — Resolução:** □♦♦=100, ▽△△=211, ▽△□=212. Os algarismos são □=0, ♦=1, △=2, ▽=... aguarda o próximo número 213 = ▽△▽ → alternativa e).

#### Bloco B — Questões modelo originais

**QM-1** · múltipla escolha · médio · inspirada em: Q-3

Analise as afirmações sobre números reais:
I. Todo número natural é racional.
II. Existe número inteiro que não é natural.
III. Todo número irracional é real.
IV. A dízima 0,142857142857... é irracional.

Quais são verdadeiras?
a) I e IV  b) I, II e III  c) II e IV  d) I, II, III e IV

✅ Gabarito: b) I, II e III
📝 Resolução: I ✓ (N ⊂ Z ⊂ Q ⊂ R) · II ✓ (ex: −3 ∈ Z, −3 ∉ N) · III ✓ (I ⊂ R) · IV ✗ (0,142857... é dízima periódica = 1/7, portanto racional)
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · múltipla escolha · médio · inspirada em: Q-2

Cinco estudantes fizeram afirmações sobre conjuntos numéricos:
- Ana: Todo número racional pode ser escrito como fração.
- Bruno: π é um número racional porque tem representação decimal.
- Carla: √9 é um número irracional.
- Diego: −7 pertence a Z mas não pertence a N.
- Elisa: Todo número real pertence a Q ou a I.

Quem errou?
a) Ana  b) Bruno e Carla  c) Carla  d) Diego

✅ Gabarito: b) Bruno e Carla
📝 Resolução: Bruno errou — π tem decimal infinito e não periódico, é irracional. Carla errou — √9 = 3 ∈ N ⊂ Q. Ana ✓, Diego ✓, Elisa ✓.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-3** · cálculo · médio · inspirada em: Q-11

Calcule o valor exato de 3,666... + 1,333... e diga a qual conjunto o resultado pertence.

✅ Gabarito: 3,6̄ = 11/3; 1,3̄ = 4/3; 11/3 + 4/3 = 15/3 = 5 ∈ N ⊂ Z ⊂ Q ⊂ R
📝 Resolução: converter cada dízima em fração, somar, simplificar. Resultado 5 é natural.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · múltipla escolha · difícil · estilo concurso · inspirada em: QC-2

Sejam x = √3 e y = −√3. Analise:
I. x + y é um número natural.
II. x · y é um número racional.
III. x² é um número irracional.

Podemos concluir que:
a) Somente II é verdadeira.
b) I e II são verdadeiras.
c) II e III são verdadeiras.
d) As três são falsas.

✅ Gabarito: b) I e II são verdadeiras
📝 Resolução: x + y = √3 + (−√3) = 0 ∈ N ✓ · x · y = √3 × (−√3) = −3 ∈ Z ⊂ Q ✓ · x² = (√3)² = 3 ∈ N ⊂ Q, não irracional ✗
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-5** · dissertativa · médio-difícil · inspirada em: Q-4

Um aplicativo de mensagens armazena os seguintes dados de um usuário: número de mensagens enviadas, saldo de créditos (pode ser negativo), avaliação média (ex: 4,7 estrelas) e tempo médio de resposta em segundos (ex: 0,333... min).

a) Indique o menor conjunto numérico ao qual cada dado pertence.
b) Justifique por que nenhum desses dados seria melhor representado por um número irracional.

✅ Gabarito:
a) Mensagens: N · Saldo: Z (ou Q) · Avaliação: Q (decimal finito) · Tempo: Q (dízima periódica = 1/3)
b) Dados do cotidiano são medidos ou contados — sempre resulam em valores racionais (inteiros, frações ou decimais finitos/periódicos). Irracionais surgem em contextos geométricos (π, √2) ou em constantes matemáticas, não em contagens ou medições práticas cotidianas.
⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: conjuntos
Hierarquia de inclusão dos conjuntos numéricos com exemplos de cada conjunto.

<svg width="100%" viewBox="0 0 680 420" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <style>
    .c-purple{fill:#6B46C1;} .c-teal{fill:#0D7377;} .c-amber{fill:#B45309;}
    .c-green{fill:#15803D;} .c-coral{fill:#C05621;} .c-gray{fill:#4B5563;}
    .t{font:14px 'Inter',sans-serif;fill:#fff;text-anchor:middle;}
    .ts{font:12px 'Inter',sans-serif;fill:#374151;text-anchor:middle;}
    .th{font:14px 'Inter',sans-serif;font-weight:700;fill:#fff;text-anchor:middle;}
    @media(prefers-color-scheme:dark){.ts{fill:#D1D5DB;}}
  </style>
</defs>

<!-- R — fundo geral -->
<rect x="20" y="20" width="640" height="380" rx="14" class="c-purple" opacity="0.15"/>
<rect x="20" y="20" width="640" height="380" rx="14" fill="none" stroke="#6B46C1" stroke-width="2"/>
<text x="640" y="48" font-size="13" font-weight="700" fill="#6B46C1" text-anchor="end" font-family="Inter">R — Reais</text>
<text x="630" y="390" font-size="11" fill="#6B46C1" text-anchor="end" font-family="Inter">Todos os números</text>

<!-- I — irracionais (lado direito) -->
<rect x="430" y="60" width="210" height="280" rx="12" class="c-coral" opacity="0.18"/>
<rect x="430" y="60" width="210" height="280" rx="12" fill="none" stroke="#C05621" stroke-width="2"/>
<text x="535" y="85" class="th" fill="#C05621">I — Irracionais</text>
<text x="535" y="108" class="ts">Decimal infinito</text>
<text x="535" y="124" class="ts">e não periódico</text>
<text x="535" y="155" class="ts">√2/2 ≈ 0,707...</text>
<text x="535" y="173" class="ts">√7 ≈ 2,645...</text>
<text x="535" y="191" class="ts">π ≈ 3,14159...</text>
<text x="535" y="209" class="ts">√12 ≈ 3,464...</text>

<!-- Q — racionais (cobre Z e N) -->
<rect x="40" y="60" width="370" height="280" rx="12" class="c-teal" opacity="0.15"/>
<rect x="40" y="60" width="370" height="280" rx="12" fill="none" stroke="#0D7377" stroke-width="2"/>
<text x="225" y="85" class="th" fill="#0D7377">Q — Racionais</text>
<text x="350" y="108" class="ts">−1,75 · 3/4</text>
<text x="350" y="126" class="ts">1,3̄ · 12,64</text>

<!-- Z — inteiros -->
<rect x="60" y="110" width="250" height="200" rx="12" class="c-amber" opacity="0.20"/>
<rect x="60" y="110" width="250" height="200" rx="12" fill="none" stroke="#B45309" stroke-width="2"/>
<text x="185" y="135" class="th" fill="#B45309">Z — Inteiros</text>
<text x="270" y="158" class="ts">−326 · −12</text>

<!-- N — naturais -->
<rect x="80" y="155" width="140" height="130" rx="12" class="c-green" opacity="0.25"/>
<rect x="80" y="155" width="140" height="130" rx="12" fill="none" stroke="#15803D" stroke-width="2"/>
<text x="150" y="178" class="th" fill="#15803D">N — Naturais</text>
<text x="150" y="202" class="ts">0 · 1 · 2 · 3</text>
<text x="150" y="220" class="ts">10 · 294</text>
<text x="150" y="245" class="ts">√100 = 10</text>
<text x="150" y="263" class="ts">4/2 = 2</text>

<!-- Seta N subset Z -->
<line x1="220" y1="220" x2="270" y2="220" stroke="#B45309" stroke-width="1.5" marker-end="url(#arr)" stroke-dasharray="4,3"/>
<text x="245" y="213" font-size="11" fill="#B45309" text-anchor="middle" font-family="Inter">⊂</text>

<!-- Seta Z subset Q -->
<line x1="310" y1="200" x2="350" y2="180" stroke="#0D7377" stroke-width="1.5" marker-end="url(#arr)" stroke-dasharray="4,3"/>
<text x="335" y="195" font-size="11" fill="#0D7377" font-family="Inter">⊂</text>

<!-- Seta Q e I subset R -->
<text x="340" y="370" font-size="12" fill="#6B46C1" text-anchor="middle" font-family="Inter">Q ∪ I = R</text>
<text x="340" y="388" font-size="11" fill="#6B46C1" text-anchor="middle" font-family="Inter">Q ∩ I = ∅</text>
</svg>

---

### DIAGRAMA: reta_numerica
Reta real com posicionamento de racionais e irracionais, incluindo aproximações de √2 e −√3.

<svg width="100%" viewBox="0 0 680 180" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <style>
    .ts2{font:12px 'Inter',sans-serif;fill:#374151;text-anchor:middle;}
    .tc{font:11px 'Inter',sans-serif;fill:#C05621;text-anchor:middle;}
    @media(prefers-color-scheme:dark){.ts2{fill:#D1D5DB;}.tc{fill:#F97316;}}
  </style>
</defs>

<!-- Reta principal -->
<line x1="30" y1="90" x2="650" y2="90" stroke="#4B5563" stroke-width="2" marker-end="url(#arr2)"/>
<line x1="30" y1="90" x2="30" y2="90" stroke="#4B5563" stroke-width="2" marker-start="url(#arr2)"/>

<!-- Escala: cada unidade = 80px, origem em x=340 (valor 0) -->
<!-- Inteiros: −3=100, −2=180, −1=260, 0=340, 1=420, 2=500, 3=580 -->

<!-- Marcas dos inteiros -->
<line x1="100" y1="83" x2="100" y2="97" stroke="#4B5563" stroke-width="2"/>
<text x="100" y="112" class="ts2">−3</text>
<line x1="180" y1="83" x2="180" y2="97" stroke="#4B5563" stroke-width="2"/>
<text x="180" y="112" class="ts2">−2</text>
<line x1="260" y1="83" x2="260" y2="97" stroke="#4B5563" stroke-width="2"/>
<text x="260" y="112" class="ts2">−1</text>
<line x1="340" y1="83" x2="340" y2="97" stroke="#4B5563" stroke-width="2"/>
<text x="340" y="112" class="ts2">0</text>
<line x1="420" y1="83" x2="420" y2="97" stroke="#4B5563" stroke-width="2"/>
<text x="420" y="112" class="ts2">1</text>
<line x1="500" y1="83" x2="500" y2="97" stroke="#4B5563" stroke-width="2"/>
<text x="500" y="112" class="ts2">2</text>
<line x1="580" y1="83" x2="580" y2="97" stroke="#4B5563" stroke-width="2"/>
<text x="580" y="112" class="ts2">3</text>

<!-- −1,5 = x=220 -->
<circle cx="220" cy="90" r="3" fill="#0D7377"/>
<text x="220" y="130" class="ts2" fill="#0D7377">−1,5</text>

<!-- 1,5 = x=460 -->
<circle cx="460" cy="90" r="3" fill="#0D7377"/>
<text x="460" y="130" class="ts2" fill="#0D7377">1,5</text>

<!-- −√3 ≅ −1,7 = x=204 -->
<circle cx="204" cy="90" r="5" fill="#C05621"/>
<line x1="204" y1="75" x2="204" y2="55" stroke="#C05621" stroke-width="1.5"/>
<text x="204" y="48" class="tc">−√3 ≅ −1,7</text>

<!-- √2 ≅ 1,4 = x=452 -->
<circle cx="452" cy="90" r="5" fill="#C05621"/>
<line x1="452" y1="75" x2="452" y2="45" stroke="#C05621" stroke-width="1.5"/>
<text x="452" y="38" class="tc">√2 ≅ 1,4</text>

<!-- π ≅ 3,14 = x=591 -->
<circle cx="591" cy="90" r="5" fill="#C05621"/>
<line x1="591" y1="105" x2="591" y2="145" stroke="#C05621" stroke-width="1.5"/>
<text x="591" y="158" class="tc">π ≅ 3,14</text>

<!-- Legenda -->
<circle cx="40" cy="165" r="5" fill="#C05621"/>
<text x="52" y="169" font-size="11" fill="#C05621" font-family="Inter">Irracionais</text>
<circle cx="130" cy="165" r="3" fill="#0D7377"/>
<text x="142" y="169" font-size="11" fill="#0D7377" font-family="Inter">Racionais</text>
</svg>

---

### DIAGRAMA: formulas
Fórmulas e expressões principais do capítulo com variáveis e condições.

<svg width="100%" viewBox="0 0 680 260" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr3" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <style>
    .t3{font:14px 'Inter',sans-serif;fill:#fff;text-anchor:middle;}
    .ts3{font:12px 'Inter',sans-serif;fill:#374151;text-anchor:start;}
    .tc3{font:12px 'Inter',sans-serif;fill:#C05621;text-anchor:middle;}
    @media(prefers-color-scheme:dark){.ts3{fill:#D1D5DB;}}
  </style>
</defs>

<!-- Fórmula 1: Q = {a/b | a∈Z, b∈Z, b≠0} -->
<rect x="20" y="20" width="200" height="44" rx="8" class="c-purple"/>
<text x="120" y="47" class="t3">Número Racional</text>
<line x1="220" y1="42" x2="270" y2="42" stroke="#6B46C1" stroke-width="2" marker-end="url(#arr3)"/>
<rect x="270" y="20" width="230" height="44" rx="8" class="c-teal"/>
<text x="385" y="38" class="t3">Q = {a/b | a∈Z,</text>
<text x="385" y="56" class="t3">b∈Z, b≠0}</text>

<!-- Variáveis -->
<text x="270" y="85" class="ts3">• a = numerador (inteiro)</text>
<text x="270" y="103" class="ts3">• b = denominador (inteiro, b ≠ 0)</text>

<!-- Pegadinha 1 -->
<rect x="270" y="115" width="390" height="30" rx="6" class="c-coral" opacity="0.15"/>
<text x="465" y="135" class="tc3">⚠️ b=0 torna a fração indefinida — divisão por zero não existe</text>

<!-- Fórmula 2: R = Q ∪ I -->
<rect x="20" y="160" width="200" height="44" rx="8" class="c-purple"/>
<text x="120" y="187" class="t3">Números Reais</text>
<line x1="220" y1="182" x2="270" y2="182" stroke="#6B46C1" stroke-width="2" marker-end="url(#arr3)"/>
<rect x="270" y="160" width="160" height="44" rx="8" class="c-teal"/>
<text x="350" y="187" class="t3">R = Q ∪ I</text>

<!-- Variáveis -->
<text x="445" y="173" class="ts3">Q ∩ I = ∅</text>
<text x="445" y="191" class="ts3">(disjuntos)</text>

<!-- Pegadinha 2 -->
<rect x="20" y="220" width="640" height="30" rx="6" class="c-coral" opacity="0.15"/>
<text x="340" y="240" class="tc3">⚠️ Um número NÃO pode ser racional e irracional ao mesmo tempo</text>
</svg>
