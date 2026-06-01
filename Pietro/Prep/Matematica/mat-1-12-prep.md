<!-- mat-1-12-prep.md -->

---

## DIAGRAMAS DISPONÍVEIS — mat-1-12

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Definição e Coeficientes | `DIAGRAMA: funcao_afim_def` | Ao apresentar f(x)=ax+b e os dois coeficientes (Seção 2) |
| Gráfico e Comportamento | `DIAGRAMA: grafico_comportamento` | Ao apresentar crescente/decrescente, zero e y-intercept (Seção 2) |
| Lei de Formação | `DIAGRAMA: lei_de_formacao` | Ao apresentar como encontrar a lei a partir de 2 pontos (Seção 2) |

### Tabelas markdown (Seção 6):
- Tabela comparativa: crescente / decrescente / constante
- Tabela de passos para construção do gráfico
- Tabela de passos para encontrar a lei de formação

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Síntese do livro disponível em: `Pietro/Raw/Matematica/mat-1-12-sintese.png`

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 12
- Tema: Função Afim
- Perfil: algébrico-geométrico
- Fórmulas principais:
    Definição: f(x) = ax + b  (a ≠ 0)
    Função linear: f(x) = ax  (b = 0; passa pela origem)
    Zero da função: x = –b/a  (onde f(x) = 0)
    Y-intercept: ponto (0, b)  (coeficiente linear)
    Coeficiente angular: a = Δy/Δx = (y₂–y₁)/(x₂–x₁)
    Lei de formação (2 pontos): sistema com ax₁+b=y₁ e ax₂+b=y₂
- Matemáticos citados: nenhum
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### **Bloco 1 — Definição e coeficientes**

Uma **função afim** é toda função da forma:

$$f(x) = ax + b \quad \text{com } a, b \in \mathbb{R} \text{ e } a \neq 0$$

| Coeficiente | Símbolo | Significado no gráfico |
|-------------|---------|------------------------|
| **Angular** | $$a$$ | Inclinação da reta — taxa de variação |
| **Linear** | $$b$$ | Onde a reta cruza o eixo vertical (y-intercept) |

**São funções afim:** f(x) = 3x–1; f(x) = –5x+1; f(x) = 2x/3+4

**NÃO são funções afim:**
- f(x) = –32 → a = 0 (função constante)
- f(x) = x² + 2x – 1 → tem x² (quadrática)

---

### **Bloco 2 — Gráfico: sempre uma reta**

O gráfico de qualquer função afim é **sempre uma reta não perpendicular ao eixo x**.

**Construção em 2 passos:**
1. Montar tabela atribuindo valores a x → calcular f(x) → pares (x, f(x))
2. Marcar os pontos e conectar com uma reta

> Basta **dois pontos** para traçar a reta — usar os mais fáceis de calcular (ex.: x = 0 e x = 1).

**Exemplos de tabela — f(x) = –3x – 2:**

| x | f(x) | Par |
|---|------|-----|
| –2 | 4 | (–2, 4) |
| 0 | –2 | (0, –2) |
| 2 | –8 | (2, –8) |

---

### **Bloco 3 — Crescente, decrescente e constante**

| Tipo | Condição | Comportamento visual |
|------|----------|----------------------|
| **Crescente** | a > 0 | Reta sobe da esq. para dir. |
| **Decrescente** | a < 0 | Reta desce da esq. para dir. |
| **Constante** | a = 0 | Reta horizontal (f(x) = b) |

**Classificação rápida:** olhar só o sinal de **a**.

---

### **Bloco 4 — Coeficiente linear b: o y-intercept**

O gráfico cruza o eixo vertical sempre no ponto **(0, b)**:
$$f(0) = a \cdot 0 + b = b$$

Portanto: **b = valor de f(0) = onde a reta encontra o eixo f(x)**.

---

### **Bloco 5 — Zero da função afim**

O **zero** (raiz) é o valor de x onde f(x) = 0 — ponto onde a reta cruza o eixo x.

**Para encontrar:** igualar f(x) = 0 e resolver:
$$ax + b = 0 \;\Rightarrow\; x = -\frac{b}{a}$$

**Exemplo — f(x) = –3x + 9:**
$$0 = -3x + 9 \;\Rightarrow\; 3x = 9 \;\Rightarrow\; x = 3$$

---

