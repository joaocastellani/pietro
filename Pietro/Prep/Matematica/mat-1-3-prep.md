# mat-1-3-prep.md

---

## DIAGRAMAS DISPONÍVEIS — mat-1-3

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Anatomia do Radical | DIAGRAMA: anatomia_radical | Ao introduzir nomenclatura (índice, radicando, raiz) |
| Propriedades dos Radicais | DIAGRAMA: propriedades | Ao apresentar as propriedades operacionais |
| Fluxo de Racionalização | DIAGRAMA: racionalizacao | Ao explicar o passo a passo da racionalização |
| Fórmulas Principais | DIAGRAMA: formulas | Revisão rápida antes dos exercícios |

### Tabelas markdown (Seção 6):
- Tabela de símbolos e variáveis das fórmulas (Seção 4)

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer. Tabelas da Seção 6 são apresentadas como markdown no chat.

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 3
- Tema: Radiciação
- Perfil: álgebra
- Fórmulas principais:
    • b^n = a ⟺ ⁿ√a = b
    • ⁿ√(aᵐ) = a^(m/n)
    • ⁿ√(a·b) = ⁿ√a · ⁿ√b
    • ⁿ√(a/b) = ⁿ√a / ⁿ√b
    • ᵐ√(ⁿ√a) = ᵐⁿ√a
    • b/ⁿ√(aᵐ) · ⁿ√(aⁿ⁻ᵐ)/ⁿ√(aⁿ⁻ᵐ) = b·ⁿ√(aⁿ⁻ᵐ)/a
- Matemáticos citados: Hipaso de Metaponto
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### 🔹 Bloco 1 — O que é Radiciação

A radiciação é a **operação inversa da potenciação**. Enquanto na potenciação perguntamos "qual é o resultado de elevar $$b$$ à potência $$n$$?", na radiciação perguntamos "que número $$b$$, elevado a $$n$$, resulta em $$a$$?"

Formalmente: $$b^n = a \Leftrightarrow \sqrt[n]{a} = b$$

O símbolo $$\sqrt[n]{a}$$ é chamado de **radical**, onde:
- $$n$$ = **índice** (qual raiz estamos extraindo)
- $$a$$ = **radicando** (o número dentro do radical)
- $$b$$ = **raiz** (o resultado)

**Condição crítica:** se o índice $$n$$ for **par**, o radicando $$a$$ deve ser **maior ou igual a zero** para que o resultado seja real. Se $$n$$ for **ímpar**, $$a$$ pode ser qualquer número real (inclusive negativo).

> Exemplo concreto: $$\sqrt[3]{-64} = -4$$ (válido, pois o índice 3 é ímpar), mas $$\sqrt{-64}$$ não é real (índice 2 é par, radicando negativo).

---

### 🔹 Bloco 2 — Simplificação de Radicais

Para simplificar um radical, **fatoramos o radicando** em fatores primos e agrupamos os fatores de acordo com o índice da raiz. A cada grupo completo de $$n$$ fatores iguais, "saímos" um fator de baixo do radical.

> Exemplo: $$\sqrt{80} = \sqrt{2^4 \cdot 5} = 2^2\sqrt{5} = 4\sqrt{5}$$

> Outro exemplo: $$\sqrt{180} = \sqrt{2^2 \cdot 3^2 \cdot 5} = 2 \cdot 3\sqrt{5} = 6\sqrt{5}$$

---

### 🔹 Bloco 3 — Potências de Expoente Fracionário

Todo radical pode ser reescrito como uma **potência de expoente fracionário**:

$$\sqrt[n]{a^m} = a^{\frac{m}{n}}$$

O **denominador** do expoente fracionário corresponde ao **índice** da raiz; o **numerador**, ao expoente do radicando.

> Exemplo: $$\sqrt[3]{8} = 8^{\frac{1}{3}} = 2$$ e $$\sqrt[4]{256} = 256^{\frac{1}{4}} = (2^8)^{\frac{1}{4}} = 2^2 = 4$$

Essa representação é especialmente útil para operar radicais com índices diferentes, reduzindo-os a um índice comum via MMC dos índices.

---

### 🔹 Bloco 4 — Radicais Semelhantes e Operações de Adição/Subtração

**Radicais semelhantes** têm o **mesmo índice E o mesmo radicando**. Apenas eles podem ser somados ou subtraídos diretamente, somando-se os coeficientes:

$$2\sqrt{3} + 4\sqrt{3} - \sqrt{3} = (2 + 4 - 1)\sqrt{3} = 5\sqrt{3}$$

Se os radicais não forem semelhantes, tentamos **simplificá-los** para torná-los semelhantes antes de operar:

$$\sqrt{18} - \sqrt{50} = 3\sqrt{2} - 5\sqrt{2} = -2\sqrt{2}$$

---

### 🔹 Bloco 5 — Multiplicação e Divisão de Radicais

Para multiplicar ou dividir radicais, eles devem ter **índices iguais**. Se os índices forem diferentes, reduzimos ao mesmo índice (usando o MMC dos índices) antes de operar.

Com índices iguais:
$$\sqrt{6} \cdot \sqrt{8} = \sqrt{48} = 4\sqrt{3}$$

Com índices diferentes:
$$\sqrt{2} \cdot \sqrt[3]{3} = \sqrt[6]{2^3} \cdot \sqrt[6]{3^2} = \sqrt[6]{8 \cdot 9} = \sqrt[6]{72}$$

A **propriedade distributiva** também vale com radicais:
$$\sqrt{2}(\sqrt{3} + \sqrt{5}) = \sqrt{6} + \sqrt{10}$$

---

### 🔹 Bloco 6 — Racionalização de Denominador

Quando uma fração possui denominador irracional, usamos a **racionalização** para transformá-lo em racional, multiplicando por uma fração equivalente a 1:

$$\frac{b}{\sqrt[n]{a^m}} \cdot \frac{\sqrt[n]{a^{n-m}}}{\sqrt[n]{a^{n-m}}} = \frac{b \cdot \sqrt[n]{a^{n-m}}}{a}$$

O expoente do fator de racionalização é sempre $$(n - m)$$, para que o produto no denominador forme uma potência de expoente inteiro.

