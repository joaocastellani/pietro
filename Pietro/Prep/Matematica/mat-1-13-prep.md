<!-- mat-1-13-prep.md -->

---

## DIAGRAMAS DISPONÍVEIS — mat-1-13

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Plano Cartesiano | `DIAGRAMA: plano_cartesiano` | Ao apresentar eixos, quadrantes e coordenadas (Seção 2 Bloco 1 e 2) |
| Casos de Distância | `DIAGRAMA: distancia_casos` | Ao apresentar os 3 casos e a fórmula geral (Seção 2 Bloco 3 e 4) |
| Baricentro | `DIAGRAMA: baricentro` | Ao apresentar o texto complementar sobre baricentro (Seção 2 Bloco 5) |

### Tabelas markdown (Seção 6):
- Tabela de sinais por quadrante
- Tabela comparativa dos 3 casos de distância
- Tabela dos cálculos de referência (AT-9)

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Síntese do livro disponível em: `Pietro/Raw/Matematica/mat-1-13-sintese.png`

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 13
- Tema: Distância Entre Dois Pontos no Plano Cartesiano
- Perfil: misto (algébrico-geométrico)
- Fórmulas principais:
    Distância geral:    d_AB = √[(x_B–x_A)² + (y_B–y_A)²]
    Mesma ordenada:     d_AB = |x_B – x_A|
    Mesma abscissa:     d_AB = |y_B – y_A|
    Baricentro:         x_G = (x_A + x_B + x_C) / 3
                        y_G = (y_A + y_B + y_C) / 3
- Matemáticos citados: nenhum
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### **Bloco 1 — Plano cartesiano: o sistema de localização**

O **plano cartesiano** é um sistema de coordenadas formado por dois eixos numéricos perpendiculares:
- **Eixo das abscissas** (eixo x) — horizontal
- **Eixo das ordenadas** (eixo y) — vertical

O ponto de cruzamento dos eixos é a **origem** O(0, 0). Os dois eixos dividem o plano em **quatro quadrantes**, numerados de 1 a 4 no sentido anti-horário, partindo do quadrante superior direito.

> **Contexto real:** o sistema de latitude e longitude da Terra funciona como um plano cartesiano "enrolado" na esfera — a origem (0°, 0°) fica no Golfo da Guiné, e a NASA usa um sistema equivalente para mapear a superfície de Marte.

---

### **Bloco 2 — Representação de pontos e quadrantes**

Cada ponto P é representado pelo **par ordenado (x, y)**, onde x é a abscissa e y é a ordenada. A ordem importa: (3, 5) ≠ (5, 3).

| Quadrante | Abscissa x | Ordenada y |
|-----------|-----------|-----------|
| **1º** | positiva (+) | positiva (+) |
| **2º** | negativa (–) | positiva (+) |
| **3º** | negativa (–) | negativa (–) |
| **4º** | positiva (+) | negativa (–) |

**Casos especiais — nos eixos:**
- Ponto no **eixo x**: y = 0 → forma P(x, 0)
- Ponto no **eixo y**: x = 0 → forma P(0, y)
- Pontos nos eixos **não pertencem a nenhum quadrante**

---

### **Bloco 3 — Distância: três casos**

**1º caso — mesma ordenada** (pontos alinhados horizontalmente):
Os pontos A(x_A, y) e B(x_B, y) formam um segmento horizontal.
$$d_{AB} = |x_B - x_A|$$

**2º caso — mesma abscissa** (pontos alinhados verticalmente):
Os pontos A(x, y_A) e B(x, y_B) formam um segmento vertical.
$$d_{AB} = |y_B - y_A|$$

> O módulo garante que a distância seja sempre positiva, independentemente da ordem dos pontos.

---

### **Bloco 4 — Caso geral: o Teorema de Pitágoras aplicado**

Dados A(x_A, y_A) e B(x_B, y_B) quaisquer, formamos o triângulo retângulo auxiliar ACB onde C = (x_B, y_A):
- Cateto horizontal: AC = |x_B – x_A|
- Cateto vertical: CB = |y_B – y_A|
- Hipotenusa: AB = d_AB

Pelo **Teorema de Pitágoras**:
$$(d_{AB})^2 = (x_B - x_A)^2 + (y_B - y_A)^2$$

$$\boxed{d_{AB} = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}}$$

Esta fórmula também funciona nos casos 1 e 2 (quando uma das diferenças é zero o termo desaparece).

**Exemplo — distância M(2, 5) e T(5, –1):**
$$d_{MT} = \sqrt{(5-2)^2 + (-1-5)^2} = \sqrt{9 + 36} = \sqrt{45} = 3\sqrt{5}$$

---

### **Bloco 5 — Ponto equidistante em um eixo**

Problema frequente: *"Encontre o ponto P no eixo Ox equidistante de A e B."*

**Método:**
1. Como P está no eixo x: P = (x, 0) — a ordenada é sempre zero
2. Impor d_PA = d_PB e elevar ao quadrado (elimina a raiz)
3. Resolver a equação linear resultante para x

**Exemplo — ER-2:** P no eixo Ox, d_PA = d_PB, A(–2, –2) e B(1, 2):
$$(x+2)^2 + 4 = (x-1)^2 + 4$$
$$x^2+4x+4 = x^2-2x+1 \Rightarrow 6x = -3 \Rightarrow x = -\frac{1}{2}$$
$$\boxed{P = \left(-\frac{1}{2},\, 0\right)}$$

