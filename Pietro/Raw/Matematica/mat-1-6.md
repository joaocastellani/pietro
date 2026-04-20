# mat-1-6.md

---

## 1. METADADOS

- Matéria: Matemática
- Unidade: 1
- Capítulo/Tema: 6 — Equações do 2º grau
- Nível de ensino: 9º ano
- Perfil do capítulo: álgebra

---

## 2. CONCEITOS E DEFINIÇÕES

**Equação**
- Toda equação é aquela que contém incógnitas, ou seja, valores desconhecidos.

**Grau de uma equação**
- O que determina o grau de uma equação é o maior dos expoentes de uma incógnita.
- Exemplos:
  - $$3x + 14 = 7$$ → expoente da incógnita é 1 → equação do 1º grau
  - $$\frac{x}{4} - 3x = 0$$ → expoente é 1 → equação do 1º grau
  - $$x^2 + 4 = 0$$ → maior expoente é 2 → equação do 2º grau
  - $$x^5 - 12x + x^4 = 5$$ → maior expoente é 4 → equação do 4º grau (não do 2º grau)

**Equação do 2º grau — definição**
- Uma equação do 2º grau com uma incógnita é aquela que pode ser escrita em sua **forma reduzida** $$ax^2 + bx + c = 0$$, com os **coeficientes da equação** $$a$$, $$b$$ e $$c$$ pertencentes aos números reais e $$a \neq 0$$.

**Coeficientes da equação**
- Na equação $$4x^2 - 3x + 10 = 0$$: $$a = 4$$, $$b = -3$$, $$c = 10$$
- Na equação $$3x^2 + (2+x)^2 - 5x = 12x + 1$$, desenvolvendo:
$$3x^2 + 4 + 4x + x^2 - 5x = 12x + 1$$
$$4x^2 - 13x + 3 = 0$$
Logo: $$a = 4$$, $$b = -13$$, $$c = 3$$

**Equação completa**
- Quando uma equação do 2º grau, na sua forma reduzida, possui todos os coeficientes (a, b e c) diferentes de zero, ela é considerada uma **equação completa**.
- Exemplos:
  - $$3x^2 + 12x - 7 = 0$$ → equação completa
  - $$7x + 6x = 0$$ → **não** é equação completa (pois não está em forma reduzida do 2º grau)
  - $$3x^2 - 7 = 0$$ → equação incompleta
  - $$7x + 6x = 0$$ → equação incompleta
  - $$9x^2 + 5x - 4 = 0$$ → equação completa
  - $$x^2 = 0$$ → equação incompleta

**Equação incompleta**
- Quando o coeficiente $$b$$ ou $$c$$ (ou ambos) é igual a zero, a equação é considerada **incompleta**.

**Raiz (ou solução) de uma equação do 2º grau**
- É o valor que, ao ser atribuído à incógnita, torna a igualdade verdadeira.
- Exemplo: Na equação $$9x + 31 = 3x + 4$$, a raiz é 2, pois substituindo $$x$$ por 2: $$3 \cdot 2 + 4 = 10$$ e $$3 \cdot 2 + 4 = 10$$.
- As equações do 2º grau podem ter até duas raízes reais distintas; há casos em que as duas raízes são reais e iguais, e casos em que não há nenhuma raiz real.
- Para encontrar as duas raízes distintas, basta encontrar os dois valores diferentes para $$x$$ que satisfazem a equação. Os valores são: 0 e 3.

**Verificação das raízes — exemplo do livro:**
$$x^2 - 3x = -36$$: equação do 2º grau incompleta (pois $$b = 0$$), na qual a incógnita com expoente 2 é igual a um número negativo. A equação não apresenta raízes reais.

**Resolução de equações na forma $$ax^2 + c = 0$$**
- Isola-se a incógnita:
$$ax^2 + c = 0 \Rightarrow ax^2 = -c \Rightarrow x^2 = \frac{-c}{a} \Rightarrow x = \pm\sqrt{\frac{-c}{a}}$$
- Exemplo resolvido 1: $$x^2 - 100 = 0$$
$$x^2 = 100 \Rightarrow x = \pm\sqrt{100} \Rightarrow x = \pm 10$$
$$S = \{-10, 10\}$$
- Exemplo resolvido 2: $$4x^2 - 25 = 0$$
$$x^2 = \frac{25}{4} \Rightarrow x = \pm\sqrt{\frac{25}{4}} = \pm\frac{5}{2}$$
$$S = \left\{-\frac{5}{2}, \frac{5}{2}\right\}$$
- Exemplo resolvido 3: $$x^2 + 36 = 0$$
$$x^2 = -36 \Rightarrow x = \pm\sqrt{-36}$$
Como não existe número real cujo quadrado resulta em $$-36$$, **a equação não possui solução dentro do conjunto dos números reais.**