Quando o denominador é uma **soma ou diferença** envolvendo radicais, usamos o **produto notável conjugado** $$(a+b)(a-b) = a^2 - b^2$$:

$$\frac{2}{\sqrt{2}+1} \cdot \frac{\sqrt{2}-1}{\sqrt{2}-1} = \frac{2(\sqrt{2}-1)}{2-1} = 2\sqrt{2} - 2$$

---

### 🔹 Bloco 7 — Conexão com o Mundo Real

O capítulo apresenta duas aplicações concretas de radiciação:

1. **Pastagem e "cerca virtual":** dado que 1 hectare = 10 000 m², uma pastagem de 150 ha tem área de 1 500 000 m². Para encontrar o lado de um quadrado com essa área, aplica-se a raiz quadrada.

2. **Queda livre:** o tempo de queda de um paraquedista lançado de altura $$h$$ metros é aproximado por $$t = \sqrt{h}$$. Alan Eustace, lançado de 41 400 m, teve tempo de queda $$t = \sqrt{41400} \approx 15{,}2 \times \sqrt{230} \approx 203{,}4$$ s.

---

## SEÇÃO 3 — MATEMÁTICOS E HISTÓRIA DA MATEMÁTICA

### Hipaso de Metaponto (séc. V a.C.)
**Área:** Aritmética e Teoria dos Números
**Contribuição no capítulo:** Percebeu que o lado e a diagonal de um quadrado não são mensuráveis — ou seja, sua razão não pode ser expressa como fração de inteiros — sinalizando a existência de números irracionais.
**O que desenvolveu:** Constatação da incomensurabilidade de grandezas, precursora do conceito de número irracional.
**Contexto histórico:** Grécia Antiga, escola pitagórica, século V a.C. A descoberta contrariava a crença pitagórica de que toda grandeza era expressa por razões de inteiros.

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Definição de Radiciação

**Expressão:** $$b^n = a \Leftrightarrow \sqrt[n]{a} = b$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$n$$ | Índice da raiz | Inteiro positivo ≥ 2 |
| $$a$$ | Radicando | Real (≥ 0 se n par) |
| $$b$$ | Raiz (resultado) | Real |

**Válida quando:** $$a \geq 0$$ se $$n$$ for par; $$a \in \mathbb{R}$$ se $$n$$ for ímpar.
**Caso especial:** Se $$n$$ é par e $$a < 0$$, a raiz não pertence aos reais.
💡 **Pegadinha:** Confundir $$\sqrt[3]{-8} = -2$$ (válido, índice ímpar) com $$\sqrt{-8}$$ (inválido nos reais, índice par).

---

### Potência de Expoente Fracionário

**Expressão:** $$\sqrt[n]{a^m} = a^{\frac{m}{n}}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$n$$ | Índice da raiz / denominador do expoente | Inteiro, $$n \geq 2$$ |
| $$m$$ | Expoente do radicando / numerador | Inteiro |
| $$a$$ | Base | Real positivo |

**Válida quando:** $$a \in \mathbb{R}^+, m \in \mathbb{Z}, n \in \mathbb{N}, n \geq 2$$
**Caso especial:** Quando $$m = 1$$, temos $$\sqrt[n]{a} = a^{\frac{1}{n}}$$.
💡 **Pegadinha:** Trocar numerador e denominador — o **índice** é o denominador, não o numerador.

---

### 3ª Propriedade — Produto e Quociente de Radicais

**Expressão:**
$$\sqrt[n]{a \cdot b} = \sqrt[n]{a} \cdot \sqrt[n]{b} \qquad \sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$n$$ | Índice comum | Inteiro ≥ 2 |
| $$a, b$$ | Fatores / dividendo e divisor | Reais (compatíveis com o índice) |

**Válida quando:** Ambos os radicais têm o **mesmo índice**. Para quociente: $$b \neq 0$$.
💡 **Pegadinha:** $$\sqrt{a + b} \neq \sqrt{a} + \sqrt{b}$$. A propriedade vale apenas para **produto** e **quociente**, nunca para soma ou diferença.

---

### 4ª Propriedade — Raiz de Raiz

**Expressão:** $$\sqrt[m]{\sqrt[n]{a}} = \sqrt[m \cdot n]{a} = a^{\frac{1}{m \cdot n}}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$m$$ | Índice da raiz externa | Inteiro ≥ 2 |
| $$n$$ | Índice da raiz interna | Inteiro ≥ 2 |
| $$a$$ | Radicando original | Real compatível |

**Caso especial:** Usado para reduzir radicais com índices diferentes ao mesmo índice (via MMC).
💡 **Pegadinha:** Somar os índices em vez de multiplicá-los — o índice resultante é o **produto** $$m \cdot n$$, não a soma.

---

### Racionalização de Denominador — Regra Geral

**Expressão:** $$\frac{b}{\sqrt[n]{a^m}} \cdot \frac{\sqrt[n]{a^{n-m}}}{\sqrt[n]{a^{n-m}}} = \frac{b \cdot \sqrt[n]{a^{n-m}}}{a}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$n$$ | Índice da raiz | Inteiro ≥ 2 |
| $$m$$ | Expoente atual do denominador | Inteiro, $$1 \leq m < n$$ |
| $$n-m$$ | Expoente do fator racionalizante | Inteiro positivo |
| $$a$$ | Base do denominador irracional | Real positivo |

**Caso especial:** Denominador com soma/diferença → usar conjugado $$(a+b)(a-b) = a^2 - b^2$$.
💡 **Pegadinha:** No caso de $$\frac{1}{\sqrt[3]{a}}$$, o fator racionalizante é $$\sqrt[3]{a^2}$$ (e não $$\sqrt[3]{a}$$), pois precisamos que o expoente do denominador atinja 3 (o índice).

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Tabela: Condições de Validade da Raiz Enésima

| Índice $$n$$ | Radicando $$a$$ | Resultado nos Reais? | Exemplo |
|:-----------:|:--------------:|:--------------------:|---------|
| Par | $$a > 0$$ | ✅ Sim | $$\sqrt{16} = 4$$ |
| Par | $$a = 0$$ | ✅ Sim (resultado = 0) | $$\sqrt{0} = 0$$ |
| Par | $$a < 0$$ | ❌ Não é real | $$\sqrt{-4}$$ ∉ ℝ |
| Ímpar | $$a > 0$$ | ✅ Sim, positivo | $$\sqrt[3]{8} = 2$$ |
| Ímpar | $$a = 0$$ | ✅ Sim (resultado = 0) | $$\sqrt[3]{0} = 0$$ |
| Ímpar | $$a < 0$$ | ✅ Sim, negativo | $$\sqrt[3]{-8} = -2$$ |

