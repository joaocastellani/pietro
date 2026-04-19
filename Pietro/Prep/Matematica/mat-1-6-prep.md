# mat-1-6-prep.md

---

## DIAGRAMAS DISPONÍVEIS — mat-1-6

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Tipos de Equação do 2º Grau | DIAGRAMA: tipos_equacao | Introdução à classificação completa/incompleta |
| Fórmulas de Resolução | DIAGRAMA: formulas | Apresentação das três fórmulas de resolução |
| Síntese do Livro | DIAGRAMA: sintese_livro | Fechamento/revisão do capítulo |

### Tabelas markdown (Seção 6):
- Tabela de categorias de aglomeração (Método de Jacobs)
- Tabela de versões de QR Code

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer. Tabelas da Seção 6 são apresentadas como markdown no chat.

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 6
- Tema: Equações do 2º grau
- Perfil: álgebra
- Fórmulas principais:
    ax² + bx + c = 0 (forma reduzida)
    x = ±√(−c/a)    (tipo ax² + c = 0)
    x = 0 ou x = −b/a  (tipo ax² + bx = 0)
    E = mc²         (Einstein — contextualização)
- Matemáticos citados: Albert Einstein
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### **Bloco 1 — O que é uma equação e seu grau**

Uma equação é toda expressão matemática que contém incógnitas — valores desconhecidos — ligadas por uma igualdade. O **grau** de uma equação é determinado pelo **maior expoente da incógnita** presente nela.

Exemplos concretos do material:
- $$3x + 14 = 7$$ → expoente máximo = 1 → **1º grau**
- $$x^2 + 4 = 0$$ → expoente máximo = 2 → **2º grau**
- $$x^5 - 12x + x^4 = 5$$ → expoente máximo = 5 → **5º grau** (atenção: não é 4º!)

> 💡 Conexão real: QR Codes crescem por versão — a quantidade de módulos em cada dimensão aumenta de acordo com uma relação quadrática, o que gera uma equação do 2º grau.

---

### **Bloco 2 — Forma reduzida e coeficientes**

Toda equação do 2º grau pode ser escrita na **forma reduzida**:

$$ax^2 + bx + c = 0, \quad a \neq 0, \quad a, b, c \in \mathbb{R}$$

Os três números $$a$$, $$b$$ e $$c$$ são chamados de **coeficientes**:
- $$a$$ → coeficiente do termo de 2º grau (**nunca zero**)
- $$b$$ → coeficiente do termo de 1º grau
- $$c$$ → termo independente

**Exemplo concreto:** $$4x^2 - 3x + 10 = 0$$ → $$a = 4$$, $$b = -3$$, $$c = 10$$

Para equações que não estão na forma reduzida, é preciso desenvolver e reorganizar:
$$3x^2 + (2+x)^2 - 5x = 12x + 1 \Rightarrow 4x^2 - 13x + 3 = 0$$

---

### **Bloco 3 — Equação completa vs. incompleta**

| Tipo | Condição | Exemplo |
|------|----------|---------|
| **Completa** | $$a \neq 0$$, $$b \neq 0$$, $$c \neq 0$$ | $$3x^2 + 12x - 7 = 0$$ |
| **Incompleta** (tipo I) | $$b = 0$$ | $$ax^2 + c = 0$$ |
| **Incompleta** (tipo II) | $$c = 0$$ | $$ax^2 + bx = 0$$ |
| **Incompleta** (tipo III) | $$b = 0$$ e $$c = 0$$ | $$ax^2 = 0$$ |

---

### **Bloco 4 — Raízes de uma equação do 2º grau**

A **raiz** (ou solução) é o valor que, ao ser substituído na incógnita, torna a igualdade verdadeira. Uma equação do 2º grau pode ter:
- **Duas raízes reais distintas**
- **Duas raízes reais iguais**
- **Nenhuma raiz real** (quando o radicando é negativo)

---

### **Bloco 5 — Resolução: tipo $$ax^2 + c = 0$$**

Estratégia: **isolar a incógnita**.

$$ax^2 = -c \Rightarrow x^2 = \frac{-c}{a} \Rightarrow x = \pm\sqrt{\frac{-c}{a}}$$

- Se $$\dfrac{-c}{a} > 0$$ → duas raízes reais opostas
- Se $$\dfrac{-c}{a} = 0$$ → raiz dupla igual a zero
- Se $$\dfrac{-c}{a} < 0$$ → **sem solução real** ($$S = \emptyset$$)

**Exemplo:** $$4x^2 - 25 = 0 \Rightarrow x = \pm\dfrac{5}{2}$$

---

### **Bloco 6 — Resolução: tipo $$ax^2 + bx = 0$$**

Estratégia: **colocar $$x$$ em evidência** e aplicar a propriedade do produto nulo.

$$x(ax + b) = 0 \Rightarrow x = 0 \quad \text{ou} \quad x = -\frac{b}{a}$$

Esta equação **sempre tem duas raízes reais**: uma nula e outra igual a $$-\dfrac{b}{a}$$.

**Exemplo:** $$4x^2 - 16x = 0 \Rightarrow x(4x - 16) = 0 \Rightarrow S = \{0, 4\}$$

---

### **Bloco 7 — Resolução: tipo $$ax^2 = 0$$**

Caso particular: $$b = 0$$ e $$c = 0$$. A única solução é $$x = 0$$ (raiz dupla nula).

$$x^2 = 0 \Rightarrow x = 0 \Rightarrow S = \{0, 0\}$$

---

## SEÇÃO 3 — MATEMÁTICOS E HISTÓRIA DA MATEMÁTICA

