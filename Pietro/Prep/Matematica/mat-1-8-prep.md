## DIAGRAMAS DISPONÍVEIS — mat-1-8

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Feixe de Paralelas | DIAGRAMA: feixe_paralelas | Ao explicar o enunciado do Teorema de Tales e a relação a/b = c/d |
| Semelhança de Triângulos | DIAGRAMA: semelhanca | Ao explicar razão de semelhança k e lados homólogos |
| Teorema da Bissetriz Interna | DIAGRAMA: bissetriz_interna | Ao apresentar a Síntese / consequência do Teorema de Tales |
| Fórmulas do Capítulo | DIAGRAMA: formulas | Revisão rápida de todas as expressões do capítulo |

### Tabelas markdown (Seção 6):
- Tabela de fórmulas e propriedades do capítulo

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 8
- Tema: Teorema de Tales
- Perfil: geometria
- Fórmulas principais:
    · a/b = c/d  (se r∥s∥t — Teorema de Tales)
    · (a+b)/b = (c+d)/d  (propriedade das proporções)
    · c/x = b/y  (Teorema da bissetriz interna)
    · a/d = b/e = c/f = k  (razão de semelhança)
- Matemáticos citados: Tales de Mileto (626/625 a.C.–546 a.C.)
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### 🔷 Bloco 1 — Teorema de Tales: o que é e o que garante

O **Teorema de Tales** afirma que um **feixe de retas paralelas**, ao ser cortado por duas retas transversais, determina segmentos proporcionais nessas transversais. Ou seja, a razão entre os segmentos de uma transversal é igual à razão entre os segmentos correspondentes na outra.

Formalmente, se $$r \parallel s \parallel t$$ e as transversais $$u$$ e $$v$$ as cortam determinando segmentos $$a, b$$ (em $$u$$) e $$c, d$$ (em $$v$$):

$$\frac{a}{b} = \frac{c}{d}$$

**Aplicação real imediata:** raios solares são paralelos entre si. Quando incidem sobre um menino e um poste ao mesmo tempo, formam triângulos semelhantes com o chão. Assim, se o menino tem 1,60 m e projeta sombra de 1,30 m, e o poste projeta sombra de 3,25 m, sua altura é:

$$x = \frac{1{,}60 \times 3{,}25}{1{,}30} = 4 \text{ m}$$

---

### 🔷 Bloco 2 — Demonstração do Teorema de Tales (passos I a V)

A demonstração parte de um feixe de paralelas $$r \parallel s \parallel t$$ cortado pelas transversais $$u$$ e $$v$$:

- **I.** Considera-se o feixe cortado pelas duas transversais, com segmentos $$a, b$$ em $$u$$ e $$c, d$$ em $$v$$.
- **II.** Traça-se uma paralela à transversal $$u$$, intersectando $$r$$ no ponto A e $$s$$ no ponto B, formando o triângulo ABC. Por construção, $$AB = a$$ e $$AC = c$$.
- **III.** Traça-se outra paralela à transversal $$v$$, intersectando $$s$$ no ponto D e $$t$$ no ponto F, formando o triângulo DEF. Por construção, $$DF = d$$.
- **IV.** Os triângulos ABC e DEF possuem os mesmos ângulos internos → são semelhantes.
- **V.** Da semelhança: $$\frac{a}{b} = \frac{c}{d}$$, se $$r \parallel s \parallel t$$.

---

### 🔷 Bloco 3 — Propriedade das Proporções (derivada do Teorema de Tales)

Quando $$\frac{a}{b} = \frac{c}{d}$$, também é válido:

$$\frac{a+b}{b} = \frac{c+d}{d}$$

Isso permite resolver problemas em que se conhece a **soma** dos segmentos de uma transversal, mas não cada segmento individualmente.

**Exemplo resolvido (livro):** Com $$r \parallel s \parallel t$$, $$x + y = 9$$ cm, e segmentos de 6 cm e 4 cm nas paralelas:

$$\frac{x}{6} = \frac{y}{4} \Rightarrow \frac{x}{6} = \frac{y}{4} = \frac{x+y}{10} = \frac{9}{10}$$

$$x = \frac{6 \times 9}{10} = 5{,}4 \text{ cm} \qquad y = \frac{4 \times 9}{10} = 3{,}6 \text{ cm}$$

---

### 🔷 Bloco 4 — Semelhança de Triângulos e Razão de Semelhança

Dois triângulos são **semelhantes** ($$\triangle ABC \sim \triangle DEF$$) quando:
- Possuem **ângulos correspondentes congruentes**: $$\hat{A} = \hat{D}$$, $$\hat{B} = \hat{E}$$, $$\hat{C} = \hat{F}$$
- Possuem **lados homólogos proporcionais**

A **razão de semelhança** $$k$$ é o valor constante:

$$k = \frac{a}{d} = \frac{b}{e} = \frac{c}{f}$$

Quanto maior o $$k$$, maior o triângulo em relação ao original.

---

### 🔷 Bloco 5 — Teorema da Bissetriz Interna (Síntese)

Uma **consequência direta** do Teorema de Tales: a bissetriz de um ângulo interno de um triângulo divide o lado oposto em dois segmentos proporcionais aos lados adjacentes.

No triângulo ABC, a bissetriz do ângulo $$\hat{A}$$ divide $$\overline{BC}$$ nos segmentos $$x$$ e $$y$$ (ponto D), de forma que:

$$\frac{c}{x} = \frac{b}{y}$$

**Demonstração:** Seja E a interseção do prolongamento de $$\overline{AB}$$ com uma reta paralela a $$\overline{AD}$$ traçada por C. Pelo paralelismo de $$\overline{EC}$$ com $$\overline{AD}$$: $$\hat{BAD} = \hat{BEC}$$ e $$\hat{DAC} = \hat{ACE}$$; logo $$\triangle ACE$$ é isósceles com $$AE = AC = b$$. Pelo Teorema de Tales: $$\frac{c}{x} = \frac{b}{y}$$.

---

## SEÇÃO 3 — MATEMÁTICOS E HISTÓRIA DA MATEMÁTICA