---

### Tabela: Resumo das Propriedades Operacionais

| Propriedade | Expressão | Condição |
|-------------|-----------|----------|
| Produto | $$\sqrt[n]{a \cdot b} = \sqrt[n]{a} \cdot \sqrt[n]{b}$$ | Mesmo índice $$n$$ |
| Quociente | $$\sqrt[n]{a/b} = \sqrt[n]{a}/\sqrt[n]{b}$$ | Mesmo índice $$n$$; $$b \neq 0$$ |
| Raiz de raiz | $$\sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a}$$ | — |
| Potência fracionária | $$\sqrt[n]{a^m} = a^{m/n}$$ | $$a > 0$$ |
| Racionalização simples | $$\frac{b}{\sqrt[n]{a^m}} = \frac{b\sqrt[n]{a^{n-m}}}{a}$$ | $$a > 0$$ |
| Racionalização conjugada | $$\frac{c}{a \pm \sqrt{b}} \cdot \frac{a \mp \sqrt{b}}{a \mp \sqrt{b}}$$ | Denominador binomial |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — A propriedade só vale para produto e quociente, nunca para soma**
$$\sqrt{9 + 16} \neq \sqrt{9} + \sqrt{16}$$ → $$\sqrt{25} = 5$$, mas $$3 + 4 = 7$$. Sempre resolva o que está dentro do radical antes de separar.

💡 **Dica 2 — Índice par + radicando negativo = armadilha de prova**
Se aparecer $$\sqrt[4]{-16}$$ ou $$\sqrt{-9}$$ em uma questão pedindo resultado real, a resposta é "não existe nos reais". Nunca escreva um número negativo como resultado de raiz de índice par.

💡 **Dica 3 — Para racionalizar com raiz cúbica, o fator é o que falta para o cubo**
$$\frac{1}{\sqrt[3]{2}} \rightarrow$$ multiplica por $$\frac{\sqrt[3]{2^2}}{\sqrt[3]{2^2}} = \frac{\sqrt[3]{4}}{\sqrt[3]{4}}$$, pois $$\sqrt[3]{2} \cdot \sqrt[3]{4} = \sqrt[3]{8} = 2$$. O expoente do fator racionalizante é sempre $$(n - m)$$.

💡 **Dica 4 — Reduzir índices diferentes ao mesmo índice: use o MMC**
Para multiplicar $$\sqrt{2} \cdot \sqrt[3]{3}$$: MMC(2,3) = 6. Converta ambos ao índice 6: $$\sqrt[6]{2^3} \cdot \sqrt[6]{3^2} = \sqrt[6]{8 \cdot 9} = \sqrt[6]{72}$$.

💡 **Dica 5 — Radicais semelhantes: índice E radicando iguais**
$$3\sqrt{2}$$ e $$5\sqrt{2}$$ são semelhantes (soma direta: $$8\sqrt{2}$$). Mas $$3\sqrt{2}$$ e $$3\sqrt{3}$$ **não** são semelhantes — radicandos diferentes. Não some!

💡 **Dica 6 — Expoente fracionário: denominador = índice, numerador = potência**
$$a^{\frac{2}{3}} = \sqrt[3]{a^2}$$, não $$\sqrt[2]{a^3}$$. O denominador do expoente é **sempre** o índice da raiz.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

#### Bloco A — Lacunas de dados

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| Q-7 (questoes.md) | Fórmula completa da velocidade do som | A fórmula capturada aparece como $$v = c20 \cdot \sqrt{T/T_1}$$, com variáveis $$c20$$ e $$T_1$$ sem definição explícita | Consultar o livro físico para capturar a fórmula completa com definição de todas as variáveis |
| Q-9 (questoes.md) | Enunciado completo | O enunciado mistura potenciação e radicais sem clareza do que é pedido nos itens a), b), c) | Revisar a página 76 do livro para reescrever o enunciado correto |
| Q-16 (questoes.md) | Enunciado | O enunciado capturado é incoerente ("multiplicando os dois denominadores de um círculo...") | Revisar a página 79 do livro e recapturar a questão |

#### Bloco B — Inconsistências factuais

```
⚠️ ALERTA — Exemplo c) do Bloco E (√[3]{-64})
- Dado no material: "√[3]{-64} = √[3]{(-2)^6} = -2 · 2 = -4"
- Problema: A notação √[3]{(-2)^6} não é o caminho correto.
  (-2)^6 = 64 (positivo), portanto √[3]{(-2)^6} = √[3]{64} = 4,
  não -4. O correto é: -64 = (-4)^3, logo √[3]{-64} = -4.
- Dado correto: √[3]{-64} = -4 porque (-4)³ = -64.
  Desenvolvimento correto: fatorar 64 = 4³, então √[3]{-64} = -∛(4³) = -4.
- Impacto na aula: Corrigir a notação intermediária ao apresentar
  o exemplo. O resultado final (-4) está correto, mas o desenvolvimento
  intermediário está errado e pode confundir os alunos.
```

```
⚠️ ALERTA — Adição de radicais, exemplo b) do Bloco B
- Dado no material: "√5 + (−2√5) + 7√5 − 8√5 = (−1 − 2 + 7 − 8)√5 = −2√5 − 8√5"
- Problema: O resultado intermediário (−1 − 2 + 7 − 8) = −4,
  portanto o resultado deveria ser −4√5, não "−2√5 − 8√5"
  (que é uma expressão não simplificada e matematicamente incorreta como resultado).
- Dado correto: √5 + (−2√5) + 7√5 − 8√5 = (1 − 2 + 7 − 8)√5 = −2√5
- Impacto na aula: Corrigir o exemplo ao apresentar adição de radicais
  semelhantes. Reforçar que o resultado deve ser um único termo.
```