### Albert Einstein (1879–1955)
**Área:** Física teórica / Ciências exatas
**Contribuição no capítulo:** Desenvolveu, entre muitas contribuições para a Ciência, a equação que talvez seja a mais famosa do mundo, tornando-se capa da revista Times em 1946.
**O que desenvolveu:** A equação $$E = mc^2$$, que determina a relação de transformação da massa de um objeto em energia e vice-versa. Uma massa de 10 kg pode ser transformada em energia suficiente para evaporar toda a água da Baía de Guanabara, no Rio de Janeiro.
**Contexto histórico:** Século XX; teoria da relatividade especial.

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Forma reduzida da equação do 2º grau

**Expressão:** $$ax^2 + bx + c = 0$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | coeficiente do termo quadrático | real |
| $$b$$ | coeficiente do termo linear | real |
| $$c$$ | termo independente | real |
| $$x$$ | incógnita | real |

**Válida quando:** $$a \neq 0$$; $$a, b, c \in \mathbb{R}$$
💡 **Pegadinha:** Se $$a = 0$$, a equação deixa de ser do 2º grau — vira do 1º grau ou deixa de ser equação. Muitos alunos esquecem essa condição.

---

### Solução de $$ax^2 + c = 0$$

**Expressão:** $$x = \pm\sqrt{\dfrac{-c}{a}}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | coeficiente do termo quadrático | real ≠ 0 |
| $$c$$ | termo independente | real |
| $$x$$ | raízes da equação | real |

**Válida quando:** $$\dfrac{-c}{a} \geq 0$$
**Caso especial:** Se $$\dfrac{-c}{a} < 0$$, não há solução em $$\mathbb{R}$$ → $$S = \emptyset$$
💡 **Pegadinha:** O sinal de $$-c$$ não é o sinal de $$c$$. Em $$x^2 - 100 = 0$$, temos $$c = -100$$, logo $$-c = 100 > 0$$ → há solução. Em $$x^2 + 36 = 0$$, $$c = 36$$, então $$-c = -36 < 0$$ → sem solução real.

---

### Solução de $$ax^2 + bx = 0$$

**Expressão:** $$x = 0 \quad \text{ou} \quad x = -\dfrac{b}{a}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | coeficiente do termo quadrático | real ≠ 0 |
| $$b$$ | coeficiente do termo linear | real ≠ 0 |
| $$x$$ | raízes da equação | real |

**Válida quando:** $$a \neq 0$$
💡 **Pegadinha:** Alunos frequentemente dividem tudo por $$x$$ e perdem a raiz $$x = 0$$. Sempre fatorar — nunca cancelar $$x$$.

---

### Propriedade do produto nulo

**Expressão:** Se $$A \cdot B = 0$$, então $$A = 0$$ ou $$B = 0$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$A$$ | primeiro fator | real |
| $$B$$ | segundo fator | real |

**Válida quando:** O produto de dois fatores reais é zero.
💡 **Pegadinha:** A propriedade vale **apenas** quando o produto é igual a zero. Se $$A \cdot B = 6$$, não se pode concluir que $$A = 2$$ e $$B = 3$$.

---

### Equação de Einstein

**Expressão:** $$E = mc^2$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$E$$ | energia | Joules (J) |
| $$m$$ | massa | quilograma (kg) |
| $$c$$ | velocidade da luz | m/s |

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Categorias de aglomeração — Método de Jacobs

| Categoria | Área por pessoa |
|-----------|----------------|
| Leve | 1 m² por pessoa |
| Densa | 0,4 m² por pessoa |
| Mais densa | 0,2 m² por pessoa |

---

### Versões de QR Code — quantidade de módulos por dimensão

| Versão | Dimensão (módulos) | Total de módulos |
|--------|--------------------|-----------------|
| 1 | 21 × 21 | 441 |
| 2 | 25 × 25 | 625 |
| Maior | 177 × 177 | 31 329 |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Nunca cancele $$x$$ dos dois lados**
Em equações do tipo $$ax^2 + bx = 0$$, o erro mais grave é dividir ambos os lados por $$x$$. Isso elimina a raiz $$x = 0$$.
**Errado:** $$5x^2 - 125x = 0 \div x \Rightarrow 5x = 125 \Rightarrow x = 25$$ (perdeu $$x = 0$$!)
**Correto:** $$x(5x - 125) = 0 \Rightarrow x = 0$$ ou $$x = 25$$

---

💡 **Dica 2 — Cuidado com o sinal de $$-c/a$$**
Em $$ax^2 + c = 0$$, a condição de existência de raízes reais é $$\dfrac{-c}{a} \geq 0$$, e **não** $$\dfrac{c}{a} \geq 0$$. Se $$c > 0$$ e $$a > 0$$, já não há solução real.
**Exemplo:** $$x^2 + 36 = 0$$ → $$c = 36 > 0$$, $$a = 1 > 0$$ → $$\dfrac{-36}{1} < 0$$ → $$S = \emptyset$$

---

💡 **Dica 3 — Condição obrigatória: $$a \neq 0$$**
Se $$a = 0$$, a equação não é do 2º grau. Ao reduzir à forma reduzida, sempre confirme que o coeficiente de $$x^2$$ é diferente de zero antes de classificar a equação.

---

💡 **Dica 4 — Raízes opostas vs. raízes nula e não nula**
- Tipo $$ax^2 + c = 0$$: as duas raízes são **opostas** (ex.: $$+5$$ e $$-5$$).
- Tipo $$ax^2 + bx = 0$$: as raízes são **$$0$$ e $$-b/a$$** — não são opostas (a menos que $$b = 0$$, o que seria outro tipo).
Muitos alunos confundem os dois casos na questão V-F.

---

💡 **Dica 5 — Reduzir antes de classificar**
Nunca classifique uma equação sem antes colocá-la na forma reduzida. A equação $$(x-6)^2 = 3(x+12)$$ **parece** ter $$c \neq 0$$, mas após desenvolver resulta em $$x^2 - 15x = 0$$ — **incompleta do tipo II**.

---

💡 **Dica 6 — $$ax^2 = 0$$ sempre tem raiz dupla nula**
Não existe nenhum número real não nulo cujo quadrado seja zero. Portanto, a única solução é $$x = 0$$ (com multiplicidade 2). Isso nunca gera um conjunto vazio.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