### **Bloco 6 — Função linear (caso particular)**

Quando **b = 0**: f(x) = ax → **função linear**

- Gráfico **passa pela origem (0, 0)**
- Ainda é crescente (a>0) ou decrescente (a<0)
- Exemplo: f(x) = 250x (salário proporcional a consoles vendidos)

---

### **Bloco 7 — Encontrar a lei de formação a partir de 2 pontos**

Dados dois pontos (x₁, y₁) e (x₂, y₂):

1. Escrever o sistema de equações:
   $$\begin{cases} ax_1 + b = y_1 \\ ax_2 + b = y_2 \end{cases}$$

2. Subtrair uma equação da outra para isolar **a**

3. Substituir **a** para encontrar **b**

4. Escrever f(x) = ax + b

**Atalho para o coeficiente angular:**
$$a = \frac{y_2 - y_1}{x_2 - x_1}$$

**Exemplo — pontos (2, 4) e (4, –2):**
- a = (–2–4)/(4–2) = –6/2 = **–3**
- b: 4 = –3(2) + b → b = **10**
- **f(x) = –3x + 10** → a + b = 7

---

### **Bloco 8 — Reconhecer funções em gráficos**

**Teste da reta vertical:** traçar retas perpendiculares ao eixo x.
- Cada reta toca o gráfico em **no máximo 1 ponto** → **é função** ✅
- Alguma reta toca em **2 ou mais pontos** → **não é função** ❌

**Domínio e Imagem pelo gráfico:**
- **Domínio (D):** intervalo de valores de x que o gráfico abrange (eixo horizontal)
- **Imagem (Im):** intervalo de valores de f(x) que o gráfico atinge (eixo vertical)

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Função afim

**Expressão:** $$f(x) = ax + b$$

| Símbolo | Significado | Restrição |
|---------|-------------|-----------|
| $$a$$ | coeficiente angular (taxa de variação) | $$a \neq 0$$ |
| $$b$$ | coeficiente linear (y-intercept) | $$b \in \mathbb{R}$$ |
| $$x$$ | variável independente (entrada) | $$x \in \mathbb{R}$$ |

💡 **Pegadinha:** f(x) = –32 (ou qualquer constante) tem a = 0 → **não é função afim**, é função constante.

---

### Zero da função afim

**Expressão:** $$x_0 = -\frac{b}{a}$$

**Uso:** encontrar onde a reta cruza o eixo x (onde f(x) = 0).

💡 **Pegadinha:** o zero é o valor de **x** (não de f(x)). O par ordenado do zero é **(x₀, 0)** — no eixo x, não no eixo y.

---

### Coeficiente angular a partir de dois pontos

**Expressão:** $$a = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$

**Uso:** calcular a inclinação da reta sem montar o sistema completo.

💡 **Pegadinha:** a ordem dos pontos não importa, mas deve ser consistente: numerador e denominador devem usar a mesma ordem (y₂–y₁ e x₂–x₁, não misturar).

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Classificação da função afim

| Coeficiente angular (a) | Tipo | Gráfico |
|------------------------|------|---------|
| a > 0 | Crescente | Reta sobe ↗ |
| a < 0 | Decrescente | Reta desce ↘ |
| a = 0 | Constante (não é afim) | Reta horizontal → |
| a = 0 e b = 0 | Função nula | Reta sobre o eixo x |

### Passos para construir o gráfico

| Passo | O que fazer |
|-------|-------------|
| 1 | Escolher 2 ou mais valores de x (sugestão: –1, 0, 1) |
| 2 | Calcular f(x) para cada x escolhido |
| 3 | Montar tabela com pares (x, f(x)) |
| 4 | Marcar pontos no plano cartesiano |
| 5 | Ligar com reta (estendendo além dos pontos) |

### Passos para encontrar a lei de formação (2 pontos)

| Passo | O que fazer |
|-------|-------------|
| 1 | Identificar os dois pares ordenados (x₁,y₁) e (x₂,y₂) |
| 2 | Calcular a = (y₂–y₁)/(x₂–x₁) |
| 3 | Substituir a e um ponto em f(x) = ax + b para encontrar b |
| 4 | Escrever f(x) = ax + b |

### Valores-chave nas funções do capítulo