```
⚠️ ALERTA — Q-2 (questoes.md): item d)
- Dado no material: "4√5 + 3√5 = 7√0"
- Problema: 7√0 = 0, o que é matematicamente absurdo como resultado
  de 4√5 + 3√5. O correto seria 7√5. Provável erro de digitação
  no original (√0 em vez de √5).
- Dado correto: 4√5 + 3√5 = 7√5 (VERDADEIRO)
- Impacto na aula: Ao corrigir a questão, esclarecer que a alternativa
  correta é Falsa com a escrita √0, mas que o resultado correto
  da operação seria 7√5 (Verdadeiro).
```

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

- **Radiciação**
  - Definição: A operação inversa da `______` (`potenciação`)
  - Notação: O símbolo `______` é chamado de radical (`√[n]{a}`)
  - Partes: No radical $$\sqrt[n]{a} = b$$, o número $$n$$ é o `______` (`índice`), $$a$$ é o `______` (`radicando`) e $$b$$ é a `______` (`raiz`)

- **Radicais Semelhantes**
  - Definição: Radicais que possuem o mesmo `______` e o mesmo `______` (`índice` e `radicando`)
  - Operação permitida diretamente: `______` e `______` (`adição` e `subtração`)

- **Racionalização**
  - Definição: Processo de eliminar o `______` irracional de uma fração (`denominador`)
  - Método: Multiplicar por uma fração equivalente a `______` (`1`)

#### Bloco 2 — Fórmulas e Propriedades

- **Definição de radiciação**
  - Expressão: `______` ($$b^n = a \Leftrightarrow \sqrt[n]{a} = b$$)
  - Condição: Se $$n$$ for par, $$a$$ deve ser `______` (`≥ 0`)

- **Potência de expoente fracionário**
  - Expressão: `______` ($$\sqrt[n]{a^m} = a^{m/n}$$)
  - O índice da raiz corresponde ao `______` do expoente fracionário (`denominador`)

- **3ª Propriedade (produto)**
  - Expressão: `______` ($$\sqrt[n]{a \cdot b} = \sqrt[n]{a} \cdot \sqrt[n]{b}$$)
  - Condição: Os radicais devem ter o mesmo `______` (`índice`)

- **4ª Propriedade (raiz de raiz)**
  - Expressão: `______` ($$\sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a}$$)
  - O índice resultante é o `______` dos índices (`produto`)

#### Bloco 3 — Lacunas para Warm-Up

1. A radiciação é a operação inversa da `______`. *(resposta: potenciação)*

2. Se o índice de um radical é **par** e o radicando é **negativo**, o resultado `______` pertence aos números reais. *(resposta: não)*

3. $$\sqrt[n]{a^m} = a^{\,\square}$$. Qual é o expoente? `______` *(resposta: $$m/n$$)*

4. Para somar $$3\sqrt{5} + 7\sqrt{5}$$, o resultado é `______`. *(resposta: $$10\sqrt{5}$$)*

5. Para multiplicar radicais com índices diferentes, o primeiro passo é reduzi-los ao mesmo `______` usando o `______` dos índices. *(resposta: índice; MMC)*

6. Hipaso de Metaponto percebeu que o lado e a `______` de um quadrado não são mensuráveis, evidenciando a existência de números `______`. *(resposta: diagonal; irracionais)*

7. Uma pastagem quadrada de 150 hectares tem área de `______` m². Para calcular o lado, aplica-se a `______` desse valor. *(resposta: 1 500 000 m²; raiz quadrada)*

8. Para racionalizar $$\dfrac{1}{\sqrt[3]{a}}$$, multiplica-se pelo fator $$\dfrac{\sqrt[3]{a^{\,\square}}}{\sqrt[3]{a^{\,\square}}}$$. O expoente é `______`. *(resposta: 2, pois $$n - m = 3 - 1 = 2$$)*

---

## SEÇÃO 10