**Resolução de equações na forma $$ax^2 + bx = 0$$**
- Coloca-se o $$x$$ em evidência: $$x(ax + b) = 0$$
- Para obter zero como resultado, pelo menos um dos fatores deve ser igual a zero:
$$x = 0 \quad \text{ou} \quad ax + b = 0$$
- Exemplo resolvido 4: $$x^2 + 2x = 0$$
$$x(x + 2) = 0$$
$$x = 0 \quad \text{ou} \quad x + 2 = 0 \Rightarrow x = -2$$
$$S = \{0, -2\}$$
- Exemplo resolvido 5: $$4x^2 - 16x = 0$$
$$x(4x - 16) = 0$$
$$x = 0 \quad \text{ou} \quad 4x = 16 \Rightarrow x = 4$$
$$S = \{0, 4\}$$
- Exemplo resolvido 6: $$(x-6)^2 = 3(x + 12)$$
$$x^2 - 12x + 36 = 3x + 36$$
$$x^2 - 12x + 36 - 3x - 36 = 0$$
$$x^2 - 15x = 0$$
$$x(x - 15) = 0$$
$$x = 0 \quad \text{ou} \quad x = 15$$
$$S = \{0, 15\}$$

**Resolução de equações na forma $$ax^2 = 0$$**
- A ideia é a mesma usada para $$ax^2 + c = 0$$, mas com $$b = 0$$ e $$c = 0$$.
$$x^2 = \frac{0}{a} = 0 \Rightarrow x = \pm\sqrt{0} = 0$$
- As duas soluções da equação são zero: $$S = \{0, 0\}$$
- Exemplo resolvido 7:
  - a) $$2x^2 = 0 \Rightarrow x = \pm\sqrt{0} = 0 \Rightarrow S = \{0, 0\}$$
  - b) $$-10x^2 = 0 \Rightarrow x = \pm\sqrt{0} = 0 \Rightarrow S = \{0, 0\}$$

---

## 3. FLASHCARDS DO CAPÍTULO

**FC-1**
Frente: O que determina o grau de uma equação?
Verso: O maior dos expoentes de uma incógnita.

**FC-2**
Frente: Qual a forma reduzida de uma equação do 2º grau?
Verso: $$ax^2 + bx + c = 0$$, com $$a, b, c \in \mathbb{R}$$ e $$a \neq 0$$.

**FC-3**
Frente: O que é uma equação do 2º grau completa?
Verso: Aquela cuja forma reduzida possui todos os coeficientes $$a$$, $$b$$ e $$c$$ diferentes de zero.

**FC-4**
Frente: O que é uma equação do 2º grau incompleta?
Verso: Aquela em que o coeficiente $$b$$, $$c$$ ou ambos são iguais a zero.

**FC-5**
Frente: Quais são os três tipos de equação incompleta do 2º grau?
Verso: Tipo $$ax^2 + c = 0$$; tipo $$ax^2 + bx = 0$$; tipo $$ax^2 = 0$$.

**FC-6**
Frente: Como se resolve uma equação do tipo $$ax^2 + c = 0$$?
Verso: Isolando a incógnita: $$x = \pm\sqrt{\dfrac{-c}{a}}$$. Exige que $$\dfrac{-c}{a} \geq 0$$ para ter solução real.

**FC-7**
Frente: Como se resolve uma equação do tipo $$ax^2 + bx = 0$$?
Verso: Coloca-se $$x$$ em evidência: $$x(ax + b) = 0$$, resultando em $$x = 0$$ ou $$x = -\dfrac{b}{a}$$.

**FC-8**
Frente: Quais são as raízes da equação $$ax^2 = 0$$?
Verso: As duas raízes são iguais a zero: $$S = \{0, 0\}$$.

**FC-9**
Frente: Quando a equação $$ax^2 + c = 0$$ não possui raízes reais?
Verso: Quando $$\dfrac{-c}{a} < 0$$, pois não existe número real cujo quadrado seja negativo.

**FC-10**
Frente: Quais são os coeficientes de $$4x^2 - 3x + 10 = 0$$?
Verso: $$a = 4$$, $$b = -3$$, $$c = 10$$.

**FC-11**
Frente: O que é a raiz (ou solução) de uma equação?
Verso: É o valor que, ao ser atribuído à incógnita, torna a igualdade verdadeira.