### Bloco A — Lacunas de dados

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| BLOCO A | Período de vida de Einstein | Não citado explicitamente no material | Informar verbalmente: 1879–1955 |
| Q-14 | Dimensão do retângulo rosa | Figura parcialmente legível na captura | Verificar no livro físico e registrar a segunda dimensão |
| Q-2 | Enunciado d) | Aparece como $$5(x \cdot 1)^2$$ — possível OCR incorreto | Confirmar no livro; provável $$5(x+1)^2$$ |
| Q-25 | Figura do quadrado | Reconstrução parcial — variáveis $$x$$ e $$y$$ não totalmente identificadas | Verificar no livro físico |

### Bloco B — Inconsistências factuais

```
⚠️ ALERTA — Raiz da equação (exemplo do livro)
- Dado no material: "Na equação 9x + 31 = 3x + 4, a raiz é 2, pois
  substituindo x por 2: 3·2 + 4 = 10 e 3·2 + 4 = 10."
- Problema: Esta é uma equação do 1º grau, não do 2º grau. Além
  disso, 9·2 + 31 = 49 ≠ 3·2 + 4 = 10. A substituição está errada.
  A raiz correta de 9x + 31 = 3x + 4 é x = −27/6 = −4,5, não x = 2.
- Dado correto: O exemplo parece ser de outra equação. Possível
  equação original do livro: 2·(0)² − 3·0 = 0 e 2·(3)² − 3·3 = 9 ≠ 0
  (as raízes 0 e 3 citadas logo depois sugerem uma equação x² − 3x = 0).
- Impacto na aula: Não usar este exemplo de verificação de raiz com
  os alunos. Substituir pela verificação direta em x² − 3x = 0 com
  x = 0 e x = 3, que aparece logo em seguida no material.
```

```
⚠️ ALERTA — Síntese do livro: exemplo do tipo ax² + bx = 0
- Dado no material (Síntese, imagem): "Exemplo: −4x² + 3 = 0"
  aparece como exemplo do tipo ax² + bx = 0.
- Problema: −4x² + 3 = 0 é do tipo ax² + c = 0 (pois b = 0, c = 3),
  não do tipo ax² + bx = 0.
- Dado correto: O exemplo do tipo ax² + bx = 0 deveria ser algo
  como −4x² + 8x = 0.
- Impacto na aula: Alertar os alunos ao usar a Síntese do livro;
  corrigir verbalmente durante a aula de revisão.
```

```
⚠️ ALERTA — Ana (Q-17): raiz perdida
- Dado no material: Ana resolve x² − 400 = 0 e obtém apenas x = 20.
- Problema: A equação tem duas raízes: x = 20 e x = −20.
  Ana esqueceu o sinal negativo (±√400).
- Dado correto: S = {−20, 20}
- Impacto na aula: Este é o erro de Ana — confirmar com os alunos
  que a questão pede justamente que identifiquem esse erro.
```

```
⚠️ VISUAL AUSENTE — Bloco 5: resolução ax² + c = 0 (número de raízes)
- Sugestão: SVG mostrando os três casos (Δ > 0, Δ = 0, Δ < 0) em
  reta numérica, ou diagrama de fluxo de decisão.
- Ação: gerar SVG na Seção 12 (DIAGRAMA: casos_raizes).
```

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

### Bloco 1 — Conceitos e Definições

- **Grau de uma equação**
  - Definição: É determinado pelo `______` da incógnita. *(maior expoente)*
  - Notação: equação de grau $$n$$ → maior expoente da incógnita é `______` *(n)*

- **Equação do 2º grau**
  - Definição: Equação cujo maior expoente da incógnita é `______` *(2)*
  - Notação: forma reduzida `______` *(ax² + bx + c = 0)*

- **Equação completa**
  - Definição: Possui os três coeficientes $$a$$, $$b$$ e $$c$$ `______` *(diferentes de zero)*

- **Equação incompleta**
  - Definição: Possui o coeficiente `______` ou `______` (ou ambos) igual a zero. *(b / c)*

- **Raiz de uma equação**
  - Definição: Valor que, ao ser `______` à incógnita, torna a igualdade verdadeira. *(atribuído)*

### Bloco 2 — Fórmulas e Propriedades

- **Forma reduzida**
  - Expressão: `______` *(ax² + bx + c = 0)*
  - Condição: `______` *(a ≠ 0)*

- **Solução de ax² + c = 0**
  - Expressão: `______` *(x = ±√(−c/a))*
  - Condição de existência real: `______` *(−c/a ≥ 0)*

- **Solução de ax² + bx = 0**
  - Expressão: `______` *(x = 0 ou x = −b/a)*
  - Estratégia: `______` *(colocar x em evidência)*

- **Propriedade do produto nulo**
  - Expressão: Se $$A \cdot B = 0$$ então `______` *(A = 0 ou B = 0)*

### Bloco 3 — Lacunas para Warm-Up

1. O grau de uma equação é determinado pelo `______` da incógnita.
*(resposta: maior expoente)*

2. Uma equação do 2º grau na forma reduzida é escrita como `______`, com a condição de que `______`.
*(resposta: ax² + bx + c = 0 / a ≠ 0)*

3. Uma equação do 2º grau é **completa** quando `______`.
*(resposta: os três coeficientes a, b e c são diferentes de zero)*

4. Para resolver $$ax^2 + bx = 0$$, coloca-se `______` em evidência e aplica-se a propriedade `______`.
*(resposta: x / do produto nulo)*

5. A equação $$x^2 + 36 = 0$$ `______` possui raízes reais porque `______`.
*(resposta: não / −c/a = −36 < 0, e não existe número real cujo quadrado seja negativo)*