| Função | a | b | Zero (x₀) | Y-intercept (0,b) | Tipo |
|--------|---|---|-----------|-------------------|------|
| f(x) = 3x – 1 | 3 | –1 | 1/3 | (0,–1) | Crescente |
| f(x) = –3x + 9 | –3 | 9 | 3 | (0,9) | Decrescente |
| f(x) = –3x – 2 | –3 | –2 | –2/3 | (0,–2) | Decrescente |
| f(x) = 3x/2 – 1 | 3/2 | –1 | 2/3 | (0,–1) | Crescente |
| f(x) = –2x + 4 | –2 | 4 | 2 | (0,4) | Decrescente |
| f(x) = 250x | 250 | 0 | 0 | (0,0) | Linear/Crescente |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Dois pontos fáceis: zero e y-intercept**
Para traçar o gráfico rapidamente, usar: (0, b) — o y-intercept — e (–b/a, 0) — o zero. São os dois pontos mais fáceis de calcular e evitam frações.

💡 **Dica 2 — Sinal de a determina tudo sobre o comportamento**
Antes de calcular qualquer coisa, verificar o sinal de a: positivo → cresce (da esq. para dir.); negativo → decresce. Isso orienta o esboço do gráfico mesmo sem montar tabela.

💡 **Dica 3 — Y-intercept = f(0) = b**
Para ler o coeficiente linear diretamente do gráfico: ver onde a reta cruza o eixo vertical. Esse valor é b. Economiza tempo em problemas de "encontrar a lei".

💡 **Dica 4 — Zero ≠ valor da função; é valor de x**
"Encontrar o zero de f(x) = 3x – 6": a resposta é x = 2, não f(x) = 2. O zero é um valor de x, não de f(x). O ponto no gráfico é (2, 0), no eixo horizontal.

💡 **Dica 5 — Para encontrar a lei: usar o y-intercept primeiro**
Se o gráfico mostra o ponto onde a reta corta o eixo y, ler b diretamente. Depois substituir qualquer outro ponto conhecido para calcular a. Muito mais rápido que montar o sistema completo.

💡 **Dica 6 — Corrida/encontro: igualar as duas funções**
Problemas de "quando dois móveis se encontram" ou "quando dois custos se igualam": igualar as duas leis de formação e resolver para x. O valor de x é o instante/quantidade do encontro.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

#### Bloco A — Lacunas de dados

| Seção | Campo | Motivo | Ação |
|-------|-------|--------|------|
| AT-4 (Unicamp) | Gabarito e análise do gráfico | Gráfico parcialmente ilegível | Verificar pág. 328 |
| AT-5 e AT-6 | Enunciados vestibulares | Imagens pequenas | Verificar págs. 329 |
| AT-12 (UEG-GO) | Gráfico e gabarito | Diferente do AT-10 mas parece similar | Verificar pág. 331 |
| AT-15 e AT-16 | Questões finais | Parcialmente ilegíveis | Verificar págs. 333 |
| Desafio | Enunciado e solução | Parcialmente ilegível | Verificar pág. 325 |

#### Bloco B — Alertas

```
⚠️ ALERTA — f(x) = constante NÃO é função afim
- f(x) = –32 tem a = 0 → CONSTANTE, não afim
- Critério: a ≠ 0 é obrigatório na definição de função afim
- Erro comum: marcar V para constantes na AT-1
```

```
⚠️ ALERTA — Zero vs y-intercept
- Zero: f(x) = 0 → resolvendo para x → ponto no EIXO X
- Y-intercept: x = 0 → f(0) = b → ponto no EIXO Y
- São conceitos distintos; não confundir nos enunciados
```

```
⚠️ ALERTA — AT-13 (ESPM): temperatura
- Gabarito d) 78 min (não 88 min)
- Cálculo: se T(20)=40 e taxa=–1°C/min → T(t) = 60 – t
- 60 – t = –18 → t = 78 min
- Verificar os dados exatos do gráfico no livro antes de usar
```

```
⚠️ ALERTA — AT-14: dois ônibus saindo da MESMA cidade
- Ambos saem de A para B (não se encontram "de frente")
- Y se move mais rápido e parte depois → alcança X
- Equação: 100(t–2) = 80t → t = 10h
- Erro comum: montar equação como se viessem em sentidos opostos
```

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO

#### Bloco 1 — Conceitos e Definições

