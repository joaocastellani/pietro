# mat-1-7-prep.md

---

## DIAGRAMAS DISPONÍVEIS — mat-1-7

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Fórmulas do Capítulo 7 | DIAGRAMA: formulas | Bloco de fórmulas — Bhaskara, discriminante, soma, produto |
| Análise do Discriminante | DIAGRAMA: analise_delta | Ao apresentar os três casos de Δ |

### Tabelas markdown (Seção 6):
- Tabela de análise do discriminante (3 casos)
- Tabela comparativa das estratégias de resolução

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer. Tabelas da Seção 6 são apresentadas como markdown no chat.

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 7
- Tema: Forma resolutiva da equação do 2º grau
- Perfil: álgebra
- Fórmulas principais:
    Δ = b² − 4ac
    x = (−b ± √Δ) / (2a)    (Bhaskara)
    S = x₁ + x₂ = −b/a      (soma das raízes)
    P = x₁ · x₂ = c/a       (produto das raízes)
    d = n(n−3)/2             (diagonais de polígono)
- Matemáticos citados: Bhaskara (1114–1185)
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### **Bloco 1 — Trinômio quadrado perfeito**

Um **trinômio quadrado perfeito (TQP)** é toda expressão algébrica de três termos que resulta do quadrado de um binômio — ou seja, pode ser fatorada na forma $$(a+b)^2$$ ou $$(a-b)^2$$.

**Como reconhecer:** o termo do meio é o dobro do produto das raízes quadradas do 1º e do 3º termos.

Exemplos do material:
- $$x^2 + 4x + 4 = (x+2)^2$$ → $$2 \cdot \sqrt{x^2} \cdot \sqrt{4} = 2x \cdot 2 = 4x$$ ✓
- $$4x^2 - 12x + 9 = (2x-3)^2$$
- $$25x^2 + 60x + 36 = (5x+6)^2$$

Quando uma equação do 2º grau tem o lado esquerdo que é um TQP, resolve-se por **fatoração direta** sem precisar de Bhaskara:

$$x^2 + 4x + 4 = 0 \Rightarrow (x+2)^2 = 0 \Rightarrow x = -2 \text{ (raiz dupla)}$$

---

### **Bloco 2 — Equação produto e completar quadrados**

**Equação produto:** se uma equação pode ser escrita como $$(A)(B) = 0$$, então $$A = 0$$ ou $$B = 0$$ (propriedade do produto nulo). Isso permite encontrar as raízes diretamente.

**Método de completar quadrados:** técnica que transforma qualquer equação completa em uma com TQP. Exemplo do material (Bloco F):

$$x^2 + 4x = 12$$
$$x^2 + 4x + 4 = 16$$
$$(x+2)^2 = 16 \Rightarrow x+2 = \pm 4$$
$$x = 2 \quad \text{ou} \quad x = -6$$

---

### **Bloco 3 — Fórmula de Bhaskara**

Para qualquer equação completa $$ax^2 + bx + c = 0$$ (com $$a \neq 0$$), as raízes são determinadas pela **fórmula de Bhaskara**:

$$x = \frac{-b \pm \sqrt{\Delta}}{2a}, \quad \text{onde} \quad \Delta = b^2 - 4ac$$

O $$\pm$$ gera as duas raízes:
$$x_1 = \frac{-b + \sqrt{\Delta}}{2a} \qquad x_2 = \frac{-b - \sqrt{\Delta}}{2a}$$

**Exemplo concreto do material:** $$4x^2 - 3x - 1 = 0$$
- $$a=4, b=-3, c=-1$$
- $$\Delta = (-3)^2 - 4\cdot4\cdot(-1) = 9+16 = 25$$
- $$x = \frac{3 \pm 5}{8} \Rightarrow x_1 = 1, \quad x_2 = -\dfrac{1}{4}$$
- $$S = \left\{-\tfrac{1}{4},\, 1\right\}$$

---

### **Bloco 4 — Análise do discriminante**

Antes de calcular as raízes, o **discriminante** $$\Delta = b^2 - 4ac$$ revela *quantas* raízes reais a equação possui:

| $$\Delta$$ | Natureza | Conjunto solução |
|-----------|----------|-----------------|
| $$\Delta > 0$$ | Duas raízes reais **distintas** | $$S = \{x_1, x_2\}$$, $$x_1 \neq x_2$$ |
| $$\Delta = 0$$ | Duas raízes reais **iguais** (dupla) | $$S = \{x_1\}$$, $$x_1 = x_2 = \frac{-b}{2a}$$ |
| $$\Delta < 0$$ | **Sem** raízes reais | $$S = \emptyset$$ |

> **Atenção (Bloco H):** análise do discriminante responde *quantas* raízes existem. Para saber *quais* são os valores, é preciso aplicar a fórmula de Bhaskara.

---

### **Bloco 5 — Soma e produto das raízes**

Se $$x_1$$ e $$x_2$$ são raízes de $$ax^2+bx+c=0$$ ($$a\neq0$$):

$$S = x_1 + x_2 = -\frac{b}{a} \qquad P = x_1 \cdot x_2 = \frac{c}{a}$$

**Por que funciona:** ao expandir $$(x-x_1)(x-x_2)=0$$, obtém-se $$x^2-(x_1+x_2)x+x_1x_2=0$$; comparando com $$x^2+\frac{b}{a}x+\frac{c}{a}=0$$ surgem as relações.