6. Albert Einstein ficou na capa da revista Times em `______` por ter desenvolvido, entre outras contribuições, a equação `______`.
*(resposta: 1946 / E = mc²)*

7. Pelo método de Jacobs, uma multidão **densa** é aquela em que cada pessoa ocupa `______` por pessoa.
*(resposta: 0,4 m²)*

8. A equação $$4x^2 - 16x = 0$$ tem como conjunto solução `______`.
*(resposta: S = {0, 4})*

### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Grau de uma equação | Determinado pelo `______` da incógnita → *maior expoente* |
| Forma reduzida do 2º grau | `______`, com $$a \neq 0$$ → *ax² + bx + c = 0* |
| Equação completa | Todos os coeficientes `______` → *diferentes de zero* |
| Solução de $$ax^2 + c = 0$$ | $$x =$$ `______` → *±√(−c/a)* |
| Solução de $$ax^2 + bx = 0$$ | $$x = 0$$ ou $$x =$$ `______` → *−b/a* |
| Propriedade do produto nulo | Se $$A \cdot B = 0$$, então `______` → *A = 0 ou B = 0* |
| Equação sem raízes reais | Ocorre quando $$-c/a$$ é `______` → *negativo* |
| Aplicação (Jacobs — densa) | Cada pessoa ocupa `______` → *0,4 m²* |
| Pegadinha: tipo $$ax^2 + bx = 0$$ | Nunca `______` por $$x$$ — perda de raiz nula → *dividir/cancelar* |
| Raízes de $$ax^2 = 0$$ | Sempre `______` → *x = 0 (raiz dupla nula)* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