**FC-12**
Frente: Quantas raízes reais pode ter uma equação do 2º grau?
Verso: Até duas raízes reais distintas; pode também ter duas iguais ou nenhuma raiz real.

**FC-13**
Frente: Como resolver $$(x-6)^2 = 3(x+12)$$?
Verso: Desenvolver, reduzir à forma $$ax^2 + bx = 0$$, colocar $$x$$ em evidência: $$S = \{0, 15\}$$.

**FC-14**
Frente: A equação $$-4x^2 + 3 = 0$$ é completa ou incompleta?
Verso: Incompleta, pois $$b = 0$$.

**FC-15**
Frente: Qual a solução de $$4x^2 - 25 = 0$$?
Verso: $$x = \pm\dfrac{5}{2}$$; $$S = \left\{-\dfrac{5}{2}, \dfrac{5}{2}\right\}$$.

---

## BLOCO A — MATEMÁTICOS E CIENTISTAS CITADOS

**Albert Einstein**
- Contribuição descrita no texto: desenvolveu, entre muitas de suas grandes contribuições para a Ciência, a equação que talvez seja a equação física mais famosa do mundo, tornando-se capa da prestigiada revista Times em 1946.
- Conceito ou teorema associado: $$E = mc^2$$, onde $$E$$ é energia, $$m$$ é massa e $$c$$ é velocidade da luz. Tal equação determina a relação de transformação da massa de um objeto em energia, e vice-versa. Para se ter uma ideia, uma massa de 10 kg pode ser transformada em energia suficiente para fazer evaporar toda a água da Baía de Guanabara, no Rio de Janeiro.

---

## BLOCO B — PROPRIEDADES E REGRAS OPERACIONAIS

**Propriedade do produto nulo**
- Enunciado: Para obter zero como resultado, pelo menos um dos fatores deve ser igual a zero.
- Expressão simbólica: Se $$A \cdot B = 0$$, então $$A = 0$$ ou $$B = 0$$.
- Aplicação: usada para resolver equações do tipo $$ax^2 + bx = 0$$ após colocar $$x$$ em evidência.

**Determinação do grau**
- Enunciado: O grau de uma equação é determinado pelo maior expoente de sua incógnita.

**Condição de equação do 2º grau**
- Enunciado: O coeficiente $$a$$ de uma equação do 2º grau deve ser sempre diferente de zero ($$a \neq 0$$), pois caso contrário a equação não seria do 2º grau.

---

## BLOCO C — FÓRMULAS PRINCIPAIS

**Forma reduzida da equação do 2º grau**
- Expressão: $$ax^2 + bx + c = 0$$
- Variáveis: $$a$$ = coeficiente do termo de 2º grau; $$b$$ = coeficiente do termo de 1º grau; $$c$$ = termo independente; $$x$$ = incógnita
- Condições de aplicação: $$a \neq 0$$; $$a, b, c \in \mathbb{R}$$

**Solução da equação do tipo $$ax^2 + c = 0$$**
- Expressão: $$x = \pm\sqrt{\dfrac{-c}{a}}$$
- Variáveis: $$a$$ = coeficiente do termo quadrático; $$c$$ = termo independente; $$x$$ = incógnita
- Condições de aplicação: $$a \neq 0$$; $$\dfrac{-c}{a} \geq 0$$ para existir solução real
- Caso especial: se $$\dfrac{-c}{a} < 0$$, a equação não possui solução no conjunto dos números reais

**Solução da equação do tipo $$ax^2 + bx = 0$$**
- Expressão: $$x = 0 \quad \text{ou} \quad x = -\dfrac{b}{a}$$
- Variáveis: $$a$$ = coeficiente do termo quadrático; $$b$$ = coeficiente do termo linear; $$x$$ = incógnita
- Condições de aplicação: $$a \neq 0$$

**Equação de Einstein (citada no capítulo)**
- Expressão: $$E = mc^2$$
- Variáveis: $$E$$ = energia; $$m$$ = massa; $$c$$ = velocidade da luz

---

## BLOCO E — EXEMPLOS RESOLVIDOS E EXERCÍCIOS DE FIXAÇÃO

**Exemplo Resolvido 1**
- Identificação: Exercício Resolvido 1
- Enunciado: Encontre o conjunto solução da equação $$x^2 - 100 = 0$$ no conjunto $$\mathbb{R}$$.
- Desenvolvimento:
$$x^2 - 100 = 0 \Rightarrow x^2 = 100$$
$$x = \pm\sqrt{100} \Rightarrow x = \pm 10$$
- Resultado final: $$S = \{-10, 10\}$$
- Conceito aplicado: Resolução de equação do tipo $$ax^2 + c = 0$$

