# DIAGRAMAS DISPONÍVEIS — mat-1-8

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Feixe de paralelas e transversais | `DIAGRAMA: feixe_paralelas` | Ao apresentar o Teorema de Tales e a proporção a/b = c/d |
| Semelhança de triângulos | `DIAGRAMA: semelhanca_triangulos` | Ao apresentar razão de semelhança e critério AA |
| Bissetriz interna | `DIAGRAMA: bissetriz_interna` | Ao apresentar o teorema da bissetriz como consequência |
| Hierarquia de aplicações | `DIAGRAMA: aplicacoes_tales` | Ao introduzir aplicações práticas (sombras, pontes, alturas) |

### Tabelas markdown (Seção 6):
- Tabela de fórmulas principais (Seção 4)
- Tabela síntese do capítulo (Seção 9, Bloco 4)
- Catálogo de questões (Seção 11, Bloco A)

### Nota ao Professor:
Para cada diagrama SVG: leia o bloco `DIAGRAMA:` da Seção 12 e passe ao Visualizer. As tabelas das Seções 6 e 9 são apresentadas como markdown no chat.

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 8
- Tema: Teorema de Tales
- Perfil: geometria
- Fórmulas principais:
    a/b = c/d  (proporção entre segmentos — Teorema de Tales)
    a/b = (a+c)/(b+d)  (propriedade da soma dos termos)
    △ABC ~ △DEF → A/D = B/E = C/F = k  (razão de semelhança)
    c/x = b/y  (Teorema da Bissetriz Interna)
- Matemáticos citados: Tales de Mileto (626 a.C.–546 a.C.)
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### 🔵 Bloco 1 — Feixe de Retas Paralelas e o Teorema de Tales

O **Teorema de Tales** afirma que quando um conjunto de retas paralelas é cortado por duas retas transversais, os segmentos determinados em cada transversal são **proporcionais entre si**. Em outras palavras: a razão entre dois segmentos consecutivos de uma transversal é igual à razão entre os segmentos correspondentes da outra transversal.

**Expressão simbólica:**

$$\frac{a}{b} = \frac{c}{d}$$

onde $$a$$ e $$b$$ são segmentos consecutivos na primeira transversal, e $$c$$ e $$d$$ são os segmentos correspondentes na segunda.

**Situação real:** Imagine que raios de sol (paralelos) incidem sobre o chão. Uma pessoa de 1,60 m projeta sombra de 1,30 m, enquanto um poste projeta sombra de 3,25 m. Pela proporção de Tales:

$$\frac{1{,}60}{1{,}30} = \frac{x}{3{,}25} \Rightarrow x = 4 \text{ m}$$

---

### 🔵 Bloco 2 — Propriedade da Soma dos Termos da Proporção

Uma propriedade poderosa que acompanha o Teorema de Tales é a **propriedade da soma dos termos**: se dois pares de segmentos são proporcionais, a soma dos numeradores e a soma dos denominadores também formam uma proporção com o mesmo valor:

$$\frac{a}{b} = \frac{c}{d} \Rightarrow \frac{a}{b} = \frac{a+c}{b+d}$$

**Aplicação direta:** Quando se conhece a soma $$x + y$$ e a proporção $$x/y = 4/6$$, pode-se calcular cada segmento sem montar um sistema. Por exemplo, com $$x + y = 9$$ cm:

$$x = \frac{4 \times 9}{10} = 3{,}6 \text{ cm}, \quad y = \frac{6 \times 9}{10} = 5{,}4 \text{ cm}$$

---

### 🔵 Bloco 3 — Semelhança de Triângulos e Razão de Semelhança

Dois triângulos são **semelhantes** ($$\sim$$) quando têm ângulos correspondentes iguais e lados homólogos proporcionais. O critério mais simples é o **AA (ângulo-ângulo):** basta dois ângulos correspondentes iguais — o terceiro é automaticamente igual, pois a soma dos ângulos internos de qualquer triângulo é 180°.

A **razão de semelhança** $$k$$ é o valor constante entre cada par de lados correspondentes:

$$\triangle ABC \sim \triangle DEF \Rightarrow \frac{AB}{DE} = \frac{BC}{EF} = \frac{AC}{DF} = k$$

**Lados homólogos** são aqueles opostos a ângulos iguais nas duas figuras.

---

### 🔵 Bloco 4 — Teorema da Bissetriz Interna (Síntese do Livro)

A imagem da Síntese revela um resultado importante apresentado como **consequência do Teorema de Tales**: a bissetriz de um ângulo interno de um triângulo divide o lado oposto em dois segmentos $$x$$ e $$y$$ tais que:

$$\frac{c}{x} = \frac{b}{y}$$

onde $$c$$ e $$b$$ são os lados adjacentes ao ângulo bissectado. Isso significa que a bissetriz divide o lado oposto **proporcionalmente aos lados adjacentes**.

---

### 🔵 Bloco 5 — Aplicações Práticas

O Teorema de Tales é uma ferramenta de **medição indireta**: sempre que objetos ou distâncias não podem ser medidos diretamente, monta-se uma configuração de paralelas e transversais (com sombras, retas auxiliares, plantas de terrenos, cabos de pontes) e resolve-se a proporção resultante.

**Exemplos do material:**
- Altura de postes/árvores via sombras
- Comprimento de pontes via triângulos auxiliares
- Comprimento de dentes via Fórmula de Bragman (radiografia)
- Dimensionamento de antenas 5G

---

## SEÇÃO 3 — MATEMÁTICOS E HISTÓRIA DA MATEMÁTICA

### Tales de Mileto (626 a.C.–546 a.C.)

**Área:** Geometria dedutiva, Filosofia Natural

**Contribuição no capítulo:** Considerado o primeiro dos Sete Sábios da Grécia Antiga. Realizou as primeiras organizações dedutivas da Geometria. Demonstrou que os ângulos da base de um triângulo isósceles são iguais e que o diâmetro divide o círculo em duas partes iguais. Previu a data de um eclipse solar em 585 a.C.

**O que desenvolveu:** O Teorema de Tales — relação de proporcionalidade entre segmentos determinados por retas paralelas sobre transversais.