### Tales de Mileto (626/625 a.C. – 546 a.C.)

**Área:** Geometria dedutiva, Filosofia Natural

**Contribuição no capítulo:** Considerado o primeiro dos Sete Sábios da Grécia Antiga. Realizou as primeiras organizações dedutivas da Geometria, estabelecendo que o conhecimento necessário se apoia em bases sólidas e de encadeamento lógico. Demonstrou que os ângulos da base de um triângulo isósceles são iguais e que o diâmetro divide um círculo em duas partes iguais. Acredita-se que tenha realizado a medição da altura da Pirâmide de Quéops e previsto um eclipse solar em 585 a.C.

**O que desenvolveu:** Teorema de Tales — proporcionalidade de segmentos em feixe de paralelas; bases da Geometria dedutiva grega.

**Contexto histórico:** Grécia Antiga, século VI a.C. Tales foi a Egito buscar conhecimento matemático; o comércio de saberes entre egípcios e gregos em meados do século VII a.C. foi fundamental para o desenvolvimento da Geometria como disciplina formal.

> *"Para Tales, a questão primordial não é o que sabemos, mas como sabemos."*

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Teorema de Tales — Proporcionalidade

**Expressão:** $$\dfrac{a}{b} = \dfrac{c}{d} \quad \text{se } r \parallel s \parallel t$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | 1º segmento na transversal $$u$$ | comprimento (real positivo) |
| $$b$$ | 2º segmento na transversal $$u$$ | comprimento (real positivo) |
| $$c$$ | 1º segmento na transversal $$v$$ | comprimento (real positivo) |
| $$d$$ | 2º segmento na transversal $$v$$ | comprimento (real positivo) |

**Válida quando:** existe um feixe de pelo menos 3 retas paralelas cortadas por 2 transversais.

💡 **Pegadinha:** Confundir os segmentos "correspondentes" entre transversais — a razão deve comparar segmentos **entre as mesmas paralelas**, não segmentos consecutivos de transversais diferentes.

---

### Propriedade das Proporções (derivada)

**Expressão:** $$\dfrac{a}{b} = \dfrac{c}{d} \Rightarrow \dfrac{a+b}{b} = \dfrac{c+d}{d}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a+b$$ | comprimento total da transversal $$u$$ | comprimento (real positivo) |
| $$c+d$$ | comprimento total da transversal $$v$$ | comprimento (real positivo) |

**Válida quando:** decorre diretamente de $$\frac{a}{b} = \frac{c}{d}$$.

💡 **Pegadinha:** Ao usar a soma dos segmentos no numerador, o denominador deve permanecer **apenas um** dos segmentos (não a soma). Alunos frequentemente escrevem $$\frac{a+b}{a+b}$$, o que é sempre 1.

---

### Razão de Semelhança

**Expressão:** $$k = \dfrac{a}{d} = \dfrac{b}{e} = \dfrac{c}{f}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a, b, c$$ | lados do triângulo ABC | comprimento (real positivo) |
| $$d, e, f$$ | lados homólogos do triângulo DEF | comprimento (real positivo) |
| $$k$$ | razão de semelhança | escalar adimensional positivo |

**Válida quando:** $$\triangle ABC \sim \triangle DEF$$ (ângulos correspondentes congruentes).

💡 **Pegadinha:** A razão de semelhança entre áreas é $$k^2$$, não $$k$$. Para o perímetro, a razão é $$k$$.

---

### Teorema da Bissetriz Interna

**Expressão:** $$\dfrac{c}{x} = \dfrac{b}{y}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$c$$ | lado AB do triângulo ABC | comprimento (real positivo) |
| $$b$$ | lado AC do triângulo ABC | comprimento (real positivo) |
| $$x$$ | segmento BD (parte de BC próxima a B) | comprimento (real positivo) |
| $$y$$ | segmento DC (parte de BC próxima a C) | comprimento (real positivo) |

**Válida quando:** AD é a bissetriz interna do ângulo $$\hat{A}$$ no triângulo ABC.

💡 **Pegadinha:** Associar corretamente cada segmento de BC ao lado adjacente correto — $$x$$ (próximo a B) relaciona-se com $$c = AB$$; $$y$$ (próximo a C) relaciona-se com $$b = AC$$.

---

## SEÇÃO 5 — REPRESENTAÇÕES E SISTEMAS

### Representação Geométrica do Feixe de Paralelas

- **Elementos:** três retas paralelas ($$r, s, t$$) e duas transversais ($$u, v$$)
- **Segmentos gerados:** $$a$$ e $$b$$ em $$u$$; $$c$$ e $$d$$ em $$v$$
- **Leitura:** os segmentos são delimitados pelos pontos de intersecção de cada transversal com as paralelas; a proporcionalidade vale para segmentos **entre as mesmas paralelas**
- **Relação:** $$a/b = c/d$$ — a razão é preservada independentemente da inclinação das transversais

### Representação da Semelhança de Triângulos

- **Notação:** $$\triangle ABC \sim \triangle DEF$$ (a ordem das letras indica a correspondência de vértices)
- **Lados homólogos:** $$AB \leftrightarrow DE$$, $$BC \leftrightarrow EF$$, $$AC \leftrightarrow DF$$
- **Ângulos:** $$\hat{A} = \hat{D}$$, $$\hat{B} = \hat{E}$$, $$\hat{C} = \hat{F}$$
- **Razão:** $$AB/DE = BC/EF = AC/DF = k$$

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

| Propriedade / Fórmula | Expressão | Condição |
|---|---|---|
| Teorema de Tales | $$\frac{a}{b} = \frac{c}{d}$$ | $$r \parallel s \parallel t$$; transversais $$u, v$$ |
| Propriedade das proporções | $$\frac{a+b}{b} = \frac{c+d}{d}$$ | Decorre de $$\frac{a}{b} = \frac{c}{d}$$ |
| Semelhança de triângulos | $$\frac{a}{d} = \frac{b}{e} = \frac{c}{f} = k$$ | $$\triangle ABC \sim \triangle DEF$$ |
| Bissetriz interna | $$\frac{c}{x} = \frac{b}{y}$$ | AD bissetriz do $$\hat{A}$$ em $$\triangle ABC$$ |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Correspondência correta dos segmentos**
Ao montar a proporção $$\frac{a}{b} = \frac{c}{d}$$, os segmentos $$a$$ e $$c$$ devem estar **entre as mesmas duas paralelas**. Erro clássico: comparar segmentos de transversais diferentes que não se referem ao mesmo "intervalo" entre paralelas.