---

**Exemplo Resolvido 2**
- Identificação: Exercício Resolvido 2
- Enunciado: Encontre o conjunto solução da equação $$4x^2 - 25 = 0$$ no conjunto $$\mathbb{R}$$.
- Desenvolvimento:
$$4x^2 = 25 \Rightarrow x^2 = \frac{25}{4}$$
$$x = \pm\sqrt{\frac{25}{4}} = \pm\frac{5}{2}$$
- Resultado final: $$S = \left\{-\frac{5}{2}, \frac{5}{2}\right\}$$
- Conceito aplicado: Resolução de equação do tipo $$ax^2 + c = 0$$

---

**Exemplo Resolvido 3**
- Identificação: Exercício Resolvido 3
- Enunciado: Encontre o conjunto solução da equação $$x^2 + 36 = 0$$ no conjunto $$\mathbb{R}$$.
- Desenvolvimento:
$$x^2 = -36 \Rightarrow x = \pm\sqrt{-36}$$
Como não existe um número real elevado ao quadrado que resulte em $$-36$$, a equação não possui solução dentro do conjunto dos números reais.
- Resultado final: $$S = \emptyset$$
- Conceito aplicado: Inexistência de raízes reais quando $$\frac{-c}{a} < 0$$

---

**Exemplo Resolvido 4**
- Identificação: Exercício Resolvido 4
- Enunciado: Resolva a equação $$x^2 + 2x = 0$$ no conjunto $$\mathbb{R}$$.
- Desenvolvimento:
Colocar $$x$$ em evidência: $$x(x + 2) = 0$$
Para obter zero como resultado, pelo menos um dos fatores deve ser igual a zero:
$$x = 0 \quad \text{ou} \quad x + 2 = 0 \Rightarrow x = -2$$
- Resultado final: $$S = \{0, -2\}$$
- Conceito aplicado: Resolução de equação do tipo $$ax^2 + bx = 0$$; propriedade do produto nulo

---

**Exemplo Resolvido 5**
- Identificação: Exercício Resolvido 5
- Enunciado: Resolva a equação $$4x^2 - 16x = 0$$ no conjunto $$\mathbb{R}$$.
- Desenvolvimento:
Colocar $$x$$ em evidência: $$x(4x - 16) = 0$$
$$x = 0 \quad \text{ou} \quad 4x - 16 = 0 \Rightarrow x = 4$$
- Resultado final: $$S = \{0, 4\}$$
- Conceito aplicado: Resolução de equação do tipo $$ax^2 + bx = 0$$; propriedade do produto nulo

---

**Exemplo Resolvido 6**
- Identificação: Exercício Resolvido 6
- Enunciado: Resolva a equação $$(x - 6)^2 = 3(x + 12)$$ no conjunto $$\mathbb{R}$$.
- Desenvolvimento:
$$x^2 - 12x + 36 = 3x + 36$$
$$x^2 - 12x + 36 - 3x - 36 = 0$$
$$x^2 - 15x = 0$$
$$x(x - 15) = 0$$
$$x = 0 \quad \text{ou} \quad x - 15 = 0 \Rightarrow x = 15$$
- Resultado final: $$S = \{0, 15\}$$
- Conceito aplicado: Desenvolvimento de produto notável, redução à forma $$ax^2 + bx = 0$$, produto nulo

---

**Exemplo Resolvido 7**
- Identificação: Exercício Resolvido 7
- Enunciado: Resolva as equações a seguir:
  a) $$2x^2 = 0$$
  b) $$-10x^2 = 0$$
- Desenvolvimento:
  a) $$x^2 = \frac{0}{2} = 0 \Rightarrow x = \pm\sqrt{0} = 0$$
  b) $$x^2 = \frac{0}{-10} = 0 \Rightarrow x = \pm\sqrt{0} = 0$$
- Resultado final:
  a) $$S = \{0, 0\}$$
  b) $$S = \{0, 0\}$$
- Conceito aplicado: Resolução de equação do tipo $$ax^2 = 0$$

---

## BLOCO F — CONTEXTUALIZAÇÃO REAL E APLICAÇÕES

