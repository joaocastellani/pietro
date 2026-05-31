<!-- mat-1-9-prep.md -->

---

## DIAGRAMAS DISPONÍVEIS — mat-1-9

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Métodos de Resolução | `DIAGRAMA: metodos_resolucao` | Ao apresentar substituição vs. soma e produto (Seção 2) |
| Número de Soluções | `DIAGRAMA: numero_solucoes` | Ao explicar os 3 casos de Δ (Seção 2) |

### Tabelas markdown (Seção 6):
- Tabela comparativa dos dois métodos de resolução
- Tabela dos 3 casos de número de soluções

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 9
- Tema: Sistemas de equações do 2º grau
- Perfil: álgebra
- Fórmulas principais:
    Método substituição: isolate → substituir → resolver eq. do 2º grau
    Método soma/produto: t² − S·t + P = 0
    Identidade: x² + y² = (x+y)² − 2xy
    Diferença: x² − y² = (x+y)(x−y)
    Torneio (n jogadores): Total = n(n−1)/2
- Matemáticos citados: nenhum
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### **Bloco 1 — Sistema de equações do 2º grau**

Um **sistema de equações do 2º grau** é um conjunto de equações simultâneas em que pelo menos uma é do 2º grau. A **solução** é o conjunto de pares ordenados $$(x, y)$$ que satisfazem todas as equações do sistema ao mesmo tempo.

**Interpretação geométrica:** cada equação representa uma curva no plano cartesiano. A solução corresponde aos pontos de interseção entre as curvas — tipicamente entre uma parábola (equação do 2º grau em $$x$$) e uma reta (equação do 1º grau).

O número de soluções depende do discriminante $$\Delta$$ da equação do 2º grau obtida após a substituição:

| $$\Delta$$ | Soluções | Geometria |
|-----------|----------|-----------|
| $$\Delta > 0$$ | Dois pares ordenados | Parábola corta a reta em 2 pontos |
| $$\Delta = 0$$ | Um par ordenado | Parábola tangencia a reta em 1 ponto |
| $$\Delta < 0$$ | Nenhum par ($$S = \emptyset$$) | Parábola e reta não se intersectam |

---

### **Bloco 2 — Método de substituição**

Usado em qualquer sistema. Procedimento:

1. Isolar uma variável na equação mais simples (geralmente a de 1º grau)
2. Substituir a expressão obtida na outra equação
3. Resolver a equação do 2º grau resultante (Bhaskara ou fatoração)
4. Para cada raiz $$x_i$$, calcular o $$y_i$$ correspondente e escrever o par $$(x_i, y_i)$$

**Exemplo concreto do material:**

$$\begin{cases} y = 2x - 1 \\ y = x^2 - 4 \end{cases}$$

Substituindo $$y = 2x-1$$ na 2ª:
$$x^2 - 4 = 2x - 1 \;\Rightarrow\; x^2 - 2x - 3 = 0$$
$$\Delta = 4 + 12 = 16 \;\Rightarrow\; x = \tfrac{2 \pm 4}{2}$$
$$x_1 = 3 \;\Rightarrow\; y_1 = 5 \qquad x_2 = -1 \;\Rightarrow\; y_2 = -3$$
$$S = \{(-1,\,-3),\;(3,\,5)\}$$

---

### **Bloco 3 — Método da soma e produto**

Usado quando o sistema é **simétrico**, com a forma $$\begin{cases} x + y = S \\ x \cdot y = P \end{cases}$$ (ou variações envolvendo $$x^2 + y^2$$, $$x^2 - y^2$$, etc., que se reduzem a soma e produto).

$$x$$ e $$y$$ são as raízes da equação:

$$t^2 - S\,t + P = 0$$

As raízes $$t_1$$ e $$t_2$$ são os dois valores procurados. O conjunto solução é $$\{(t_1, t_2),\;(t_2, t_1)\}$$ (pares distintos, quando $$t_1 \neq t_2$$).

**Exemplo concreto do material:**

$$\begin{cases} x + y = 10 \\ x \cdot y = 24 \end{cases}$$