**Contexto histórico:** Grécia Antiga, século VI a.C. Tales é considerado o primeiro filósofo ocidental e um dos fundadores do pensamento racional e matemático dedutivo, rompendo com explicações mitológicas da natureza.

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Propriedade 1 — Proporção entre segmentos (Teorema de Tales)

**Expressão:**

$$\frac{a}{b} = \frac{c}{d}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$a$$ | Segmento na 1ª transversal (parte superior) | Real positivo |
| $$b$$ | Segmento na 1ª transversal (parte inferior) | Real positivo |
| $$c$$ | Segmento correspondente na 2ª transversal (parte superior) | Real positivo |
| $$d$$ | Segmento correspondente na 2ª transversal (parte inferior) | Real positivo |

**Válida quando:** Feixe de retas paralelas cortado por duas transversais; os segmentos devem ser **correspondentes** (determinados pelas mesmas paralelas).

**Caso especial:** A proporção vale mesmo quando as transversais se cruzam entre as paralelas — os segmentos continuam proporcionais.

💡 **Pegadinha:** Confundir quais segmentos são "correspondentes". Sempre verifique se os segmentos comparados estão entre **as mesmas duas paralelas** nas duas transversais.

---

### Propriedade 2 — Soma dos termos da proporção

**Expressão:**

$$\frac{a}{b} = \frac{c}{d} \Rightarrow \frac{a}{b} = \frac{a+c}{b+d}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$a+c$$ | Soma dos antecedentes (segmentos totais de uma transversal) | Real positivo |
| $$b+d$$ | Soma dos consequentes (segmentos totais da outra transversal) | Real positivo |

**Válida quando:** A proporção $$a/b = c/d$$ já está estabelecida pelo Teorema de Tales.

💡 **Pegadinha:** Esta propriedade só vale quando os segmentos são da **mesma configuração de paralelas**. Não se pode somar segmentos de transversais diferentes entre si.

---

### Propriedade 3 — Razão de semelhança

**Expressão:**

$$k = \frac{\text{lado do triângulo imagem}}{\text{lado do triângulo original}}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$k$$ | Razão de semelhança (constante) | Real positivo |

**Válida quando:** Dois triângulos são semelhantes (ângulos correspondentes iguais).

💡 **Pegadinha:** A ordem importa! $$k = AB/DE \neq DE/AB$$. Se o aluno inverter a razão, o resultado de qualquer medida calculada também fica invertido.

---

### Propriedade 4 — Teorema da Bissetriz Interna

**Expressão:**

$$\frac{c}{x} = \frac{b}{y}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$c$$ | Lado do triângulo adjacente ao ângulo bissectado (esquerdo) | Real positivo |
| $$b$$ | Lado do triângulo adjacente ao ângulo bissectado (direito) | Real positivo |
| $$x$$ | Segmento do lado oposto à esquerda do pé da bissetriz | Real positivo |
| $$y$$ | Segmento do lado oposto à direita do pé da bissetriz | Real positivo |

**Válida quando:** A bissetriz de um ângulo interno de um triângulo divide o lado oposto nos pontos $$x$$ e $$y$$.

💡 **Pegadinha:** Muitos alunos pensam que a bissetriz divide o lado oposto **ao meio**. Ela divide **proporcionalmente** aos lados adjacentes — só divide ao meio se os dois lados adjacentes forem iguais (triângulo isósceles).

---

## SEÇÃO 5 — GLOSSÁRIO

| Termo | Definição simples (9º ano) |
|---|---|
| **Feixe de retas paralelas** | Conjunto de retas que são todas paralelas entre si — nunca se cruzam e mantêm a mesma distância. |
| **Retas transversais** | Retas que cruzam o feixe de paralelas, sendo "cortadas" por elas em vários pontos. |
| **Segmentos proporcionais** | Segmentos cujas razões são iguais: se $$a/b = c/d$$, os quatro segmentos são proporcionais. |
| **Razão** | Divisão entre dois valores — indica quantas vezes um é maior que o outro. Ex: razão 2/5. |
| **Proporção** | Igualdade entre duas razões. Ex: $$2/5 = 4/10$$ é uma proporção. |
| **Semelhança de triângulos** | Dois triângulos são semelhantes quando têm ângulos correspondentes iguais e lados homólogos proporcionais. |
| **Lados homólogos** | Lados que ficam em posições correspondentes (opostos aos mesmos ângulos) em dois triângulos semelhantes. |
| **Razão de semelhança (k)** | O valor constante que relaciona os lados correspondentes de dois triângulos semelhantes: $$k = \text{lado}_{\text{imagem}} / \text{lado}_{\text{original}}$$. |
| **Critério AA** | Critério de semelhança: basta dois ângulos correspondentes iguais para garantir que dois triângulos são semelhantes. |
| **Bissetriz interna** | Reta que divide um ângulo interno de um triângulo ao meio. Ela também divide o lado oposto proporcionalmente aos lados adjacentes. |
| **Medição indireta** | Técnica de calcular distâncias ou alturas inacessíveis usando proporções — ex: altura de um poste pela sombra. |

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Tabela 1 — Resumo das Fórmulas do Capítulo

| Situação | Fórmula | Condição |
|---|---|---|
| Feixe de paralelas / 2 transversais | $$\dfrac{a}{b} = \dfrac{c}{d}$$ | r // s // t |
| Soma dos segmentos conhecida | $$\dfrac{a}{b} = \dfrac{a+c}{b+d}$$ | Mesma configuração de paralelas |
| Triângulos semelhantes | $$\dfrac{AB}{DE} = \dfrac{BC}{EF} = k$$ | Critério AA (ou AAA) |
| Bissetriz interna | $$\dfrac{c}{x} = \dfrac{b}{y}$$ | Bissetriz do ângulo A divide BC em x e y |
| Medição indireta (sombras) | $$\dfrac{h_1}{s_1} = \dfrac{h_2}{s_2}$$ | Raios solares paralelos, mesmo instante |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Correspondência é tudo**
Ao montar a proporção do Teorema de Tales, garanta que os segmentos estejam em posições **correspondentes**: o que está entre a 1ª e 2ª paralelas numa transversal deve ser comparado com o que está entre a 1ª e 2ª paralelas na outra. Erro clássico: comparar um segmento inteiro com um parcial.