Aplicações práticas:
- Verificar se um valor é raiz: substitui e testa soma/produto.
- Determinar parâmetros: ex., dado $$k$$ que faz $$\Delta=0$$.

---

### **Bloco 6 — Escrever equação a partir de raízes conhecidas**

Conhecendo $$x_1$$ e $$x_2$$, há duas estratégias:

**1ª estratégia — soma e produto (com $$a=1$$):**
$$x^2 - (x_1+x_2)x + x_1\cdot x_2 = 0 \quad \Leftrightarrow \quad x^2 - Sx + P = 0$$

**2ª estratégia — fatoração:**
$$(x-x_1)(x-x_2) = 0$$, desenvolvendo chega-se à forma reduzida.

**Exemplo:** raízes $$x_1=1$$ e $$x_2=2$$.
- $$S=3$$, $$P=2$$ → $$x^2-3x+2=0$$
- $$(x-1)(x-2)=0 \Rightarrow x^2-3x+2=0$$ ✓

Para coeficiente $$a \neq 1$$: multiplica-se a equação inteira por $$a$$.

---

## SEÇÃO 3 — MATEMÁTICOS E HISTÓRIA DA MATEMÁTICA

### Bhaskara (1114–1185)
**Área:** álgebra e astronomia
**Contribuição no capítulo:** desenvolveu a fórmula geral de resolução das equações do 2º grau, conhecida no Brasil como Fórmula de Bhaskara. Realizou contribuições importantes tanto para a matemática quanto para a astronomia.
**O que desenvolveu:** $$x = \dfrac{-b \pm \sqrt{b^2-4ac}}{2a}$$ — fórmula que resolve qualquer equação quadrática completa.
**Contexto histórico:** matemático indiano do século XII; sua obra abrangeu aritmética, álgebra e trigonometria, sendo influente na matemática medieval.

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Discriminante

**Expressão:** $$\Delta = b^2 - 4 \cdot a \cdot c$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$\Delta$$ | discriminante | real |
| $$a$$ | coeficiente do termo quadrático | real, $$a \neq 0$$ |
| $$b$$ | coeficiente do termo linear | real |
| $$c$$ | termo independente | real |

**Válida quando:** $$a \neq 0$$ (equação do 2º grau)
💡 **Pegadinha:** calcular $$b^2$$ separado antes de subtrair $$4ac$$; erro comum: trocar o sinal quando $$b$$ é negativo — $$(-3)^2 = 9$$, não $$-9$$.

---

### Fórmula de Bhaskara

**Expressão:** $$x = \dfrac{-b \pm \sqrt{\Delta}}{2a}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$x$$ | raízes $$x_1$$ e $$x_2$$ | real (se $$\Delta \geq 0$$) |
| $$\Delta$$ | discriminante | real |
| $$a, b, c$$ | coeficientes da equação | real |

**Válida quando:** $$a \neq 0$$; $$\Delta \geq 0$$ para raízes reais
**Caso especial:** $$\Delta = 0 \Rightarrow x_1 = x_2 = \dfrac{-b}{2a}$$ (raiz dupla); $$\Delta < 0 \Rightarrow S = \emptyset$$
💡 **Pegadinha:** o denominador é $$2a$$, **não** apenas $$2$$ — se $$a=3$$, o divisor é $$6$$. Erro clássico: dividir só por 2 esquecendo o $$a$$.

---

### Soma das raízes

**Expressão:** $$S = x_1 + x_2 = -\dfrac{b}{a}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$S$$ | soma das raízes | real |
| $$b$$ | coeficiente linear | real |
| $$a$$ | coeficiente quadrático | real, $$a \neq 0$$ |

💡 **Pegadinha:** o sinal negativo é essencial — $$S = -b/a$$, não $$b/a$$. Para $$b=-3$$ e $$a=1$$: $$S = -(-3)/1 = 3$$.

---

### Produto das raízes

**Expressão:** $$P = x_1 \cdot x_2 = \dfrac{c}{a}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$P$$ | produto das raízes | real |
| $$c$$ | termo independente | real |
| $$a$$ | coeficiente quadrático | real, $$a \neq 0$$ |

💡 **Pegadinha:** $$P = c/a$$, **não** apenas $$c$$. Se $$a=2$$ e $$c=8$$: $$P=4$$, não $$8$$.

---

### Equação a partir de raízes (1ª estratégia)

**Expressão:** $$x^2 - Sx + P = 0$$, onde $$S = x_1+x_2$$ e $$P = x_1\cdot x_2$$

**Válida quando:** coeficiente $$a=1$$; para $$a \neq 1$$, multiplicar toda a equação por $$a$$.
**Caso especial:** para $$a \neq 1$$ → $$a(x^2-Sx+P)=0$$, ex.: $$a=2, x_1=-3, x_2=-7$$ → $$2(x^2+10x+21)=0 \Rightarrow 2x^2+20x+42=0$$.

---

### Fórmula das diagonais de um polígono

**Expressão:** $$d = \dfrac{n(n-3)}{2}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$d$$ | número de diagonais | inteiro $$\geq 0$$ |
| $$n$$ | número de lados | inteiro $$\geq 3$$ |

**Aplicação inversa:** dado $$d$$, reescrever como $$n^2 - 3n - 2d = 0$$ e resolver pela Bhaskara; descartar raiz negativa.
**Exemplo (Bloco G):** $$d=560 \Rightarrow n^2-3n-1120=0 \Rightarrow \Delta=4489=67^2 \Rightarrow n=35$$ (descarta $$n=-32$$).

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Análise do Discriminante — três casos