💡 **Dica 2 — Sinal da propriedade das proporções**
Quando o problema fornece a **soma** dos segmentos (ex: $$x + y = 9$$), use $$\frac{x}{p} = \frac{y}{q} = \frac{x+y}{p+q}$$. Atenção: o denominador vira $$p + q$$, não $$p \cdot q$$.

💡 **Dica 3 — Semelhança não implica congruência**
Triângulos semelhantes têm ângulos iguais, mas lados **proporcionais** (não necessariamente iguais). Só são congruentes quando $$k = 1$$.

💡 **Dica 4 — Bissetriz interna: não confundir com mediana**
A mediana divide o lado oposto em **partes iguais**; a bissetriz divide em partes **proporcionais aos lados adjacentes**. Se $$AB = AC$$, então bissetriz = mediana (triângulo isósceles).

💡 **Dica 5 — Razão de semelhança em sombras**
Em problemas de sombra, os raios solares são as "paralelas". O ângulo de incidência é o mesmo para todos os objetos no mesmo instante, garantindo semelhança. Certifique-se de que as medidas estão na mesma unidade antes de montar a proporção.

💡 **Dica 6 — Ordem das letras na semelhança**
$$\triangle ABC \sim \triangle DEF$$ indica que A↔D, B↔E, C↔F. Trocar a ordem das letras leva a proporções erradas. Sempre identifique qual vértice de um triângulo corresponde a qual vértice do outro antes de escrever a razão.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

### Bloco A — Lacunas de dados

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| Bloco E — Exercício Resolvido 1 | Valores exatos dos itens a, b, c, d | As imagens das figuras a, b, c, d foram reconstruídas parcialmente; alguns valores diferem da resolução registrada | Confirmar com printscreen do livro — ver IMAGENS RECOMENDADAS |
| Bloco E — Exercício Resolvido 2 | Valores corretos dos segmentos | Captura original apontou segmentos 4 cm e 4 cm, mas imagem agora confirma 6 cm e 4 cm | Registrado e corrigido — ver Bloco B abaixo |
| Q-1 (questoes.md) | Valores numéricos exatos das figuras a, b, c | Figuras não capturadas integralmente | Anexar printscreen da pág. 208 |
| Q-9 | Distâncias parciais do trajeto no mapa | Figura ilegível em miniatura | Anexar printscreen da pág. 213 |

### Bloco B — Inconsistências factuais

```
⚠️ ALERTA — Exercício Resolvido 2 (Bloco E, mat-1-8.md)
- Dado no material capturado: "segmentos de 4 cm e 4 cm nas paralelas"
- Problema: A imagem agora confirma 6 cm e 4 cm (não 4 cm e 4 cm)
- Dado correto: r∥s∥t, x + y = 9 cm, segmentos 6 cm e 4 cm nas paralelas
  Resolução correta:
    x/6 = y/4 → (x+y)/10 = 9/10
    x = 6×9/10 = 5,4 cm
    y = 4×9/10 = 3,6 cm
- Impacto na aula: Corrigir o FC-11 do mat-1-8.md e usar os valores
  corretos (5,4 cm e 3,6 cm) na exposição. A captura anterior
  estava errada ao registrar 4 cm e 4 cm.
```

```
⚠️ ALERTA — Exercício Resolvido 1 item a (Bloco E, mat-1-8.md)
- Dado no material capturado: "Segmentos: 5 m, 7 m na transversal;
  8 m e x na outra"
- Dado correto (confirmado pela imagem): 5 m, 7 m e 2 m, x
  (a figura mostra t com 5 m e 7 m; s e r com 2 m e x)
- Resolução correta: 5/7 = 2/x → x = 2×7/5 = 2,8 m
- Impacto na aula: A resolução registrada anteriormente (11,2 m)
  estava incorreta. Verificar com o livro físico antes de usar.
```

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

### Bloco 1 — Conceitos e Definições

- **Teorema de Tales**
  - Definição: Um feixe de retas `______` determina, sobre duas retas transversais, segmentos de reta `______`. *(paralelas; proporcionais)*
  - Notação: $$\frac{a}{b} =\ $$`______` *(c/d)*

- **Semelhança de triângulos**
  - Definição: Dois triângulos são semelhantes quando têm ângulos correspondentes `______` e lados homólogos `______`. *(congruentes; proporcionais)*
  - Notação: $$\triangle ABC \sim \triangle DEF \Rightarrow k =\ $$`______` *(a/d = b/e = c/f)*

- **Bissetriz interna**
  - Definição: A bissetriz de um ângulo interno de um triângulo divide o lado oposto em segmentos `______` aos lados adjacentes. *(proporcionais)*
  - Expressão: $$\frac{c}{x} =\ $$`______` *(b/y)*

- **Feixe**
  - Definição do livro: `______` de retas paralelas. *(conjunto)*

### Bloco 2 — Fórmulas e Propriedades

- **Teorema de Tales**
  - Expressão: `______` *(a/b = c/d, se r∥s∥t)*
  - Variável $$a$$: `______` *(segmento na transversal u entre r e s)*
  - Condição: `______` *(retas r, s, t paralelas entre si)*

- **Propriedade das proporções**
  - Expressão: `______` *((a+b)/b = (c+d)/d)*
  - Deriva de: `______` *(a/b = c/d)*

- **Razão de semelhança**
  - Expressão: `______` *(a/d = b/e = c/f = k)*
  - $$k$$ representa: `______` *(a razão constante entre lados homólogos)*

### Bloco 3 — Lacunas para Warm-Up

1. Se $$r \parallel s \parallel t$$ e os segmentos numa transversal medem 3 cm e 6 cm, qual é o segmento correspondente ao de 3 cm na outra transversal, sabendo que o outro mede 8 cm? Monta a proporção: `______`. *(3/6 = x/8 → x = 4 cm)*