$$t^2 - 10t + 24 = 0 \;\Rightarrow\; \Delta = 100 - 96 = 4$$
$$t = \tfrac{10 \pm 2}{2} \;\Rightarrow\; t_1 = 6,\quad t_2 = 4$$
$$S = \{(4,\,6),\;(6,\,4)\}$$

---

### **Bloco 4 — Identidades úteis para sistemas simétricos**

Quando o sistema envolve $$x^2 + y^2$$ ou $$x^2 - y^2$$, as identidades a seguir permitem converter para soma e produto:

$$x^2 + y^2 = (x+y)^2 - 2xy = S^2 - 2P$$

$$x^2 - y^2 = (x+y)(x-y)$$

**Exemplo (QI-11):** Sistema $$\begin{cases} x^2 + y^2 = 61 \\ x^2 - y^2 = 11 \end{cases}$$

Somando: $$2x^2 = 72 \Rightarrow x = \pm 6$$. Subtraindo: $$2y^2 = 50 \Rightarrow y = \pm 5$$.
$$S = \{(6,5),\;(6,-5),\;(-6,5),\;(-6,-5)\}$$

---

### **Bloco 5 — Aplicações contextualizadas**

O capítulo aplica sistemas em problemas de:
- **Dimensões de retângulos:** perímetro = $$2(x+y)$$ e área = $$x\cdot y$$ formam sistema de soma e produto.
- **Triângulos retângulos:** área = $$\frac{xy}{2}$$ e hipotenusa = $$\sqrt{x^2+y^2}$$; usando identidade converte para soma e produto.
- **Pares de números:** enunciados do tipo "a soma é X e o produto é Y" (direto); "a soma dos quadrados é X e a diferença é Y" (usa identidades).
- **Torneios (Obmep — Desafio):** número de jogadores via $$\dfrac{n(n-1)}{2} = \text{total de pontos}$$.

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Equação do método soma e produto

**Expressão:** $$t^2 - S\,t + P = 0$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$t$$ | variável auxiliar (raízes = valores de $$x$$ e $$y$$) | real |
| $$S$$ | soma $$x + y$$ | real |
| $$P$$ | produto $$x \cdot y$$ | real |

**Válida quando:** o sistema tem a forma $$x+y = S$$ e $$x\cdot y = P$$ (ou redutível a ela)
💡 **Pegadinha:** a equação é $$t^2 - St + P$$, não $$t^2 + St + P$$. O coeficiente de $$t$$ é $$-S$$ (negativo da soma).

---

### Identidade soma dos quadrados

**Expressão:** $$x^2 + y^2 = (x+y)^2 - 2xy$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$x^2 + y^2$$ | soma dos quadrados | real |
| $$(x+y)^2$$ | quadrado da soma | real |
| $$2xy$$ | dobro do produto | real |

**Uso:** converte sistemas com $$x^2+y^2$$ em sistemas de soma e produto.
💡 **Pegadinha:** $$(x+y)^2 = x^2 + 2xy + y^2$$, não $$x^2+y^2$$. O $$2xy$$ precisa ser subtraído.

---

### Identidade diferença dos quadrados

**Expressão:** $$x^2 - y^2 = (x+y)(x-y)$$

**Uso:** quando o sistema fornece $$x^2-y^2$$ e $$x-y$$ (ou $$x+y$$), permite isolar o outro fator diretamente.

---

### Total de pontos em torneio (rodada simples)

**Expressão:** $$\text{Total} = \dfrac{n(n-1)}{2}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$n$$ | número de participantes | inteiro positivo |
| Total | soma de todos os pontos distribuídos | real |

**Por que funciona:** cada par de jogadores disputa 1 partida, que distribui exatamente 1 ponto total (1-0, 0-1 ou ½-½). Há $$\binom{n}{2} = \tfrac{n(n-1)}{2}$$ partidas.

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Comparativo dos dois métodos de resolução