Para o eixo y: P = (0, y) — a abscissa é zero, mesma lógica.

---

### **Bloco 6 — Baricentro de um triângulo (Texto complementar)**

O **baricentro** G é o ponto de interseção das três medianas do triângulo. Sua posição no plano cartesiano pode ser calculada diretamente:

Dado triângulo ABC com A(x_A, y_A), B(x_B, y_B), C(x_C, y_C):

$$\boxed{x_G = \frac{x_A + x_B + x_C}{3} \qquad y_G = \frac{y_A + y_B + y_C}{3}}$$

> **Intuição:** as coordenadas do baricentro são a **média aritmética** das coordenadas dos três vértices.

**Exemplo — A(1,1), B(3,–1), C(5,3):**
$$G = \left(\frac{1+3+5}{3},\, \frac{1-1+3}{3}\right) = (3,\, 1)$$

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Distância entre dois pontos (caso geral)

**Expressão:** $$d_{AB} = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$d_{AB}$$ | distância do ponto A ao ponto B | real não negativo |
| $$x_A, x_B$$ | abscissas dos pontos A e B | real |
| $$y_A, y_B$$ | ordenadas dos pontos A e B | real |

**Válida quando:** quaisquer dois pontos distintos no plano.
**Caso especial:** se os pontos são iguais, d = 0.
💡 **Pegadinha:** a fórmula usa diferença ao quadrado — o sinal não importa (negativo ao quadrado = positivo). Não é necessário garantir x_B > x_A.

---

### Distância — casos especiais

**Mesma ordenada:** $$d_{AB} = |x_B - x_A|$$
**Mesma abscissa:** $$d_{AB} = |y_B - y_A|$$

💡 **Pegadinha:** se os pontos têm mesma ordenada, a distância usa só a diferença das **abscissas** (e vice-versa). Trocar x e y é um erro comum.

---

### Baricentro de triângulo

**Expressão:**
$$G = \left(\frac{x_A + x_B + x_C}{3},\; \frac{y_A + y_B + y_C}{3}\right)$$

| Símbolo | Significado |
|---------|-------------|
| $$G$$ | baricentro (ponto de interseção das medianas) |
| $$x_A, x_B, x_C$$ | abscissas dos vértices |
| $$y_A, y_B, y_C$$ | ordenadas dos vértices |

💡 **Pegadinha:** dividir por 3, não por 2. Confundir com ponto médio (que usa 2 pontos e divide por 2) é erro frequente.

---

## SEÇÃO 5 — REPRESENTAÇÕES E SISTEMAS

### Plano Cartesiano

**Definição:** sistema de coordenadas formado por dois eixos numéricos perpendiculares que se cruzam na origem.

**Elementos:**
- Eixo x (abscissas) — valores crescem para a direita
- Eixo y (ordenadas) — valores crescem para cima
- Origem O(0, 0) — ponto de interseção dos eixos
- Par ordenado (x, y) — representa qualquer ponto do plano

**Regras de leitura:**
1. Ler a abscissa (movimento horizontal a partir da origem)
2. Ler a ordenada (movimento vertical a partir da origem)
3. Escrever sempre na ordem: (abscissa, ordenada)

**Relações especiais:**
- Ponto no eixo x → y = 0
- Ponto no eixo y → x = 0
- Ponto na origem → (0, 0)
- Bissetriz do 1º e 3º quadrantes → reta y = x
- Bissetriz do 2º e 4º quadrantes → reta y = –x

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Sinais das coordenadas por quadrante

| Quadrante | x (abscissa) | y (ordenada) | Exemplo |
|-----------|-------------|-------------|---------|
| **1º** | + | + | (3, 5) |
| **2º** | – | + | (–4, 2) |
| **3º** | – | – | (–1, –7) |
| **4º** | + | – | (6, –3) |
| Eixo x | qualquer | **0** | (5, 0) |
| Eixo y | **0** | qualquer | (0, –2) |
| Origem | **0** | **0** | (0, 0) |

### Comparativo dos 3 casos de distância

| Caso | Condição | Fórmula | Intuição |
|------|----------|---------|----------|
| 1 | y_A = y_B | $$\|x_B - x_A\|$$ | segmento horizontal |
| 2 | x_A = x_B | $$\|y_B - y_A\|$$ | segmento vertical |
| 3 | geral | $$\sqrt{(x_B-x_A)^2+(y_B-y_A)^2}$$ | hipotenusa do triângulo retângulo |

### Distâncias de referência do capítulo (AT-9)

| Pontos | Cálculo | Resultado |
|--------|---------|-----------|
| A(1,8) e B(4,12) | √[(4–1)²+(12–8)²] = √[9+16] | **5** |
| A(–1,3) e B(–9,18) | √[(–9+1)²+(18–3)²] = √[64+225] | **17** |
| A(4,–7) e B(–16,–22) | √[(–16–4)²+(–22+7)²] = √[400+225] | **25** |
| A(2,–3) e B(7,–15) | √[(7–2)²+(–15+3)²] = √[25+144] | **13** |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Elevar ao quadrado elimina a raiz**
Em problemas de ponto equidistante, impor d_PA = d_PB e elevar **ambos os lados** ao quadrado elimina a raiz e transforma em equação linear. Não esquecer de elevar os dois lados — elevar só um lado é erro de álgebra.