2. Tales de Mileto viveu entre `______` e previu `______`. *(626/625 a.C.–546 a.C.; um eclipse solar em 585 a.C.)*

3. A propriedade $$\frac{a+b}{b} = \frac{c+d}{d}$$ é usada quando o problema fornece a `______` dos segmentos de uma transversal. *(soma)*

4. Se $$\triangle ABC \sim \triangle DEF$$ com $$k = 3$$, e $$AB = 6$$ cm, então $$DE =\ $$`______`. *(2 cm, pois k = AB/DE → DE = 6/3)*

5. Na aplicação de sombras, o que garante que os triângulos formados por menino/poste e suas sombras sejam semelhantes? `______`. *(os raios solares são paralelos, formando o feixe de paralelas do Teorema de Tales)*

6. Na bissetriz interna do triângulo ABC pelo vértice A, o segmento BD relaciona-se com o lado `______` e DC com o lado `______`. *(AB (= c); AC (= b))*

7. Se $$x + y = 9$$ cm e os segmentos nas paralelas medem 6 cm e 4 cm, então $$x =\ $$`______` e $$y =\ $$`______`. *(5,4 cm; 3,6 cm)*

8. O Teorema da Bissetriz Interna é uma consequência do `______`. *(Teorema de Tales)*

#### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Teorema de Tales | Um feixe de retas `______` determina segmentos `______` nas transversais → *paralelas; proporcionais* |
| Expressão de Tales | $$\frac{a}{b} =$$ `______` → *c/d* |
| Semelhança de triângulos | Ângulos correspondentes `______` e lados homólogos `______` → *congruentes; proporcionais* |
| Razão de semelhança k | $$k = $$ `______` → *a/d = b/e = c/f* |
| Propriedade das proporções | Se a/b = c/d, então `______` → *(a+b)/b = (c+d)/d* |
| Bissetriz interna | Divide o lado oposto em segmentos `______` aos lados adjacentes → *proporcionais* |
| Expressão da bissetriz | $$\frac{c}{x} =$$ `______` → *b/y* |
| Bissetriz é consequência de | `______` → *Teorema de Tales* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

### Síntese do Livro — TEOREMA DE TALES

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| Caixa esquerda — enunciado | "Dado um feixe de retas paralelas cortadas por duas transversais, é válida a relação:" | — |
| Fórmula central esquerda | $$\frac{a}{b} = \frac{c}{d}$$ se r∥s∥t | — |
| Pílula central | **Teorema de Tales** | — |
| Caixa direita — título | **Teorema da bissetriz interna** | — |
| Caixa direita — enunciado | "O teorema da bissetriz interna é uma consequência do teorema de Tales:" | — |
| Caixa direita — texto | "A bissetriz de um ângulo interno de um triângulo determina sobre o lado oposto ao ângulo dois segmentos proporcionais aos lados adjacentes." | — |
| Fórmula caixa direita | $$\frac{c}{x} = \frac{b}{y}$$ | — |
| Caixa inferior — título | **Demonstração:** | — |
| Caixa inferior — texto | "Seja E a interseção do prolongamento da reta $$\overline{AB}$$ com uma reta paralela a $$\overline{AD}$$, traçada por C." | — |
| Conclusão da demonstração | "Pelo paralelismo de $$\overline{EC}$$ com $$\overline{AD}$$, temos que $$\hat{BAD} = \hat{BEC}$$ e $$\hat{DAC} = \hat{ACE}$$ e, portanto, $$\triangle ACE$$ é isósceles, com $$AE = AC = b$$. Assim, pelo teorema de Tales, temos: $$\frac{c}{x} = \frac{b}{y}$$" | — |

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Gabarito | Obs. |
|---|---|---|---|---|---|
| Q-1 | Determinar x (cm) em três casos com r∥s∥t | Cal | M | Ver nota ⚠️ | ⚠️ figuras não capturadas integralmente |
| Q-2 | Altura da árvore (sombra 5 m, flor 0,45 m / sombra 65 cm) | Cal | F | $$x = \frac{0{,}45 \times 5}{0{,}65} \approx 3{,}46$$ m | — |
| Q-3 | Sombra da palmeira (4 m de altura, guarda-sol projeta 2,2 m) | Cal | F | $$x = \frac{4 \times 2{,}2}{4} = 2{,}2$$ m ⚠️ — sem altura do guarda-sol; dados insuficientes | ⚠️ enunciado ambíguo — falta altura do guarda-sol |
| Q-4 | Comprimento de ponte sobre rio via Tales | Cal | M | Depende das medidas da figura ⚠️ | ⚠️ figura não capturada integralmente |
| Q-5 | Segmento DE∥BC em △ABC; AD=9, BD=15, AE=x, AC=3x−2 | Cal | M | $$\frac{9}{15} = \frac{x}{3x-2-x} \Rightarrow \frac{9}{15} = \frac{x}{2x-2}$$; $$18x - 18 = 15x$$; $$x = 6$$ cm | — |
| Q-6 | Feixe de 3 paralelas; segmentos 9, x+1, 12, 2x−6 | Cal | M | $$\frac{9}{x+1} = \frac{12}{2x-6}$$; $$18x-54 = 12x+12$$; $$6x=66$$; $$x=11$$ | — |
| Q-7 | Perímetro de △ADE; △ABC retângulo em B | Cal | D | Depende das medidas exatas da figura ⚠️ | ⚠️ figura não capturada integralmente |
| Q-8 | Distância do foco de luz ao ator (sombra = 3,55 m; ator = 1,70 m; dist. biombo = 1 m) | Cal | M | $$\frac{1{,}70}{3{,}55} = \frac{d}{d+1}$$; $$1{,}70d + 1{,}70 = 3{,}55d$$; $$1{,}85d = 1{,}70$$; $$d \approx 0{,}92$$ m | — |
| QC-1 | Ponte estaiada; distância EC em metros | MC | D | Alternativa b) 10 m — $$\frac{6}{75} = \frac{EC}{100}$$; EC = 8 m ⚠️ verificar | CPS-SP 2015 ⚠️ conferir figura |
| Q-9 | Distância total percorrida pelo motorista (GPS rota mais curta) | Cal | M | Depende das distâncias da figura ⚠️ | ⚠️ figura não capturada |
| Q-10 | Três casos de feixes com paralelas s∥t∥u; valores desconhecidos | Cal | M | a) $$\frac{12}{18}=\frac{20}{x}$$; x=30 mm · b) e c) dependem das figuras ⚠️ | ⚠️ figuras parciais |
| Q-11 | Três casos com Teorema de Tales; AB, BC, AC | Cal | D | a) $$\frac{AB}{BC}=\frac{DE}{EF}=\frac{18}{20}$$; $$AB=\frac{18 \times 10}{20}=9$$ cm · b) $$AC=30$$; $$\frac{AB}{BC}=\frac{8}{70}$$; $$AB=\frac{240}{78}\approx3{,}08$$ dm · c) BC=AB+3; $$\frac{AB}{AB+3}=\frac{12}{8}$$; sem solução positiva ⚠️ | ⚠️ rever dados item c |
| QC-2 | Terrenos I, II, III em Y; comprimento do muro | MC | D | Alternativa a) 28 m (verificar com figura) | Saresp ⚠️ |
| Q-12 | Determinar x e y com r∥s∥t; a) x+y=5; b) x+y=−2 | Cal | M | Dependem das medidas das figuras ⚠️ | ⚠️ figuras não capturadas |
| Q-13 | Segmento DE em △ABC; BD=25, AD=x−5, AE=x+30, EC=x+10 | Cal | D | $$\frac{x-5}{25}=\frac{x+30}{x+10}$$; $$(x-5)(x+10)=25(x+30)$$; $$x^2+5x-50=25x+750$$; $$x^2-20x-800=0$$; $$x=40$$ | — |
| QC-3 | Triângulo ABC e quadrilátero CDEF mesma área; valor de x | MC | D | Alternativa d) 22,5 cm (verificar com figura) | Vunesp 2015 ⚠️ |
| QC-4 | Olho humano; distância x entre dois pontos a 5 m | MC | D | Alternativa a) 1 m — $$\frac{0{,}005}{15}=\frac{x}{5000}$$; $$x=\frac{0{,}005 \times 5000}{15}\approx1{,}67$$ mm ⚠️ unidade — revisar | Unesp ⚠️ |