- **Função afim**
  - Lei: `______` (f(x) = ax + b, a≠0)
  - Coeficiente angular: `______` (a = taxa de variação = inclinação)
  - Coeficiente linear: `______` (b = onde a reta cruza o eixo f(x))

- **Gráfico**
  - Forma: `______` (sempre uma reta não perpendicular ao eixo x)
  - Crescente quando: `______` (a > 0)
  - Decrescente quando: `______` (a < 0)

- **Zero da função**
  - Definição: `______` (valor de x onde f(x) = 0)
  - Fórmula: `______` (x = –b/a)

- **Função linear**
  - Diferença: `______` (b = 0; passa pela origem)
  - Lei: `______` (f(x) = ax)

#### Bloco 2 — Lacunas para Warm-Up

1. A função f(x) = 5x – 3 tem coeficiente angular `______` e coeficiente linear `______`.
*(resposta: 5; –3)*

2. O zero de f(x) = 4x – 20 é x = `______`.
*(resposta: 5 — 4x = 20 → x = 5)*

3. A função f(x) = –32 é crescente, decrescente ou constante? `______`
*(resposta: constante — a = 0)*

4. O gráfico de f(x) = ax + b cruza o eixo f(x) no ponto `______`.
*(resposta: (0, b))*

5. Dada f(x) = –3x + 9, qual o zero? `______`
*(resposta: x = 3 — 0 = –3x + 9 → x = 3)*

6. f(x) = 250x é uma função `______` (tipo especial da afim).
*(resposta: linear — b = 0, passa pela origem)*

7. Pontos (2, 4) e (4, –2): a = `______`, b = `______`, f(x) = `______`.
*(resposta: a = –3; b = 10; f(x) = –3x + 10)*

8. O teste para saber se um gráfico representa uma função é `______`.
*(resposta: teste da reta vertical — cada x com no máximo 1 imagem)*

9. Luca (10 m/s) e Júlia (5 m/s, 30 m à frente). Luca alcança Júlia em t = `______`.
*(resposta: t = 6 s — 10t = 30 + 5t → t = 6)*

10. f(x) = –2x + 4 cruza o eixo x em x = `______` e o eixo f(x) em f(x) = `______`.
*(resposta: x = 2 (zero); f(x) = 4 (coef. linear b))*

#### Bloco 3 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Forma geral da função afim | `______` → *f(x) = ax + b, a ≠ 0* |
| Coeficiente angular | `______` → *a: taxa de variação; determina crescimento* |
| Coeficiente linear | `______` → *b: y-intercept; f(0) = b* |
| Crescente | `______` → *a > 0* |
| Decrescente | `______` → *a < 0* |
| Zero da função | `______` → *x = –b/a (onde a reta cruza eixo x)* |
| Função linear | `______` → *f(x) = ax; b = 0; passa pela origem* |
| Encontrar lei (2 pontos) | `______` → *calcular a = Δy/Δx; depois b = y – ax* |
| Teste da reta vertical | `______` → *reta perpendicular ao eixo x corta em ≤1 ponto* |
| Y-intercept do gráfico | `______` → *ponto (0, b); lido diretamente no eixo vertical* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

Imagem disponível: `Pietro/Raw/Matematica/mat-1-12-sintese.png`