**Código de barras completa 50 anos e ganha cara nova**
- Conexão com o conceito matemático: Crescimento quadrático da quantidade de pixels em um QR Code.
- Dados e fatos relevantes:
  - O código de barras foi inventado em 1973 por dois cientistas americanos, que o revolucionaram a indústria e o comércio.
  - Tornou-se um padrão mundial que permite o rastreamento de todos os itens comercializados.
  - Com o advento dos QR Codes em 1994, que armazenam muito mais informações, e sua crescente disseminação, o código de barras será relançado com o nome de 2D, unindo os dois tipos de código.
  - A quantidade de quadradinhos em cada dimensão aumenta 4 unidades de uma versão para outra: a versão 1 tem $$21 \times 21$$ e a versão 2 tem $$25 \times 25$$.
  - O menor QR Code tem 144 pixels; o maior tem $$177 \times 177$$ (31 329 pixels).
  - QR Codes existem em diferentes tamanhos, medidos em pixels.

---

## BLOCO G — MATEMÁTICA EM QUESTÃO

- Título e tema: **Como se estima uma multidão?**
- Texto completo:
  Durante a pandemia de Covid-19, uma das orientações para diminuir o contágio foi evitar aglomerações. Respeitando o distanciamento social de 2 metros, também uma orientação, cada pessoa ocuparia 2 m². Um desafio é manter essa distribuição nos transportes coletivos. Antes da pandemia, o metrô da cidade de São Paulo chegou a comportar 9 pessoas por m². Mas, afinal, como se calculam essas distribuições?

  O método mais conhecido e utilizado para entregar estimativas confiáveis é o chamado método de Jacobs, em alusão ao seu criador, Herbert Jacobs. Ele separou as multidões em três categorias de aglomeração:
  - **leve**: cada pessoa ocupa em média 1 m²;
  - **densa**: cada pessoa ocupa 0,4 m²;
  - **mais densa**: cada pessoa ocupa 0,2 m².

  Com isso, basta captar imagens aéreas de uma região a ser estudada e dividi-la em setores, classificando cada um deles em categorias. Uma vez conhecidas as áreas de cada setor, é possível estimar a quantidade de pessoas nessas condições e, ao adicionar as estimativas encontradas em cada setor, obter uma estimativa do número total de pessoas presentes no local.

  No entanto, apesar de a maioria dos órgãos de estatística utilizar o método de Jacobs, é muito comum encontrar diferenças em estimativas de um mesmo evento, uma vez que a medida da área do local e sua classificação dentro das categorias de aglomeração podem mudar bastante.

---

## BLOCO H — REFLEXÃO

- Texto da reflexão: Podemos resolver as equações incompletas do tipo $$ax^2 + bx = 0$$ de forma similar às equações incompletas do tipo $$ax^2 + c = 0$$?
- Conceito matemático central: Comparação entre os métodos de resolução das equações incompletas do 2º grau.
- Contexto algébrico: Equações do tipo $$ax^2 + bx = 0$$ versus $$ax^2 + c = 0$$.

---

## SEÇÃO ATIVIDADES

**Q-1** · pág. 129
Enunciado: Responda em quais itens a seguir há uma equação. Naqueles em que houver, responda, também, quais são as incógnitas.
a) $$2x - 4 = 5$$
b) $$2x + 6y = 7x$$
c) $$3 + 4 = 6 + 1$$
d) $$x^2 - 7x = 0$$
e) $$5x - 8 > 0$$
f) $$x^2 - 5y + x = 0$$
Alternativas: (dissertativa)
Gabarito:
Tipo: dissertativa
Classificação: fácil

---

**Q-2** · pág. 129
Enunciado: Indique o grau de cada equação a seguir. Caso necessário, desenvolva as equações, conforme o exemplo:
$$(4x-5)^2 = 2x^2 - 12x$$
$$16x^2 - 40x + 25 = 2x^2 - 12x$$
Equação do 4º grau.

a) $$13x^2 - 12x - 11 = 10$$
b) $$x(x-4) = x^2 + 12x - 8$$
c) $$2x^3 \cdot x^2 = 5x + 2x^4 + 1$$
d) $$5(x \cdot 1)^2 = 5x^2 + 5x + 5$$
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: fácil

---

**Q-3** · pág. 129
Enunciado: Determine os coeficientes das equações do 2º grau a seguir:
a) $$x^2 + 5x - 10 = 0$$
b) $$2x^2 - 15x + 45 = 0$$
c) $$3x^2 - 3x = 0$$
d) $$4x^2 - 100 = 0$$
e) $$x^2 - x = 0$$
f) $$0{,}5x^2 - 12 = 0$$
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: fácil

---