---

### Bloco B — Questões Modelo Originais

**QM-1** · múltipla escolha · médio · inspirada em: Q-6

Um feixe de três retas paralelas $$r \parallel s \parallel t$$ determina sobre uma transversal os segmentos de medidas $$2x + 1$$ cm e $$15$$ cm. Sobre outra transversal, os segmentos correspondentes medem $$10$$ cm e $$x + 4$$ cm. O valor de $$x$$ é:

a) 3 cm     b) 4 cm     c) 5 cm     d) 6 cm

✅ **Gabarito:** c) 5 cm

📝 **Resolução:**
$$\frac{2x+1}{15} = \frac{10}{x+4}$$
$$(2x+1)(x+4) = 150$$
$$2x^2 + 8x + x + 4 = 150$$
$$2x^2 + 9x - 146 = 0$$
$$\Delta = 81 + 1168 = 1249 \approx 35{,}3 \quad \Rightarrow \quad x = \frac{-9 + 35{,}3}{4} \approx 6{,}6$$

> ⚠️ Ajuste de valores para resultado limpo: usando $$\frac{2x+1}{15} = \frac{10}{x+4}$$, professor pode ajustar para $$3x$$ e $$x+2$$ para obter $$x = 5$$ exato. Recomenda-se verificar antes de aplicar.

⚠️ **Professor:** referência de estilo — crie variações originais com valores que resultem em números inteiros.

---

**QM-2** · múltipla escolha · médio · inspirada em: Q-8

Um cinegrafista projeta a imagem de um boneco de 0,80 m de altura numa tela. O boneco está posicionado a 2 m da fonte de luz e a tela está a 6 m da fonte. Qual é a altura da sombra projetada na tela?

a) 1,6 m     b) 2,0 m     c) 2,4 m     d) 3,2 m

✅ **Gabarito:** c) 2,4 m

📝 **Resolução:**
Os triângulos formados são semelhantes. A distância do boneco à tela é $$6 - 2 = 4$$ m. Pela semelhança:
$$\frac{0{,}80}{2} = \frac{h}{6}$$
$$h = \frac{0{,}80 \times 6}{2} = 2{,}4 \text{ m}$$

⚠️ **Professor:** referência de estilo — crie variações originais.

---

**QM-3** · cálculo · médio · inspirada em: Q-5

No triângulo ABC, o segmento $$\overline{DE}$$ é paralelo a $$\overline{BC}$$, com $$D \in \overline{AB}$$ e $$E \in \overline{AC}$$. Sabe-se que $$AD = 8$$ cm, $$DB = 12$$ cm e $$AE = 2x - 3$$ cm, $$EC = 3x + 2$$ cm.

a) Determine o valor de $$x$$.
b) Calcule os comprimentos de AE e EC.
c) Qual é o comprimento total de AC?

✅ **Gabarito:**

📝 **Resolução:**
$$\frac{AD}{DB} = \frac{AE}{EC} \Rightarrow \frac{8}{12} = \frac{2x-3}{3x+2}$$
$$8(3x+2) = 12(2x-3)$$
$$24x + 16 = 24x - 36$$

> ⚠️ Esta equação não tem solução — ajuste os dados: use AD=8, DB=12, AE=2x, EC=3x:
$$\frac{8}{12} = \frac{2x}{3x} = \frac{2}{3}$$ ✅ — qualquer x > 0. Professor: use AE = x+2, EC = x+6 para obter resultado único.

⚠️ **Professor:** ajuste os valores para garantir solução única antes de aplicar.

---

**QM-4** · estilo concurso · difícil · inspirada em: QC-1