💡 **Dica 2 — Ponto no eixo x tem y = 0; ponto no eixo y tem x = 0**
Antes de montar qualquer equação, substituir imediatamente. Se o enunciado diz "P pertence ao eixo Ox", escrever P(x, 0) logo de início. Esse passo simples evita sistemas de 2 incógnitas desnecessários.

💡 **Dica 3 — Verificar tipo de triângulo com distâncias**
Para classificar um triângulo pelos lados: calcular os 3 lados com a fórmula, depois comparar. Equilátero: todos iguais. Isósceles: dois iguais. Retângulo: a² + b² = c² (onde c é o maior). Verificar o critério de Pitágoras separa retângulo de isósceles.

💡 **Dica 4 — Baricentro: sempre dividir por 3**
O baricentro usa a média de 3 pontos → divisor é 3. O ponto médio usa 2 pontos → divisor é 2. Em prova, ler bem se pedem baricentro ou ponto médio — são coisas diferentes.

💡 **Dica 5 — A fórmula geral serve para todos os casos**
Não é necessário memorizar as fórmulas dos casos 1 e 2 separadamente. A fórmula geral d = √[(Δx)²+(Δy)²] funciona sempre: quando Δx = 0 ou Δy = 0, o termo vira zero e some.

💡 **Dica 6 — Distância geodésica ≠ distância cartesiana**
Na superfície da Terra, a menor distância entre duas cidades não é uma reta, mas um arco de esfera (distância geodésica). A fórmula do plano cartesiano vale para superfícies planas — aplicar a cidades em países diferentes introduz erro.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

#### Bloco A — Lacunas de dados

| Seção | Campo | Motivo | Ação |
|-------|-------|--------|------|
| AT-8 (atividade intercalada) | Enunciado completo | Imagem parcialmente ilegível (torres de telecomunicações) | Verificar pág. 347 |
| AT-IC-2 | Coordenadas exatas dos pontos no gráfico | Pontos coloridos no gráfico sem rótulo legível | Verificar pág. 341 |
| AT-7 (atividades vestibulares) | Gráfico com triângulo | Figura pequena e parcialmente ilegível | Verificar pág. 354 |
| AT-3, AT-4, AT-5 (vestibulares) | Enunciados e gabaritos | Imagens com texto pequeno | Verificar págs. 353–354 |
| Desafio | Enunciado completo (incenter G e circumcenter P) | Coordenadas fracionárias parcialmente ilegíveis | Verificar pág. 352 |

#### Bloco B — Alertas

```
✅ RESOLVIDO — AT-15 (UPF-RS): bissetriz confirmada como 1º quadrante
- OB é bissetriz do 1º quadrante (reta y = x, x > 0) — confirmado por recaptura
- Gabarito confirmado: b) A(–2, 2) e B(5, 5)
- Resolução: A(–a,a); B(b,b); b=a+3; área=a(a+3)=10 → a=2
```

```
✅ RESOLVIDO — AT-11 EEAR-SP (pág. 349): gabarito d) 10 confirmado
- Alternativas confirmadas: a)√14  b)3√2  c)3√7  d)10
- Gabarito: d) 10 — cálculo: √[(8–2)²+(0–8)²] = √100 = 10
```

```
✅ RESOLVIDO — AT-16 (UEM-PR): coordenadas confirmadas por recaptura
- Coordenadas corretas: A(1/2, 0) e B(5/2, 3/2)
- AB = 5/2
- Item 01 C(5, 3/2): BC=AB=5/2 → isósceles → VERDADEIRO
- Item 02 C(5/2,–1): AC=√5≠5/2 → não equilátero → FALSO
- Item 04 C(1/2,3/2): AC=3/2, BC=2; AC²+BC²=AB² → retângulo → VERDADEIRO
- Item 08 C(1/2,9/2): área=9/2≠3 → FALSO
- Item 16 C(1/2,3/2): perímetro=3/2+2+5/2=6 → VERDADEIRO
- Soma: 01+04+16 = 21
```

```
✅ RESOLVIDO — AT-9: era IFSC (Oktoberfest), não UPF-RS
- A questão AT-9 é (IFSC) sobre deslocamento A→B→C→D no pavilhão da Oktoberfest
- A questão UPF-RS (bissetrizes) é AT-15
```

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO

#### Bloco 1 — Conceitos e Definições

- **Plano cartesiano**
  - Formado por: `______` (dois eixos perpendiculares — x e y — cruzando na origem)
  - Quadrantes: `______` (4 regiões; numerados 1º a 4º no sentido anti-horário)
  - Representação de ponto: `______` (par ordenado (abscissa, ordenada))

- **Distância entre dois pontos**
  - Fórmula geral: `______` (d_AB = √[(x_B–x_A)²+(y_B–y_A)²])
  - Origem do método: `______` (Teorema de Pitágoras aplicado ao triângulo retângulo auxiliar)
  - Ponto equidistante em eixo: `______` (substituir y=0 ou x=0, igualar distâncias, resolver)

- **Baricentro**
  - Definição: `______` (ponto de interseção das medianas do triângulo)
  - Fórmula: `______` (média aritmética das coordenadas dos vértices)