Seção 10 não gerada — anexe a imagem da Síntese para incluir.

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Gabarito | Obs. |
|---|---|---|---|---|---|
| Q-1 | Calcular: $$\sqrt{144}$$, $$\sqrt[3]{8}$$, $$\sqrt{0,25}$$, $$\sqrt[4]{296}$$, $$\sqrt[3]{-64}$$, $$-\sqrt{64}$$ | Cal | F | a) 12; b) 2; c) 0,5; d) ≈4,05 (não é inteiro — ⚠️); e) -4; f) -8 | ⚠️ item d): $$\sqrt[4]{296}$$ não tem resultado inteiro exato |
| Q-2 | Classificar igualdades em V ou F | VF | M | a) V: $$3\sqrt{9}=3\cdot3=9=\sqrt{81}$$ ✅; b) F: $$\sqrt{40}-\sqrt{10}\neq\sqrt{5}$$; c) F: $$2\sqrt{3}\neq6$$; d) ⚠️ item com erro de impressão ($$7\sqrt{0}$$) | ⚠️ item d) provavelmente deveria ser $$7\sqrt{5}$$ (V) |
| Q-3 | Calcular expressões numéricas aninhadas | Cal | M | a) $$8+2\cdot\sqrt[3]{32}+2$$; b) requer avaliação de raízes aninhadas; c)-e) cálculo direto por fatoração | — |
| Q-4 | Identificar e corrigir erros de Eduardo e Antônio em cálculos com radicais | Dis | D | Eduardo: $$\sqrt{-6^2+(-8)^2}=\sqrt{36+64}=\sqrt{100}=10$$; resultado correto: $$10+4=14$$. Antônio: $$\sqrt[3]{-125}=-5$$; resultado correto: $$9+8-(-5)=22$$ | — |
| Q-5 | Valor de $$\sqrt[3]{0,216}$$ | MC | M | a) 0,3. Pois $$0,216=0,6^3$$, logo $$\sqrt[3]{0,216}=0,6$$ — ⚠️ nenhuma alternativa apresenta 0,6 | ⚠️ gabarito correto (0,6) não está entre as alternativas |
| QC-1 | PUC-Rio 2017 — alternativa correta sobre operações com radicais | MC | M | a) ✅ $$2\sqrt{8}=2\cdot2\sqrt{2}=4\sqrt{2}=\sqrt{32}$$ VERDADEIRO | PUC-Rio · 2017 |
| QC-2 | ENEM — Calcular RIP de menina de 64 kg com IMC=25 | MC | D | IMC=25 → altura²=64/25=2,56 → h=1,6m=160cm. RIP=$$\sqrt[3]{160}/64\approx5,43/64\approx0,085$$ — ⚠️ verificar unidades e alternativas | ENEM · ⚠️ enunciado capturado com unidades inconsistentes |
| Q-6 | Calcular tempo de queda de Alan Eustace de 41 400 m | Cal | M | $$t=\sqrt{h}=\sqrt{41400}=\sqrt{4\cdot 9\cdot 100\cdot 115}=60\sqrt{115}\approx60\cdot10{,}72\approx643$$ s. Ou via $$\sqrt{230}\approx15{,}2$$: $$\sqrt{41400}=\sqrt{180\cdot230}=\sqrt{180}\cdot15{,}2\approx6\sqrt{5}\cdot15{,}2$$ | — |
| Q-7 | Velocidade do som em função da temperatura | Cal | D | Fórmula incompleta no material capturado | ⚠️ fórmula incompleta — ver Seção 8 |
| Q-8 | Valor de $$4^{2\cdot6^{-0,5}}$$ | MC | M | $$6^{-0,5}=1/\sqrt{6}$$; $$4^{2/\sqrt{6}}$$ — alternativas não batem com cálculo direto; ⚠️ enunciado possivelmente com erro de digitação | ⚠️ enunciado ambíguo |
| Q-9 | Identificar erro de Lelo/Pedro em operações com potências | MC | M | Enunciado inconsistente | ⚠️ enunciado ambíguo — ver Seção 8 |
| Q-10 | Simplificar radicais usando propriedades | Cal | M | b) $$\sqrt[3]{32}=2\sqrt[3]{4}$$; c) $$\sqrt{32}=4\sqrt{2}$$; e) $$\sqrt{\sqrt[4]{a^{16}}}=\sqrt{a^4}=a^2$$; f) $$\sqrt[3]{2^{300}}=2^{100}$$ | — |
| Q-11 | Identificar quem errou: Método/Pedro/Lucas | MC | M | Pedro e Lucas estão corretos ($$a^6=(a^2)^3$$ ✅; $$a^{12}=a^{6\cdot2}$$ ✅); Método apresenta equação sem sentido | ⚠️ enunciado do Texto com equação sem sentido |
| Q-12 | Simplificar expressões até um único radical | Cal | D | a) $$(\sqrt[3]{2})^6=2^2=4$$; $$\sqrt[6]{8}=\sqrt[6]{2^3}=2^{1/2}=\sqrt{2}$$; soma: $$4+\sqrt{2}$$ (não é único radical); demais itens requerem análise cuidadosa | — |
| Q-13 | Calcular diagonais de retângulos 28×25 e 32×24 | Cal | M | a) $$d=\sqrt{28^2+25^2}=\sqrt{784+625}=\sqrt{1409}\approx37{,}5$$ cm; b) $$d=\sqrt{32^2+24^2}=\sqrt{1024+576}=\sqrt{1600}=40$$ cm | — |
| Q-14 | Encontrar radicando $$n$$ em expressões | Cal | M | Enunciado ambíguo; requer revisão do livro | ⚠️ enunciado ambíguo |
| Q-15 | Forma simplificada de $$4\sqrt{2}$$ | MC | F | a) $$4\sqrt{2}$$ — já está simplificado | — |
| Q-16 | Enunciado incoerente | Cal | D | Não calculável com o enunciado capturado | ⚠️ enunciado incoerente — ver Seção 8 |
| Q-17 | Racionalizar 6 frações com raízes quadradas e cúbicas | Cal | M | a) $$\frac{2\sqrt{5}}{5}$$; b) $$\frac{4\sqrt{7}}{7}$$; c) $$\frac{\sqrt[3]{4}}{2}$$; d) $$\frac{3\sqrt[3]{2}}{4}$$; e) $$\frac{\sqrt[4]{27}}{3}$$; f) $$\frac{5\sqrt[4]{27}}{9}$$ | — |
| Q-18 | Simplificar $$\sqrt[3]{\sqrt[3]{2^{18}}\cdot\sqrt[3]{ab}}$$ | Cal | D | $$\sqrt[3]{2^{18}}=2^6=64$$; $$\sqrt[3]{64\cdot\sqrt[3]{ab}}$$; $$=\sqrt[3]{64\cdot(ab)^{1/3}}=4\cdot(ab)^{1/9}=4\sqrt[9]{ab}$$ | — |

---

#### Bloco B — Questões Modelo Originais

---

**QM-1** · múltipla escolha · médio · inspirada em: Q-5

Em uma receita industrial, uma cuba cúbica tem volume de 3,375 litros. Sabendo que 1 litro = 1 dm³, qual é a medida da aresta dessa cuba?

a) 1,5 dm
b) 1,8 dm
c) 2,0 dm
d) 2,5 dm

✅ Gabarito: a)
📝 Resolução:
Volume = aresta³ → aresta = $$\sqrt[3]{3,375}$$
$$3,375 = \frac{3375}{1000} = \frac{27 \cdot 125}{1000} = \left(\frac{15}{10}\right)^3 = 1,5^3$$
Portanto: $$\sqrt[3]{3,375} = 1,5$$ dm ✅
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · múltipla escolha · médio · inspirada em: QC-1

Assinale a alternativa **verdadeira**:

a) $$\sqrt{3} + \sqrt{12} = \sqrt{15}$$
b) $$\sqrt{50} - \sqrt{8} = 3\sqrt{2}$$
c) $$\sqrt{6} \cdot \sqrt{6} = 12$$
d) $$\sqrt[3]{16} \cdot \sqrt[3]{4} = 8$$

✅ Gabarito: b) e d) [ambas verdadeiras — ver resolução]
📝 Resolução:
- a) $$\sqrt{3}+\sqrt{12} = \sqrt{3}+2\sqrt{3}=3\sqrt{3}\neq\sqrt{15}$$ ❌
- b) $$\sqrt{50}-\sqrt{8}=5\sqrt{2}-2\sqrt{2}=3\sqrt{2}$$ ✅
- c) $$\sqrt{6}\cdot\sqrt{6}=6\neq12$$ ❌
- d) $$\sqrt[3]{16}\cdot\sqrt[3]{4}=\sqrt[3]{64}=4\neq8$$ ❌