### Síntese do Livro — EQUAÇÕES DO 2º GRAU

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| Nó central | Equações do 2º grau | — |
| Ramo esquerdo — definição | São aquelas que possuem o maior expoente de suas incógnitas igual a 2. Ex.: $$2x^2 - 4x + 3 = 0$$ | — |
| Ramo direito — forma | Podem sempre ser escritas na **forma reduzida** | `______` → *ax² + bx + c = 0* |
| Condição dos coeficientes | sendo a, b e c coeficientes da equação, com `______` e a, b e c reais | *a ≠ 0* |
| Sub-ramo esquerdo | **Equação completa:** apresenta os três coeficientes `______` | *diferentes de zero* |
| Exemplo equação completa | Ex.: $$-4x^2 - 8x + 3 = 0$$ | — |
| Sub-ramo direito | **Equação incompleta:** apresenta o coeficiente b, c ou ambos iguais a `______` | *zero* |
| Tipos de incompleta | Tipo $$ax^2 + c = 0$$ / Tipo `______` / Tipo $$ax^2 = 0$$ | *ax² + bx = 0* |
| Caixa: tipo $$ax^2 + c = 0$$ | a ≠ 0, c ≠ 0 e a e c com sinais opostos → duas raízes reais opostas. Forma: $$x = \pm\sqrt{-\dfrac{c}{a}}$$ | Exemplo: `______` → *−4x² − 8x = 0* *(nota: o livro usa −4x² − 8x = 0 como exemplo desta caixa — ver alerta na Seção 8)* |
| Caixa: tipo $$ax^2 + bx = 0$$ | uma raiz nula e outra como número real qualquer. $$x = 0$$ e $$x = -\dfrac{b}{a}$$ | Exemplo: `______` → *−4x² + 3 = 0* *(ver alerta Seção 8 — exemplo parece trocado no livro)* |
| Caixa: tipo $$ax^2 = 0$$ | Duas raízes reais e iguais a zero: $$x = 0$$ | Exemplo: `______` → *−4x² = 0* |

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| Q-1 | Identificar equações e incógnitas em 6 expressões | Dis | F | AT | a) sim, x; b) sim, x e y; c) não (igualdade sem incógnita); d) sim, x; e) não (inequação); f) sim, x e y | — |
| Q-2 | Indicar o grau de 4 equações (com desenvolvimento) | Cal | F | AT | a) 2º grau; b) 1º grau (x² se cancela); c) 5º grau; d) confirmar enunciado ⚠️ | ⚠️ item d) enunciado suspeito |
| Q-3 | Determinar coeficientes a, b, c de 6 equações | Cal | F | AT | a) a=1,b=5,c=−10; b) a=2,b=−15,c=45; c) a=3,b=−3,c=0; d) a=4,b=0,c=−100; e) a=1,b=−1,c=0; f) a=0,5,b=0,c=−12 | — |
| Q-4 | Reduzir 4 equações e determinar coeficientes | Cal | M | AT | a) 7x²−8x+14=0; b) 2x²+5x−6=0; c) 5x²+13x+17=0; d) −2x²−2x+¾=0 | — |
| Q-5 | Explicar por que a≠0 na equação do 2º grau | Dis | F | AT | Se a=0, o termo x² some e a equação deixa de ser do 2º grau | — |
| Q-6 | Classificar 6 equações em completa/incompleta | Dis | M | AT | a) incompleta (ax²+bx); b) completa; c) completa; d) completa; e) incompleta (ax²+bx); f) incompleta (ax²+bx) | — |
| Q-7 | Verificar se valores dados são raízes de 5 equações | Dis | M | AT | a) não (4−4+1=1≠0); b) sim (16−20+4=0); c) não (raiz negativa impossível em v²+25); d) sim; e) verificar | — |
| Q-8 | Resolver 6 equações do tipo ax²+c=0 | Cal | M | AT | a) S={−4,4}; b) S={−10,10}; c) S={−√20,√20}; d) S={−√2,√2}; e) S={−5,5}; f) S={−√75,√75} | — |
| Q-9 | Reduzir e resolver 3 equações com produtos notáveis | Cal | M | AT | a) desenvolver (2x+7)²=4x²+45→S={−3,3} aprox; b) desenvolver; c) x²+8x+16=8x+40→x²=24→S={−√24,√24} | — |
| Q-10 | Terreno 400m²; um lado é quádruplo do outro | Cal | M | AT | a) x·4x=400→4x²=400; b) x²=100→x=10; dimensões: 10m e 40m | — |
| Q-11 | Perguntas sobre equação do professor (ax²+bx=0) | Dis | M | AT | a) incompleta tipo II; b) a=1, b=valor do enunciado da aula, c=0; c) a outra solução é −b/a | — |
| Q-12 | Raízes de 6 equações do tipo ax²+bx=0 | Cal | M | AT | a) S={0,−1}; b) S={0,25}; c) S={0,2}; d) S={0,−1/2}; e) S={0,−√3/√2}; f) S={0,5} | — |
| Q-13 | Equação fracionária → reduzir e resolver | Cal | D | AT | Mmc=12: 3(x²−x)=12x−2(3x²−x)→3x²−3x=12x−6x²+2x→9x²−17x=0→x(9x−17)=0→S={0, 17/9} | — |
| Q-14 | Retângulos verde e rosa com áreas iguais → perímetro | Cal | D | AT | ⚠️ figura parcialmente capturada — conferir dimensão do rosa no livro | ⚠️ |
| Q-15 | Resolver 2 equações do tipo ax²=0 | Cal | F | AT | a) S={0,0}; b) S={0,0} | — |
| Q-16 | V-F: 5 afirmações sobre tipos de equação incompleta | V-F | M | AT | a) V (quando −c/a>0); b) F (a raiz é ±√(−c/a), não nula); c) F (raízes são 0 e −b/a, não opostas); d) V; e) V | — |
| Q-17 | Identificar erro de Ana ou Bruno | Dis | M | AT | Ana errou: esqueceu ±, obteve só x=20; correto: S={−20,20}. Bruno está correto. | — |
| Q-18 | Resolver 8 equações incompletas | Cal | M | AT | a) S={−4,4}; b) S={−√200,√200}; c) S={−35,35}; d) S={−5/4,5/4}; e) S={0,5}; f) S={0,3}; g) S={0,−27}; h) S={0,√7/√5} | — |
| Q-19 | Traduzir 4 frases em equações e resolver | Cal | M | AT | a) x²+36=100→x²=64→S={−8,8}; b) x²=3x→x²−3x=0→S={0,3}; c) x²=121→S={−11,11}; d) x²−45=396→x²=441→S={−21,21} | — |
| Q-20 | Potência do gerador = 300x−25x²; quando é nula? | MC | M | AT | x(300−25x)=0→x=0 ou x=12 → alternativa b) | — |
| Q-21 | Resolver 4 equações incompletas com desenvolvimento | Cal | D | AT | b) x²−16x+64=64−x²−4x→2x²−12x=0→S={0,6}; c) (x+5)²=10x+50→x²=25→S={−5,5}; d) verificar redução | — |
| Q-22 | Toalha retangular: largura = comprimento/3; área = 10800 cm² | Cal | M | AT | Seja comp=x, larg=x/3: x·(x/3)=10800→x²=32400→x=180cm; larg=60cm | — |
| Q-23 | Retângulo (x+5)×(x−4)=128 cm² | Cal | M | AT | x²+x−20=128→x²+x−148=0 → verificar se é ax²+c ou completa | — |
| Q-24 | Cubo mágico: área total da superfície = 240 cm² | Cal | M | AT | 6a²=240→a²=40→a=√40=2√10 cm | — |
| Q-25 | Quadrado maior com área 720 cm²; 4 regiões internas | Cal | D | AT | ⚠️ figura parcialmente capturada | ⚠️ |
| QC-1 | Raízes 3 e 1/3 em ax²−6x+p=0; valor de a+p | MC | D | AT | Soma das raízes: 3+1/3=10/3=6/a→a=9/5; Produto: 3·(1/3)=1=p/a→p=9/5; a+p=18/5 → rever alternativas | IF-CE |
| QC-2 | Cercado retangular; raízes de x²−45x+500=0; 5 voltas de arame | MC | D | AT | Raízes: x=20 e x=25; perímetro=2(20+25)=90m; 5 voltas=450m → alternativa e) | IF-SC |
| QC-3 | x²+3x=0: classificar as raízes | MC | M | AT | x(x+3)=0→x=0 ou x=−3; uma raiz nula e outra negativa → alternativa b) | Saresp |
| QC-4 | k para que x²+kx+6=0 tenha raízes 2 e 3 | MC | M | AT | Soma: 2+3=5=−k→k=−5 → alternativa a) | Fatec 2017 |
| QC-5 | Forno: T(t)=−t²/4+400; quando T=39? | MC | D | AT | 39=−t²/4+400→t²/4=361→t²=1444→t=38 → alternativa d) | ENEM |

---

### Bloco B — Questões modelo originais

---

**QM-1** · múltipla escolha · médio · inspirada em: Q-3

Uma equação do 2º grau tem a forma reduzida $$3x^2 - 7 = 0$$. Quais são seus coeficientes?

a) $$a = 3$$, $$b = 0$$, $$c = -7$$
b) $$a = 3$$, $$b = -7$$, $$c = 0$$
c) $$a = 0$$, $$b = 3$$, $$c = -7$$
d) $$a = 3$$, $$b = 7$$, $$c = 0$$

✅ Gabarito: a)
📝 Resolução: A equação $$3x^2 - 7 = 0$$ não possui termo em $$x$$, portanto $$b = 0$$. O coeficiente de $$x^2$$ é $$a = 3$$ e o termo independente é $$c = -7$.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · múltipla escolha · médio · inspirada em: Q-16 / QC-3

Qual das equações abaixo possui uma raiz igual a zero e outra raiz igual a $$-6$$?

a) $$x^2 + 6 = 0$$
b) $$x^2 - 36 = 0$$
c) $$x^2 + 6x = 0$$
d) $$x^2 - 6x = 0$$