#### Bloco 2 — Fórmulas e Propriedades

- **Distância geral**
  - Expressão: `______` (√[(x_B–x_A)²+(y_B–y_A)²])
  - Origem: `______` (Teorema de Pitágoras)

- **Baricentro G de triângulo ABC**
  - x_G: `______` ((x_A+x_B+x_C)/3)
  - y_G: `______` ((y_A+y_B+y_C)/3)
  - Divisor: `______` (3 — média de 3 pontos; não confundir com ponto médio que divide por 2)

#### Bloco 3 — Lacunas para Warm-Up

1. Um ponto no 3º quadrante tem abscissa `______` e ordenada `______`.
*(resposta: negativa; negativa)*

2. O par ordenado de um ponto no eixo y tem a forma `______`.
*(resposta: (0, y) — abscissa é sempre zero)*

3. A fórmula da distância entre A(x_A, y_A) e B(x_B, y_B) é `______`.
*(resposta: d_AB = √[(x_B–x_A)²+(y_B–y_A)²])*

4. A distância entre M(2, 5) e T(5, –1) é `______`.
*(resposta: 3√5 — √[9+36] = √45 = 3√5)*

5. Para encontrar P no eixo Ox equidistante de dois pontos, começo escrevendo P = `______`.
*(resposta: P = (x, 0) — ponto no eixo x tem ordenada zero)*

6. O baricentro de um triângulo com vértices A(1,1), B(3,–1), C(5,3) tem coordenadas `______`.
*(resposta: (3, 1) — x_G = 9/3 = 3; y_G = 3/3 = 1)*

7. A distância entre A(4,–7) e B(–16,–22) é `______`.
*(resposta: 25 — √[400+225] = √625 = 25)*

8. Um ponto no eixo das abscissas tem `______` igual a zero.
*(resposta: ordenada)*

#### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Plano cartesiano | `______` → *2 eixos perpendiculares (x e y) dividindo o plano em 4 quadrantes* |
| Par ordenado | `______` → *(abscissa, ordenada) — nessa ordem* |
| 1º quadrante | `______` → *x > 0 e y > 0* |
| 2º quadrante | `______` → *x < 0 e y > 0* |
| Distância geral | `______` → *√[(x_B–x_A)²+(y_B–y_A)²]* |
| Origem da fórmula | `______` → *Teorema de Pitágoras no triângulo retângulo auxiliar* |
| Ponto equidistante no eixo x | `______` → *substituir y=0; igualar d_PA = d_PB; resolver* |
| Baricentro — fórmula | `______` → *média das coordenadas dos 3 vértices (dividir por 3)* |
| Pegadinha baricentro | `______` → *divisor é 3 (média de 3 pontos), não 2 como no ponto médio* |
| Ponto no eixo y | `______` → *x = 0; forma P(0, y)* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

Imagem disponível: `Pietro/Raw/Matematica/mat-1-13-sintese.png`