💡 **Dica 2 — Transversais cruzadas não mudam nada**
Quando as transversais se cruzam **dentro** do feixe de paralelas (configuração "X"), o teorema continua valendo. O aluno não deve se deixar confundir pela aparência da figura — o que importa é quais segmentos estão entre as mesmas paralelas.

💡 **Dica 3 — Use a propriedade da soma quando der x + y**
Sempre que o enunciado fornecer a **soma** de dois segmentos (ex: $$x + y = 9$$), aplique $$\frac{a}{b} = \frac{a+c}{b+d}$$ diretamente. Isso evita montar sistema de equações e economiza tempo de prova.

💡 **Dica 4 — Bissetriz ≠ mediana**
A bissetriz divide o lado oposto proporcionalmente aos lados adjacentes. A mediana divide ao meio. Confundi-las é um erro gravíssimo e frequente. Se o triângulo não for isósceles, a bissetriz **nunca** divide o lado oposto ao meio.

💡 **Dica 5 — Verifique as unidades antes de montar a proporção**
Em problemas com sombras e alturas, as medidas podem aparecer em unidades diferentes (metros e centímetros, por exemplo). Converta tudo para a mesma unidade **antes** de escrever a proporção. Erro de unidade é a causa mais comum de resposta errada em questões fáceis.

💡 **Dica 6 — Critério AA basta para semelhança**
Nunca é preciso verificar os três ângulos. Se dois ângulos de um triângulo são iguais a dois ângulos do outro, o terceiro par automaticamente também é igual (pois a soma é sempre 180°). Em problemas com raios solares, o ângulo reto com o chão + o ângulo de inclinação solar já garantem a semelhança.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

### Bloco A — Lacunas de dados

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| Q-3 (pág. 199) | Medidas exatas dos segmentos | Questão pede medição com régua na figura impressa | Usar a imagem capturada em aula; não há valores numéricos fixos |
| Q-6 (pág. 201) | Medidas dos terrenos B e C | Figura não capturada no `.md` | Capturar imagem da página 201 |
| Q-7 (pág. 201) | Medidas completas do terreno B | Figura parcialmente descrita | Verificar figura da página 201 |
| QC-3 (pág. 214) | Figura do mapa de terrenos I, II, III | Alternativas disponíveis, figura não detalhada | Capturar imagem da página 214 |

---

### Bloco B — Inconsistências factuais

⚠️ **ALERTA 1 — Exercício Resolvido 1a (valores e proporção)**
- **Dado no material (.md):** `2/7 = M/14 → M = 2×14/7 = 2,8 m`
- **Dado correto (imagem do livro):** A figura mostra segmentos `5 m`, `2 m` e `7 m`. A proporção correta é `2/5 = x/7 → x = 2×7/5 = 14/5 = 2,8 m`
- **Problema:** Os valores no `.md` (numeradores 2 e 7, denominador 14) não coincidem com a figura. O resultado final (2,8 m) é correto por coincidência de cálculo, mas a proporção escrita estava errada.
- **Impacto na aula:** Reescrever a proporção correta na lousa: $$\frac{2}{5} = \frac{x}{7}$$

⚠️ **ALERTA 2 — Exercício Resolvido 1b**
- **Dado no material (.md):** `5/8 = M/10 → M = 6,25 cm`
- **Dado correto (imagem do livro):** Segmentos são `3 cm`, `8 cm` e `14 cm`. Proporção: `3/8 = x/14 → x = 3×14/8 = 42/8 = 5,25 cm`
- **Problema:** O `.md` tinha valores e resultado incorretos.
- **Impacto na aula:** Usar $$\frac{3}{8} = \frac{x}{14} \Rightarrow x = 5{,}25$$ cm

⚠️ **ALERTA 3 — Exercício Resolvido 1c**
- **Dado no material (.md):** `p/0,5 = 34/p → p = 21,5 cm` (inconsistente matematicamente: p² = 17 → p ≈ 4,12)
- **Dado correto (imagem do livro):** Segmentos são `5 m`, `6 m`, `x` e `9 m`. Proporção: `5/x = 6/9 → x = 5×9/6 = 45/6 = 7,5 m`
- **Problema:** Os valores do `.md` eram completamente errados para este item.
- **Impacto na aula:** Usar $$\frac{5}{x} = \frac{6}{9} \Rightarrow x = 7{,}5 \text{ m}$$

⚠️ **ALERTA 4 — Exercício Resolvido 1d**
- **Dado no material (.md):** `7/M = 42/34,5 → M = 21,5 cm`
- **Dado correto (imagem do livro):** Segmentos são `10,5 cm`, `7 cm`, `9 cm` e `x`. Proporção: `10,5/x = 7/9 → x = 10,5×9/7 = 94,5/7 = 13,5 cm`
- **Problema:** Valores e resultado do `.md` incorretos.
- **Impacto na aula:** Usar $$\frac{10{,}5}{x} = \frac{7}{9} \Rightarrow x = 13{,}5 \text{ cm}$$

⚠️ **ALERTA 5 — Q-11 (pág. 202): descrição da ponte**
- **Dado no material (.md):** "BD ∥ AE; BO = 5 cm, AD = 15 cm"
- **Dado correto (imagem do livro):** A ponte é identificada pelo segmento **BC** (não AE). Os pontos marcados são A, D, E, B, C com **BD // CE**. Medidas: AB = 55 m, AD = 11 m, AE = 20 m.
- **Impacto na aula:** Usar a figura correta. Proporção: $$\frac{AD}{AB} = \frac{AE}{BC} \Rightarrow \frac{11}{55} = \frac{20}{BC} \Rightarrow BC = 100 \text{ m}$$

⚠️ **ALERTA 6 — QC-4 (Vunesp 2015): medidas da figura**
- **Dado no material (.md):** "medidas: 70 cm, 35 mm, 36 mm, 10 mm"
- **Dado correto (imagem do livro):** A figura mostra: EF = 10 cm (entre retas r e s), AB = 15 cm (entre retas s e t), com alturas 15 cm e 15 cm nas transversais paralelas u e v, e FE = 10 cm no topo.
- **Impacto na aula:** Verificar a resolução completa com os valores da imagem antes de apresentar em aula.