A síntese (pág. 335) apresenta mapa conceitual com os ramos:
- **Definição:** f(x) = ax + b (coef. angular a; coef. linear b)
- **Caso particular:** função linear f(x) = ax (reta pela origem)
- **Gráfico:** crescente/decrescente/constante; traçado com 2 pontos
- **Zero:** valor de x onde a reta intersecta o eixo x
- **Reconhecer se é função:** teste da reta vertical
- **Encontrar lei de formação:** 2 pares ordenados → sistema de equações
- **Domínio e imagem pelo gráfico:** eixo x (domínio), eixo y (imagem)

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| AT-1 | Identificar V/F se é função afim (6 opções) | MC | F | IC | a)V b)F c)V d)F e)V f)V | ⚠️ b e d são falsas |
| AT-3 | Carcaças: C(x)=750+1,25x; calcular custo e máximo | Cal | F | IC | C(10000)=R$13.250; máx=7400 | — |
| AT-5 | Classificar 6 funções: crescente/dec./constante | Cal | F | IC | a)cres b)const c)dec d)dec e)cres f)const | — |
| AT-6 | Intersecção de f(x)=x+2 e g(x)=–x+4 | Cal | F | IC | (1, 3) | — |
| AT-7 | Zero de 6 funções afim | Cal | F | IC | a)–1 b)5 c)9 d)–5 e)60 f)36 | — |
| AT-16a | Lei: pontos (1,2) e (0,4) | Cal | F | AT | f(x) = –2x + 4 | — |
| AT-16b | Lei: pontos (–4,3) e (1,2) | Cal | M | AT | f(x) = –x/5 + 11/5 | — |
| AT-17a | Lei do gráfico: y-int=3, zero x=2 | Cal | M | AT | f(x) = –(3/2)x + 3 | — |
| AT-17b | Lei do gráfico: y-int=–3, zero x=3/2 | Cal | M | AT | f(x) = 2x – 3 | — |
| AT-17c | Lei do gráfico: pontos (0,1) e (4,3) | Cal | M | AT | f(x) = x/2 + 1 | — |
| AT-17e | Lei do gráfico: y-int=2, zero x=–4 | Cal | M | AT | f(x) = x/2 + 2 | — |
| AT-18 | Luciana costureira: S(x)=10x+110 | Cal | F | IC | a)10x+110; b)R$260; c)10 roupas | — |
| Q-2 | Luca e Júlia: equações de corrida | Cal | M | AT | t=6s; d=60m | — |
| Q-10 | (UEG-GO) Função a partir de gráfico | MC | M | AT | **b) –0,25x+1** | — |
| Q-11 | (Ifal) Pontos (2,4) e (4,–2): a+b | MC | M | AT | **b) 7** | — |
| Q-13 | (ESPM) Temperatura câmara: tempo | MC | D | AT | **d) 78 min** | ⚠️ ver alerta |
| Q-14 | Ônibus X e Y: cruzamento | MC | D | AT | **d) 10h** | ⚠️ ver alerta |
| Q-15 | (UCS-RS) Produção: lucro % da receita | MC | M | AT | **a) 5%** | — |

---

### Bloco B — Questões modelo originais

**QM-1** · Cal · fácil · inspirada em: AT-7

Determine o zero das funções:
a) f(x) = 5x – 15
b) f(x) = –2x + 8
c) f(x) = x/3 + 2

✅ Gabarito: **a) x=3 · b) x=4 · c) x=–6**
📝 Resolução: a) 5x=15→x=3; b) 2x=8→x=4; c) x/3=–2→x=–6.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · Cal · médio · inspirada em: AT-16 / AT-17

Encontre a lei de formação da função afim que passa pelos pontos (–1, 5) e (3, –3).

✅ Gabarito: **f(x) = –2x + 3**
📝 Resolução: a = (–3–5)/(3–(–1)) = –8/4 = –2. Usando ponto (–1,5): 5 = –2(–1) + b → 5 = 2 + b → b = 3. f(x) = –2x + 3. Verificação: f(3) = –6+3 = –3 ✓.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-3** · MC · médio · inspirada em: Q-14 (ônibus)

Uma torneira enche um reservatório vazio a 8 litros/minuto. Outra torneira, com o reservatório já com 40 litros, enche a 5 litros/minuto. Em que momento os dois reservatórios terão o mesmo volume?

a) t = 10 min   b) t = 12 min   c) t = 13⅓ min   d) t = 20 min

✅ Gabarito: **c) t = 13⅓ min**
📝 Resolução: R₁(t) = 8t; R₂(t) = 40 + 5t. Igualar: 8t = 40 + 5t → 3t = 40 → t = 40/3 = 13⅓ min. Volume: R₁(40/3) = 320/3 ≈ 106,7 L.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · Cal · médio-difícil · inspirada em: Q-15 (UCS-RS)

Uma empresa tem custo de produção C(x) = 150x + 2000 e receita R(x) = 200x, onde x é a quantidade produzida.

a) A partir de quantas unidades a empresa começa a ter lucro?
b) Qual é o lucro líquido com 80 unidades produzidas?
c) Qual é o lucro líquido como porcentagem da receita com 80 unidades?