Gabarito único: **b)**
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-3** · cálculo · médio · inspirada em: Q-17

Racionalize o denominador das expressões abaixo e simplifique quando possível:

a) $$\dfrac{6}{\sqrt{3}}$$
b) $$\dfrac{10}{\sqrt[3]{5}}$$
c) $$\dfrac{4}{\sqrt{7} - \sqrt{3}}$$

✅ Gabarito:
📝 Resolução:

**a)** $$\dfrac{6}{\sqrt{3}} \cdot \dfrac{\sqrt{3}}{\sqrt{3}} = \dfrac{6\sqrt{3}}{3} = 2\sqrt{3}$$

**b)** $$\dfrac{10}{\sqrt[3]{5}} \cdot \dfrac{\sqrt[3]{5^2}}{\sqrt[3]{5^2}} = \dfrac{10\sqrt[3]{25}}{5} = 2\sqrt[3]{25}$$

**c)** $$\dfrac{4}{\sqrt{7}-\sqrt{3}} \cdot \dfrac{\sqrt{7}+\sqrt{3}}{\sqrt{7}+\sqrt{3}} = \dfrac{4(\sqrt{7}+\sqrt{3})}{7-3} = \dfrac{4(\sqrt{7}+\sqrt{3})}{4} = \sqrt{7}+\sqrt{3}$$

⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · estilo concurso · difícil · inspirada em: QC-2

*(Estilo ENEM)* Um engenheiro projeta uma caixa d'água cúbica para abastecer um condomínio. O volume necessário é de 13 824 litros. Sabendo que a aresta da caixa deve ser expressa em metros e que 1 m³ = 1000 litros, determine:

a) O volume da caixa em m³.
b) A aresta da caixa cúbica em metros. Expresse o desenvolvimento completo usando radiciação.
c) Qual o valor exato de $$\sqrt[3]{13{,}824}$$?

✅ Gabarito:
📝 Resolução:

**a)** $$V = 13824 \div 1000 = 13{,}824 \text{ m}^3$$

**b)** Aresta $$= \sqrt[3]{13{,}824}$$

**c)** $$13{,}824 = \frac{13824}{1000}$$
Fatorando 13824:
$$13824 = 2^9 \cdot 27 = 2^9 \cdot 3^3 = 512 \cdot 27$$
$$\sqrt[3]{13824} = \sqrt[3]{2^9 \cdot 3^3} = 2^3 \cdot 3 = 24$$
$$\sqrt[3]{13{,}824} = \frac{24}{10} = 2{,}4 \text{ m}$$

⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-5** · dissertativa · médio-difícil · inspirada em: Q-4

Três alunos calcularam a expressão $$E = \sqrt{(-5)^2 + 12^2} - \sqrt[3]{-27} + \sqrt[4]{81}$$ e obtiveram resultados diferentes:

- **Aluno A:** $$E = -5 + 12 + 3 + 3 = 13$$
- **Aluno B:** $$E = \sqrt{119} + 3 + 3 = \sqrt{119} + 6$$
- **Aluno C:** $$E = 13 - (-3) + 3 = 19$$

a) Identifique o erro cometido por cada aluno que errou.
b) Calcule o resultado correto de $$E$$, apresentando cada passo.

✅ Gabarito:
📝 Resolução:

**Resolução correta passo a passo:**
- $$(-5)^2 = 25$$; $$12^2 = 144$$; $$\sqrt{25 + 144} = \sqrt{169} = 13$$
- $$\sqrt[3]{-27} = -3$$ (índice ímpar, radicando negativo → resultado negativo)
- $$\sqrt[4]{81} = \sqrt[4]{3^4} = 3$$
- $$E = 13 - (-3) + 3 = 13 + 3 + 3 = \mathbf{19}$$

**Erros:**
- **Aluno A:** Não calculou $$\sqrt{(-5)^2 + 12^2}$$ corretamente — separou como $$-5 + 12$$ (violou a 3ª propriedade: vale para produto, não para soma sob raiz).
- **Aluno B:** Calculou $$(-5)^2 + 12^2 = 25 + 144 = 169$$ corretamente, mas não extraiu a raiz: $$\sqrt{169} = 13$$, não $$\sqrt{119}$$ (erro aritmético: $$25+144=169$$, não 119).
- **Aluno C:** Calculou corretamente! $$E = 13 + 3 + 3 = 19$$ ✅

⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: anatomia_radical
Estrutura e nomenclatura do símbolo radical com identificação de cada parte.

```svg
<svg width="100%" viewBox="0 0 680 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .c-purple { fill: #6c3fc5; }
      .c-teal   { fill: #0d7f7f; }
      .c-amber  { fill: #b07d00; }
      .c-coral  { fill: #c0392b; }
      .c-gray   { fill: #4a4a4a; }
      .c-green  { fill: #1a7a3f; }
      .th { font-family: Inter, sans-serif; font-size: 15px; font-weight: 700; fill: #fff; dominant-baseline: central; text-anchor: middle; }
      .t  { font-family: Inter, sans-serif; font-size: 13px; fill: #fff; dominant-baseline: central; text-anchor: middle; }
      .ts { font-family: Inter, sans-serif; font-size: 12px; fill: #333; dominant-baseline: central; text-anchor: middle; }
      .tl { font-family: Inter, sans-serif; font-size: 13px; fill: #333; dominant-baseline: central; text-anchor: start; }
    </style>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
    </marker>
  </defs>

  <!-- Título -->
  <rect x="140" y="10" width="400" height="44" rx="8" class="c-purple"/>
  <text x="340" y="32" class="th">Anatomia do Radical</text>

  <!-- Radical grande desenhado como texto -->
  <text x="340" y="110" font-family="Inter, sans-serif" font-size="72" fill="#1a3a5c" text-anchor="middle" dominant-baseline="central" font-weight="bold">ⁿ√a = b</text>

  <!-- Seta + label: Índice -->
  <line x1="230" y1="75" x2="270" y2="100" stroke="#6c3fc5" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="120" y="52" width="108" height="44" rx="8" class="c-purple"/>
  <text x="174" y="74" class="th">Índice (n)</text>

  <!-- Seta + label: Radicando -->
  <line x1="390" y1="75" x2="360" y2="100" stroke="#0d7f7f" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="390" y="52" width="130" height="44" rx="8" class="c-teal"/>
  <text x="455" y="74" class="th">Radicando (a)</text>

  <!-- Seta + label: Raiz -->
  <line x1="460" y1="150" x2="430" y2="120" stroke="#1a7a3f" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="460" y="150" width="100" height="44" rx="8" class="c-green"/>
  <text x="510" y="172" class="th">Raiz (b)</text>

  <!-- Seta + label: Símbolo Radical -->
  <line x1="190" y1="150" x2="260" y2="120" stroke="#b07d00" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="80" y="150" width="110" height="44" rx="8" class="c-amber"/>
  <text x="135" y="172" class="th">Radical</text>

  <!-- Condição de validade -->
  <rect x="100" y="195" width="480" height="18" rx="4" fill="#f0f0f0"/>
  <text x="340" y="204" class="ts">Condição: se n for par → a ≥ 0 | se n for ímpar → a ∈ ℝ</text>
</svg>
```