✅ Gabarito: c)
📝 Resolução:
$$x^2 + 6x = 0 \Rightarrow x(x + 6) = 0$$
$$x = 0 \quad \text{ou} \quad x + 6 = 0 \Rightarrow x = -6$$
$$S = \{0, -6\}$$
As demais: a) sem raiz real; b) raízes ±6; d) raízes 0 e +6.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-3** · cálculo · médio · inspirada em: Q-10 / Q-22

Uma piscina retangular tem área igual a $$675 \text{ m}^2$$. Sabe-se que o comprimento da piscina é o triplo de sua largura.

a) Escreva uma equação do 2º grau que represente essa situação.
b) Determine as dimensões da piscina.

✅ Gabarito:
a) Seja $$x$$ a largura. Comprimento $$= 3x$$. Equação: $$3x^2 = 675$$
b) Resolução:
$$3x^2 = 675 \Rightarrow x^2 = 225 \Rightarrow x = \pm 15$$
Como medida de comprimento, $$x = 15$$ m.
Dimensões: largura = **15 m** e comprimento = **45 m**.
📝 Verificação: $$15 \times 45 = 675 \text{ m}^2$$ ✓
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · estilo concurso · difícil · inspirada em: QC-5 / Q-20

A altura (em metros) de um foguete de brinquedo $$t$$ segundos após o lançamento é dada por:

$$h(t) = -5t^2 + 20t$$

Determine os instantes $$t$$ (em segundos) em que o foguete está ao nível do solo ($$h = 0$$) e interprete cada solução no contexto do problema.

a) $$t = 0$$ e $$t = 2$$
b) $$t = 0$$ e $$t = 4$$
c) $$t = 4$$ e $$t = 20$$
d) $$t = 0$$ e $$t = 20$$
e) $$t = 2$$ e $$t = 4$$

✅ Gabarito: b)
📝 Resolução:
$$-5t^2 + 20t = 0 \Rightarrow t(-5t + 20) = 0$$
$$t = 0 \quad \text{ou} \quad -5t + 20 = 0 \Rightarrow t = 4$$
- $$t = 0$$: instante do lançamento (foguete ainda no solo).
- $$t = 4$$: foguete retorna ao solo após 4 segundos.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-5** · dissertativa · médio-difícil · inspirada em: Q-17 / Q-5

Caio resolveu a equação $$6x^2 - 18x = 0$$ da seguinte maneira:

> "Dividi os dois lados por $$x$$ e obtive $$6x - 18 = 0$$, portanto $$x = 3$$."

a) Caio cometeu algum erro? Justifique.
b) Apresente a resolução correta e o conjunto solução completo.

✅ Gabarito:
a) Sim. Ao dividir ambos os lados por $$x$$, Caio assumiu implicitamente que $$x \neq 0$$, o que eliminou a raiz $$x = 0$$. Nunca se pode dividir por uma expressão que pode valer zero.

b) Resolução correta:
$$6x^2 - 18x = 0$$
$$x(6x - 18) = 0$$
$$x = 0 \quad \text{ou} \quad 6x - 18 = 0 \Rightarrow x = 3$$
$$S = \{0, 3\}$$

⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: tipos_equacao
Classificação hierárquica das equações do 2º grau: completa e tipos incompletos.

```svg
<svg width="100%" viewBox="0 0 680 420">
<defs>
  <style>
    .c-purple{fill:#6c3fc5;} .c-teal{fill:#1a8a7a;} .c-amber{fill:#c87800;}
    .c-coral{fill:#c0392b;} .c-gray{fill:#555;} .c-green{fill:#2e7d32;}
    .t{font:bold 13px sans-serif;fill:#fff;text-anchor:middle;dominant-baseline:central;}
    .ts{font:11px sans-serif;fill:#333;text-anchor:middle;dominant-baseline:central;}
    .th{font:bold 14px sans-serif;fill:#fff;text-anchor:middle;dominant-baseline:central;}
    line{stroke:#555;stroke-width:1.5;}
  </style>
  <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
    <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
  </marker>
</defs>

<!-- Nó raiz -->
<rect x="215" y="10" width="250" height="44" rx="8" class="c-purple"/>
<text x="340" y="32" class="th">Equação do 2º grau</text>

<!-- Linhas para filhos -->
<line x1="340" y1="54" x2="340" y2="80" marker-end="url(#arr)"/>
<line x1="340" y1="80" x2="130" y2="80"/>
<line x1="340" y1="80" x2="550" y2="80"/>
<line x1="130" y1="80" x2="130" y2="100" marker-end="url(#arr)"/>
<line x1="550" y1="80" x2="550" y2="100" marker-end="url(#arr)"/>

<!-- Completa -->
<rect x="40" y="100" width="180" height="58" rx="8" class="c-teal"/>
<text x="130" y="120" class="t">Completa</text>
<text x="130" y="138" class="t">a≠0, b≠0, c≠0</text>

<!-- Incompleta -->
<rect x="460" y="100" width="180" height="44" rx="8" class="c-amber"/>
<text x="550" y="122" class="th">Incompleta</text>

<!-- Linha incompleta → 3 tipos -->
<line x1="550" y1="144" x2="550" y2="175"/>
<line x1="550" y1="175" x2="190" y2="175"/>
<line x1="550" y1="175" x2="550" y2="195" marker-end="url(#arr)"/>
<line x1="370" y1="175" x2="370" y2="195" marker-end="url(#arr)"/>
<line x1="190" y1="175" x2="190" y2="195" marker-end="url(#arr)"/>

<!-- Tipo I -->
<rect x="100" y="195" width="180" height="58" rx="8" class="c-coral"/>
<text x="190" y="215" class="t">Tipo I</text>
<text x="190" y="233" class="t">ax² + c = 0</text>

<!-- Tipo II -->
<rect x="280" y="195" width="180" height="58" rx="8" class="c-coral"/>
<text x="370" y="215" class="t">Tipo II</text>
<text x="370" y="233" class="t">ax² + bx = 0</text>

<!-- Tipo III -->
<rect x="460" y="195" width="180" height="58" rx="8" class="c-coral"/>
<text x="550" y="215" class="t">Tipo III</text>
<text x="550" y="233" class="t">ax² = 0</text>

<!-- Soluções -->
<line x1="190" y1="253" x2="190" y2="280" marker-end="url(#arr)"/>
<rect x="60" y="280" width="260" height="58" rx="6" class="c-gray"/>
<text x="190" y="300" class="t">x = ±√(−c/a)</text>
<text x="190" y="318" class="t">duas raízes opostas</text>

<line x1="370" y1="253" x2="370" y2="280" marker-end="url(#arr)"/>
<rect x="240" y="280" width="260" height="58" rx="6" class="c-gray"/>
<text x="370" y="300" class="t">x=0 ou x=−b/a</text>
<text x="370" y="318" class="t">raiz nula + outra real</text>

<line x1="550" y1="253" x2="550" y2="280" marker-end="url(#arr)"/>
<rect x="420" y="280" width="220" height="58" rx="6" class="c-gray"/>
<text x="530" y="300" class="t">x = 0</text>
<text x="530" y="318" class="t">raiz dupla nula</text>

<!-- Exemplos -->
<text x="190" y="365" class="ts">Ex.: x² − 100 = 0</text>
<text x="190" y="380" class="ts">S = {−10, 10}</text>
<text x="370" y="365" class="ts">Ex.: 4x² − 16x = 0</text>
<text x="370" y="380" class="ts">S = {0, 4}</text>
<text x="530" y="365" class="ts">Ex.: 2x² = 0</text>
<text x="530" y="380" class="ts">S = {0, 0}</text>
</svg>
```