⚠️ **ALERTA 7 — QC-5 (Unesp): distância entre pontos**
- **Dado no material (.md):** "dois pontos luminosos a 5 mm de distância"
- **Dado correto (imagem do livro):** A distância entre os dois pontos luminosos é **1 mm** (não 5 mm). O diâmetro do olho é 15 mm e a separação na retina é 0,005 mm.
- **Resolução correta:** $$\frac{1}{x} = \frac{0{,}005}{15} \Rightarrow x = \frac{15}{0{,}005} = 3000 \text{ mm} = 3 \text{ m}$$ → **Alternativa c) 3**
- **Impacto na aula:** Corrigir o valor no enunciado antes de apresentar a questão.

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

### Bloco 1 — Conceitos e Definições

- **Teorema de Tales**
  - Definição: `______` *(Um feixe de retas paralelas determina, sobre duas retas transversais, segmentos de reta proporcionais)*
  - Notação: `______` *( $$\frac{a}{b} = \frac{c}{d}$$ )*

- **Semelhança de triângulos**
  - Definição: `______` *(Dois triângulos são semelhantes quando possuem ângulos correspondentes congruentes e lados homólogos proporcionais)*
  - Símbolo: `______` *( $$\sim$$ )*

- **Lados homólogos**
  - Definição: `______` *(Lados que ocupam posições correspondentes — opostos a ângulos iguais — em dois triângulos semelhantes)*

- **Bissetriz interna**
  - Propriedade: `______` *(Divide o lado oposto proporcionalmente aos lados adjacentes ao ângulo bissectado)*

---

### Bloco 2 — Fórmulas e Propriedades

- **Proporção de Tales**
  - Expressão: `______` *( $$\frac{a}{b} = \frac{c}{d}$$ )*
  - Condição: `______` *(Feixe de retas paralelas cortado por duas transversais)*

- **Propriedade da soma dos termos**
  - Expressão: `______` *( $$\frac{a}{b} = \frac{a+c}{b+d}$$ )*
  - Uso principal: `______` *(Quando se conhece a soma dos dois segmentos de uma transversal)*

- **Razão de semelhança k**
  - Expressão: `______` *( $$k = \dfrac{\text{lado imagem}}{\text{lado original}}$$ )*
  - Característica: `______` *(É uma constante — o mesmo valor para todos os pares de lados correspondentes)*

- **Bissetriz interna**
  - Expressão: `______` *( $$\frac{c}{x} = \frac{b}{y}$$ )*

---

### Bloco 3 — Lacunas para Warm-Up

1. O Teorema de Tales afirma que um feixe de retas paralelas determina, sobre duas retas transversais, segmentos `______`.
*(resposta: proporcionais)*

2. A expressão simbólica do Teorema de Tales para duas transversais é `______`.
*(resposta: $$\frac{a}{b} = \frac{c}{d}$$)*

3. Dois triângulos são semelhantes quando possuem `______` correspondentes congruentes e `______` proporcionais.
*(resposta: ângulos; lados homólogos)*

4. Tales de Mileto viveu aproximadamente entre `______` e `______` a.C., sendo considerado o primeiro dos `______` Sábios da Grécia Antiga.
*(resposta: 626; 546; Sete)*

5. Se um menino de 1,60 m projeta sombra de 1,30 m e um poste projeta sombra de 3,25 m, a altura do poste é `______` metros.
*(resposta: 4 m)*

6. A propriedade da soma dos termos estabelece que se $$\frac{a}{b} = \frac{c}{d}$$, então também vale que `______`.
*(resposta: $$\frac{a}{b} = \frac{a+c}{b+d}$$)*

7. A bissetriz interna de um ângulo de um triângulo divide o lado oposto `______` aos lados adjacentes.
*(resposta: proporcionalmente)*

8. A instalação de antenas 5G no Brasil começou em julho de `______`, no estado de `______`, na frequência de `______` GHz.
*(resposta: 2022; Brasília/DF; 3,5)*

---

### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Teorema de Tales | Um feixe de paralelas determina segmentos `______` nas transversais → *proporcionais* |
| Fórmula principal | $$\frac{a}{b} =$$ `______` → *$$\frac{c}{d}$$* |
| Propriedade da soma | $$\frac{a}{b} = \frac{c}{d} \Rightarrow \frac{a}{b} =$$ `______` → *$$\frac{a+c}{b+d}$$* |
| Semelhança (critério) | Basta `______` ângulos correspondentes iguais (critério AA) → *dois* |
| Razão de semelhança | O valor $$k$$ é `______` para todos os pares de lados correspondentes → *constante* |
| Bissetriz interna | Divide o lado oposto `______` aos lados adjacentes → *proporcionalmente* |
| Tales de Mileto | Previu um eclipse solar em `______` a.C. → *585* |
| Aplicação (sombras) | Menino 1,60 m, sombra 1,30 m; poste com sombra 3,25 m → altura do poste = `______` → *4 m* |
| Pegadinha | A bissetriz interna divide o lado oposto ao meio? → *Não — só se o triângulo for isósceles* |
| Unidades | Antes de montar a proporção, é preciso `______` as medidas → *converter para a mesma unidade* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

### Síntese do Livro — TEOREMA DE TALES