✅ Gabarito: **a) 40 unidades · b) R$2.000 · c) 12,5%**
📝 Resolução:
a) Lucro = R – C > 0: 200x > 150x + 2000 → 50x > 2000 → x > 40. Break-even em x = 40.
b) L(80) = 200(80) – [150(80)+2000] = 16000 – 14000 = R$2.000.
c) L/R × 100 = 2000/16000 × 100 = 12,5%.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-5** · Dis · difícil · inspirada em: AT-6 / Q-2 (corrida)

Uma empresa A cobra R$50,00 + R$1,20/km para entregas. Uma empresa B cobra R$20,00 + R$1,80/km.

a) Escreva as funções de custo de cada empresa.
b) Para qual distância o custo é igual?
c) Qual empresa é mais econômica para 40 km? E para 60 km?

✅ Gabarito: **a) A(k)=1,20k+50; B(k)=1,80k+20 · b) k=50 km · c) 40km → B; 60km → A**
📝 Resolução:
a) A(k) = 1,20k + 50; B(k) = 1,80k + 20.
b) 1,20k + 50 = 1,80k + 20 → 30 = 0,60k → k = 50 km.
c) A(40)=98; B(40)=92 → B mais barata. A(60)=122; B(60)=128 → A mais barata.
⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: funcao_afim_def
Definição da função afim e papel dos coeficientes angular e linear.

```svg
<svg width="100%" viewBox="0 0 680 310" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat12a" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Central formula -->
<rect x="190" y="10" width="300" height="52" rx="10" class="c-purple"/>
<text x="340" y="30" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Funcao Afim</text>
<text x="340" y="52" class="th" text-anchor="middle" fill="var(--on-accent)">f(x) = ax + b  (a diferente de 0)</text>

<!-- Arrow to a -->
<line x1="270" y1="62" x2="175" y2="105" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat12a)"/>
<!-- Arrow to b -->
<line x1="410" y1="62" x2="505" y2="105" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat12a)"/>

<!-- Left: coef angular -->
<rect x="15" y="105" width="305" height="110" rx="8" class="c-teal"/>
<text x="167" y="125" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Coeficiente Angular (a)</text>
<text x="167" y="147" class="ts" text-anchor="middle" fill="var(--on-accent)">Taxa de variacao (inclinacao da reta)</text>
<text x="167" y="165" class="ts" text-anchor="middle" fill="var(--on-accent)">a &gt; 0: reta sobe (crescente)</text>
<text x="167" y="183" class="ts" text-anchor="middle" fill="var(--on-accent)">a &lt; 0: reta desce (decrescente)</text>
<text x="167" y="201" class="ts" text-anchor="middle" fill="var(--on-accent)">a = 0: reta horizontal (constante)</text>

<!-- Right: coef linear -->
<rect x="360" y="105" width="305" height="110" rx="8" class="c-amber"/>
<text x="512" y="125" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Coeficiente Linear (b)</text>
<text x="512" y="147" class="ts" text-anchor="middle" fill="var(--on-accent)">Onde a reta cruza o eixo f(x)</text>
<text x="512" y="165" class="ts" text-anchor="middle" fill="var(--on-accent)">f(0) = a.0 + b = b</text>
<text x="512" y="183" class="ts" text-anchor="middle" fill="var(--on-accent)">Ponto: (0, b)</text>
<text x="512" y="201" class="ts" text-anchor="middle" fill="var(--on-accent)">Lido diretamente no grafico</text>

<!-- Examples -->
<rect x="15" y="230" width="200" height="66" rx="6" class="c-teal"/>
<text x="115" y="250" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Sao funcao afim:</text>
<text x="115" y="268" class="ts" text-anchor="middle" fill="var(--on-accent)">3x - 1  |  -5x + 1</text>
<text x="115" y="286" class="ts" text-anchor="middle" fill="var(--on-accent)">2x/3 + 4  |  -x + 10</text>

<rect x="235" y="230" width="210" height="66" rx="6" class="c-coral"/>
<text x="340" y="250" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">NAO sao funcao afim:</text>
<text x="340" y="268" class="ts" text-anchor="middle" fill="var(--on-accent)">f(x) = -32  (a = 0, constante)</text>
<text x="340" y="286" class="ts" text-anchor="middle" fill="var(--on-accent)">f(x) = x2 + 2x - 1  (grau 2)</text>

<rect x="465" y="230" width="200" height="66" rx="6" class="c-amber"/>
<text x="565" y="250" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Funcao linear (b = 0):</text>
<text x="565" y="268" class="ts" text-anchor="middle" fill="var(--on-accent)">f(x) = ax</text>
<text x="565" y="286" class="ts" text-anchor="middle" fill="var(--on-accent)">Passa pela origem (0, 0)</text>
</svg>
```