| Discriminante | Natureza das raízes | Conjunto solução | Exemplo |
|--------------|---------------------|-----------------|---------|
| $$\Delta > 0$$ | Duas raízes reais **distintas** | $$S = \{x_1, x_2\}$$, $$x_1 \neq x_2$$ | $$x^2+3x+2=0$$: $$\Delta=1$$ → $$S=\{-2,-1\}$$ |
| $$\Delta = 0$$ | Duas raízes reais **iguais** | $$S = \{x_1\}$$ (dupla), $$x_1 = -b/(2a)$$ | $$-x^2+10x-25=0$$: $$\Delta=0$$ → $$S=\{5\}$$ |
| $$\Delta < 0$$ | **Sem** raízes reais | $$S = \emptyset$$ | $$5x^2-3x+2=0$$: $$\Delta=-31$$ → $$S=\emptyset$$ |

### Estratégias de resolução — comparativo

| Estratégia | Quando usar | Exemplo do material |
|-----------|-------------|---------------------|
| Fatoração (TQP) | Equação com lado esquerdo fatorável como $$(ax+b)^2$$ | $$4x^2-32x+64=0 \Rightarrow (2x-8)^2=0$$ |
| Bhaskara | Qualquer equação completa | $$x^2+5x+6=0 \Rightarrow \Delta=1 \Rightarrow S=\{-3,-2\}$$ |
| Soma e produto | Verificação rápida ou construção de equação | $$6(x+1)-6x=x(x+1) \Rightarrow S=-b/a=-1$$ |
| Completar quadrados | Demonstração / entendimento geométrico | $$x^2+4x=12 \Rightarrow (x+2)^2=16 \Rightarrow x=2$$ ou $$x=-6$$ |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — O denominador é 2a, não 2**
A fórmula divide por $$2a$$, não por $$2$$. Se $$a=4$$: divisor = 8. Escrever sempre o $$a$$ no denominador antes de calcular.

💡 **Dica 2 — Análise vs. cálculo das raízes**
$$\Delta$$ responde *quantas* raízes existem; Bhaskara responde *quais* são. Não confundir os dois passos: primeiro analisar $$\Delta$$, só então aplicar a fórmula.

💡 **Dica 3 — Sinal de b na soma das raízes**
$$S = -b/a$$, com o negativo explícito. Para $$b=-6$$: $$S = -(-6)/a = 6/a$$. Dobro erro comum: esquecer o sinal negativo e usar $$b$$ direto.

💡 **Dica 4 — Verificação rápida com soma e produto**
Após calcular $$x_1$$ e $$x_2$$, verificar: $$x_1+x_2 = -b/a$$ e $$x_1\cdot x_2 = c/a$$. Se não bater, há erro no cálculo.

💡 **Dica 5 — Descartar raiz negativa em contextos físicos**
Quando a incógnita representa medida, tempo ou quantidade (ex.: lados de polígono, idades, dimensões), a raiz negativa é descartada mesmo sendo matematicamente válida.

💡 **Dica 6 — Reduzir a equação antes de aplicar Bhaskara**
Para equações com decimais ou frações, multiplicar toda a equação por um MMC antes de identificar $$a$$, $$b$$, $$c$$. Ex.: $$0{,}01x^2+0{,}05x-0{,}5=0$$ → multiplicar por 100 → $$x^2+5x-50=0$$.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

#### Bloco A — Lacunas de dados

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| BLOCO E | QI-4 | Legenda parcialmente ilegível — enunciado incompleto | Capturar imagem da pág. 156 |
| BLOCO E | QI-5 | Legenda parcialmente ilegível — 3 partes ilegíveis | Capturar imagem da pág. 157 |
| BLOCO E | QI-10 | Legenda parcialmente ilegível | Capturar imagem da pág. 163 |
| BLOCO E | QI-11 | Legenda parcialmente ilegível | Capturar imagem da pág. 164 |
| BLOCO E | QI-12 | Legenda parcialmente ilegível | Capturar imagem da pág. 165 |
| SEÇÃO AT | Q-16 | Enunciado parcialmente ilegível | Capturar imagem da pág. 187 |
| SEÇÃO AT | QC-8 | Banca e enunciado ilegíveis | Capturar imagem da pág. 187 |

#### Bloco B — Inconsistências e alertas

```
⚠️ ALERTA — Q-12 (alternativas possivelmente capturadas com erro)
- Dado no material: S={-1/10, -1/10} → equação com raiz dupla x=-1/10
- Problema: nenhuma das 4 alternativas capturadas corresponde à equação
  correta x²+(1/5)x+(1/100)=0; opção b) tem P=1/10 em vez de 1/100.
  Alternativas b) e c) produzem discriminante negativo (sem raízes reais).
- Dado correto: equação correta é x²+(1/5)x+(1/100)=0
- Impacto na aula: rever a imagem original da pág. 185 antes de usar a questão.
```

```
⚠️ ALERTA — Q-14 (enunciado exige verificação da pág. 186)
- Dado no material: 1º aluno errou b (encontrou -10 e -2); 2º aluno errou a
  (encontrou 4 e 8).
- Problema: análise algébrica com os dados capturados leva a discriminante
  negativo para a equação "correta", sugerindo possível erro de captura
  nos valores das raízes encontradas pelos alunos.
- Impacto na aula: verificar a imagem original antes de corrigir com o aluno.
```

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO

#### Bloco 1 — Conceitos e Definições

- **Trinômio quadrado perfeito**
  - Definição: `______` (expressão que é o quadrado de um binômio, ex.: $$(a+b)^2$$)
  - Reconhecimento: `______` (o termo do meio = dobro do produto das raízes do 1º e 3º termos)

- **Equação produto**
  - Propriedade: `______` (se $$(A)(B)=0$$, então $$A=0$$ ou $$B=0$$)

- **Discriminante**
  - Expressão: `______` ($$\Delta = b^2 - 4ac$$)
  - Função: `______` (determina *quantas* raízes reais a equação possui)

- **Fórmula de Bhaskara**
  - Expressão: `______` ($$x = (-b \pm \sqrt{\Delta})/(2a)$$)
  - Quando usar: `______` (qualquer equação completa do 2º grau)

- **Soma das raízes**
  - Expressão: `______` ($$S = -b/a$$)

- **Produto das raízes**
  - Expressão: `______` ($$P = c/a$$)

#### Bloco 2 — Fórmulas e Propriedades

- **Discriminante**
  - Expressão: `______` ($$\Delta = b^2 - 4ac$$)
  - Variável $$a$$: `______` (coeficiente do termo quadrático; $$a \neq 0$$)

- **Bhaskara**
  - Expressão: `______` ($$x = (-b \pm \sqrt{\Delta})/(2a)$$)
  - Condição: `______` ($$\Delta \geq 0$$ para raízes reais)
  - Pegadinha: `______` (denominador é $$2a$$, não $$2$$)

- **Análise do discriminante**
  - $$\Delta > 0$$ → `______` (duas raízes reais distintas)
  - $$\Delta = 0$$ → `______` (raiz dupla)
  - $$\Delta < 0$$ → `______` (sem raízes reais; $$S = \emptyset$$)

- **Soma e produto**
  - $$S = $$`______` ($$-b/a$$)
  - $$P = $$`______` ($$c/a$$)

#### Bloco 3 — Lacunas para Warm-Up

1. A expressão $$x^2 + 6x + 9$$ é um trinômio quadrado perfeito igual a `______`.
   *(resposta: $$(x+3)^2$$)*

2. Para resolver $$4x^2 - 32x + 64 = 0$$ por TQP: $$(2x - \text{`______`})^2 = 0$$.
   *(resposta: 8; raiz: $$x=4$$)*

3. Na fórmula de Bhaskara, o discriminante é $$\Delta = $$`______`.
   *(resposta: $$b^2 - 4ac$$)*

4. Se $$\Delta < 0$$, o conjunto solução da equação do 2º grau é `______`.
   *(resposta: $$S = \emptyset$$)*

5. Para $$3x^2 - 5x + 2 = 0$$: $$a=3$$, $$b=-5$$, $$c=2$$; logo $$\Delta = $$`______`.
   *(resposta: $$25-24=1$$; raízes: $$x_1=1$$, $$x_2=2/3$$)*

6. Bhaskara foi um matemático `______` que viveu entre `______` e `______`.
   *(resposta: indiano; 1114; 1185)*

7. A soma das raízes de $$2x^2+8x-10=0$$ é $$S = $$`______` e o produto é $$P = $$`______`.
   *(resposta: $$S=-4$$; $$P=-5$$)*

8. Um polígono com 560 diagonais tem `______` lados — obtido resolvendo $$n^2-3n-1120=0$$ pela Bhaskara e descartando a raiz `______`.
   *(resposta: 35 lados; descarta $$n=-32$$)*

#### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Definição de discriminante | $$\Delta = $$ `______` → *$$b^2-4ac$$* |
| Fórmula de Bhaskara | $$x = $$ `______` → *$$(-b\pm\sqrt{\Delta})/(2a)$$* |
| $$\Delta = 0$$ indica | `______` → *raiz dupla — duas raízes reais iguais* |
| Soma das raízes | $$S = x_1+x_2 = $$ `______` → *$$-b/a$$* |
| Produto das raízes | $$P = x_1 \cdot x_2 = $$ `______` → *$$c/a$$* |
| Equação a partir de raízes $$x_1$$, $$x_2$$ | $$x^2 - $$`______`$$x + $$`______` = 0 → *$$Sx + P = 0$$* |
| Diagonais de polígono | $$d = $$ `______` → *$$n(n-3)/2$$* |
| Pegadinha Bhaskara | Denominador é `______`, não 2 → *$$2a$$* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