*(Baseada na imagem da página 218 capturada pelo usuário)*

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| Pílula central | Teorema de Tales | — |
| Bloco esquerdo — enunciado | Feixe de paralelas cortadas por 2 transversais | Relação: $$\frac{a}{b} = \frac{c}{d}$$ se r//s//t |
| Bloco direito — consequência | Teorema da Bissetriz Interna | `______` → *A bissetriz de um ângulo interno divide o lado oposto proporcionalmente aos lados adjacentes* |
| Fórmula da bissetriz | $$\frac{c}{x} = \frac{b}{y}$$ | Onde x e y são `______` → *os segmentos em que o lado oposto BC é dividido* |
| Bloco inferior — demonstração | Ponto E = interseção do prolongamento de AB com paralela a AD por C | Conclusão: $$\triangle ACE$$ é `______` → *isósceles (AE = AC = b)* |
| Resultado da demonstração | Pelo Teorema de Tales: $$\frac{c}{x} = \frac{b}{y}$$ | Condição usada: paralelismo de `______` com `______` → *EC com AD* |

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das Questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| Q-1 | Ponto de luz a 20 m do prédio; pessoa de 1,80 m a 5 m do ponto de luz — altura da sombra no prédio | Cal | M | AT | Triângulos semelhantes: $$\frac{1{,}80}{5} = \frac{h}{20} \Rightarrow h = 7{,}2 \text{ m}$$ | ⚠️ figura não capturada |
| Q-2 | Escorregador de 6 m; bandeira a 2 m de altura indica 2,4 m restantes — distância do topo até a bandeira | Cal | M | AT | Tales no triângulo: $$\frac{(6-2)}{6} = \frac{d_{\text{bandeira}}}{d_{\text{total}}}$$; distância percorrida proporcional | ⚠️ figura não capturada |
| Q-3 | Medir segmentos com régua em 3 configurações de paralelas e transversais | Dis | F | AT | Atividade de medição — razões devem ser iguais em cada par | ⚠️ depende de figura impressa |
| Q-4 | Feixe de paralelas; segmentos 9 cm / (x+1) cm e 12 cm / (2x−6) cm — calcular x | Cal | M | AT | $$\frac{9}{x+1} = \frac{12}{2x-6} \Rightarrow 18x - 54 = 12x + 12 \Rightarrow x = 11$$ | — |
| Q-5 | Triângulo ABC retângulo em B; DE ∥ base; AB=32, BC=28, hip=90 — perímetro de ADE | Cal | M | AT | Razão de semelhança + proporcionalidade dos lados | ⚠️ figura não capturada |
| Q-6 | Frente dos terrenos B e C para Av. dos Flâmures | Cal | M | AT | Proporção entre segmentos de terrenos | ⚠️ figura não capturada |
| Q-7 | Terreno A com 45 m na Rua Dois Melo; calcular frente do terreno B | Cal | M | AT | Tales aplicado a terrenos: $$\frac{20}{30} = \frac{x}{45} \Rightarrow x = 30 \text{ m}$$ | — |
| Q-8 | Paralelas com segmentos 15 cm e 3 cm; outra transversal com x e 9 cm | Cal | F | AT | $$\frac{15}{3} = \frac{x}{9} \Rightarrow x = 45 \text{ cm}$$ | — |
| Q-9 | DE ∥ AC no triângulo ABC; AD=9, BD=15, AE=x, AC=3x−2 — calcular x | Cal | M | AT | $$\frac{9}{15} = \frac{x}{3x-2} \Rightarrow 27x - 18 = 15x \Rightarrow x = 1{,}5$$ | — |
| Q-10 | Guarda-sol projeta sombra 2,2 m; palmeira de 4 m — sombra da palmeira | Cal | M | AT | Altura do guarda-sol necessária ou proporção direta com dados faltantes | ⚠️ altura do guarda-sol não especificada no `.md` |
| Q-11 | Ponte BC sobre rio; BD // CE; AB=55 m, AD=11 m, AE=20 m — comprimento da ponte | Cal | D | AT | $$\frac{11}{55} = \frac{20}{BC} \Rightarrow BC = 100 \text{ m}$$ | ⚠️ dados corrigidos pela imagem |
| Q-12 | Sombra da árvore = 5 m; sombra da flor = 65 cm; flor = 0,45 m — altura da árvore | Cal | M | AT | $$\frac{0{,}45}{0{,}65} = \frac{h}{5} \Rightarrow h \approx 3{,}46 \text{ m}$$ | — |
| Q-13 | Calcular x em 3 configurações com retas r//s//t | Cal | M | AT | Montar proporção e resolver equação de 1º grau em cada item | ⚠️ valores das figuras parciais no `.md` |
| Q-14 | Retas l, s, t paralelas — calcular desconhecidos em 4 sub-itens | Cal | M | AT | a) $$\frac{4}{8}=\frac{9}{x} \Rightarrow x=18$$; demais dependem da figura | ⚠️ figura não capturada |
| Q-15 | DE // BC; AD=25 m, AE=x, EC=x+10 — calcular x e perímetro | Cal | D | AT | $$\frac{25}{AD+BD} = \frac{x}{x+x+10}$$; requer BD para completar | ⚠️ BD=v não especificado |
| Q-16 | Paralelas l, s, t; x+y=5 e x+y=−2 — calcular x e y | Cal | M | AT | Usar propriedade da soma + proporção fornecida | ⚠️ razão base não especificada |
| Q-17 | Paralelas com 12 cm, x, y, 8 cm — calcular x e y | Cal | M | AT | Proporção com soma dos termos | — |
| Q-18 | Triângulo com DE // BC; 4 cm indicado — calcular desconhecido | Cal | M | AT | Tales no triângulo | ⚠️ figura incompleta |
| Q-19 | Feixe de paralelas; calcular AB em 3 sub-itens com diferentes medidas | Cal | M | AT | a) $$\frac{AB}{10}=\frac{18}{20} \Rightarrow AB=9$$ cm; b) e c) analogamente | — |
| Q-20 | Triângulo retângulo catetos 28 e 21 cm; quadrado inscrito — perímetro do quadrado | Cal | D | AT | Sistema com Tales: $$l = \frac{28 \times 21}{28+21} = 12 \text{ cm}$$; perímetro = 48 cm | — |
| Q-21 | Ator 1,70 m a 1 m do biombo; sombra projetada = 3,55 m — distância do ponto de luz | Cal | D | AT | Triângulos semelhantes: $$\frac{1{,}70}{3{,}55} = \frac{1}{d} \Rightarrow d \approx 2{,}09 \text{ m}$$ do biombo | — |
| QC-1 | Teleférico entre picos A (500 m) e B (800 m), dist. horiz. 900 m — deslocamento e tempo | Cal | D | AT | a) $$\frac{x}{y}=\frac{900}{300} \Rightarrow x=60 \text{ m}$$ quando y=20 m; b) dist=$$\sqrt{900^2+300^2}$$; t=dist/1,5 | Fuvest-SP |
| QC-2 | Ponte estaiada harpa; AB=75 m, BC=100 m, AD=6 m — distância EC | MC | D | AT | $$\frac{AD}{AB}=\frac{EC}{BC} \Rightarrow \frac{6}{75}=\frac{EC}{100} \Rightarrow EC=8 \text{ m}$$ → **a) 8** | CPS-SP 2015 |
| QC-3 | Terrenos I, II, III — comprimento do muro do terreno II | MC | M | AT | Tales entre as ruas: gabarito **b) 30** | Saresp ⚠️ figura não capturada |
| QC-4 | Retas r,s,t e u,v paralelas; △ABC e quadrilátero CDEF mesmas áreas — valor de x | MC | D | AT | Áreas iguais + Tales: analisar com valores corrigidos da imagem | Vunesp 2015 ⚠️ verificar valores |
| QC-5 | Olho humano (diâm. 15 mm); pontos sep. 1 mm — maior dist. para perceber separados | MC | D | AT | $$\frac{1}{x}=\frac{0{,}005}{15} \Rightarrow x=3000 \text{ mm}=3 \text{ m}$$ → **c) 3** | Unesp ⚠️ corrigido pela imagem |
| QC-6 | GPS mostra rota mais curta — calcular distância total do trajeto | Cal | M | AT | Tales aplicado ao mapa | ⚠️ figura não capturada |

