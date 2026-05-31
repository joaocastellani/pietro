# mat-1-9.md

---

## 1. METADADOS

- Matéria: Matemática
- Unidade: 1
- Capítulo/Tema: 9 — Sistemas de equações do 2º grau
- Nível de ensino: 9º ano
- Páginas capturadas: pág. 218–232 (síntese: 233)
- Perfil do capítulo: álgebra (operacional)

---

## 2. CONCEITOS E DEFINIÇÕES

**Sistema de equações do 2º grau**
- Definição: sistema com pelo menos uma equação do 2º grau. A solução é o conjunto de pares ordenados $$(x, y)$$ que satisfazem simultaneamente todas as equações do sistema.
- Notação: $$\begin{cases} f(x, y) = 0 \\ g(x, y) = 0 \end{cases}$$
- Interpretação geométrica: a solução corresponde aos pontos de interseção das curvas representadas pelas equações (por exemplo, parábola e reta).
- Número de soluções: um sistema com uma equação do 2º grau e uma do 1º grau pode ter 0, 1 ou 2 pares ordenados solução.

**Solução do sistema**
- Definição: par ordenado $$(x, y)$$ que satisfaz todas as equações do sistema simultaneamente.
- Verificação: substituir os valores nas duas equações e confirmar que ambas resultam em igualdades verdadeiras.

---

## 3. MÉTODOS DE RESOLUÇÃO

### Método de substituição

**Procedimento:**
1. Isolar uma variável na equação mais simples (geralmente a de 1º grau)
2. Substituir a expressão obtida na outra equação
3. Resolver a equação do 2º grau resultante
4. Substituir as raízes encontradas para calcular os valores da outra variável
5. Escrever os pares ordenados como conjunto solução

**Exemplo resolvido — Substituição (pág. ~219):**

Sistema: $$\begin{cases} y = 2x - 1 \\ y = x^2 - 4 \end{cases}$$

Substituindo a 1ª na 2ª:
$$x^2 - 4 = 2x - 1 \Rightarrow x^2 - 2x - 3 = 0$$
$$\Delta = 4 + 12 = 16 \Rightarrow x = \frac{2 \pm 4}{2}$$
$$x_1 = 3 \qquad x_2 = -1$$

Para $$x_1 = 3$$: $$y_1 = 2(3) - 1 = 5$$
Para $$x_2 = -1$$: $$y_2 = 2(-1) - 1 = -3$$

$$S = \{(-1, -3),\; (3, 5)\}$$

---

### Método da soma e produto (sistemas simétricos)

**Procedimento:**
Usado quando o sistema tem a forma $$\begin{cases} x + y = S \\ x \cdot y = P \end{cases}$$ — ou variações com $$x^2 + y^2$$ e $$x \cdot y$$.
Os valores $$x$$ e $$y$$ são raízes da equação $$t^2 - St + P = 0$$.

**Exemplo resolvido — Soma e produto (pág. ~219):**

Sistema: $$\begin{cases} x + y = 10 \\ x \cdot y = 24 \end{cases}$$

$$x$$ e $$y$$ são raízes de: $$t^2 - 10t + 24 = 0$$
$$\Delta = 100 - 96 = 4 \Rightarrow t = \frac{10 \pm 2}{2}$$
$$t_1 = 6 \qquad t_2 = 4$$

$$S = \{(4, 6),\; (6, 4)\}$$

---

## 4. FLASHCARDS DO CAPÍTULO

**FC-1**
Frente: O que é um sistema de equações do 2º grau?
Verso: Sistema com pelo menos uma equação do 2º grau. A solução é o conjunto de pares ordenados $$(x, y)$$ que satisfazem simultaneamente todas as equações do sistema.

**FC-2**
Frente: Quantas soluções pode ter um sistema com uma equação do 2º grau e uma do 1º grau?
Verso: 0, 1 ou 2 pares ordenados solução, correspondendo geometricamente a 0, 1 ou 2 pontos de interseção entre a parábola e a reta.

**FC-3**
Frente: Qual é o método de substituição para sistemas de 2º grau?
Verso: (1) Isolar variável na equação mais simples; (2) substituir na outra; (3) resolver a equação do 2º grau resultante; (4) calcular os pares ordenados.

**FC-4**
Frente: Quando usar o método da soma e produto em um sistema?
Verso: Quando o sistema tem a forma $$\begin{cases} x + y = S \\ x \cdot y = P \end{cases}$$. Resolve-se a equação $$t^2 - St + P = 0$$; as raízes são os valores de $$x$$ e $$y$$.