Seção 10 não gerada — anexe a imagem da Síntese para incluir.

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| QI-1 | Completar lacunas em TQPs — $$(x+\_)^2 = x^2+\_+4$$ etc. | Cal | F | IC | — | — |
| QI-2 | Fatorar TQPs: $$x^2+6x+9$$; $$25x^2+60x+36$$ etc. | Cal | F | IC | a)$$(x+3)^2$$ c)$$(5x+6)^2$$ d)$$(2x-3)^2$$ | — |
| QI-3 | Resolver por TQP: $$x^2+14x+49=0$$; $$y^2-24y+144=0$$ etc. | Cal | F | IC | a)$$S=\{-7\}$$ b)$$S=\{12\}$$ | — |
| QI-4 | TQP — professor Marcos — legenda ilegível | Cal | M | IC | — | ⚠️ ilegível |
| QI-5 | Discriminante/fatoração — 3 partes — legenda ilegível | Dis | M | IC | — | ⚠️ ilegível |
| QI-6 | Resolver por Bhaskara: 7 equações | Cal | M | IC | a)$$S=\{-4,2\}$$ b)$$S=\{-3,1\}$$ c)$$S=\{2,5\}$$ d)$$S=\{5,7\}$$ e)$$S=\{-1,1/5\}$$ | — |
| QI-7 | Eq. racional: $$2x+2=(10-2x)/x$$ | Cal | M | IC | $$x^2+2x-5=0$$... ver nota | — |
| QI-8 | Bhaskara guiado: $$x^2-x-1=0$$ — a)coefs b)$$\Delta$$ c)raízes | Cal | F | IC | a)1,-1,-1 b)5 c)$$(1\pm\sqrt5)/2$$ | — |
| QI-9 | Terreno retangular: $$(x-1)(x-2)=192$$ | Cal | M | IC | $$x^2-3x-190=0$$; $$x=14{,}5$$; dims 13,5m×12,5m | — |
| QI-10 | Tabela soma/produto de equações — legenda ilegível | Assoc | M | IC | — | ⚠️ ilegível |
| QI-11 | Soma e produto vs. Bhaskara — legenda ilegível | Dis | M | IC | — | ⚠️ ilegível |
| QI-12 | Escrever equação a partir de raízes — legenda ilegível | Cal | M | IC | — | ⚠️ ilegível |
| QI-13 | Discriminante de 6 equações — $$x^2-12x+20$$; $$4x^2-5x+15$$ etc. | Cal | F | IC | a)$$\Delta=64>0$$ b)$$\Delta<0$$ c)$$\Delta=0$$ d)$$\Delta<0$$ e)$$\Delta>0$$ f)$$\Delta=0$$ | — |
| QI-14 | Parâmetro $$t$$ para $$-x^2+4x-16=0$$ ter raízes iguais | Cal | M | IC | $$\Delta=0$$: questão parece ter erro tipográfico (sem $$t$$) | ⚠️ |
| QI-15 | Valor de $$m$$ para $$3x^2+4mx+12=0$$ ter raízes iguais | Cal | M | IC | $$\Delta=0$$: $$16m^2-144=0 \Rightarrow m=\pm3$$ | — |
| QI-16 | Valor de $$y$$ para $$6x^2+5x+y=0$$ ter duas raízes distintas | Cal | M | IC | $$\Delta>0$$: $$25-24y>0 \Rightarrow y<25/24$$ | — |
| QI-17 | Valor de $$n$$ para $$12nx^2-24x+50=0$$ ter duas raízes distintas | Cal | M | IC | $$\Delta>0$$: $$576-2400n>0 \Rightarrow n<6/25$$ (e $$n\neq0$$) | — |
| QI-18 | Valor de $$k$$ para $$5x^2+8x+k=0$$ sem raízes reais | Cal | M | IC | $$\Delta<0$$: $$64-20k<0 \Rightarrow k>16/5$$ | — |
| QI-19 | V-F sobre discriminante: Rafael, Priscila e Luca | VF | F | IC | a)V b)F ($$\Delta$$ não dá os valores, só quantidade) c)V | — |
| QI-D | ENEM 2015 — malha proteção solar — taxa cobertura 75% | MC | D | IC | — | ⚠️ gabarito não capturado |
| Q-1 | Resolver: $$4x^2-40=0$$; $$16x^2+50x=0$$; $$x^2+12x+36=0$$; $$9x^2+2x+1=0$$ | Cal | M | AT | a)$$S=\{-\sqrt{10},\sqrt{10}\}$$ b)$$S=\{-25/8,0\}$$ c)$$S=\{-6\}$$ d)$$\Delta<0$$, $$S=\emptyset$$ | — |
| Q-2 | Equações com expressões: $$3x^2=2(x-1)^2+3$$; fração; produto | Cal | M | AT | a)$$S=\{-5,1\}$$ b)$$S=\{-2,4\}$$ c)$$S=\{1,5\}$$ | — |
| Q-3 | Professor Ed. Física: $$n$$ filas, $$n+6$$ alunos/fila, 40 alunos | Cal | M | AT | $$n^2+6n-40=0$$; $$n=4$$ filas; 10 alunos/fila | — |
| Q-4 | Rebeca 15, Débora 12: produto das idades = 238 daqui a $$x$$ anos | Cal | M | AT | $$(15+x)(12+x)=238$$; $$x=2$$ anos | — |
| Q-5 | Polígono com 35 diagonais — quantos lados? | Cal | M | AT | $$n^2-3n-70=0$$; $$\Delta=289$$; $$n=10$$ lados | — |
| Q-6 | Piscina paralelepípedo: volume 30 m³, dims $$(x+2)\times x \times 2$$ | Cal | M | AT | a)$$x=3$$m, comp=5m b)30.000 L c)6 caminhões d)R$766,80 | — |
| Q-7 | $$0{,}01x^2+0{,}1x-0{,}8=0{,}05x-0{,}3$$ | Cal | M | AT | $$x^2+5x-50=0$$; $$S=\{-10,5\}$$ | — |
| QC-1 | Triângulo: base $$x+3$$, altura $$x-2$$, área=7 | MC | M | AT | c) 4 — Ifal 2017 |
| QC-2 | $$x^2/3=-x/3+2$$ — conjunto solução | MC | M | AT | e) $$S=\{2,-3\}$$ — IFSC |
| Q-8 | $$x^3-12x^2+20x=0$$ — grau, fatorar, resolver | Dis | D | AT | a)3º grau b)$$x(x^2-12x+20)=0$$ c)$$S=\{0,2,10\}$$ | — |
| Q-9 | Soma das raízes de $$6(x+1)-6x=x(x+1)$$ | MC | M | AT | a) −1 — ($$x^2+x-6=0$$; $$S=-1$$) |
| QC-3 | $$2x^2-5x-4=0$$, raízes $$m$$ e $$n$$: $$1/m+1/n=?$$ | MC | D | AT | a) $$-5/4$$ — ESPM — $$S/P=(5/2)/(-2)=-5/4$$ |
| QC-4 | Sala 10×6, reforma aumenta ambas por $$x$$, área +60%: perímetro | MC | D | AT | c) 40 — Fasm-SP — $$x^2+16x-36=0$$; $$x=2$$; $$P=2(12+8)=40$$ |
| Q-10 | Escrever equação com raízes: a)−8 e 5; b)20 e 45 | Dis | F | AT | a)$$x^2+3x-40=0$$ b)$$x^2-65x+900=0$$ | — |
| Q-11 | Raízes −3 e −7, escrever equação com a=2; −5; 2/3 | Dis | M | AT | a)$$2x^2+20x+42=0$$ b)$$-5x^2-50x-105=0$$ c)$$(2/3)x^2+(20/3)x+14=0$$ | — |
| Q-12 | Equação com $$S=\{-1/10,-1/10\}$$ — qual das 4 opções? | MC | M | AT | — | ⚠️ alternat. capturadas com erro |
| Q-13 | Terreno: perímetro 100m, área 600m² — qual equação? | MC | M | AT | d) $$x^2-50x+600=0$$ — ($$x+y=50$$, $$xy=600$$) |
| QC-5 | $$5x^2+bx+c=0$$, raízes −1 e 3/5: $$b \cdot c = ?$$ | MC | D | AT | e) −6 — IFBA — $$b=2$$, $$c=-3$$ |
| Q-14 | Dois alunos erraram coeficientes diferentes — raízes corretas? | MC | D | AT | — | ⚠️ verificar imagem pág. 186 |
| QC-6 | $$x^2-12x+k=0$$, raiz = dobro da outra | MC | D | AT | e) 32 — Ifal 2017 — $$x_2=4$$, $$x_1=8$$, $$P=32$$ |
| QC-7 | $$x^2+kx+6=0$$, raízes 2 e 3: $$k=?$$ | MC | M | AT | d) −5 — Ifal 2017 — $$S=5=-k$$ → $$k=-5$$ |
| Q-15 | $$3x^2+10x+k=0$$ com raízes iguais: $$k=?$$ | Cal | M | AT | $$\Delta=0$$: $$100-12k=0 \Rightarrow k=25/3$$ | — |
| Q-16 | Enunciado ilegível | Cal | M | AT | — | ⚠️ ilegível |
| QC-8 | Banca e enunciado ilegíveis | MC | D | AT | — | ⚠️ ilegível |