---

### Bloco B — Questões Modelo Originais

---

**QM-1** · Múltipla Escolha · Médio · inspirada em: Q-8

Uma faixa de três retas paralelas determina, sobre uma primeira transversal, segmentos de 18 cm e 6 cm. Sobre uma segunda transversal, o segmento correspondente ao de 18 cm mede $$x$$ cm. Sabendo que o segmento correspondente ao de 6 cm mede 4 cm, qual é o valor de $$x$$?

a) 8 cm   b) 10 cm   c) 12 cm   d) 15 cm

✅ **Gabarito: c) 12 cm**

📝 **Resolução:**
$$\frac{18}{6} = \frac{x}{4} \Rightarrow 6x = 72 \Rightarrow x = 12 \text{ cm}$$

⚠️ **Professor:** variação direta — troque os valores mantendo a proporção inteira para facilitar ou dificult ar.

---

**QM-2** · Múltipla Escolha · Médio · inspirada em: Q-12

Em um momento ensolarado, uma estátua de 3 m de altura projeta uma sombra de 2 m no chão. No mesmo instante, uma placa de sinalização projeta uma sombra de 80 cm. Qual é a altura da placa?

a) 100 cm   b) 110 cm   c) 120 cm   d) 130 cm

✅ **Gabarito: c) 120 cm**

📝 **Resolução:**
$$\frac{3}{2} = \frac{h}{0{,}80} \Rightarrow h = \frac{3 \times 0{,}80}{2} = 1{,}20 \text{ m} = 120 \text{ cm}$$

⚠️ **Professor:** pegadinha de unidade — sombra da placa em cm, altura da estátua em m. Peça aos alunos que convertam antes.

---

**QM-3** · Cálculo · Médio · inspirada em: Exercício Resolvido 2

Três retas paralelas determinam sobre uma transversal dois segmentos $$x$$ e $$y$$, com $$x + y = 20$$ cm. O mesmo feixe determina sobre outra transversal segmentos de 9 cm e 6 cm, respectivamente correspondentes a $$x$$ e $$y$$. Determine os valores de $$x$$ e de $$y$$.

✅ **Gabarito: $$x = 12$$ cm e $$y = 8$$ cm**

📝 **Resolução:**

Do Teorema de Tales:
$$\frac{x}{y} = \frac{9}{6}$$

Pela propriedade da soma dos termos:
$$\frac{x}{9} = \frac{x+y}{9+6} = \frac{20}{15}$$

$$x = \frac{9 \times 20}{15} = \frac{180}{15} = 12 \text{ cm}$$

$$y = 20 - 12 = 8 \text{ cm}$$

⚠️ **Professor:** destaque o uso da propriedade da soma — evita montar sistema de duas equações.

---

**QM-4** · Estilo Concurso · Difícil · inspirada em: QC-2 e Q-11

Para medir a largura de um canal, um topógrafo posicionou estacas nos pontos A, D e E, de modo que $$\overline{BD} \parallel \overline{CE}$$, conforme o esquema. As distâncias medidas foram: $$AB = 48 \text{ m}$$, $$AD = 16 \text{ m}$$ e $$AE = 25 \text{ m}$$. Qual é a largura $$BC$$ do canal?

a) 60 m   b) 70 m   c) 72 m   d) 75 m   e) 80 m

✅ **Gabarito: d) 75 m**

📝 **Resolução:**

Como $$BD \parallel CE$$, pelo Teorema de Tales aplicado ao triângulo:

$$\frac{AD}{AB} = \frac{AE}{AC}$$

$$\frac{16}{48} = \frac{25}{AC} \Rightarrow AC = \frac{25 \times 48}{16} = 75 \text{ m}$$

Como $$AC = AE + EC$$... na configuração do problema, $$BC$$ é o segmento procurado:

$$BC = \frac{AB \times AE}{AD} = \frac{48 \times 25}{16} = 75 \text{ m}$$

⚠️ **Professor:** referência de estilo — crie variações originais com diferentes medidas e posições dos pontos.

---

**QM-5** · Dissertativa · Médio-Difícil · inspirada em: Q-21 e Bloco G

Em um espetáculo de teatro de sombras, uma marionete de 45 cm de altura é posicionada a 60 cm de uma tela branca. O ponto de luz está a 2,10 m da tela (do mesmo lado da marionete).

a) Faça um esboço representando a situação, indicando as medidas.

b) Qual será a altura da sombra projetada na tela?

c) Se o artista quiser que a sombra tenha 90 cm de altura, a que distância da tela deve posicionar a marionete?

✅ **Gabarito:**

**b)** Ponto de luz → marionete: distância até a tela = 2,10 m; marionete a 0,60 m da tela, portanto a 2,10 − 0,60 = 1,50 m do ponto de luz.

Triângulos semelhantes:

$$\frac{0{,}45}{1{,}50} = \frac{h}{2{,}10} \Rightarrow h = \frac{0{,}45 \times 2{,}10}{1{,}50} = 0{,}63 \text{ m} = 63 \text{ cm}$$

**c)** Para sombra de 90 cm:

$$\frac{0{,}45}{d_{\text{luz-marionete}}} = \frac{0{,}90}{2{,}10} \Rightarrow d = \frac{0{,}45 \times 2{,}10}{0{,}90} = 1{,}05 \text{ m}$$

Distância da marionete à tela: $$2{,}10 - 1{,}05 = 1{,}05 \text{ m}$$

⚠️ **Professor:** referência de estilo — crie variações originais com diferentes alturas e distâncias.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: feixe_paralelas
Feixe de três retas paralelas (r, s, t) cortado por duas transversais, com segmentos a, b, c, d e a proporção a/b = c/d.

```svg
<svg width="100%" viewBox="0 0 680 320">
  <defs>
    <style>
      .c-purple{fill:#6c3fc5;} .c-teal{fill:#1a8a7a;} .c-amber{fill:#b07d0a;}
      .c-coral{fill:#c0392b;} .c-gray{fill:#555;} .c-green{fill:#1a7a3a;}
      .t{font-family:sans-serif;font-size:15px;fill:#222;dominant-baseline:central;}
      .ts{font-family:sans-serif;font-size:12px;fill:#555;dominant-baseline:central;}
      .th{font-family:sans-serif;font-size:16px;font-weight:bold;fill:#1a3a5c;dominant-baseline:central;}
    </style>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
    </marker>
  </defs>
  <!-- Retas paralelas horizontais -->
  <line x1="60" y1="60" x2="560" y2="60" stroke="#1a3a5c" stroke-width="2"/>
  <line x1="60" y1="160" x2="560" y2="160" stroke="#1a3a5c" stroke-width="2"/>
  <line x1="60" y1="260" x2="560" y2="260" stroke="#1a3a5c" stroke-width="2"/>
  <!-- Labels das retas -->
  <text x="572" y="60" class="th">r</text>
  <text x="572" y="160" class="th">s</text>
  <text x="572" y="260" class="th">t</text>
  <!-- Transversal 1 (esquerda) -->
  <line x1="140" y1="30" x2="200" y2="290" stroke="#c0392b" stroke-width="2.5"/>
  <!-- Transversal 2 (direita) -->
  <line x1="400" y1="30" x2="480" y2="290" stroke="#1a8a7a" stroke-width="2.5"/>
  <!-- Segmentos e labels transversal 1 -->
  <text x="108" y="110" class="t" fill="#c0392b">a</text>
  <text x="100" y="210" class="t" fill="#c0392b">b</text>
  <!-- Segmentos e labels transversal 2 -->
  <text x="448" y="110" class="t" fill="#1a8a7a">c</text>
  <text x="456" y="210" class="t" fill="#1a8a7a">d</text>
  <!-- Fórmula central -->
  <rect x="220" y="120" width="220" height="56" rx="10" fill="#f0eeff" stroke="#6c3fc5" stroke-width="1.5"/>
  <text x="330" y="148" class="th" text-anchor="middle">a/b = c/d</text>
  <text x="330" y="168" class="ts" text-anchor="middle">se r // s // t</text>
  <!-- Título -->
  <text x="340" y="300" class="th" text-anchor="middle">Teorema de Tales — Feixe de Paralelas</text>
</svg>
```

---

### DIAGRAMA: semelhanca_triangulos
Dois triângulos semelhantes lado a lado com a razão de semelhança k indicada entre lados correspondentes.

```svg
<svg width="100%" viewBox="0 0 680 300">
  <defs>
    <style>
      .c-purple{fill:#6c3fc5;} .c-teal{fill:#1a8a7a;} .c-amber{fill:#b07d0a;}
      .c-coral{fill:#c0392b;} .c-gray{fill:#555;} .c-green{fill:#1a7a3a;}
      .t{font-family:sans-serif;font-size:15px;fill:#222;dominant-baseline:central;}
      .ts{font-family:sans-serif;font-size:12px;fill:#555;dominant-baseline:central;}
      .th{font-family:sans-serif;font-size:16px;font-weight:bold;fill:#1a3a5c;dominant-baseline:central;}
    </style>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
    </marker>
  </defs>
  <!-- Triângulo ABC (menor) -->
  <polygon points="80,220 180,220 130,80" fill="#e8f0ff" stroke="#1a3a5c" stroke-width="2"/>
  <text x="72" y="235" class="t">B</text>
  <text x="182" y="235" class="t">C</text>
  <text x="122" y="68" class="t">A</text>
  <!-- Triângulo DEF (maior) -->
  <polygon points="360,240 560,240 460,60" fill="#e8fff4" stroke="#1a8a7a" stroke-width="2"/>
  <text x="348" y="255" class="t" fill="#1a8a7a">D</text>
  <text x="562" y="255" class="t" fill="#1a8a7a">F</text>
  <text x="452" y="48" class="t" fill="#1a8a7a">E</text>
  <!-- Sinal de semelhança -->
  <text x="240" y="155" class="th" text-anchor="middle">~</text>
  <!-- Razão k -->
  <rect x="230" y="190" width="120" height="44" rx="8" fill="#fff8e0" stroke="#b07d0a" stroke-width="1.5"/>
  <text x="290" y="208" class="ts" text-anchor="middle">razão de semelhança</text>
  <text x="290" y="226" class="th" text-anchor="middle" font-size="14">k = AB/DE = BC/DF</text>
  <!-- Título -->
  <text x="340" y="280" class="th" text-anchor="middle">△ABC ~ △DEF</text>
</svg>
```

---

### DIAGRAMA: bissetriz_interna
Triângulo ABC com bissetriz interna do ângulo A dividindo BC em segmentos x e y, com a proporção c/x = b/y.