| Critério | Método de Substituição | Método Soma e Produto |
|---|---|---|
| **Quando usar** | Qualquer sistema (universal) | Sistema com $$x+y=S$$ e $$xy=P$$ (simétrico) |
| **Passo central** | Isolar variável → substituir | Montar $$t^2 - St + P = 0$$ |
| **Tipo de eq. resultante** | Equação do 2º grau em $$x$$ | Equação do 2º grau em $$t$$ |
| **Resultado** | Pares $$(x_i, y_i)$$ calculados individualmente | Raízes $$t_1, t_2$$ são diretamente os dois valores |
| **Exemplo** | $$\{y=2x-1;\; y=x^2-4\}$$ | $$\{x+y=10;\; xy=24\}$$ |

### Casos de número de soluções

| $$\Delta$$ (após substituição) | Nº de pares solução | Conjunto solução |
|---|---|---|
| $$\Delta > 0$$ | **2** | $$S = \{(x_1,y_1),\;(x_2,y_2)\}$$ |
| $$\Delta = 0$$ | **1** | $$S = \{(x_0,y_0)\}$$ (raiz dupla) |
| $$\Delta < 0$$ | **0** | $$S = \emptyset$$ |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Verificar o par nas DUAS equações**
Após encontrar os pares solução, substituir em ambas as equações. Erro comum: verificar só na equação mais simples.

💡 **Dica 2 — Sinal negativo em t² − St + P = 0**
A equação é $$t^2 \mathbf{-} St + P = 0$$. Para $$S = 10$$: $$t^2 - 10t + P = 0$$. Escrever com $$+S$$ é o erro mais comum; lembrar da construção: $$t^2 - (\text{soma})\,t + (\text{produto})$$.

💡 **Dica 3 — Identidade x² + y² antes de tentar resolver**
Quando o sistema envolve $$x^2+y^2$$, não substituir diretamente — é mais eficiente aplicar $$x^2+y^2 = (x+y)^2 - 2xy$$ para converter em soma e produto, geralmente mais rápido.

💡 **Dica 4 — Dois pares ou um par?**
Para $$\{x+y=S;\; xy=P\}$$ com $$\Delta > 0$$: há **dois** pares $$(t_1,t_2)$$ e $$(t_2,t_1)$$ — ambos são soluções válidas, pois a ordem em que aparecem $$x$$ e $$y$$ importa. Não esquecer o par invertido.

💡 **Dica 5 — Descartar raiz negativa em contextos reais**
Quando $$x$$ e $$y$$ representam dimensões, quantidades ou medidas, raízes negativas devem ser descartadas mesmo sendo matematicamente válidas.

💡 **Dica 6 — Torneio: ponto médio como referência**
No Obmep/xadrez, o ponto médio por jogador é $$\frac{n-1}{2}$$. Para verificar se alguém **pode** ser o vencedor: o score deve superar a média do grupo (190/20 = 9,5 para 20 jogadores). Score ≤ 9,5 → não pode ser o único vencedor.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

#### Bloco A — Lacunas de dados

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| BLOCO E | QI-1 a QI-10 | Imagens 01–03 parcialmente legíveis | Capturar páginas 218–227 individualmente |
| SEÇÃO AT | Síntese do livro | Imagem da síntese rejeitada pela API (tamanho) | Visualizar mat-1-9-sintese.png localmente |

#### Bloco B — Inconsistências e alertas

```
⚠️ ALERTA — Q-2 (gabarito no raw incorreto)
- Dado no raw: "b) Apenas um" com nota "revisar: provavelmente c)"
- Análise correta: y=2-x → 2x²-4x=0 → x=0 (y=2) e x=2 (y=0)
- Dado correto: c) Dois — S={(0,2),(2,0)}
- Impacto na aula: usar gabarito c) Dois.
```

```
⚠️ ALERTA — Q-8 (gabarito no raw para conferir)
- Nota no raw: "gabarito provável c) 30"
- Análise: x=8y/7; x²-y²=60 → 15y²/49=60 → y=14; x=16; soma=30
- Dado correto: c) 30 ✓ — gabarito confirmado.
```

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO

#### Bloco 1 — Conceitos e Definições

- **Sistema de equações do 2º grau**
  - Definição: `______` (conjunto de equações simultâneas com pelo menos uma do 2º grau; solução = par ordenado $$(x,y)$$ que satisfaz ambas)
  - Solução: `______` (par ordenado $$(x,y)$$)

- **Método de substituição**
  - Passo 1: `______` (isolar variável na equação mais simples)
  - Passo 2: `______` (substituir na outra equação)
  - Resultado: `______` (equação do 2º grau em uma variável)

- **Método soma e produto**
  - Equação auxiliar: `______` ($$t^2 - St + P = 0$$)
  - Raízes $$t_1, t_2$$: `______` (são os valores de $$x$$ e $$y$$)

#### Bloco 2 — Fórmulas e Propriedades

- **Equação do método soma e produto**
  - Expressão: `______` ($$t^2 - St + P = 0$$)
  - Sinal de $$S$$: `______` (negativo: $$-St$$, não $$+St$$)

- **Identidade $$x^2 + y^2$$**
  - Expressão: `______` ($$(x+y)^2 - 2xy$$)
  - Para $$x+y=7$$ e $$xy=10$$: `______` ($$49-20=29$$)

#### Bloco 3 — Lacunas para Warm-Up

1. A solução de um sistema de equações do 2º grau é um conjunto de `______`.
*(resposta: pares ordenados $$(x,y)$$)*

2. Quando $$\Delta > 0$$ no sistema, há `______` par(es) ordenado(s) solução.
*(resposta: dois)*

3. O método da soma e produto usa a equação `______`.
*(resposta: $$t^2 - St + P = 0$$)*

4. $$x^2 + y^2$$ pode ser reescrito como `______`.
*(resposta: $$(x+y)^2 - 2xy$$)*

5. No sistema $$\{x+y=10;\; xy=24\}$$, a equação auxiliar é `______`.
*(resposta: $$t^2-10t+24=0$$; raízes: $$t_1=6, t_2=4$$)*

6. Num torneio de xadrez com $$n$$ jogadores (cada par joga 1 vez), o total de pontos distribuídos é `______`.
*(resposta: $$\dfrac{n(n-1)}{2}$$)*

7. No sistema $$\{x+y=13;\; xy=40\}$$ (problema do fazendeiro), as dimensões são `______`.
*(resposta: 8 km e 5 km)*

8. A diferença entre os lados de um retângulo com $$P=80\text{ cm}$$ e área $$=256\text{ cm}^2$$ é `______`.
*(resposta: $$32-8=24\text{ cm}$$)*

#### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Sistema — o que é a solução | `______` → *par ordenado $$(x,y)$$ que satisfaz ambas equações* |
| Método de substituição — passo 1 | `______` → *isolar variável na equação mais simples* |
| Equação do método soma/produto | `______` → *$$t^2 - St + P = 0$$* |
| Δ > 0 no sistema | `______` → *dois pares ordenados solução* |
| Δ = 0 no sistema | `______` → *um par ordenado solução (raiz dupla)* |
| Δ < 0 no sistema | `______` → *nenhum par real ($$S = \emptyset$$)* |
| $$x^2 + y^2$$ em termos de $$S$$ e $$P$$ | `______` → *$$S^2 - 2P$$* |
| Torneio com 20 jogadores — total de pontos | `______` → *$$\dfrac{20 \cdot 19}{2} = 190$$* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