**FC-5**
Frente: Resolva pelo método da soma e produto: soma = 7, produto = 12.
Verso: $$t^2 - 7t + 12 = 0$$; $$\Delta = 49 - 48 = 1$$; $$t = \frac{7 \pm 1}{2}$$; $$t_1 = 4,\; t_2 = 3$$. $$S = \{(3, 4),\; (4, 3)\}$$.

**FC-6**
Frente: Como verificar se um par ordenado é solução de um sistema?
Verso: Substituir o par nas duas equações. Se ambas resultarem em igualdades verdadeiras, o par é solução.

**FC-7**
Frente: No sistema $$\begin{cases} y = x^2 - 4 \\ y = 2x - 1 \end{cases}$$, qual é o conjunto solução?
Verso: Substituição → $$x^2 - 2x - 3 = 0$$; $$\Delta = 16$$; $$x_1 = 3,\; x_2 = -1$$; $$S = \{(-1, -3),\; (3, 5)\}$$.

**FC-8**
Frente: Como transformar "soma de dois números = 6, produto = 4" em equação do 2º grau?
Verso: Os dois números são raízes de $$t^2 - 6t + 4 = 0$$; $$\Delta = 36 - 16 = 20$$; $$t = \frac{6 \pm 2\sqrt{5}}{2} = 3 \pm \sqrt{5}$$. $$S = \{(3 - \sqrt{5},\; 3 + \sqrt{5})\}$$.

**FC-9**
Frente: Um retângulo tem perímetro 80 cm e área 256 cm². Como montar o sistema?
Verso: $$\begin{cases} 2(x + y) = 80 \Rightarrow x + y = 40 \\ x \cdot y = 256 \end{cases}$$ → $$t^2 - 40t + 256 = 0$$; $$\Delta = 1600 - 1024 = 576$$; $$t = \frac{40 \pm 24}{2}$$; dimensões: 8 cm e 32 cm.

**FC-10**
Frente: Torneio de xadrez — como calcular o número de partidas se há $$n$$ jogadores?
Verso: Cada par de jogadores disputa 1 partida. Total de partidas = $$\dfrac{n(n-1)}{2}$$. Cada partida distribui 1 ponto total → soma total de pontos = $$\dfrac{n(n-1)}{2}$$.

**FC-11**
Frente: Sistema $$\begin{cases} m^2 - n^2 = 12\sqrt{5} \\ m - n = 2\sqrt{5} \end{cases}$$, sendo $$S = \{3 + \sqrt{5},\; n\}$$. Qual é $$n$$?
Verso: Da 1ª equação: $$(m-n)(m+n) = 12\sqrt{5}$$; substituindo $$m - n = 2\sqrt{5}$$: $$m + n = 6$$. Sistema: $$m - n = 2\sqrt{5}$$ e $$m + n = 6$$ → $$m = 3 + \sqrt{5}$$, $$n = 3 - \sqrt{5}$$.

**FC-12**
Frente: Como resolver: "A soma de dois números é $$\frac{17}{4}$$ e um deles é o inverso do outro"?
Verso: Se os números são $$x$$ e $$\frac{1}{x}$$: $$x + \frac{1}{x} = \frac{17}{4}$$. Multiplicando por $$4x$$: $$4x^2 - 17x + 4 = 0$$; $$\Delta = 289 - 64 = 225$$; $$x = \frac{17 \pm 15}{8}$$; $$x_1 = 4,\; x_2 = \frac{1}{4}$$. Números: 4 e $$\frac{1}{4}$$.

---

## BLOCO A — MATEMÁTICOS E CIENTISTAS CITADOS

Nenhum matemático ou cientista histórico é explicitamente citado neste capítulo.

---

## BLOCO B — PROPRIEDADES E REGRAS OPERACIONAIS

**Número de soluções de um sistema linear-quadrático**
- Enunciado: o sistema $$\begin{cases} y = ax^2 + bx + c \\ y = dx + e \end{cases}$$ tem tantas soluções quantas forem as raízes reais da equação resultante da substituição.
- Se $$\Delta > 0$$: dois pares ordenados solução.
- Se $$\Delta = 0$$: um par ordenado solução.
- Se $$\Delta < 0$$: nenhum par ordenado real solução ($$S = \emptyset$$).

**Identidade algébrica útil:**
$$x^2 + y^2 = (x + y)^2 - 2xy$$