A síntese (pág. 359) apresenta mapa conceitual com os ramos:
- **Distância entre dois pontos:** fórmula d_AB = √[(x_B–x_A)²+(y_B–y_A)²] com diagrama do triângulo retângulo auxiliar
- **Introdução à Geometria Analítica** → **Plano cartesiano** como nó central
  - Ramo 1: sistema de dois eixos perpendiculares, 4 quadrantes
  - Ramo 2: localização por par ordenado (abscissa, ordenada)
  - Ramo 3: sinais das coordenadas por quadrante (1º: +,+; 2º: –,+; 3º: –,–; 4º: +,–)

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| IC-1 | Localizar A(12,10), B(2,4), ..., L(14,0) no plano | Const | F | IC | plotagem | — |
| IC-2 | Dar coordenadas de pontos no gráfico (pág. 341) | Cal | F | IC | A(9,4) B(4,3) C(–5,4) D(–3,8) E(–10,–4) F(–6,–6) G(4,–6) H(8,–6) I(6,7) J(–7,1) K(–1,–6) L(10,1) | ✅ confirmado |
| IC-3 | Concluir sobre sinais por quadrante | Dis | F | IC | 1º:+,+; 2º:–,+; 3º:–,–; 4º:+,– | — |
| IC-4 | Pontos no eixo das ordenadas: o que têm em comum | Dis | F | IC | abscissa = 0 | — |
| IC-5 | Pontos no eixo das abscissas: o que têm em comum | Dis | F | IC | ordenada = 0 | — |
| IC-6 | (Saresp) Triângulo MNP com M(–2,3), N(0,–1), P(2,0) | MC | F | IC | **a)** — M no 2º quad., N no eixo y abaixo de O, P no eixo x positivo | ✅ confirmado |
| IC-9a | Distância A(1,8) e B(4,12) | Cal | F | IC | 5 | — |
| IC-9b | Distância A(–1,3) e B(–9,18) | Cal | F | IC | 17 | — |
| IC-9c | Distância A(4,–7) e B(–16,–22) | Cal | M | IC | 25 | — |
| IC-9d | Distância A(2,–3) e B(7,–15) | Cal | M | IC | 13 | — |
| IC-10 | Triângulo ABC: A simétrico de B(5,4) pelo eixo y; C simétrico de B pela origem; área? | Cal | M | IC | A=(–5,4); C=(–5,–4); área=40 u² | — |
| IC-11 | (EEAR-SP) A(2,8) e B(8,0): distância | MC | F | IC | **d) 10** (a)√14 b)3√2 c)3√7 d)10) | ✅ confirmado |
| IC-12 | Perímetro do triângulo R(0,2), S(3,5), T(9,–1) | Cal | M | IC | 9√2 + 3√10 | — |
| IC-13 | Ponto P no eixo x equidistante de A(0,6) e B(5,–6) | Cal | M | IC | P = (5/2, 0) | — |
| IC-14 | Ponto P no eixo y equidistante de A(–12,8) e B(5,1) | Cal | M | IC | calcular com livro | — |
| IC-15 | (PUC-Rio) A(–1,0), B(1,0), C(x,y) equilátero: AC = ? | MC | M | IC | **b) 2** | — |
| AT-1 | (Enem) Formigas: 4 km/h horizontal e 3 km/h vertical, após 2h | MC | F | AT | **a) (8,0) e (0,6)** | ✅ confirmado |
| AT-2 | (Feevale-RS) Praça A(–2,1) e livraria B(4,2) — distância em km | MC | F | AT | **c) 6 km** (√37≈6,08) | ✅ confirmado |
| AT-3 | (banca ilegível — pág. 353/354) | MC | — | AT | verificar no livro | ⚠️ ilegível |
| AT-4 | (PPY) Candy Crush — distância entre peças especiais no plano | Cal | F | AT | verificar no livro | ⚠️ figura |
| AT-5 | (OPP-RS) Perímetro de polígono com vértices no plano | Cal | M | AT | verificar no livro | ⚠️ figura |
| AT-6 | (CPS-SP 2018) Ilhas A(2,3), B(18,15), C(18,3) — tan(BAC) | MC | M | AT | **b) 3/4** (BC=12, AC=16) | ✅ confirmado |
| AT-7 | (Enem) Terreno escala 1:500; vértices (1,1)(9,1)(9,4)(7,6)(1,6) | MC | M | AT | **c) 124 m** | ✅ confirmado |
| AT-8 | (Unicamp-SP) Catedral(1,1), Prefeitura(3,1), Câmara(5,3); d=500m | MC | M | AT | **b) 500√5 m** | ✅ confirmado |
| AT-9 | (IFSC) Oktoberfest A(5,5)→B(15,10)→C(0,30)→D(20,40) | MC | M | AT | **a) 5(3√5+5) m** | ✅ confirmado |
| AT-10 | Triângulo equilátero A(1,2), B(7,2), C — medir lado BC | Cal | F | AT | **BC = 6** (AB=6, equilátero) | ✅ confirmado |
| AT-11 | d(A(y,–1), B(5,3)) = 5; valor de y | MC | M | AT | **c) 2 ou 8** | — |
| AT-12 | Triângulo (3,3), (3,–3), (–5,0): mostrar retângulo | Dis | M | AT | verificar catetos e hipotenusa | — |
| AT-13 | (EEAR-SP) Baricentro de A(1,1), B(3,–1), C(5,3) | MC | F | AT | **d) (3, 1)** | — |
| AT-14 | (Unesp) Triângulo P(0,0), Q(6,0), R(3,3): tipo | MC | M | AT | **b) isósceles, não equilátero** | — |
| AT-15 | (UPF-RS) Triângulo AOB; OB bissetriz do 1º quad.; área=10 | MC | D | AT | **b) A(–2,2) e B(5,5)** | ✅ confirmado |
| AT-16 | (UEM-PR) A(1/2,0) e B(5/2,3/2) — soma de corretas | Soma | D | AT | **Soma = 21** (01+04+16) | ✅ confirmado |

**Resolução IC-10:** A é simétrico de B(5,4) pelo eixo y → A = (–5, 4). C é simétrico de B pela origem → C = (–5, –4). Vértices: A(–5,4), B(5,4), C(–5,–4). AB = 10 (horizontal); AC = 8 (vertical). Área = (1/2)×10×8 = **40 u²**.

**Resolução AT-11:** (y–5)² + (–1–3)² = 25 → (y–5)² + 16 = 25 → (y–5)² = 9 → y–5 = ±3 → y = 8 ou y = 2.

**Resolução AT-14:** PQ = 6; PR = √[9+9] = 3√2; QR = √[9+9] = 3√2. PR = QR e PQ ≠ PR → isósceles, não equilátero.

**Resolução AT-15:** A(–a, a) na bissetriz do 2º quad.; B(b, b) na bissetriz do 1º quad.; b = a+3; área = a(a+3) = 10 → a²+3a–10 = 0 → a = 2 → A(–2, 2) e B(5, 5).

---

### Bloco B — Questões modelo originais

**QM-1** · MC · fácil · inspirada em: IC-9

Calcule a distância entre os pontos indicados:

a) A(0, 0) e B(3, 4) &nbsp;&nbsp; b) C(–2, 1) e D(2, 4) &nbsp;&nbsp; c) E(1, –3) e F(1, 5) &nbsp;&nbsp; d) G(–3, –3) e H(6, 9)

✅ Gabarito: **a) 5 · b) 5 · c) 8 · d) 15**
📝 Resolução:
a) √[9+16] = 5
b) √[16+9] = 5
c) mesma abscissa → |5–(–3)| = 8
d) √[81+144] = √225 = 15
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · MC · médio · inspirada em: AT-14 (Unesp)