Seção 10 não gerada — imagem `mat-1-9-sintese.png` rejeitada pela API (arquivo muito grande). Visualizar localmente em `Pietro/Raw/Matematica/mat-1-9-sintese.png`.

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| QI-1…QI-10 | Variados — substituição, verificação, nº de soluções, palavra | Cal/MC | M | IC | — | ⚠️ págs. 218–227 ilegíveis |
| QI-11 | Soma dos quadrados=61, diferença dos quadrados=11 — montar e resolver | Cal | M | IC | $$S=\{(6,5),(6,-5),(-6,5),(-6,-5)\}$$ | — |
| QI-12 | Soma=17/4; um número é inverso do outro — encontrar os números | Cal | M | IC | 4 e $$\frac{1}{4}$$ (via $$4t^2-17t+4=0$$) | — |
| QI-13 | Soma=6, produto=4 — determinar os números reais | Cal | M | IC | $$3-\sqrt{5}$$ e $$3+\sqrt{5}$$ | — |
| QI-14 | Sistema $$m^2-n^2=12\sqrt{5}$$, $$m-n=2\sqrt{5}$$; $$S=\{3+\sqrt{5},n\}$$ — determinar $$n$$ | Cal | D | IC | $$n = 3-\sqrt{5}$$ (via $$m+n=6$$) | — |
| Q-inv | Criar problema com sistema do 2º grau tendo $$(1,0)$$ como solução | PT | D | IC | aberto | — |
| Desafio | Obmep — torneio de xadrez; 190 pontos; a) nº de jogadores; b) André (9 pts) não foi o vencedor | Dis | D | IC | a) 20 jogadores ($$n^2-n-380=0$$, $$\Delta=1521=39^2$$); b) média=9,5 > André | — |
| Q-1 | Jardim retangular, área=119 m², diferença=10 m — dimensões | Cal | M | AT | 17 m × 7 m ($$t^2-10t-119=0$$, $$\Delta=576=24^2$$) | — |
| Q-2 | MC — quantos pares: $$\{x^2+y^2=4;\; x+y=2\}$$ | MC | M | AT | **c) Dois** — $$(0,2)$$ e $$(2,0)$$ | ⚠️ raw tinha b) |
| Q-3 | Retângulo, perímetro=80 cm, área=256 cm² — dimensões | Cal | M | AT | 32 cm × 8 cm ($$t^2-40t+256=0$$, $$\Delta=576$$) | — |
| Q-4 | Soma=15, produto=56 — diferença entre o maior e o menor | Cal | M | AT | $$8-7=1$$ ($$t^2-15t+56=0$$, $$\Delta=1$$) | — |
| Q-5 | Quociente=2, soma dos quadrados=125 — determinar os números naturais | Cal | M | AT | 10 e 5 ($$x=2y$$; $$5y^2=125$$; $$y=5$$) | — |
| Q-6 | Fazendeiro, perímetro=26 km, área=40 km² — dimensões | Cal | M | AT | 8 km × 5 km ($$t^2-13t+40=0$$, $$\Delta=9$$) | — |
| Q-7 | Triângulo retângulo, área=60 m², hipotenusa=17 m — a) sistema; b) perímetro | Cal | M | AT | Catetos 15 m e 8 m; $$P=40$$ m ($$xy=120$$, $$x^2+y^2=289$$, $$x+y=23$$) | — |
| Q-8 | MC — $$x^2-y^2=60$$, $$x/y=8/7$$ — soma dos números | MC | D | AT | **c) 30** — $$y=14$$, $$x=16$$, soma=30 | — |

---

### Bloco B — Questões modelo originais

**QM-1** · MC · médio · inspirada em: Q-2

Quantos pares ordenados satisfazem o sistema $$\begin{cases} x^2 + y^2 = 25 \\ x + y = 7 \end{cases}$$?

a) Nenhum.   b) Apenas um.   c) Dois.   d) Infinitos.

✅ Gabarito: **c) Dois**
📝 Resolução: $$y = 7-x$$; $$x^2+(7-x)^2=25 \Rightarrow 2x^2-14x+49=25 \Rightarrow 2x^2-14x+24=0 \Rightarrow x^2-7x+12=0$$; $$\Delta=49-48=1$$; $$x_1=4$$ ($$y_1=3$$); $$x_2=3$$ ($$y_2=4$$). $$S=\{(3,4),(4,3)\}$$ — dois pares.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · MC · médio · inspirada em: Q-4

Dois números têm soma 8 e produto 15. Qual é a soma dos quadrados desses números?

a) 30   b) 34   c) 40   d) 64