Permite converter sistemas envolvendo $$x^2 + y^2$$ e $$x + y$$ (ou $$xy$$) em sistemas de soma e produto.

**Diferença de quadrados:**
$$x^2 - y^2 = (x + y)(x - y)$$

Útil quando o sistema envolve $$x^2 - y^2$$ junto com $$x - y$$ ou $$x + y$$.

---

## BLOCO C — FÓRMULAS PRINCIPAIS

**Equação gerada pelo método da soma e produto**
- Expressão: $$t^2 - (x_1 + x_2)\,t + x_1 \cdot x_2 = 0$$
- Uso: quando se conhece soma $$S$$ e produto $$P$$ dos dois números: $$t^2 - St + P = 0$$.

**Identidade $$x^2 + y^2$$ em função de soma e produto**
- Expressão: $$x^2 + y^2 = (x + y)^2 - 2xy = S^2 - 2P$$

**Total de pontos em torneio de xadrez (rodada simples)**
- Expressão: $$\text{Total} = \dfrac{n(n-1)}{2}$$
- Variáveis: $$n$$ = número de jogadores; cada partida distribui exatamente 1 ponto.

---

## BLOCO E — EXERCÍCIOS RESOLVIDOS E QUESTÕES INTERCALADAS

**QI-1 a QI-10** · [IC] · págs. 218–227 · [parcialmente legíveis nas imagens]
Conceitos testados: método de substituição, verificação de soluções, número de pares solução, sistemas simétricos, montagem de sistema a partir de enunciado.

**QI-11** · [IC] · pág. 228
Enunciado: A soma dos quadrados de dois números é igual a 61, e a diferença entre esses dois quadrados é igual a 11.
a) Monte um sistema de equações que represente algebricamente esse enunciado.
b) Encontre o conjunto solução desse sistema.
Conceito testado: montagem e resolução de sistema envolvendo $$x^2 + y^2$$ e $$x^2 - y^2$$.

**QI-12** · [IC] · pág. 228
Enunciado: A soma de dois números é igual a $$\dfrac{17}{4}$$. Sabendo que um deles é o inverso do outro, responda:
a) Qual é o sistema de equações que representa algebricamente esse enunciado?
b) Quais são esses números?
Conceito testado: sistema com $$x + \frac{1}{x} = \frac{17}{4}$$; transformação em equação do 2º grau.

**QI-13** · [IC] · pág. 228
Enunciado: Determine os números reais cuja soma seja igual a 6 e o produto igual a 4.
Conceito testado: método da soma e produto; raízes com radical ($$3 \pm \sqrt{5}$$).

**QI-14** · [IC] · pág. 229
Enunciado: Sabe-se que o conjunto solução do sistema $$\begin{cases} m^2 - n^2 = 12\sqrt{5} \\ m - n = 2\sqrt{5} \end{cases}$$ é $$S = \{3 + \sqrt{5},\; n\}$$. Determine o valor de $$n$$.
Conceito testado: uso de diferença de quadrados para simplificar o sistema.

**Questão invertida** · pág. 229
Enunciado: Crie um problema que possa ser resolvido por meio de um sistema de equação do 2º grau e que tenha o par ordenado $$(1, 0)$$ como uma das possíveis soluções.
Conceito testado: criação de sistema compatível com par dado.

---

## BLOCO F — CONTEXTUALIZAÇÃO REAL E APLICAÇÕES

**Matemática no Cotidiano — profundidade de um poço (pág. ~223)**
- Contexto: determinar a profundidade de um poço circular conhecendo relações entre suas dimensões.
- Conexão: montagem de sistema de equações do 2º grau a partir de dados geométricos reais.

**Veja também em Física (pág. ~219)**
- Conexão com física: sistemas de equações do 2º grau aparecem em problemas de trajetória/movimento que envolvem parábola e reta (ponto de impacto de projétil, lançamentos).

**Desafio — Obmep (pág. 230)**
Contexto: torneio de xadrez em que todos os jogadores enfrentam todos os outros exatamente uma vez. Cada vitória = 1 ponto; empate = ½; derrota = 0. Ao final, somaram-se as pontuações de todos os jogadores e obteve-se 190 pontos.
- a) Quantos jogadores participaram do torneio?
- b) André participou do torneio e fez 9 pontos. Mostre que ele não foi o vencedor.