Os vértices de um triângulo são P(0, 0), Q(4, 0) e R(2, 2√3). Esse triângulo é:

a) ( ) escaleno &nbsp; b) ( ) isósceles, mas não equilátero &nbsp; c) ( ) equilátero &nbsp; d) ( ) retângulo &nbsp; e) ( ) obtusângulo

✅ Gabarito: **c) equilátero**
📝 Resolução: PQ = 4; PR = √[4+12] = √16 = 4; QR = √[4+12] = 4. Os três lados são iguais → equilátero.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-3** · Cal · médio · inspirada em: IC-13

Determine o ponto P pertencente ao eixo das ordenadas equidistante de A(3, 7) e B(–5, 1).

✅ Gabarito: **P = (0, 4)**
📝 Resolução: P = (0, y). d_PA = d_PB:
9 + (y–7)² = 25 + (y–1)²
9 + y²–14y+49 = 25 + y²–2y+1
58 – 14y = 26 – 2y
32 = 12y
y = 8/3... 

Verificando: 9+(8/3–7)² = 9+(–13/3)² = 9+169/9 = 81/9+169/9 = 250/9; 25+(8/3–1)² = 25+(5/3)² = 25+25/9 = 225/9+25/9 = 250/9 ✓ → **P = (0, 8/3)**

*(Nota: o gabarito acima continha erro — a resposta correta é P = (0, 8/3) ≈ (0, 2,67))*
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · Cal · difícil · inspirada em: IC-10 / AT-15

Um triângulo isósceles tem base AB com A(–3, 0) e B(3, 0), e o vértice C(x, y) sobre o eixo y com y > 0. Sabendo que a área do triângulo é 18 u², determine as coordenadas de C e o comprimento do lado AC.

✅ Gabarito: **C = (0, 6); AC = 3√5**
📝 Resolução: Base AB = 6 (distância horizontal). Área = (1/2)×base×altura = (1/2)×6×y = 18 → y = 6. Portanto C = (0, 6).
AC = √[(0–(–3))²+(6–0)²] = √[9+36] = √45 = 3√5.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-5** · Dis · médio-difícil · inspirada em: AT-12 / IC-10

Mostre que o triângulo de vértices A(1, 2), B(4, 6) e C(8, 3) é retângulo e calcule sua área.

✅ Gabarito: **retângulo em B; área = 12,5 u²**
📝 Resolução:
AB = √[9+16] = √25 = 5
BC = √[16+9] = √25 = 5
AC = √[49+1] = √50 = 5√2

Verificar Pitágoras: AB² + BC² = 25 + 25 = 50 = AC² ✓ → retângulo em B.
Área = (1/2)×AB×BC = (1/2)×5×5 = **12,5 u²**
⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: plano_cartesiano
Plano cartesiano completo com quadrantes, sinais e representação de ponto.

```svg
<svg width="100%" viewBox="0 0 680 340" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat13a" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Title -->
<rect x="200" y="8" width="280" height="30" rx="6" class="c-purple"/>
<text x="340" y="23" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Plano Cartesiano</text>

<!-- Quadrant boxes -->
<!-- 2nd quadrant (top-left) -->
<rect x="15" y="50" width="195" height="120" rx="8" class="c-teal"/>
<text x="112" y="80" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">2o quadrante</text>
<text x="112" y="102" class="ts" text-anchor="middle" fill="var(--on-accent)">x negativo (-)</text>
<text x="112" y="120" class="ts" text-anchor="middle" fill="var(--on-accent)">y positivo (+)</text>
<text x="112" y="138" class="ts" text-anchor="middle" fill="var(--on-accent)">Exemplo: (-4, 2)</text>
<text x="112" y="158" class="ts" text-anchor="middle" fill="var(--on-accent)">(-  ,  +)</text>

<!-- 1st quadrant (top-right) -->
<rect x="225" y="50" width="195" height="120" rx="8" class="c-teal"/>
<text x="322" y="80" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">1o quadrante</text>
<text x="322" y="102" class="ts" text-anchor="middle" fill="var(--on-accent)">x positivo (+)</text>
<text x="322" y="120" class="ts" text-anchor="middle" fill="var(--on-accent)">y positivo (+)</text>
<text x="322" y="138" class="ts" text-anchor="middle" fill="var(--on-accent)">Exemplo: (3, 5)</text>
<text x="322" y="158" class="ts" text-anchor="middle" fill="var(--on-accent)">(+  ,  +)</text>

<!-- 3rd quadrant (bottom-left) -->
<rect x="15" y="185" width="195" height="120" rx="8" class="c-coral"/>
<text x="112" y="215" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">3o quadrante</text>
<text x="112" y="237" class="ts" text-anchor="middle" fill="var(--on-accent)">x negativo (-)</text>
<text x="112" y="255" class="ts" text-anchor="middle" fill="var(--on-accent)">y negativo (-)</text>
<text x="112" y="273" class="ts" text-anchor="middle" fill="var(--on-accent)">Exemplo: (-1, -7)</text>
<text x="112" y="293" class="ts" text-anchor="middle" fill="var(--on-accent)">(-  ,  -)</text>

<!-- 4th quadrant (bottom-right) -->
<rect x="225" y="185" width="195" height="120" rx="8" class="c-amber"/>
<text x="322" y="215" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">4o quadrante</text>
<text x="322" y="237" class="ts" text-anchor="middle" fill="var(--on-accent)">x positivo (+)</text>
<text x="322" y="255" class="ts" text-anchor="middle" fill="var(--on-accent)">y negativo (-)</text>
<text x="322" y="273" class="ts" text-anchor="middle" fill="var(--on-accent)">Exemplo: (6, -3)</text>
<text x="322" y="293" class="ts" text-anchor="middle" fill="var(--on-accent)">(+  ,  -)</text>

<!-- Right info: axes -->
<rect x="440" y="50" width="225" height="255" rx="8" class="c-purple"/>
<text x="552" y="72" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Casos especiais</text>
<text x="552" y="96" class="ts" text-anchor="middle" fill="var(--on-accent)">Eixo x (abscissas):</text>
<text x="552" y="114" class="ts" text-anchor="middle" fill="var(--on-accent)">y = 0  forma: P(x, 0)</text>
<text x="552" y="140" class="ts" text-anchor="middle" fill="var(--on-accent)">Eixo y (ordenadas):</text>
<text x="552" y="158" class="ts" text-anchor="middle" fill="var(--on-accent)">x = 0  forma: P(0, y)</text>
<text x="552" y="184" class="ts" text-anchor="middle" fill="var(--on-accent)">Origem:</text>
<text x="552" y="202" class="ts" text-anchor="middle" fill="var(--on-accent)">O(0, 0)</text>
<text x="552" y="228" class="ts" text-anchor="middle" fill="var(--on-accent)">Par ordenado:</text>
<text x="552" y="246" class="ts" text-anchor="middle" fill="var(--on-accent)">(abscissa, ordenada)</text>
<text x="552" y="270" class="ts" text-anchor="middle" fill="var(--on-accent)">sempre nessa ordem</text>
<text x="552" y="291" class="ts" text-anchor="middle" fill="var(--on-accent)">(3, 5) diferente de (5, 3)</text>
</svg>
```