✅ Gabarito: **b) 34**
📝 Resolução: $$x^2+y^2 = (x+y)^2-2xy = 64-30 = 34$$. Verificação: raízes de $$t^2-8t+15=0$$: $$\Delta=64-60=4$$; $$t_1=5, t_2=3$$; $$5^2+3^2=25+9=34$$ ✓.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-3** · Cal · médio · inspirada em: Q-6

Uma piscina retangular tem área de 120 m² e perímetro de 44 m. Determine as dimensões da piscina.

✅ Gabarito: 12 m × 10 m
📝 Resolução: $$\begin{cases} x+y=22 \\ xy=120 \end{cases}$$; $$t^2-22t+120=0$$; $$\Delta=484-480=4$$; $$t_1=12, t_2=10$$. Dimensões: **12 m × 10 m**.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · MC · difícil · inspirada em: Q-8

A soma dos quadrados de dois números inteiros positivos é 130, e o produto deles é 63. Qual é a diferença entre o maior e o menor?

a) 1   b) 2   c) 3   d) 4

✅ Gabarito: **b) 2**
📝 Resolução: $$(x+y)^2 = x^2+y^2+2xy = 130+126 = 256 \Rightarrow x+y=16$$. Pela identidade diferença de quadrados: $$(x-y)^2 = x^2+y^2-2xy = 130-126=4 \Rightarrow x-y=2$$. Alternativa direta: $$t^2-16t+63=0$$; $$\Delta=256-252=4$$; $$t_1=9, t_2=7$$; diferença $$=9-7=2$$.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-5** · Dis · médio-difícil · inspirada em: Q-7

Um triângulo retângulo tem um cateto $$2$$ m maior que o outro e hipotenusa igual a $$10$$ m.

a) Monte um sistema de equações representando a situação.
b) Determine as medidas dos catetos e o perímetro do triângulo.

✅ Gabarito: catetos 6 m e 8 m; perímetro = 24 m
📝 Resolução:
a) $$\begin{cases} y = x+2 \\ x^2+y^2 = 100 \end{cases}$$
b) $$x^2+(x+2)^2=100 \Rightarrow 2x^2+4x+4=100 \Rightarrow x^2+2x-48=0$$; $$\Delta=4+192=196$$; $$x=\tfrac{-2+14}{2}=6$$; $$y=8$$. Verificação: $$36+64=100$$ ✓. Perímetro $$=6+8+10=24$$ m.
⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: metodos_resolucao
Comparativo entre o método de substituição e o método da soma e produto.

```svg
<svg width="100%" viewBox="0 0 680 290" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat9a" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Root -->
<rect x="130" y="16" width="420" height="44" rx="8" class="c-purple"/>
<text x="340" y="34" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Sistemas de Equacoes do 2o Grau</text>
<text x="340" y="52" class="ts" text-anchor="middle" fill="var(--on-accent)">solucao = par ordenado (x,y) que satisfaz ambas as equacoes</text>

<!-- Lines root to boxes -->
<line x1="260" y1="60" x2="170" y2="100" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat9a)"/>
<line x1="420" y1="60" x2="510" y2="100" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat9a)"/>

<!-- Left box: Substituicao -->
<rect x="15" y="100" width="310" height="148" rx="8" class="c-teal"/>
<text x="170" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Metodo de Substituicao</text>
<text x="170" y="142" class="ts" text-anchor="middle" fill="var(--on-accent)">1. Isolar variavel na eq. simples</text>
<text x="170" y="160" class="ts" text-anchor="middle" fill="var(--on-accent)">2. Substituir na outra equacao</text>
<text x="170" y="178" class="ts" text-anchor="middle" fill="var(--on-accent)">3. Resolver a eq. do 2o grau</text>
<text x="170" y="196" class="ts" text-anchor="middle" fill="var(--on-accent)">4. Calcular cada par (xi, yi)</text>
<text x="170" y="216" class="ts" text-anchor="middle" fill="var(--on-accent)">Ex: y=2x-1; y=x2-4 → S={(-1,-3),(3,5)}</text>

<!-- Right box: Soma e Produto -->
<rect x="355" y="100" width="310" height="148" rx="8" class="c-amber"/>
<text x="510" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Metodo Soma e Produto</text>
<text x="510" y="142" class="ts" text-anchor="middle" fill="var(--on-accent)">Usar quando: x+y=S e x.y=P</text>
<text x="510" y="160" class="ts" text-anchor="middle" fill="var(--on-accent)">Equacao: t² - S·t + P = 0</text>
<text x="510" y="178" class="ts" text-anchor="middle" fill="var(--on-accent)">Raizes t1, t2 sao os valores</text>
<text x="510" y="196" class="ts" text-anchor="middle" fill="var(--on-accent)">Escrever S={(t1,t2),(t2,t1)}</text>
<text x="510" y="216" class="ts" text-anchor="middle" fill="var(--on-accent)">Ex: x+y=10; x.y=24 → S={(4,6),(6,4)}</text>

<!-- Pegadinha -->
<rect x="15" y="260" width="650" height="24" rx="6" class="c-coral"/>
<text x="340" y="272" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Atencao: eq. soma/produto e t² - St + P = 0 (sinal NEGATIVO em S) — nao confundir com +St</text>
</svg>
```