---

### DIAGRAMA: grafico_comportamento
Comportamento do gráfico — crescente/decrescente, zero e y-intercept.

```svg
<svg width="100%" viewBox="0 0 680 310" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat12b" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Top: crescente vs decrescente -->
<rect x="15" y="10" width="200" height="120" rx="8" class="c-teal"/>
<text x="115" y="28" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">CRESCENTE (a &gt; 0)</text>
<!-- Axes crescente -->
<line x1="35" y1="100" x2="195" y2="100" stroke="white" stroke-width="1"/>
<line x1="115" y1="40" x2="115" y2="115" stroke="white" stroke-width="1"/>
<!-- Crescente line -->
<line x1="45" y1="105" x2="185" y2="48" stroke="white" stroke-width="2"/>
<text x="115" y="118" class="ts" text-anchor="middle" fill="var(--on-accent)">sobe da esq para dir</text>

<rect x="240" y="10" width="200" height="120" rx="8" class="c-coral"/>
<text x="340" y="28" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">DECRESCENTE (a &lt; 0)</text>
<!-- Axes decrescente -->
<line x1="260" y1="100" x2="420" y2="100" stroke="white" stroke-width="1"/>
<line x1="340" y1="40" x2="340" y2="115" stroke="white" stroke-width="1"/>
<!-- Decrescente line -->
<line x1="265" y1="48" x2="415" y2="105" stroke="white" stroke-width="2"/>
<text x="340" y="118" class="ts" text-anchor="middle" fill="var(--on-accent)">desce da esq para dir</text>

<rect x="465" y="10" width="200" height="120" rx="8" class="c-gray"/>
<text x="565" y="28" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">CONSTANTE (a = 0)</text>
<!-- Axes constante -->
<line x1="480" y1="80" x2="650" y2="80" stroke="white" stroke-width="1"/>
<line x1="565" y1="35" x2="565" y2="110" stroke="white" stroke-width="1"/>
<!-- Constant line -->
<line x1="490" y1="65" x2="645" y2="65" stroke="white" stroke-width="2"/>
<text x="565" y="100" class="ts" text-anchor="middle" fill="var(--on-accent)">reta horizontal = b</text>
<text x="565" y="118" class="ts" text-anchor="middle" fill="var(--on-accent)">nao e funcao afim</text>

<!-- Bottom: zero and y-intercept -->
<rect x="15" y="148" width="310" height="148" rx="8" class="c-purple"/>
<text x="170" y="168" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Zero da Funcao</text>
<text x="170" y="188" class="ts" text-anchor="middle" fill="var(--on-accent)">Onde a reta cruza o EIXO X</text>
<text x="170" y="208" class="ts" text-anchor="middle" fill="var(--on-accent)">f(x) = 0  →  ax + b = 0  →  x = -b/a</text>
<text x="170" y="228" class="ts" text-anchor="middle" fill="var(--on-accent)">Ponto no grafico: (x0, 0)</text>
<text x="170" y="250" class="ts" text-anchor="middle" fill="var(--on-accent)">Ex: f(x) = -3x + 9</text>
<text x="170" y="268" class="ts" text-anchor="middle" fill="var(--on-accent)">0 = -3x + 9  →  x = 3</text>
<text x="170" y="286" class="ts" text-anchor="middle" fill="var(--on-accent)">Zero: x = 3  →  ponto (3, 0)</text>

<rect x="355" y="148" width="310" height="148" rx="8" class="c-amber"/>
<text x="510" y="168" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Coeficiente Linear b</text>
<text x="510" y="188" class="ts" text-anchor="middle" fill="var(--on-accent)">Onde a reta cruza o EIXO f(x)</text>
<text x="510" y="208" class="ts" text-anchor="middle" fill="var(--on-accent)">f(0) = a.0 + b = b</text>
<text x="510" y="228" class="ts" text-anchor="middle" fill="var(--on-accent)">Ponto no grafico: (0, b)</text>
<text x="510" y="250" class="ts" text-anchor="middle" fill="var(--on-accent)">Ex: f(x) = -3x + 9</text>
<text x="510" y="268" class="ts" text-anchor="middle" fill="var(--on-accent)">f(0) = 9  →  y-intercept = 9</text>
<text x="510" y="286" class="ts" text-anchor="middle" fill="var(--on-accent)">Ponto (0, 9) no grafico</text>
</svg>
```