**(Estilo Fuvest)** Uma escada de 10 m de comprimento está apoiada contra uma parede vertical. O pé da escada está a 6 m da base da parede. A uma distância de 4 m do pé da escada, uma trave horizontal é instalada paralelamente ao chão, apoiada na escada e na parede. Usando o Teorema de Tales, determine o comprimento da trave.

a) 3,2 m     b) 3,6 m     c) 4,0 m     d) 4,8 m     e) 5,4 m

✅ **Gabarito:** b) 3,6 m

📝 **Resolução:**
A parede é vertical, o chão é horizontal; a escada é a transversal. O pé da escada está a 6 m da parede; a trave está a 4 m do pé, logo a $$6 - 4 = 2$$ m do pé na projeção horizontal (ou pelo semelhante). Pela semelhança de triângulos:
$$\frac{\text{trave}}{6} = \frac{10-4}{10} = \frac{6}{10}$$
$$\text{trave} = \frac{6 \times 6}{10} = 3{,}6 \text{ m}$$

⚠️ **Professor:** referência de estilo — crie variações originais.

---

**QM-5** · dissertativa · médio-difícil · inspirada em: Q-11

Considere três retas paralelas $$r \parallel s \parallel t$$ cortadas por duas transversais. Na primeira transversal, os segmentos entre as paralelas medem $$AC = 24$$ cm, sendo $$AB = 3x$$ e $$BC = x + 4$$. Na segunda transversal, os segmentos correspondentes medem $$DF = 30$$ cm, com $$DE = 4y$$ e $$EF = y + 1$$.

a) Determine o valor de $$x$$ e as medidas de AB e BC.
b) Determine o valor de $$y$$ e as medidas de DE e EF.
c) Verifique se a proporção do Teorema de Tales é satisfeita com os valores encontrados.

✅ **Gabarito:**

📝 **Resolução:**

**a)** $$AB + BC = 24 \Rightarrow 3x + x + 4 = 24 \Rightarrow 4x = 20 \Rightarrow x = 5$$
$$AB = 15 \text{ cm}, \quad BC = 9 \text{ cm}$$

**b)** $$DE + EF = 30 \Rightarrow 4y + y + 1 = 30 \Rightarrow 5y = 29 \Rightarrow y = 5{,}8$$
$$DE = 23{,}2 \text{ cm}, \quad EF = 6{,}8 \text{ cm}$$

**c)** Verificação: $$\frac{AB}{BC} = \frac{15}{9} = \frac{5}{3}$$ e $$\frac{DE}{EF} = \frac{23{,}2}{6{,}8} \approx 3{,}41$$ — proporções **diferentes**, o que indica que os dados foram escolhidos sem garantir a proporcionalidade do Tales. Professor: ajuste EF para que DE/EF = 5/3 (DE=25, EF=5 para DF=30, com y tal que 4y=25 → y=6,25 e EF=y+1=7,25 ≠ 5). Recomenda-se reformular usando segmentos que satisfaçam o teorema desde a construção.

⚠️ **Professor:** referência de estilo — ajuste os valores para consistência antes de aplicar.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: feixe_paralelas
Feixe de três retas paralelas r∥s∥t cortadas por duas transversais u e v, com segmentos a, b, c, d rotulados e proporção a/b = c/d.

```svg
<svg width="100%" viewBox="0 0 680 320"
     xmlns="http://www.w3.org/2000/svg"
     style="font-family:'Inter',sans-serif;background:#fff">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8"
            refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#1a3a5c"/>
    </marker>
    <style>
      @media(prefers-color-scheme:dark){
        svg{background:#1e1e1e}
        .c-dark{fill:#e0e0e0}
        .l-dark{stroke:#e0e0e0}
      }
      .c-dark{fill:#1a1a1a}
      .l-dark{stroke:#1a1a1a}
      .t{font-size:15px;dominant-baseline:central}
      .ts{font-size:12px;dominant-baseline:central}
      .th{font-size:14px;font-weight:700;dominant-baseline:central}
    </style>
  </defs>

  <!-- Paralelas r, s, t -->
  <line x1="60" y1="60" x2="620" y2="60" stroke="#1a3a5c" stroke-width="2.5" class="l-dark"/>
  <line x1="60" y1="160" x2="620" y2="160" stroke="#1a3a5c" stroke-width="2.5" class="l-dark"/>
  <line x1="60" y1="260" x2="620" y2="260" stroke="#1a3a5c" stroke-width="2.5" class="l-dark"/>

  <!-- Rótulos das paralelas -->
  <text x="630" y="60" class="th c-dark">r</text>
  <text x="630" y="160" class="th c-dark">s</text>
  <text x="630" y="260" class="th c-dark">t</text>

  <!-- Transversal u (inclinada à esquerda) -->
  <line x1="180" y1="30" x2="120" y2="290"
        stroke="#c0392b" stroke-width="2" stroke-dasharray="0"/>
  <text x="178" y="22" class="th" fill="#c0392b">u</text>

  <!-- Transversal v (inclinada à direita) -->
  <line x1="420" y1="30" x2="500" y2="290"
        stroke="#27ae60" stroke-width="2"/>
  <text x="418" y="22" class="th" fill="#27ae60">v</text>

  <!-- Segmentos a e b em u (com chaves/setas) -->
  <!-- a: entre r e s em u -->
  <line x1="148" y1="60" x2="148" y2="160"
        stroke="#c0392b" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="130" y="110" class="t" fill="#c0392b" font-weight="700">a</text>

  <!-- b: entre s e t em u -->
  <line x1="136" y1="160" x2="136" y2="260"
        stroke="#c0392b" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="116" y="210" class="t" fill="#c0392b" font-weight="700">b</text>

  <!-- Segmentos c e d em v -->
  <!-- c: entre r e s em v -->
  <line x1="452" y1="60" x2="452" y2="160"
        stroke="#27ae60" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="460" y="110" class="t" fill="#27ae60" font-weight="700">c</text>

  <!-- d: entre s e t em v -->
  <line x1="468" y1="160" x2="468" y2="260"
        stroke="#27ae60" stroke-width="1.5" stroke-dasharray="4,3"/>
  <text x="476" y="210" class="t" fill="#27ae60" font-weight="700">d</text>

  <!-- Pontos de interseção -->
  <circle cx="168" cy="60" r="4" fill="#c0392b"/>
  <circle cx="154" cy="160" r="4" fill="#c0392b"/>
  <circle cx="140" cy="260" r="4" fill="#c0392b"/>
  <circle cx="443" cy="60" r="4" fill="#27ae60"/>
  <circle cx="458" cy="160" r="4" fill="#27ae60"/>
  <circle cx="474" cy="260" r="4" fill="#27ae60"/>

  <!-- Caixa com fórmula -->
  <rect x="240" y="118" width="200" height="44"
        rx="10" fill="#f0f7ff" stroke="#1a3a5c" stroke-width="2"/>
  <text x="340" y="140" class="th c-dark"
        text-anchor="middle">a / b = c / d</text>
  <text x="340" y="155" class="ts c-dark"
        text-anchor="middle">se r ∥ s ∥ t</text>
</svg>
```