---

### DIAGRAMA: distancia_casos
Três casos de distância e derivação da fórmula geral pelo Teorema de Pitágoras.

```svg
<svg width="100%" viewBox="0 0 680 330" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat13b" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Title -->
<rect x="180" y="8" width="320" height="30" rx="6" class="c-purple"/>
<text x="340" y="23" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Distancia Entre Dois Pontos</text>

<!-- Case 1: same y -->
<rect x="8" y="52" width="198" height="140" rx="8" class="c-teal"/>
<text x="107" y="72" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Caso 1: mesma ordenada</text>
<text x="107" y="92" class="ts" text-anchor="middle" fill="var(--on-accent)">y_A = y_B</text>
<!-- Horizontal line -->
<line x1="28" y1="125" x2="186" y2="125" stroke="white" stroke-width="2"/>
<circle cx="28" cy="125" r="4" fill="white"/>
<circle cx="186" cy="125" r="4" fill="white"/>
<text x="28" y="143" class="ts" text-anchor="middle" fill="var(--on-accent)">A</text>
<text x="186" y="143" class="ts" text-anchor="middle" fill="var(--on-accent)">B</text>
<text x="107" y="162" class="ts" text-anchor="middle" fill="var(--on-accent)">d = |x_B - x_A|</text>
<text x="107" y="180" class="ts" text-anchor="middle" fill="var(--on-accent)">distancia horizontal</text>

<!-- Case 2: same x -->
<rect x="242" y="52" width="196" height="140" rx="8" class="c-amber"/>
<text x="340" y="72" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Caso 2: mesma abscissa</text>
<text x="340" y="92" class="ts" text-anchor="middle" fill="var(--on-accent)">x_A = x_B</text>
<!-- Vertical line -->
<line x1="340" y1="105" x2="340" y2="163" stroke="white" stroke-width="2"/>
<circle cx="340" cy="105" r="4" fill="white"/>
<circle cx="340" cy="163" r="4" fill="white"/>
<text x="358" y="109" class="ts" text-anchor="start" fill="var(--on-accent)">B</text>
<text x="358" y="167" class="ts" text-anchor="start" fill="var(--on-accent)">A</text>
<text x="340" y="185" class="ts" text-anchor="middle" fill="var(--on-accent)">d = |y_B - y_A|</text>
<text x="340" y="183" class="ts" text-anchor="middle" fill="var(--on-accent)">distancia vertical</text>

<!-- Case 3: general -->
<rect x="474" y="52" width="198" height="140" rx="8" class="c-coral"/>
<text x="573" y="68" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Caso 3: geral</text>
<text x="573" y="86" class="ts" text-anchor="middle" fill="var(--on-accent)">x_A dif. x_B e y_A dif. y_B</text>
<!-- Triangle -->
<circle cx="504" cy="160" r="4" fill="white"/>
<circle cx="642" cy="100" r="4" fill="white"/>
<circle cx="642" cy="160" r="4" fill="white"/>
<line x1="504" y1="160" x2="642" y2="100" stroke="white" stroke-width="2"/>
<line x1="504" y1="160" x2="642" y2="160" stroke="white" stroke-width="1.5" stroke-dasharray="4,3"/>
<line x1="642" y1="100" x2="642" y2="160" stroke="white" stroke-width="1.5" stroke-dasharray="4,3"/>
<text x="490" y="164" class="ts" text-anchor="middle" fill="var(--on-accent)">A</text>
<text x="656" y="104" class="ts" text-anchor="start" fill="var(--on-accent)">B</text>
<text x="656" y="164" class="ts" text-anchor="start" fill="var(--on-accent)">C</text>
<text x="563" y="117" class="ts" text-anchor="middle" fill="var(--on-accent)">d_AB</text>
<text x="573" y="183" class="ts" text-anchor="middle" fill="var(--on-accent)">Pitag: d2 = AC2 + CB2</text>

<!-- General formula -->
<rect x="8" y="210" width="664" height="52" rx="8" class="c-purple"/>
<text x="340" y="228" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Formula Geral (funciona para todos os casos):</text>
<text x="340" y="250" class="th" text-anchor="middle" fill="var(--on-accent)">d_AB = raiz[ (x_B - x_A)2 + (y_B - y_A)2 ]</text>

<!-- Example -->
<rect x="8" y="276" width="664" height="44" rx="8" class="c-gray"/>
<text x="340" y="294" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Exemplo: M(2, 5) e T(5, -1)</text>
<text x="340" y="312" class="ts" text-anchor="middle" fill="var(--on-accent)">d = raiz[(5-2)2 + (-1-5)2] = raiz[9+36] = raiz[45] = 3 raiz[5]</text>
</svg>
```