---

### DIAGRAMA: formulas
Fórmulas de resolução das equações incompletas do 2º grau com variáveis e pegadinhas.

```svg
<svg width="100%" viewBox="0 0 680 340">
<defs>
  <style>
    .c-purple{fill:#6c3fc5;} .c-teal{fill:#1a8a7a;} .c-amber{fill:#c87800;}
    .c-coral{fill:#c0392b;} .c-gray{fill:#555;} .c-green{fill:#2e7d32;}
    .t{font:bold 13px sans-serif;fill:#fff;text-anchor:middle;dominant-baseline:central;}
    .ts{font:11px sans-serif;fill:#333;text-anchor:middle;dominant-baseline:central;}
    .th{font:bold 13px sans-serif;fill:#fff;text-anchor:middle;dominant-baseline:central;}
    line{stroke:#999;stroke-width:1.5;}
  </style>
  <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
    <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
  </marker>
</defs>

<!-- Cabeçalho -->
<rect x="190" y="10" width="300" height="40" rx="8" class="c-purple"/>
<text x="340" y="30" class="th">Fórmulas — Equação do 2º grau</text>

<!-- Linha 1: ax² + c = 0 -->
<rect x="10" y="70" width="160" height="44" rx="6" class="c-teal"/>
<text x="90" y="92" class="t">ax² + c = 0</text>

<line x1="170" y1="92" x2="210" y2="92" marker-end="url(#arr)"/>

<rect x="212" y="70" width="200" height="44" rx="6" class="c-amber"/>
<text x="312" y="92" class="t">x = ±√(−c / a)</text>

<line x1="412" y1="92" x2="452" y2="92" marker-end="url(#arr)"/>

<rect x="454" y="58" width="218" height="72" rx="6" class="c-coral"/>
<text x="563" y="78" class="t">⚠️ Pegadinha</text>
<text x="563" y="96" class="t">Se −c/a &lt; 0:</text>
<text x="563" y="114" class="t">S = ∅ (sem raiz real)</text>

<!-- Linha 2: ax² + bx = 0 -->
<rect x="10" y="155" width="160" height="44" rx="6" class="c-teal"/>
<text x="90" y="177" class="t">ax² + bx = 0</text>

<line x1="170" y1="177" x2="210" y2="177" marker-end="url(#arr)"/>

<rect x="212" y="155" width="200" height="44" rx="6" class="c-amber"/>
<text x="312" y="170" class="t">x = 0</text>
<text x="312" y="188" class="t">ou x = −b/a</text>

<line x1="412" y1="177" x2="452" y2="177" marker-end="url(#arr)"/>

<rect x="454" y="143" width="218" height="72" rx="6" class="c-coral"/>
<text x="563" y="163" class="t">⚠️ Pegadinha</text>
<text x="563" y="181" class="t">Não divida por x!</text>
<text x="563" y="199" class="t">Perde x = 0.</text>

<!-- Linha 3: ax² = 0 -->
<rect x="10" y="240" width="160" height="44" rx="6" class="c-teal"/>
<text x="90" y="262" class="t">ax² = 0</text>

<line x1="170" y1="262" x2="210" y2="262" marker-end="url(#arr)"/>

<rect x="212" y="240" width="200" height="44" rx="6" class="c-amber"/>
<text x="312" y="262" class="t">x = 0 (raiz dupla)</text>

<line x1="412" y1="262" x2="452" y2="262" marker-end="url(#arr)"/>

<rect x="454" y="240" width="218" height="44" rx="6" class="c-gray"/>
<text x="563" y="262" class="t">S = {0, 0} sempre</text>
</svg>
```

---

### DIAGRAMA: sintese_livro
Fluxograma da Síntese do livro — Equações do 2º grau (pág. 151).