**Q-4** · pág. 130
Enunciado: Coloque as equações a seguir em sua forma reduzida e determine os valores dos coeficientes.
a) $$7x^2 = 8x - 14$$
b) $$8x + 2x^2 = 4x - (3 - x) + 3$$
c) $$5 + 5x^2 + 6x = -7x - 12$$
d) $$\dfrac{3}{4} - 2x + x^2 = 3x^2$$
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

---

**Q-5** · pág. 130
Enunciado: Explique a razão de o coeficiente $$a$$ de uma equação do 2º grau ser o único diferente de zero.
Alternativas: (dissertativa)
Gabarito:
Tipo: dissertativa
Classificação: fácil

---

**Q-6** · pág. 132
Enunciado: Classifique cada equação a seguir em completa ou incompleta. Se incompleta, coloque-as em sua forma reduzida.
a) $$2x^2 - 4x = 0$$
b) $$13x^2 + 9x - 4 = 0$$
c) $$12x^2 + 5x = 8$$
d) $$x \cdot (x - 2) = 5$$
e) $$8x - 5x^2 + 12 = 12$$
f) $$12 - 2x^2 + 5x^2 = x$$
Alternativas: (dissertativa)
Gabarito:
Tipo: dissertativa
Classificação: médio

---

**Q-7** · pág. 133
Enunciado: Verifique e responda:
a) 2 é raiz da equação $$x^2 - 2x + 1 = 0$$?
b) 4 é raiz da equação $$m^2 - 5m + 4 = 0$$?
c) $$-5$$ é raiz da equação $$v^2 + 25 = 0$$?
d) $$-4$$ e $$4$$ são raízes da equação $$x^2 - 16 = 0$$?
e) $$\dfrac{1}{5}$$ é raiz da equação $$5x^2 = 8x - \dfrac{15}{5}$$?
Alternativas: (dissertativa)
Gabarito:
Tipo: dissertativa
Classificação: médio

---

**Q-8** · pág. 135
Enunciado: Determine o conjunto solução das equações do 2º grau.
a) $$x^2 - 16 = 0$$
b) $$4x^2 - 400 = 0$$
c) $$3x^2 - 60 = 0$$
d) $$2x^2 - 4 = 0$$
e) $$2x^2 - 50 = 0$$
f) $$\dfrac{4x^2}{5} - 60 = 0$$
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

---

**Q-9** · pág. 136
Enunciado: Escreva as equações a seguir na forma reduzida e, depois, resolva-as.
a) $$(2x + 7)^2 = 4x + 9$$
b) $$(2m - 1)(m + 2) = 3m - 7m^2$$
c) $$(x + 4)^2 = 8x + 40$$
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

---

**Q-10** · pág. 136
Enunciado: Alex comprou uma casa em um terreno de 400 m² e quer construir um minicampo de futebol para as crianças. Para tanto, ele precisa conhecer as dimensões totais do terreno, a fim de criar um projeto adequado. Alex sabe apenas que um lado do terreno é o quádruplo do outro.
a) Escreva uma equação que represente a área do terreno.
b) Determine as dimensões do terreno que Alex comprou.
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

---

**Q-11** · pág. 138
Enunciado: Responda às perguntas sobre a equação descrita pelo professor.
a) Escreva a equação do 2º grau formal. Ela é completa ou incompleta?
b) Quais são os coeficientes da equação?
c) Sabendo que uma das soluções dessa equação é zero, qual é a outra solução?
Alternativas: (dissertativa)
Gabarito:
Tipo: dissertativa
Classificação: médio

---

**Q-12** · pág. 140
Enunciado: Determine as raízes das equações incompletas do 2º grau a seguir:
a) $$x^2 + x = 0$$
b) $$5x^2 - 125x = 0$$
c) $$\dfrac{x^2}{4} - \dfrac{2x}{4} = 0$$
d) $$\dfrac{4x^2}{3} + \dfrac{2x}{3} = 0$$
e) $$\sqrt{2} \cdot x^2 + \sqrt{3} \cdot x = 0$$
f) $$0{,}5x^2 - 2{,}5x = 0$$
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

---

**Q-13** · pág. 140
Enunciado: Determine o conjunto solução da equação $$\dfrac{x^2 - x}{4} = x - \dfrac{3x^2 - x}{6}$$.
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: difícil

---

**Q-14** · pág. 141
> Figura: dois retângulos, um verde e um rosa. Retângulo verde: dimensões $$(x + 4)$$ por $$(2x - 8)$$. Retângulo rosa: dimensões $$(x - 2)$$ por expressão visível. Regiões com áreas iguais indicadas.
Enunciado: Sabendo que as regiões verde e rosa têm áreas iguais, qual é o valor do perímetro de cada figura, considerando que as medidas estão em metros?
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: difícil