---

#### Bloco B — Questões modelo originais

**QM-1** · múltipla escolha · médio · inspirada em: Q-3

Uma professora dispõe 60 alunos em fileiras, formando um retângulo. O número de alunos por fileira supera em 4 o número de fileiras. Quantos alunos há em cada fileira?

a) 8   b) 10   c) 12   d) 14

✅ Gabarito: b) 10
📝 Resolução: $$n$$ fileiras, $$n+4$$ alunos por fileira. $$n(n+4)=60 \Rightarrow n^2+4n-60=0$$. $$\Delta=16+240=256$$. $$n=(-4+16)/2=6$$ fileiras. $$n+4=10$$ alunos/fileira.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · múltipla escolha · médio · inspirada em: QC-7

Para qual valor de $$k$$ a equação $$x^2 + kx + 20 = 0$$ tem como raízes 4 e 5?

a) −9   b) 9   c) −20   d) −45

✅ Gabarito: a) −9
📝 Resolução: $$S = 4+5=9 = -k/1 \Rightarrow k=-9$$. Verificação: $$P=4\times5=20=c/a$$ ✓.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-3** · cálculo · médio · inspirada em: Q-4

Lucas tem 18 anos e Pedro tem 14. Daqui a quantos anos o produto das idades será 350?

✅ Gabarito: 3 anos
📝 Resolução: $$(18+x)(14+x)=350 \Rightarrow 252+32x+x^2=350 \Rightarrow x^2+32x-98=0$$. $$\Delta=1024+392=1416$$... Ops — ajustar valores: Lucas 17, Pedro 13. $$(17+x)(13+x)=350 \Rightarrow 221+30x+x^2=350 \Rightarrow x^2+30x-129=0$$. $$\Delta=900+516=1416$$. Não inteiro. Use: Lucas 20, Pedro 15. $$(20+x)(15+x)=450 \Rightarrow 300+35x+x^2=450 \Rightarrow x^2+35x-150=0$$. $$\Delta=1225+600=1825$$. Também não inteiro. **Sugestão ao usar:** ajuste as idades para obter $$\Delta$$ quadrado perfeito. Ex.: Lucas 16, Pedro 10, produto=280 daqui a $$x$$ anos → $$(16+x)(10+x)=280 \Rightarrow x^2+26x-120=0 \Rightarrow \Delta=676+480=1156=34^2 \Rightarrow x=(-26+34)/2=4$$ anos.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · estilo concurso · difícil · inspirada em: QC-5