```svg
<svg width="100%" viewBox="0 0 680 520">
<defs>
  <style>
    .c-purple{fill:#6c3fc5;} .c-teal{fill:#1a8a7a;} .c-amber{fill:#c87800;}
    .c-coral{fill:#c0392b;} .c-gray{fill:#555;} .c-green{fill:#2e7d32;}
    .t{font:bold 12px sans-serif;fill:#fff;text-anchor:middle;dominant-baseline:central;}
    .ts{font:11px sans-serif;fill:#333;text-anchor:middle;dominant-baseline:central;}
    .tb{font:bold 12px sans-serif;fill:#333;text-anchor:middle;dominant-baseline:central;}
    line{stroke:#c87800;stroke-width:2;}
  </style>
  <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
    <path d="M0,0 L0,6 L8,3 Z" fill="#c87800"/>
  </marker>
</defs>

<!-- Topo: nó central -->
<rect x="215" y="10" width="250" height="44" rx="8" class="c-purple"/>
<text x="340" y="32" class="t">Equações do 2º grau</text>

<!-- Ramo esquerdo: definição -->
<line x1="280" y1="54" x2="140" y2="100" marker-end="url(#arr)"/>
<rect x="20" y="100" width="240" height="72" rx="6" class="c-teal"/>
<text x="140" y="120" class="t">Maior expoente da</text>
<text x="140" y="138" class="t">incógnita = 2</text>
<text x="140" y="156" class="t">Ex.: 2x² − 4x + 3 = 0</text>

<!-- Ramo direito: forma reduzida -->
<line x1="400" y1="54" x2="540" y2="100" marker-end="url(#arr)"/>
<rect x="420" y="100" width="240" height="72" rx="6" class="c-teal"/>
<text x="540" y="116" class="t">Forma reduzida:</text>
<text x="540" y="134" class="t">ax² + bx + c = 0</text>
<text x="540" y="152" class="t">a≠0; a, b, c ∈ ℝ</text>

<!-- Seta central para completa/incompleta -->
<line x1="340" y1="54" x2="340" y2="200" marker-end="url(#arr)"/>

<!-- Completa -->
<rect x="20" y="200" width="240" height="72" rx="6" fill="#1a4fa0"/>
<text x="140" y="218" class="t">EQUAÇÃO COMPLETA</text>
<text x="140" y="236" class="t">a≠0, b≠0, c≠0</text>
<text x="140" y="254" class="t">Ex.: −4x² − 8x + 3 = 0</text>

<!-- Incompleta -->
<rect x="420" y="200" width="240" height="88" rx="6" class="c-coral"/>
<text x="540" y="218" class="t">EQUAÇÃO INCOMPLETA</text>
<text x="540" y="236" class="t">b=0 ou c=0 (ou ambos)</text>
<text x="540" y="254" class="t">ax²+c=0 / ax²+bx=0</text>
<text x="540" y="272" class="t">ax²=0</text>

<!-- Linhas para caixas de resolução -->
<line x1="540" y1="288" x2="540" y2="320"/>
<line x1="540" y1="320" x2="200" y2="320"/>
<line x1="200" y1="320" x2="200" y2="340" marker-end="url(#arr)"/>
<line x1="370" y1="320" x2="370" y2="340" marker-end="url(#arr)"/>
<line x1="540" y1="320" x2="540" y2="340" marker-end="url(#arr)"/>

<!-- Caixa tipo I -->
<rect x="60" y="340" width="280" height="72" rx="6" class="c-gray"/>
<text x="200" y="358" class="t">ax² + c = 0</text>
<text x="200" y="376" class="t">x = ±√(−c/a)</text>
<text x="200" y="394" class="t">duas raízes opostas</text>

<!-- Caixa tipo II -->
<rect x="230" y="340" width="280" height="72" rx="6" fill="#2e7d32"/>
<text x="370" y="358" class="t">ax² + bx = 0</text>
<text x="370" y="376" class="t">x=0 ou x=−b/a</text>
<text x="370" y="394" class="t">raiz nula + outra real</text>

<!-- Caixa tipo III -->
<rect x="400" y="340" width="260" height="72" rx="6" class="c-amber"/>
<text x="530" y="358" class="t">ax² = 0</text>
<text x="530" y="376" class="t">x = 0</text>
<text x="530" y="394" class="t">raiz dupla nula</text>

<!-- Exemplos linha final -->
<text x="200" y="432" class="ts">Ex.: −4x²−8x=0</text>
<text x="370" y="432" class="ts">Ex.: −4x²+3=0 ⚠️</text>
<text x="530" y="432" class="ts">Ex.: −4x²=0</text>

<!-- Aviso -->
<rect x="160" y="450" width="360" height="44" rx="6" class="c-coral"/>
<text x="340" y="466" class="t">⚠️ Atenção: exemplos das caixas II e III</text>
<text x="340" y="484" class="t">podem estar trocados no livro (ver Seção 8)</text>
</svg>
```

---

> ✅ **Preparação concluída — mat-1-6-prep.md**
>
> **Resumo do arquivo gerado:**
> - **Seção 0:** Índice de 3 diagramas SVG + 2 tabelas markdown
> - **Seções 1–4:** Metadados, resumo em 7 blocos temáticos, Einstein, 5 fórmulas/propriedades
> - **Seção 6:** 2 tabelas de referência (Jacobs + QR Code)
> - **Seção 7:** 6 dicas de ouro com exemplos numéricos
> - **Seção 8:** 3 alertas de inconsistência factual (exemplo de raiz errado, exemplo trocado na Síntese, erro de Ana na Q-17) + 4 lacunas de dados + 1 visual ausente
> - **Seção 9:** Warm-up com 8 lacunas + tabela síntese de 10 linhas
> - **Seção 10:** Síntese do livro mapeada linha a linha (imagem fornecida)
> - **Seção 11:** 30 questões catalogadas com gabaritos inferidos + 5 questões modelo originais (QM-1 a QM-5)
> - **Seção 12:** 3 SVGs embutidos (tipos_equacao · formulas · sintese_livro)
>
> **⚠️ Ação prioritária antes da aula:** Conferir no livro físico os exemplos das caixas da Síntese (pág. 151) — os exemplos dos tipos $$ax^2 + bx = 0$$ e $$ax^2 + c = 0$$ parecem estar trocados.