---

### DIAGRAMA: propriedades
Mapa das propriedades operacionais dos radicais com expressões e condições.

```svg
<svg width="100%" viewBox="0 0 680 380" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .c-purple { fill: #6c3fc5; }
      .c-teal   { fill: #0d7f7f; }
      .c-amber  { fill: #b07d00; }
      .c-coral  { fill: #c0392b; }
      .c-gray   { fill: #4a4a4a; }
      .c-green  { fill: #1a7a3f; }
      .th { font-family: Inter, sans-serif; font-size: 14px; font-weight: 700; fill: #fff; dominant-baseline: central; text-anchor: middle; }
      .t  { font-family: Inter, sans-serif; font-size: 12px; fill: #fff; dominant-baseline: central; text-anchor: middle; }
      .ts { font-family: Inter, sans-serif; font-size: 11px; fill: #333; dominant-baseline: central; text-anchor: middle; }
    </style>
    <marker id="arr2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
    </marker>
  </defs>

  <!-- Título -->
  <rect x="140" y="8" width="400" height="40" rx="8" class="c-purple"/>
  <text x="340" y="28" class="th">Propriedades dos Radicais</text>

  <!-- Nó central -->
  <rect x="255" y="62" width="170" height="44" rx="10" class="c-purple"/>
  <text x="340" y="84" class="th">Radicais</text>

  <!-- 3ª Prop Produto -->
  <line x1="255" y1="90" x2="155" y2="145" stroke="#555" stroke-width="1.5" marker-end="url(#arr2)"/>
  <rect x="30" y="142" width="240" height="58" rx="8" class="c-teal"/>
  <text x="150" y="162" class="th">3ª Prop. — Produto</text>
  <text x="150" y="182" class="t">ⁿ√(a·b) = ⁿ√a · ⁿ√b</text>

  <!-- 3ª Prop Quociente -->
  <line x1="280" y1="106" x2="200" y2="220" stroke="#555" stroke-width="1.5" marker-end="url(#arr2)"/>
  <rect x="30" y="218" width="240" height="58" rx="8" class="c-teal"/>
  <text x="150" y="238" class="th">3ª Prop. — Quociente</text>
  <text x="150" y="258" class="t">ⁿ√(a/b) = ⁿ√a / ⁿ√b</text>

  <!-- 4ª Prop Raiz de raiz -->
  <line x1="425" y1="90" x2="520" y2="145" stroke="#555" stroke-width="1.5" marker-end="url(#arr2)"/>
  <rect x="410" y="142" width="240" height="58" rx="8" class="c-amber"/>
  <text x="530" y="162" class="th">4ª Prop. — Raiz de Raiz</text>
  <text x="530" y="182" class="t">ᵐ√(ⁿ√a) = ᵐⁿ√a</text>

  <!-- Pot. Fracionária -->
  <line x1="400" y1="106" x2="460" y2="220" stroke="#555" stroke-width="1.5" marker-end="url(#arr2)"/>
  <rect x="410" y="218" width="240" height="58" rx="8" class="c-green"/>
  <text x="530" y="238" class="th">Potência Fracionária</text>
  <text x="530" y="258" class="t">ⁿ√(aᵐ) = a^(m/n)</text>

  <!-- Condições -->
  <rect x="200" y="295" width="280" height="44" rx="8" class="c-coral"/>
  <text x="340" y="310" class="th">⚠ Atenção!</text>
  <text x="340" y="328" class="t">Prod/Quot: índices iguais</text>

  <!-- Pegadinha -->
  <rect x="30" y="295" width="155" height="58" rx="8" fill="#fff0f0" stroke="#c0392b" stroke-width="1.5"/>
  <text x="107" y="315" class="ts" fill="#c0392b" font-weight="700">Pegadinha</text>
  <text x="107" y="333" class="ts">√(a+b) ≠ √a + √b</text>
  <text x="107" y="348" class="ts">Só vale p/ · e ÷</text>

  <!-- Raiz de índice diferentes -->
  <rect x="495" y="295" width="155" height="58" rx="8" fill="#e8f5e9" stroke="#1a7a3f" stroke-width="1.5"/>
  <text x="572" y="315" class="ts" fill="#1a7a3f" font-weight="700">Índices diferentes</text>
  <text x="572" y="333" class="ts">Use MMC dos</text>
  <text x="572" y="348" class="ts">índices para igualar</text>
</svg>
```

---

### DIAGRAMA: racionalizacao
Fluxo do processo de racionalização de denominador — simples e com conjugado.