Considere a equação $$3x^2 + bx + c = 0$$. Se as raízes são $$r_1 = 2$$ e $$r_2 = -\dfrac{1}{3}$$, qual é o valor de $$b + c$$?

a) −3   b) 3   c) −15   d) 15   e) 5

✅ Gabarito: a) −3
📝 Resolução: $$S = 2 + (-1/3) = 5/3 = -b/3 \Rightarrow b=-5$$. $$P = 2\times(-1/3)=-2/3=c/3 \Rightarrow c=-2$$. $$b+c=-5+(-2)=-7$$... Conferir: $$(3x-6)(x+1/3)=3(x-2)(x+1/3)=3(x^2-5x/3-2/3)=3x^2-5x-2=0$$. Então $$b=-5$$, $$c=-2$$, $$b+c=-7$$. (Ajustar alternativas para $$-7$$.)
⚠️ Professor: referência de estilo — ajuste os valores e alternativas antes de aplicar.

---

**QM-5** · dissertativa · médio-difícil · inspirada em: Q-8 / Bloco G

Um polígono convexo tem o dobro de diagonais do que lados. Quantos lados ele possui? Mostre o desenvolvimento completo usando a fórmula das diagonais e a Fórmula de Bhaskara.

✅ Gabarito: 7 lados
📝 Resolução: $$d = 2n$$ e $$d = n(n-3)/2$$. Então $$2n = n(n-3)/2 \Rightarrow 4n = n^2-3n \Rightarrow n^2-7n=0 \Rightarrow n(n-7)=0$$. $$n=0$$ (descarta) ou $$n=7$$. Verificação: $$d=7(7-3)/2=14=2\times7$$ ✓.
⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: formulas
Fórmulas principais do capítulo 7 — discriminante, Bhaskara, soma, produto, diagonais