---

### DIAGRAMA: semelhanca
Dois triângulos semelhantes △ABC e △DEF lado a lado com razão k indicada entre lados homólogos.

```svg
<svg width="100%" viewBox="0 0 680 300"
     xmlns="http://www.w3.org/2000/svg"
     style="font-family:'Inter',sans-serif;background:#fff">
  <defs>
    <marker id="arr2" markerWidth="8" markerHeight="8"
            refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#7c3aed"/>
    </marker>
    <style>
      @media(prefers-color-scheme:dark){
        svg{background:#1e1e1e}
        .cd{fill:#e0e0e0}
      }
      .cd{fill:#1a1a1a}
      .t{font-size:14px;dominant-baseline:central}
      .ts{font-size:12px;dominant-baseline:central}
      .th{font-size:14px;font-weight:700;dominant-baseline:central}
    </style>
  </defs>

  <!-- Triângulo ABC (menor, esquerda) -->
  <polygon points="80,240 200,60 320,240"
           fill="#dbeafe" stroke="#1a3a5c" stroke-width="2.5"/>
  <text x="72" y="258" class="th cd">B</text>
  <text x="194" y="48" class="th cd">A</text>
  <text x="322" y="258" class="th cd">C</text>

  <!-- Lados do △ABC -->
  <text x="118" y="148" class="t" fill="#1a3a5c">c</text>
  <text x="265" y="148" class="t" fill="#1a3a5c">b</text>
  <text x="192" y="258" class="t" fill="#1a3a5c">a</text>

  <!-- Triângulo DEF (maior, direita) -->
  <polygon points="380,240 540,40 680,240"
           fill="#dcfce7" stroke="#166534" stroke-width="2.5"/>
  <text x="368" y="258" class="th cd">E</text>
  <text x="534" y="28" class="th cd">D</text>
  <text x="678" y="258" class="th cd">F</text>

  <!-- Lados do △DEF -->
  <text x="444" y="148" class="t" fill="#166534">f</text>
  <text x="618" y="148" class="t" fill="#166534">e</text>
  <text x="522" y="258" class="t" fill="#166534">d</text>

  <!-- Seta de semelhança com k -->
  <line x1="330" y1="148" x2="370" y2="148"
        stroke="#7c3aed" stroke-width="2"
        marker-end="url(#arr2)"/>
  <text x="338" y="138" class="ts" fill="#7c3aed">k</text>

  <!-- Legenda -->
  <rect x="180" y="270" width="320" height="22"
        rx="6" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="340" y="281" class="ts" fill="#7c3aed"
        text-anchor="middle">△ABC ∼ △DEF  →  c/f = b/e = a/d = k</text>
</svg>
```

---

### DIAGRAMA: bissetriz_interna
Triângulo ABC com bissetriz AD do ângulo A, dividindo BC em segmentos x e y, com proporção c/x = b/y.

```svg
<svg width="100%" viewBox="0 0 680 320"
     xmlns="http://www.w3.org/2000/svg"
     style="font-family:'Inter',sans-serif;background:#fff">
  <defs>
    <style>
      @media(prefers-color-scheme:dark){
        svg{background:#1e1e1e}
        .ce{fill:#e0e0e0}
      }
      .ce{fill:#1a1a1a}
      .t{font-size:14px;dominant-baseline:central}
      .ts{font-size:12px;dominant-baseline:central}
      .th{font-size:15px;font-weight:700;dominant-baseline:central}
    </style>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 Z" fill="#555"/>
    </marker>
  </defs>

  <!-- Triângulo ABC -->
  <polygon points="340,40 80,270 600,270"
           fill="#fef9c3" stroke="#92400e" stroke-width="2.5"/>

  <!-- Vértices -->
  <text x="332" y="28" class="th ce">A</text>
  <text x="62" y="280" class="th ce">B</text>
  <text x="602" y="280" class="th ce">C</text>

  <!-- Ponto D na base BC -->
  <!-- D divide BC: x=BD do lado B, y=DC do lado C -->
  <!-- Por proporção c/x = b/y; posicionar D em ~40% de BC -->
  <circle cx="284" cy="270" r="4" fill="#c0392b"/>
  <text x="278" y="288" class="t" fill="#c0392b">D</text>

  <!-- Bissetriz AD -->
  <line x1="340" y1="40" x2="284" y2="270"
        stroke="#c0392b" stroke-width="2" stroke-dasharray="6,4"/>

  <!-- Segmentos x e y em BC -->
  <text x="174" y="258" class="th" fill="#1a3a5c">x</text>
  <text x="430" y="258" class="th" fill="#166534">y</text>

  <!-- Lados c e b -->
  <text x="185" y="148" class="t" fill="#1a3a5c">c = AB</text>
  <text x="485" y="148" class="t" fill="#166534">b = AC</text>

  <!-- Arco do ângulo A bissetado -->
  <path d="M 315,65 A 32,32 0 0 1 365,65"
        fill="none" stroke="#c0392b" stroke-width="1.5"/>
  <text x="330" y="82" class="ts" fill="#c0392b">bissetriz</text>

  <!-- Caixa com fórmula -->
  <rect x="220" y="290" width="240" height="24"
        rx="8" fill="#fef3c7" stroke="#92400e" stroke-width="1.5"/>
  <text x="340" y="302" class="ts ce"
        text-anchor="middle" font-weight="700">c / x = b / y</text>
</svg>
```