---

**Q-15** · pág. 142
Enunciado: Resolva as equações incompletas a seguir:
a) $$12x^2 = 0$$
b) $$\dfrac{2x^2}{3} = 0$$
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: fácil

---

**Q-16** · pág. 142
Enunciado: Assinale V (verdadeiro) ou F (falso), justificando as falsas.
a) ( ) Uma equação do 2º grau do tipo $$ax^2 + c = 0$$ tem duas raízes reais opostas.
b) ( ) Uma equação do 2º grau do tipo $$ax^2 + c = 0$$ tem uma raiz real nula e outra que é um número real qualquer.
c) ( ) Uma equação do 2º grau do tipo $$ax^2 + bx = 0$$ tem duas raízes reais opostas.
d) ( ) Uma equação do 2º grau do tipo $$ax^2 + bx = 0$$ tem uma raiz real nula e outra que é um número real não nulo qualquer.
e) ( ) Uma equação do 2º grau do tipo $$ax^2 = 0$$ tem raízes reais nulas.
Alternativas: (V-F)
Gabarito:
Tipo: V-F
Classificação: médio

---

**Q-17** · pág. 143
Enunciado: Observe a resolução de duas equações do 2º grau feitas pelos alunos Ana e Bruno. (tabela com os passos de resolução de cada aluno). Qual dos alunos errou na resolução das equações? Justifique sua resposta.

> Figura: Tabela com duas colunas (Ana e Bruno). Ana: $$x^2 - 400 = 0 \Rightarrow x^2 = 400 \Rightarrow x = 20$$. Bruno: $$-2x^2 + 10x = 0 \Rightarrow 2x(-x+5)=0 \Rightarrow x=0 \text{ ou } -x+5=0 \Rightarrow x=5$$.

Alternativas: (dissertativa)
Gabarito:
Tipo: dissertativa
Classificação: médio

---

**Q-18** · pág. 146
Enunciado: Resolva as equações incompletas a seguir no conjunto dos números reais.
a) $$3x^2 - 48 = 0$$
b) $$12x^2 - 2400 = 0$$
c) $$2x^2 - 2450 = 0$$
d) $$16x^2 = 25$$
e) $$-2x^2 + 10x = 0$$
f) $$15x^2 - 45x = 0$$
g) $$3x^2 + 81x = 0$$
h) $$\sqrt{5}x^2 - \sqrt{7}x = 0$$
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

---

**Q-19** · pág. 147
Enunciado: Vinicius é um aluno dedicado e está estudando para a avaliação de Matemática. Para se preparar, ele escreveu algumas frases que remetem às equações do 2º grau. Observe as frases, escreva a equação que representa cada uma delas e determine seu conjunto solução.
a) A soma entre o quadrado de um número e 36 é igual a 100.
b) O quadrado de um número é igual ao triplo desse número.
c) O quadrado de um número é igual a 121. Que é esse número?
d) A diferença entre o quadrado de um número e 45 é igual a 396.
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

---

**Q-20** · pág. 147
Enunciado: O gerador elétrico é um aparelho capaz de transformar qualquer tipo de energia em energia elétrica. A potência elétrica fornecida por um gerador depende da intensidade da corrente elétrica e da energia dissipada no processo de transformação. Certo gerador tem sua potência elétrica dada pela seguinte expressão: Potência = $$300x - 25x^2$$. Sendo $$x$$ a intensidade da corrente elétrica que o atravessa, os valores de $$x$$ para que a potência desse gerador seja nula são:
a) ( ) 0 e −12
b) ( ) 0 e 12
c) ( ) 0 e 25
d) ( ) 0 e −25
Alternativas:
  a) 0 e −12
  b) 0 e 12
  c) 0 e 25
  d) 0 e −25
Gabarito:
Tipo: múltipla escolha
Classificação: médio

---

**Q-21** · pág. 146
Enunciado: Resolva as equações incompletas a seguir no conjunto dos números reais.
a) $$(1 - x)(5 \cdot 2x) = 5$$
b) $$(x - 8)^2 = 64 - x(x + 4)$$
c) $$(x + 5)^2 = 10x + 50$$
d) $$\dfrac{6x^2 - 2x^2 + 14}{8} = \dfrac{x^2}{12}$$
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: difícil

---