```svg
<svg width="100%" viewBox="0 0 680 340" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .c-purple { fill: #6c3fc5; }
      .c-teal   { fill: #0d7f7f; }
      .c-amber  { fill: #b07d00; }
      .c-coral  { fill: #c0392b; }
      .c-gray   { fill: #4a4a4a; }
      .c-green  { fill: #1a7a3f; }
      .th { font-family: Inter, sans-serif; font-size: 13px; font-weight: 700; fill: #fff; dominant-baseline: central; text-anchor: middle; }
      .t  { font-family: Inter, sans-serif; font-size: 12px; fill: #fff; dominant-baseline: central; text-anchor: middle; }
      .ts { font-family: Inter, sans-serif; font-size: 11px; fill: #333; dominant-baseline: central; text-anchor: middle; }
    </style>
    <marker id="arr3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
    </marker>
  </defs>

  <!-- Título -->
  <rect x="140" y="8" width="400" height="40" rx="8" class="c-purple"/>
  <text x="340" y="28" class="th">Racionalização de Denominador</text>

  <!-- Passo 1: Identificar -->
  <rect x="220" y="62" width="240" height="44" rx="8" class="c-gray"/>
  <text x="340" y="77" class="th">Passo 1: Identificar</text>
  <text x="340" y="95" class="t">O denominador é irracional?</text>

  <!-- Seta para Passo 2 -->
  <line x1="340" y1="106" x2="340" y2="128" stroke="#555" stroke-width="1.5" marker-end="url(#arr3)"/>

  <!-- Passo 2: Tipo -->
  <rect x="220" y="128" width="240" height="44" rx="8" class="c-purple"/>
  <text x="340" y="143" class="th">Passo 2: Tipo de Denominador</text>
  <text x="340" y="161" class="t">Monômio ou Binômio?</text>

  <!-- Seta esquerda (monômio) -->
  <line x1="255" y1="172" x2="160" y2="205" stroke="#555" stroke-width="1.5" marker-end="url(#arr3)"/>
  <!-- Seta direita (binômio) -->
  <line x1="425" y1="172" x2="520" y2="205" stroke="#555" stroke-width="1.5" marker-end="url(#arr3)"/>

  <!-- Monômio -->
  <rect x="30" y="202" width="240" height="72" rx="8" class="c-teal"/>
  <text x="150" y="222" class="th">Monômio</text>
  <text x="150" y="242" class="t">Fator: ⁿ√(aⁿ⁻ᵐ)</text>
  <text x="150" y="260" class="t">b/ⁿ√(aᵐ) · ⁿ√(aⁿ⁻ᵐ)/ⁿ√(aⁿ⁻ᵐ)</text>

  <!-- Binômio -->
  <rect x="410" y="202" width="240" height="72" rx="8" class="c-amber"/>
  <text x="530" y="222" class="th">Binômio</text>
  <text x="530" y="242" class="t">Usar conjugado</text>
  <text x="530" y="260" class="t">(a+b)(a−b) = a²−b²</text>

  <!-- Resultado final -->
  <line x1="150" y1="274" x2="250" y2="302" stroke="#555" stroke-width="1.5" marker-end="url(#arr3)"/>
  <line x1="530" y1="274" x2="430" y2="302" stroke="#555" stroke-width="1.5" marker-end="url(#arr3)"/>
  <rect x="210" y="300" width="260" height="32" rx="8" class="c-green"/>
  <text x="340" y="316" class="th">Denominador Racional ✓</text>
</svg>
```

---

### DIAGRAMA: formulas
Resumo visual das fórmulas principais do capítulo.

```svg
<svg width="100%" viewBox="0 0 680 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .c-purple { fill: #6c3fc5; }
      .c-teal   { fill: #0d7f7f; }
      .c-amber  { fill: #b07d00; }
      .c-coral  { fill: #c0392b; }
      .c-gray   { fill: #4a4a4a; }
      .c-green  { fill: #1a7a3f; }
      .th { font-family: Inter, sans-serif; font-size: 13px; font-weight: 700; fill: #fff; dominant-baseline: central; text-anchor: middle; }
      .t  { font-family: Inter, sans-serif; font-size: 12px; fill: #fff; dominant-baseline: central; text-anchor: middle; }
      .ts { font-family: Inter, sans-serif; font-size: 11px; fill: #444; dominant-baseline: central; text-anchor: middle; }
    </style>
  </defs>

  <!-- Título -->
  <rect x="140" y="8" width="400" height="40" rx="8" class="c-purple"/>
  <text x="340" y="28" class="th">Fórmulas Principais — Radiciação</text>

  <!-- F1 -->
  <rect x="20" y="65" width="300" height="58" rx="8" class="c-purple"/>
  <text x="170" y="85" class="th">Definição</text>
  <text x="170" y="107" class="t">bⁿ = a  ⟺  ⁿ√a = b</text>

  <!-- F2 -->
  <rect x="360" y="65" width="300" height="58" rx="8" class="c-teal"/>
  <text x="510" y="85" class="th">Pot. Fracionária</text>
  <text x="510" y="107" class="t">ⁿ√(aᵐ) = a^(m/n)</text>

  <!-- F3 -->
  <rect x="20" y="145" width="300" height="58" rx="8" class="c-amber"/>
  <text x="170" y="165" class="th">3ª Prop. Produto</text>
  <text x="170" y="187" class="t">ⁿ√(a·b) = ⁿ√a · ⁿ√b</text>

  <!-- F4 -->
  <rect x="360" y="145" width="300" height="58" rx="8" class="c-amber"/>
  <text x="510" y="165" class="th">3ª Prop. Quociente</text>
  <text x="510" y="187" class="t">ⁿ√(a/b) = ⁿ√a / ⁿ√b</text>

  <!-- F5 -->
  <rect x="20" y="225" width="300" height="58" rx="8" class="c-green"/>
  <text x="170" y="245" class="th">4ª Prop. Raiz de Raiz</text>
  <text x="170" y="267" class="t">ᵐ√(ⁿ√a) = ᵐⁿ√a</text>

  <!-- F6 -->
  <rect x="360" y="225" width="300" height="58" rx="8" class="c-green"/>
  <text x="510" y="245" class="th">Racionalização</text>
  <text x="510" y="267" class="t">b/ⁿ√(aᵐ) = b·ⁿ√(aⁿ⁻ᵐ) / a</text>

  <!-- Pegadinha -->
  <rect x="20" y="305" width="300" height="72" rx="8" class="c-coral"/>
  <text x="170" y="325" class="th">⚠ Pegadinha 1</text>
  <text x="170" y="345" class="t">√(a+b) ≠ √a + √b</text>
  <text x="170" y="363" class="t">Prop. só p/ produto e quociente!</text>

  <!-- Pegadinha 2 -->
  <rect x="360" y="305" width="300" height="72" rx="8" class="c-coral"/>
  <text x="510" y="325" class="th">⚠ Pegadinha 2</text>
  <text x="510" y="345" class="t">a^(m/n): índice = denominador</text>
  <text x="510" y="363" class="t">Não trocar num. e den.!</text>
</svg>
```