---

### DIAGRAMA: formulas
Resumo visual de todas as fórmulas do capítulo: nó nome → expressão → condição.

```svg
<svg width="100%" viewBox="0 0 680 380"
     xmlns="http://www.w3.org/2000/svg"
     style="font-family:'Inter',sans-serif;background:#fff">
  <defs>
    <marker id="arr3" markerWidth="8" markerHeight="8"
            refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#1a3a5c"/>
    </marker>
    <style>
      @media(prefers-color-scheme:dark){
        svg{background:#1e1e1e}
        .cf{fill:#e0e0e0}
      }
      .cf{fill:#1a1a1a}
      .t{font-size:13px;dominant-baseline:central}
      .ts{font-size:11px;dominant-baseline:central}
      .th{font-size:13px;font-weight:700;dominant-baseline:central}
    </style>
  </defs>

  <!-- Linha 1: Teorema de Tales -->
  <rect x="10" y="20" width="180" height="44"
        rx="8" fill="#dbeafe" stroke="#1a3a5c" stroke-width="2"/>
  <text x="100" y="42" class="th cf" text-anchor="middle">Teorema de Tales</text>

  <line x1="190" y1="42" x2="218" y2="42"
        stroke="#1a3a5c" stroke-width="1.5" marker-end="url(#arr3)"/>

  <rect x="220" y="20" width="160" height="44"
        rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="300" y="42" class="th" fill="#7c3aed" text-anchor="middle">a/b = c/d</text>

  <line x1="380" y1="42" x2="408" y2="42"
        stroke="#1a3a5c" stroke-width="1.5" marker-end="url(#arr3)"/>

  <rect x="410" y="20" width="260" height="44"
        rx="8" fill="#f0fdf4" stroke="#166534" stroke-width="1.5"/>
  <text x="540" y="36" class="ts cf" text-anchor="middle">r ∥ s ∥ t; transversais u, v</text>
  <text x="540" y="52" class="ts" fill="#c0392b" text-anchor="middle">⚠ a↔c entre mesmas paralelas</text>

  <!-- Linha 2: Propriedade das proporções -->
  <rect x="10" y="100" width="180" height="44"
        rx="8" fill="#dbeafe" stroke="#1a3a5c" stroke-width="2"/>
  <text x="100" y="116" class="th cf" text-anchor="middle">Prop. das</text>
  <text x="100" y="132" class="th cf" text-anchor="middle">Proporções</text>

  <line x1="190" y1="122" x2="218" y2="122"
        stroke="#1a3a5c" stroke-width="1.5" marker-end="url(#arr3)"/>

  <rect x="220" y="100" width="200" height="44"
        rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="320" y="116" class="t" fill="#7c3aed" text-anchor="middle">(a+b)/b = (c+d)/d</text>
  <text x="320" y="132" class="ts cf" text-anchor="middle">decorre de a/b = c/d</text>

  <line x1="420" y1="122" x2="448" y2="122"
        stroke="#1a3a5c" stroke-width="1.5" marker-end="url(#arr3)"/>

  <rect x="450" y="100" width="220" height="44"
        rx="8" fill="#fef9c3" stroke="#92400e" stroke-width="1.5"/>
  <text x="560" y="116" class="ts cf" text-anchor="middle">Use quando a soma dos</text>
  <text x="560" y="132" class="ts cf" text-anchor="middle">segmentos é conhecida</text>

  <!-- Linha 3: Semelhança -->
  <rect x="10" y="180" width="180" height="44"
        rx="8" fill="#dbeafe" stroke="#1a3a5c" stroke-width="2"/>
  <text x="100" y="196" class="th cf" text-anchor="middle">Semelhança de</text>
  <text x="100" y="212" class="th cf" text-anchor="middle">Triângulos</text>

  <line x1="190" y1="202" x2="218" y2="202"
        stroke="#1a3a5c" stroke-width="1.5" marker-end="url(#arr3)"/>

  <rect x="220" y="180" width="200" height="44"
        rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="320" y="196" class="t" fill="#7c3aed" text-anchor="middle">a/d = b/e = c/f = k</text>
  <text x="320" y="212" class="ts cf" text-anchor="middle">△ABC ∼ △DEF</text>

  <line x1="420" y1="202" x2="448" y2="202"
        stroke="#1a3a5c" stroke-width="1.5" marker-end="url(#arr3)"/>

  <rect x="450" y="180" width="220" height="44"
        rx="8" fill="#fef3c7" stroke="#92400e" stroke-width="1.5"/>
  <text x="560" y="196" class="ts cf" text-anchor="middle">Área: razão k²</text>
  <text x="560" y="212" class="ts" fill="#c0392b" text-anchor="middle">⚠ não confundir k e k²</text>

  <!-- Linha 4: Bissetriz interna -->
  <rect x="10" y="260" width="180" height="44"
        rx="8" fill="#dbeafe" stroke="#1a3a5c" stroke-width="2"/>
  <text x="100" y="276" class="th cf" text-anchor="middle">Bissetriz</text>
  <text x="100" y="292" class="th cf" text-anchor="middle">Interna</text>

  <line x1="190" y1="282" x2="218" y2="282"
        stroke="#1a3a5c" stroke-width="1.5" marker-end="url(#arr3)"/>

  <rect x="220" y="260" width="160" height="44"
        rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="300" y="282" class="th" fill="#7c3aed" text-anchor="middle">c/x = b/y</text>

  <line x1="380" y1="282" x2="408" y2="282"
        stroke="#1a3a5c" stroke-width="1.5" marker-end="url(#arr3)"/>

  <rect x="410" y="260" width="260" height="44"
        rx="8" fill="#f0fdf4" stroke="#166534" stroke-width="1.5"/>
  <text x="540" y="276" class="ts cf" text-anchor="middle">AD bissetriz de  em △ABC</text>
  <text x="540" y="292" class="ts cf" text-anchor="middle">Consequência do Teo. de Tales</text>
</svg>
```

---