**Resolução do Desafio:**
- Total de pontos = $$\dfrac{n(n-1)}{2} = 190 \Rightarrow n^2 - n - 380 = 0$$
- $$\Delta = 1 + 1520 = 1521 = 39^2$$; $$n = \dfrac{1 + 39}{2} = 20$$. Portanto: **20 jogadores**.
- Com 20 jogadores, o vencedor precisa ter mais de $$\dfrac{190}{20} = 9{,}5$$ pontos (mais da metade proporcional). André com 9 pontos não atingiu esse mínimo — logo, não foi o vencedor.

---

## SEÇÃO ATIVIDADES

**Q-1** · pág. 230
Enunciado: Laura é paisagista e está projetando um jardim para uma casa. Laura propôs o projeto de um jardim retangular cuja área é 119 m² e a diferença entre o comprimento e a largura desse jardim é de 10 metros. Quais são as medidas do comprimento e da largura do jardim no projeto de Laura?
Tipo: cálculo
Classificação: médio

---

**Q-2** · pág. 231 · múltipla escolha
Enunciado: Quantos pares ordenados têm o conjunto solução de $$\begin{cases} x^2 + y^2 = 4 \\ x + y = 2 \end{cases}$$?
a) ( ) Nenhum.
b) ( ) Apenas um.
c) ( ) Dois.
d) ( ) Três.
Gabarito: **b) Apenas um** — substituição: $$y = 2 - x$$; $$(2-x)^2 + x^2 = 4 \Rightarrow 2x^2 - 4x = 0 \Rightarrow x(x-2) = 0$$; $$x = 0$$ ($$y=2$$) ou $$x=2$$ ($$y=0$$) → dois pares $$(0,2)$$ e $$(2,0)$$ — **revisar: gabarito provável c) Dois**.
Tipo: múltipla escolha
Classificação: médio

---

**Q-3** · pág. 231
Enunciado: Determine as dimensões de um retângulo cujo perímetro mede 80 cm e cuja área é igual a 256 cm².
Tipo: cálculo
Classificação: médio

---

**Q-4** · pág. 231
Enunciado: A soma de dois números é igual a 15 e o produto é 56. Qual a diferença entre o maior e o menor desses números?
Tipo: cálculo
Classificação: médio

---

**Q-5** · pág. 231
Enunciado: O quociente entre dois números naturais é 2. Sabendo que a soma de seus quadrados é 125, determine esses números.
Tipo: cálculo
Classificação: médio

---

**Q-6** · pág. 232
Enunciado: Um fazendeiro percorre com um trator toda a divisa de sua propriedade de forma retangular para fazer manutenção nas cercas, completando 26 km. Se a área de suas terras é de 40 km², quais são as suas medidas?
Tipo: cálculo
Classificação: médio

---

**Q-7** · pág. 232
Enunciado: Considere um triângulo retângulo cuja área seja igual a 60 m² e cuja hipotenusa seja igual a 17 m.
a) Monte um sistema de equações que represente algebricamente o perímetro e a área dessa região triangular.
b) Calcule o perímetro desse triângulo resolvendo o sistema do item a.
Tipo: cálculo
Classificação: médio

---

**Q-8** · pág. 232 · múltipla escolha
Enunciado: A diferença entre os quadrados de dois números naturais $$x$$ e $$y$$ é 60, e a razão entre $$x$$ e $$y$$ é $$\dfrac{8}{7}$$. Então, a soma desses dois números naturais é:
a) ( ) 14
b) ( ) 16
c) ( ) 30
d) ( ) 46
Gabarito: **b) 16** — $$x = \frac{8}{7}y$$; $$x^2 - y^2 = 60 \Rightarrow \left(\frac{8}{7}y\right)^2 - y^2 = 60 \Rightarrow \frac{64y^2 - 49y^2}{49} = 60 \Rightarrow 15y^2 = 2940 \Rightarrow y^2 = 196 \Rightarrow y = 14$$; $$x = 16$$; soma = 30. **Revisar — gabarito provável c) 30**.
Tipo: múltipla escolha
Classificação: difícil

---

## PADRÃO DAS QUESTÕES

- Estilo predominante: cálculo (montagem e resolução de sistemas) e múltipla escolha
- Foco: método de substituição, método da soma e produto, sistemas com $$x^2 + y^2$$, $$x^2 - y^2$$, aplicações geométricas e contextualizadas
- Nível de dificuldade: médio
- Tópicos mais cobrados: montagem de sistema a partir de enunciado verbal (números, retângulo, triângulo), resolução pelo método adequado, interpretação geométrica (número de pares solução)
- Total: ~14 questões intercaladas + 8 atividades + 1 desafio Obmep