**Q-22** · pág. 148
Enunciado: André comprou uma toalha de banho, no formato retangular, para presentear sua mãe, Madelena. Ele não sabe as dimensões da toalha, sabe apenas que a largura é a terça parte do comprimento.
a) Escreva uma equação que represente a área da toalha de banho que André comprou.
b) Sabendo que a área da toalha é de 10 800 cm², quais são suas dimensões?
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

---

**Q-23** · pág. 148
Enunciado: A área do retângulo a seguir é igual a 128 cm². Quais são as dimensões desse retângulo?
> Figura: Retângulo com dimensões $$(x + 5)$$ e $$(x - 4)$$.
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

---

**Q-24** · pág. 148
Enunciado: Neuza comprou um cubo mágico. As instruções indicam que a área da superfície dele é de 240 cm². Quanto mede cada aresta desse cubo mágico?
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

---

**Q-25** · pág. 149
Enunciado: Na figura a seguir, o quadrado maior tem área de 720 cm². Determine a área de cada uma das quatro regiões que estão dentro do quadrado maior.
> Figura: Quadrado maior com lado não nomeado; dentro dele, quatro regiões com áreas $$25x^2$$ e $$y^2$$ indicadas.
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: difícil

---

**QC-1** · IF-CE · pág. 145
Enunciado: Se 3 e $$\frac{1}{3}$$ são raízes da equação $$ax^2 - 6x + p = 0$$, então o valor de $$a + p$$ é:
Alternativas:
  a) ( ) −5
  b) ( ) 0
  c) ( ) $$-\dfrac{8}{5}$$
  d) ( ) $$\dfrac{1}{3}$$
  e) ( ) 4
Gabarito:
Tipo: múltipla escolha
Classificação: difícil

---

**QC-2** · IF-SC · pág. 145
Enunciado: Pedro é pecuarista e, com o aumento da criação, ele terá que fazer um novo cercado para acomodar seus animais. Sabendo-se que ele terá que utilizar 5 voltas de arame farpado e que o cercado tem formato retangular cujas dimensões são as raízes da equação $$x^2 - 45x + 500 = 0$$, qual a quantidade mínima de arame que Pedro terá que comprar para fazer esse cercado?
Alternativas:
  a) ( ) 545 m
  b) ( ) 1 225 m
  c) ( ) 225 m
  d) ( ) 500 m
  e) ( ) 450 m
Gabarito:
Tipo: múltipla escolha
Classificação: difícil

---

**QC-3** · Saresp · pág. 149
Enunciado: A equação $$x^2 + 3x = 0$$:
Alternativas:
  a) ( ) não tem raízes reais.
  b) ( ) tem uma raiz real e outra negativa.
  c) ( ) tem uma raiz real e outra positiva.
  d) ( ) tem duas raízes reais simétricas.
Gabarito:
Tipo: múltipla escolha
Classificação: médio

---

**QC-4** · Fatul 2017 · pág. 144
Enunciado: Determine o valor de $$k$$ para que a equação $$x^2 + kx + 6 = 0$$ tenha como raízes os valores 2 e 3.
Alternativas:
  a) ( ) −5
  b) ( ) 5
  c) ( ) 3
  d) ( ) −5
  e) ( ) −6
Gabarito:
Tipo: múltipla escolha
Classificação: médio

---

**QC-5** · ENEM · pág. 150
Enunciado: A temperatura $$T$$ de um forno (em graus centígrados) é reduzida por um sistema a partir do instante de seu desligamento ($$t = 0$$) e varia de acordo com a expressão $$T(t) = -\dfrac{t^2}{4} + 400$$, com $$t$$ em minutos. Por motivos de segurança, a trava do forno só é liberada para abertura quando o forno atinge a temperatura de 39 °C. Qual o tempo mínimo de espera, em minutos, após se desligar o forno, para que a porta possa ser aberta?
Alternativas:
  a) ( ) 19,0
  b) ( ) 19,8
  c) ( ) 20,0
  d) ( ) 38,0
  e) ( ) 39,0
Gabarito:
Tipo: múltipla escolha
Classificação: difícil

---

## PADRÃO DAS QUESTÕES

- Estilo predominante: misto
- Foco: cálculo algébrico / aplicação
- Nível de dificuldade médio: médio
- Tópicos mais cobrados: identificação de grau e coeficientes; resolução de equações incompletas do tipo $$ax^2 + c = 0$$, $$ax^2 + bx = 0$$ e $$ax^2 = 0$$; verificação de raízes; redução à forma reduzida; aplicações contextualizadas
- Total: 25 questões do capítulo + 5 questões de concurso