---

### DIAGRAMA: baricentro
Baricentro de triângulo: definição geométrica e fórmula analítica.

```svg
<svg width="100%" viewBox="0 0 680 280" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat13c" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Title -->
<rect x="190" y="8" width="300" height="30" rx="6" class="c-purple"/>
<text x="340" y="23" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Baricentro de um Triangulo</text>

<!-- Triangle visual (left side) -->
<rect x="8" y="52" width="290" height="210" rx="8" class="c-gray"/>
<!-- Triangle vertices: A(60,230), B(200,230), C(140,90) -->
<line x1="68" y1="240" x2="208" y2="240" stroke="white" stroke-width="2"/>
<line x1="68" y1="240" x2="150" y2="100" stroke="white" stroke-width="2"/>
<line x1="208" y1="240" x2="150" y2="100" stroke="white" stroke-width="2"/>
<!-- Midpoints for medians: MA_mid=(179,170), MB_mid=(109,170), MC_mid=(138,240) -->
<!-- Barycenter G approx at (142, 193) -->
<circle cx="68" cy="240" r="4" fill="white"/>
<circle cx="208" cy="240" r="4" fill="white"/>
<circle cx="150" cy="100" r="4" fill="white"/>
<!-- Midpoints -->
<circle cx="179" cy="170" r="3" fill="var(--c-amber)"/>
<circle cx="109" cy="170" r="3" fill="var(--c-amber)"/>
<circle cx="138" cy="240" r="3" fill="var(--c-amber)"/>
<!-- Medians -->
<line x1="68" y1="240" x2="179" y2="170" stroke="var(--c-teal)" stroke-width="1.5" stroke-dasharray="5,3"/>
<line x1="208" y1="240" x2="109" y2="170" stroke="var(--c-teal)" stroke-width="1.5" stroke-dasharray="5,3"/>
<line x1="150" y1="100" x2="138" y2="240" stroke="var(--c-teal)" stroke-width="1.5" stroke-dasharray="5,3"/>
<!-- Barycenter G -->
<circle cx="142" cy="203" r="6" fill="var(--c-purple)"/>
<text x="155" y="207" class="ts" text-anchor="start" fill="var(--on-accent)">G</text>
<!-- Labels -->
<text x="55" y="258" class="ts" text-anchor="middle" fill="var(--on-accent)">A</text>
<text x="220" y="258" class="ts" text-anchor="middle" fill="var(--on-accent)">B</text>
<text x="150" y="88" class="ts" text-anchor="middle" fill="var(--on-accent)">C</text>
<text x="153" y="73" class="ts" text-anchor="middle" fill="var(--on-accent)">medianas</text>

<!-- Formula side -->
<rect x="318" y="52" width="354" height="210" rx="8" class="c-purple"/>
<text x="495" y="76" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Formula do Baricentro G</text>

<text x="342" y="108" class="ts" text-anchor="start" fill="var(--on-accent)">x_G = (x_A + x_B + x_C) / 3</text>
<text x="342" y="130" class="ts" text-anchor="start" fill="var(--on-accent)">y_G = (y_A + y_B + y_C) / 3</text>

<text x="495" y="158" class="ts" text-anchor="middle" fill="var(--on-accent)">Media das coordenadas</text>
<text x="495" y="176" class="ts" text-anchor="middle" fill="var(--on-accent)">dos 3 vertices</text>

<text x="342" y="208" class="ts" text-anchor="start" fill="var(--on-accent)">Exemplo: A(1,1), B(3,-1), C(5,3)</text>
<text x="342" y="228" class="ts" text-anchor="start" fill="var(--on-accent)">G = ((1+3+5)/3, (1-1+3)/3)</text>
<text x="342" y="248" class="ts" text-anchor="start" fill="var(--on-accent)">G = (3, 1)</text>
</svg>
```