---

### DIAGRAMA: lei_de_formacao
Método para encontrar a lei de formação a partir de dois pontos.

```svg
<svg width="100%" viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat12c" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Title -->
<rect x="160" y="8" width="360" height="30" rx="6" class="c-purple"/>
<text x="340" y="23" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Encontrar a Lei de Formacao (2 pontos)</text>

<!-- Step boxes -->
<rect x="15" y="50" width="136" height="80" rx="6" class="c-teal"/>
<text x="83" y="68" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">1. Dois pontos</text>
<text x="83" y="88" class="ts" text-anchor="middle" fill="var(--on-accent)">(x1, y1)</text>
<text x="83" y="106" class="ts" text-anchor="middle" fill="var(--on-accent)">(x2, y2)</text>
<text x="83" y="122" class="ts" text-anchor="middle" fill="var(--on-accent)">do grafico</text>

<line x1="151" y1="90" x2="170" y2="90" stroke="var(--c-teal)" stroke-width="1.5" marker-end="url(#arr-mat12c)"/>

<rect x="172" y="50" width="136" height="80" rx="6" class="c-teal"/>
<text x="240" y="68" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">2. Calcular a</text>
<text x="240" y="88" class="ts" text-anchor="middle" fill="var(--on-accent)">a = (y2 - y1)</text>
<text x="240" y="106" class="ts" text-anchor="middle" fill="var(--on-accent)">   (x2 - x1)</text>
<text x="240" y="122" class="ts" text-anchor="middle" fill="var(--on-accent)">delta y / delta x</text>

<line x1="308" y1="90" x2="327" y2="90" stroke="var(--c-teal)" stroke-width="1.5" marker-end="url(#arr-mat12c)"/>

<rect x="329" y="50" width="136" height="80" rx="6" class="c-amber"/>
<text x="397" y="68" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">3. Calcular b</text>
<text x="397" y="88" class="ts" text-anchor="middle" fill="var(--on-accent)">b = y1 - a.x1</text>
<text x="397" y="106" class="ts" text-anchor="middle" fill="var(--on-accent)">usar qualquer</text>
<text x="397" y="122" class="ts" text-anchor="middle" fill="var(--on-accent)">dos 2 pontos</text>

<line x1="465" y1="90" x2="484" y2="90" stroke="var(--c-amber)" stroke-width="1.5" marker-end="url(#arr-mat12c)"/>

<rect x="486" y="50" width="179" height="80" rx="6" class="c-purple"/>
<text x="575" y="68" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">4. Escrever lei</text>
<text x="575" y="90" class="ts" text-anchor="middle" fill="var(--on-accent)">f(x) = ax + b</text>
<text x="575" y="110" class="ts" text-anchor="middle" fill="var(--on-accent)">Verificar com</text>
<text x="575" y="126" class="ts" text-anchor="middle" fill="var(--on-accent)">os 2 pontos</text>

<!-- Example box -->
<rect x="15" y="148" width="650" height="140" rx="8" class="c-gray"/>
<text x="340" y="166" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Exemplo: pontos (2, 4) e (4, -2)</text>

<text x="50" y="190" class="ts" text-anchor="start" fill="var(--on-accent)">Passo 2: a = (-2 - 4) / (4 - 2) = -6 / 2 = -3</text>
<text x="50" y="210" class="ts" text-anchor="start" fill="var(--on-accent)">Passo 3: b = y1 - a.x1 = 4 - (-3)(2) = 4 + 6 = 10</text>
<text x="50" y="230" class="ts" text-anchor="start" fill="var(--on-accent)">Passo 4: f(x) = -3x + 10</text>
<text x="50" y="250" class="ts" text-anchor="start" fill="var(--on-accent)">Verificar: f(2) = -6+10 = 4 v  |  f(4) = -12+10 = -2 v</text>
<text x="50" y="275" class="th" text-anchor="start" fill="var(--on-accent)">a + b = -3 + 10 = 7  (resposta Ifal)</text>
</svg>
```