```svg
<svg width="100%" viewBox="0 0 680 320">
  <defs>
    <style>
      .c-purple{fill:#6c3fc5;} .c-teal{fill:#1a8a7a;} .c-amber{fill:#b07d0a;}
      .c-coral{fill:#c0392b;} .c-gray{fill:#555;} .c-green{fill:#1a7a3a;}
      .t{font-family:sans-serif;font-size:15px;fill:#222;dominant-baseline:central;}
      .ts{font-family:sans-serif;font-size:12px;fill:#555;dominant-baseline:central;}
      .th{font-family:sans-serif;font-size:16px;font-weight:bold;fill:#1a3a5c;dominant-baseline:central;}
    </style>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
    </marker>
  </defs>
  <!-- Triângulo ABC -->
  <polygon points="280,40 80,260 520,260" fill="#f0eeff" stroke="#1a3a5c" stroke-width="2.5"/>
  <!-- Ponto A no topo -->
  <text x="272" y="28" class="th">A</text>
  <!-- Ponto B -->
  <text x="60" y="272" class="th">B</text>
  <!-- Ponto C -->
  <text x="524" y="272" class="th">C</text>
  <!-- Bissetriz AD (D na base BC) -->
  <line x1="280" y1="40" x2="300" y2="260" stroke="#c0392b" stroke-width="2" stroke-dasharray="8,4"/>
  <circle cx="300" cy="260" r="4" fill="#c0392b"/>
  <text x="300" y="278" class="t" fill="#c0392b" text-anchor="middle">D</text>
  <!-- Labels dos lados -->
  <text x="156" y="142" class="t" fill="#1a8a7a">c</text>
  <text x="408" y="142" class="t" fill="#6c3fc5">b</text>
  <!-- Labels dos segmentos x e y -->
  <text x="185" y="272" class="t" fill="#c0392b">x</text>
  <text x="405" y="272" class="t" fill="#b07d0a">y</text>
  <!-- Fórmula -->
  <rect x="200" y="300" width="280" height="44" rx="10" fill="#fff0f0" stroke="#c0392b" stroke-width="1.5"/>
  <text x="340" y="318" class="th" text-anchor="middle">c/x = b/y</text>
  <text x="340" y="336" class="ts" text-anchor="middle">Teorema da Bissetriz Interna</text>
  <!-- Nota -->
  <text x="340" y="20" class="ts" text-anchor="middle">AD é a bissetriz do ângulo A</text>
</svg>
```

---

### DIAGRAMA: aplicacoes_tales
Hierarquia de aplicações práticas do Teorema de Tales em situações reais.

```svg
<svg width="100%" viewBox="0 0 680 380">
  <defs>
    <style>
      .c-purple{fill:#6c3fc5;} .c-teal{fill:#1a8a7a;} .c-amber{fill:#b07d0a;}
      .c-coral{fill:#c0392b;} .c-gray{fill:#555;} .c-green{fill:#1a7a3a;}
      .t{font-family:sans-serif;font-size:15px;fill:#222;dominant-baseline:central;}
      .ts{font-family:sans-serif;font-size:12px;fill:#555;dominant-baseline:central;}
      .th{font-family:sans-serif;font-size:16px;font-weight:bold;fill:#fff;dominant-baseline:central;}
    </style>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
    </marker>
  </defs>
  <!-- Nó central -->
  <rect x="220" y="20" width="240" height="58" rx="14" fill="#1a3a5c"/>
  <text x="340" y="49" class="th" text-anchor="middle">Teorema de Tales</text>
  <!-- Linhas para filhos -->
  <line x1="280" y1="78" x2="100" y2="150" stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="340" y1="78" x2="340" y2="150" stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="400" y1="78" x2="580" y2="150" stroke="#888" stroke-width="1.5" marker-end="url(#arr)"/>
  <!-- Aplicação 1: Sombras -->
  <rect x="20" y="150" width="160" height="58" rx="10" fill="#1a8a7a"/>
  <text x="100" y="170" class="th" text-anchor="middle" font-size="13">Medição por</text>
  <text x="100" y="190" class="th" text-anchor="middle" font-size="13">Sombras</text>
  <!-- Aplicação 2: Pontes/Distâncias -->
  <rect x="250" y="150" width="180" height="58" rx="10" fill="#6c3fc5"/>
  <text x="340" y="170" class="th" text-anchor="middle" font-size="13">Distâncias</text>
  <text x="340" y="190" class="th" text-anchor="middle" font-size="13">Inacessíveis</text>
  <!-- Aplicação 3: Terrenos -->
  <rect x="500" y="150" width="160" height="58" rx="10" fill="#b07d0a"/>
  <text x="580" y="170" class="th" text-anchor="middle" font-size="13">Divisão de</text>
  <text x="580" y="190" class="th" text-anchor="middle" font-size="13">Terrenos</text>
  <!-- Exemplos de cada aplicação -->
  <rect x="20" y="240" width="160" height="72" rx="8" fill="#e8fff4" stroke="#1a8a7a" stroke-width="1"/>
  <text x="100" y="260" class="ts" text-anchor="middle">Postes, árvores,</text>
  <text x="100" y="276" class="ts" text-anchor="middle">palmeiras, estátuas</text>
  <text x="100" y="292" class="ts" text-anchor="middle">Teatro de sombras</text>
  <text x="100" y="308" class="ts" text-anchor="middle">Dentes (Bragman)</text>
  <rect x="250" y="240" width="180" height="72" rx="8" fill="#f0eeff" stroke="#6c3fc5" stroke-width="1"/>
  <text x="340" y="260" class="ts" text-anchor="middle">Pontes sobre rios</text>
  <text x="340" y="276" class="ts" text-anchor="middle">Largura de canais</text>
  <text x="340" y="292" class="ts" text-anchor="middle">Teleférico (morros)</text>
  <text x="340" y="308" class="ts" text-anchor="middle">Antenas 5G</text>
  <rect x="500" y="240" width="160" height="72" rx="8" fill="#fff8e0" stroke="#b07d0a" stroke-width="1"/>
  <text x="580" y="260" class="ts" text-anchor="middle">Frente de terrenos</text>
  <text x="580" y="276" class="ts" text-anchor="middle">para ruas paralelas</text>
  <text x="580" y="292" class="ts" text-anchor="middle">Plantas urbanas</text>
  <text x="580" y="308" class="ts" text-anchor="middle">Estais de pontes</text>
  <!-- Fórmula base -->
  <rect x="180" y="340" width="320" height="30" rx="8" fill="#f4f2ee" stroke="#1a3a5c" stroke-width="1.5"/>
  <text x="340" y="355" class="t" text-anchor="middle" fill="#1a3a5c">Em todas: montar proporção a/b = c/d</text>
</svg>
```

---