---

### DIAGRAMA: numero_solucoes
Os três casos de número de pares ordenados solução, ligados ao discriminante.

```svg
<svg width="100%" viewBox="0 0 680 250" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat9b" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Root -->
<rect x="185" y="16" width="310" height="44" rx="8" class="c-purple"/>
<text x="340" y="34" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Numero de Solucoes do Sistema</text>
<text x="340" y="52" class="ts" text-anchor="middle" fill="var(--on-accent)">depende do Delta da eq. resultante apos substituicao</text>

<!-- Lines root to 3 boxes -->
<line x1="265" y1="60" x2="120" y2="100" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat9b)"/>
<line x1="340" y1="60" x2="340" y2="100" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat9b)"/>
<line x1="415" y1="60" x2="560" y2="100" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat9b)"/>

<!-- Box 1: Delta > 0 -->
<rect x="15" y="100" width="210" height="100" rx="8" class="c-teal"/>
<text x="120" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Delta &gt; 0</text>
<text x="120" y="142" class="ts" text-anchor="middle" fill="var(--on-accent)">Dois pares ordenados</text>
<text x="120" y="160" class="ts" text-anchor="middle" fill="var(--on-accent)">S = {(x1,y1),(x2,y2)}</text>
<text x="120" y="178" class="ts" text-anchor="middle" fill="var(--on-accent)">Parabola corta a reta: 2 pts</text>

<!-- Box 2: Delta = 0 -->
<rect x="235" y="100" width="210" height="100" rx="8" class="c-amber"/>
<text x="340" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Delta = 0</text>
<text x="340" y="142" class="ts" text-anchor="middle" fill="var(--on-accent)">Um par ordenado</text>
<text x="340" y="160" class="ts" text-anchor="middle" fill="var(--on-accent)">S = {(x0, y0)}</text>
<text x="340" y="178" class="ts" text-anchor="middle" fill="var(--on-accent)">Parabola tangencia a reta: 1 pt</text>

<!-- Box 3: Delta < 0 -->
<rect x="455" y="100" width="210" height="100" rx="8" class="c-coral"/>
<text x="560" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Delta &lt; 0</text>
<text x="560" y="142" class="ts" text-anchor="middle" fill="var(--on-accent)">Nenhum par ordenado</text>
<text x="560" y="160" class="ts" text-anchor="middle" fill="var(--on-accent)">S = vazio</text>
<text x="560" y="178" class="ts" text-anchor="middle" fill="var(--on-accent)">Parabola e reta: 0 intersecoes</text>

<!-- Note -->
<rect x="15" y="212" width="650" height="24" rx="6" class="c-gray"/>
<text x="340" y="224" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Identidade util: x² + y² = (x+y)² - 2xy — converte sistemas simetricos em soma e produto</text>
</svg>
```