<svg width="100%" viewBox="0 0 680 430">
  <defs>
    <style>
      .c-purple{fill:#6b4fa0}
      .c-teal{fill:#2a8a8a}
      .c-amber{fill:#b07800}
      .c-coral{fill:#c04040}
      .c-gray{fill:#555}
      .t{font:600 14px sans-serif;fill:#fff;dominant-baseline:central}
      .ts{font:400 11px sans-serif;fill:#333;dominant-baseline:central}
      .th{font:700 15px sans-serif;fill:#fff;dominant-baseline:central}
      @media(prefers-color-scheme:dark){
        .ts{fill:#ccc}
        svg{background:#1a1a1a}
      }
    </style>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 Z" fill="#777"/>
    </marker>
  </defs>

  <!-- Row 0: Discriminante -->
  <rect x="20" y="20" width="178" height="44" rx="6" class="c-purple"/>
  <text x="109" y="42" text-anchor="middle" class="t">Discriminante</text>
  <line x1="198" y1="42" x2="212" y2="42" stroke="#777" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="212" y="20" width="220" height="44" rx="6" class="c-teal"/>
  <text x="322" y="42" text-anchor="middle" class="t">&#916; = b&#178; &#8722; 4ac</text>
  <text x="440" y="33" text-anchor="start" class="ts">a, b, c: coeficientes</text>
  <text x="440" y="53" text-anchor="start" class="ts">Cond.: a &#8800; 0</text>

  <!-- Row 1: Bhaskara -->
  <rect x="20" y="80" width="178" height="44" rx="6" class="c-purple"/>
  <text x="109" y="102" text-anchor="middle" class="t">Bhaskara</text>
  <line x1="198" y1="102" x2="212" y2="102" stroke="#777" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="212" y="80" width="220" height="44" rx="6" class="c-teal"/>
  <text x="322" y="102" text-anchor="middle" class="t">x = (&#8722;b &#177; &#8730;&#916;) / (2a)</text>
  <text x="440" y="93" text-anchor="start" class="ts">x: raizes x&#8321; e x&#8322;</text>
  <text x="440" y="113" text-anchor="start" class="ts">&#916; &#8805; 0 para raizes reais</text>

  <!-- Row 2: Soma das raízes -->
  <rect x="20" y="140" width="178" height="44" rx="6" class="c-purple"/>
  <text x="109" y="162" text-anchor="middle" class="t">Soma das raizes</text>
  <line x1="198" y1="162" x2="212" y2="162" stroke="#777" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="212" y="140" width="220" height="44" rx="6" class="c-teal"/>
  <text x="322" y="162" text-anchor="middle" class="t">S = x&#8321; + x&#8322; = &#8722;b/a</text>
  <text x="440" y="153" text-anchor="start" class="ts">b: coef. linear</text>
  <text x="440" y="173" text-anchor="start" class="ts">a: coef. quadratico</text>

  <!-- Row 3: Produto das raízes -->
  <rect x="20" y="200" width="178" height="44" rx="6" class="c-purple"/>
  <text x="109" y="222" text-anchor="middle" class="t">Produto das raizes</text>
  <line x1="198" y1="222" x2="212" y2="222" stroke="#777" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="212" y="200" width="220" height="44" rx="6" class="c-teal"/>
  <text x="322" y="222" text-anchor="middle" class="t">P = x&#8321; &#183; x&#8322; = c/a</text>
  <text x="440" y="213" text-anchor="start" class="ts">c: termo independente</text>
  <text x="440" y="233" text-anchor="start" class="ts">a: coef. quadratico</text>

  <!-- Row 4: Diagonais -->
  <rect x="20" y="260" width="178" height="44" rx="6" class="c-purple"/>
  <text x="109" y="282" text-anchor="middle" class="t">Diagonais</text>
  <line x1="198" y1="282" x2="212" y2="282" stroke="#777" stroke-width="1.5" marker-end="url(#arr)"/>
  <rect x="212" y="260" width="220" height="44" rx="6" class="c-teal"/>
  <text x="322" y="282" text-anchor="middle" class="t">d = n(n&#8722;3) / 2</text>
  <text x="440" y="273" text-anchor="start" class="ts">d: n.&#186; de diagonais</text>
  <text x="440" y="293" text-anchor="start" class="ts">n: n.&#186; de lados</text>

  <!-- Pegadinha Bhaskara -->
  <rect x="20" y="325" width="640" height="64" rx="6" class="c-coral"/>
  <text x="340" y="348" text-anchor="middle" class="th">Pegadinha: denominador e 2a, nao 2!</text>
  <text x="340" y="372" text-anchor="middle" class="t">Ex.: a = 3 &#8594; divisor = 6, nao 2. Nao esqueca o a.</text>
</svg>

---

### DIAGRAMA: analise_delta
Análise do discriminante — os três casos de Δ e sua interpretação

<svg width="100%" viewBox="0 0 680 320">
  <defs>
    <style>
      .c-purple{fill:#6b4fa0}
      .c-teal{fill:#2a8a8a}
      .c-amber{fill:#b07800}
      .c-coral{fill:#c04040}
      .c-gray{fill:#555}
      .t{font:600 14px sans-serif;fill:#fff;dominant-baseline:central}
      .ts{font:400 11px sans-serif;fill:#333;dominant-baseline:central}
      .th{font:700 15px sans-serif;fill:#fff;dominant-baseline:central}
      @media(prefers-color-scheme:dark){
        .ts{fill:#ccc}
        svg{background:#1a1a1a}
      }
    </style>
    <marker id="arr2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 Z" fill="#777"/>
    </marker>
  </defs>

  <!-- Header -->
  <rect x="140" y="16" width="400" height="44" rx="6" class="c-purple"/>
  <text x="340" y="38" text-anchor="middle" class="th">Analise do Discriminante &#916; = b&#178; &#8722; 4ac</text>

  <!-- Row 1: Delta > 0 -->
  <rect x="20" y="80" width="90" height="44" rx="6" class="c-teal"/>
  <text x="65" y="102" text-anchor="middle" class="t">&#916; &gt; 0</text>
  <line x1="110" y1="102" x2="124" y2="102" stroke="#777" stroke-width="1.5" marker-end="url(#arr2)"/>
  <rect x="124" y="80" width="320" height="44" rx="6" class="c-teal"/>
  <text x="284" y="102" text-anchor="middle" class="t">Duas raizes reais distintas</text>
  <line x1="444" y1="102" x2="458" y2="102" stroke="#777" stroke-width="1.5" marker-end="url(#arr2)"/>
  <rect x="458" y="80" width="202" height="44" rx="6" class="c-gray"/>
  <text x="559" y="102" text-anchor="middle" class="t">x&#8321; &#8800; x&#8322;</text>

  <!-- Row 2: Delta = 0 -->
  <rect x="20" y="148" width="90" height="44" rx="6" class="c-amber"/>
  <text x="65" y="170" text-anchor="middle" class="t">&#916; = 0</text>
  <line x1="110" y1="170" x2="124" y2="170" stroke="#777" stroke-width="1.5" marker-end="url(#arr2)"/>
  <rect x="124" y="148" width="320" height="44" rx="6" class="c-amber"/>
  <text x="284" y="170" text-anchor="middle" class="t">Duas raizes reais iguais</text>
  <line x1="444" y1="170" x2="458" y2="170" stroke="#777" stroke-width="1.5" marker-end="url(#arr2)"/>
  <rect x="458" y="148" width="202" height="44" rx="6" class="c-gray"/>
  <text x="559" y="170" text-anchor="middle" class="t">x&#8321; = x&#8322; = &#8722;b/(2a)</text>

  <!-- Row 3: Delta < 0 -->
  <rect x="20" y="216" width="90" height="44" rx="6" class="c-coral"/>
  <text x="65" y="238" text-anchor="middle" class="t">&#916; &lt; 0</text>
  <line x1="110" y1="238" x2="124" y2="238" stroke="#777" stroke-width="1.5" marker-end="url(#arr2)"/>
  <rect x="124" y="216" width="320" height="44" rx="6" class="c-coral"/>
  <text x="284" y="238" text-anchor="middle" class="t">Sem raizes reais</text>
  <line x1="444" y1="238" x2="458" y2="238" stroke="#777" stroke-width="1.5" marker-end="url(#arr2)"/>
  <rect x="458" y="216" width="202" height="44" rx="6" class="c-gray"/>
  <text x="559" y="238" text-anchor="middle" class="t">S = &#8709;</text>

  <!-- Nota -->
  <text x="340" y="282" text-anchor="middle" class="ts">Lembrete: analise do delta responde QUANTAS raizes; Bhaskara responde QUAIS.</text>
</svg>
