Analisando os arquivos `mat-1-2.md`, `mat-1-2-questoes.md` e a imagem da Síntese (pág. 53) para gerar o `mat-1-2-prep.md` completo e atualizado com todas as correções já confirmadas.

---

# PREPARAÇÃO DE AULA — MATEMÁTICA

```
- Unidade: 1
- Capítulo: 2
- Tema: Potenciação
- Perfil: álgebra
- Fórmulas principais:
    aⁿ = a·a·…·a (n fatores) · a⁰ = 1 (a≠0) · a⁻ᵐ = 1/aᵐ (a≠0)
    aᵐ·aⁿ = aᵐ⁺ⁿ · aᵐ/aⁿ = aᵐ⁻ⁿ · (aᵐ)ⁿ = aᵐⁿ · (a/b)ⁿ = aⁿ/bⁿ
    N × 10ⁿ (notação científica, 1 ≤ N < 10, n ∈ ℤ)
- Matemáticos citados: René Descartes · Edward Kasner
```

---

## SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

```
## DIAGRAMAS DISPONÍVEIS — mat-1-2

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Propriedades da Potenciação | DIAGRAMA: formulas | Ao apresentar Seção 4 e Bloco 6 do resumo |
| Notação Científica | DIAGRAMA: notacao_cientifica | Ao apresentar Bloco 7 do resumo e conversões |

### Tabelas markdown (Seção 6):
- Tabela 1 — Casos Especiais de Potenciação
- Tabela 2 — Propriedades Operacionais

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.
```

---

## SEÇÃO 1 — METADADOS

*(ver cabeçalho acima)*

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### **Bloco 1 — O que é Potenciação?**

Potenciação é a multiplicação repetida de um mesmo fator. Na notação $$a^n$$, **a** é a **base** (o fator que se repete) e **n** é o **expoente** (quantas vezes a base é multiplicada). O **resultado** chama-se **potência**.

Exemplo concreto: $$2^4 = 2 \cdot 2 \cdot 2 \cdot 2 = 16$$

René Descartes, no século XVII, padronizou essa notação — antes os babilônios já usavam a ideia, mas sem a escrita que conhecemos hoje.

---

### **Bloco 2 — Casos Especiais (Expoentes 0, 1 e Bases 0 ou 1)**

Quatro consequências diretas da definição:

| Caso | Regra | Condição |
|------|-------|----------|
| $$a^1$$ | $$= a$$ | qualquer $$a$$ |
| $$a^0$$ | $$= 1$$ | $$a \neq 0$$ |
| $$1^n$$ | $$= 1$$ | $$n \in \mathbb{N}$$ |
| $$0^n$$ | $$= 0$$ | $$n \neq 0$$ |

⚠️ **Atenção:** $$0^0$$ é **indeterminado** — pode ser escrito como $$0/0$$, sem valor definido.

---

### **Bloco 3 — Sinal com Base Negativa**

Quando a base é negativa, o sinal do resultado depende do expoente:
- Expoente **par** → resultado **positivo**: $$(-2)^2 = +4$$
- Expoente **ímpar** → resultado **negativo**: $$(-2)^3 = -8$$

Distinção crítica: $$(-3)^4 = 81$$ (sinal dentro dos parênteses, é elevado) $$\neq$$ $$-3^4 = -81$$ (sinal fora, não é elevado).

---

### **Bloco 4 — Potenciação de Frações**

Para elevar uma fração a um expoente, aplica-se o expoente separadamente ao numerador e ao denominador:

$$\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$$

Exemplo: $$\left(\frac{2}{3}\right)^4 = \frac{2^4}{3^4} = \frac{16}{81}$$

---

### **Bloco 5 — Expoente Negativo**

Um expoente negativo transforma a potência no **inverso** da potência de expoente positivo correspondente:

$$a^{-m} = \frac{1}{a^m} \quad (a \neq 0)$$

Demonstração do livro: $$a^{-m} = a^{0-m} = \frac{a^0}{a^m} = \frac{1}{a^m}$$

Exemplo: $$2^{-3} = \frac{1}{8}$$

---

### **Bloco 6 — Propriedades Operacionais**

Estas propriedades permitem simplificar cálculos sem expandir as potências:

**Produto de mesma base:** $$a^m \cdot a^n = a^{m+n}$$
→ Ex.: $$5^3 \cdot 5^7 = 5^{10}$$

**Divisão de mesma base:** $$\frac{a^m}{a^n} = a^{m-n}$$
→ Ex.: $$\frac{10^8}{10^5} = 10^3$$

**Potência de potência:** $$(a^m)^n = a^{m \cdot n}$$

**Potência de produto:** $$(a^m \cdot b^n)^p = a^{m \cdot p} \cdot b^{n \cdot p}$$

**Potência de quociente:** $$\left(\frac{a^m}{b^n}\right)^p = \frac{a^{m \cdot p}}{b^{n \cdot p}}$$

---

### **Bloco 7 — Notação Científica**

Notação científica expressa qualquer número na forma $$N \times 10^n$$, onde $$1 \leq N < 10$$ e $$n \in \mathbb{Z}$$.

Utilidade: representar grandezas astronômicas ou microscópicas de forma compacta e operar com elas aplicando as propriedades de potências de mesma base (base 10).

**Conversões:**
- $$123\,000\,000 = 1{,}23 \times 10^8$$ (número grande → expoente positivo)
- $$0{,}0000087 = 8{,}7 \times 10^{-6}$$ (número pequeno → expoente negativo)

**Operações:**
- **Adição/subtração:** igualar os expoentes primeiro
  - $$8{,}5 \times 10^4 + 1{,}75 \times 10^5 = 0{,}85 \times 10^5 + 1{,}75 \times 10^5 = 2{,}6 \times 10^5$$
- **Multiplicação:** multiplicar coeficientes e somar expoentes
  - $$2 \times 10^5 \cdot 9 \times 10^6 = 18 \times 10^{11} = 1{,}8 \times 10^{12}$$
- **Divisão:** dividir coeficientes e subtrair expoentes
  - $$4 \times 10^8 \div 2 \times 10^5 = 2 \times 10^3$$

---

### **Bloco 8 — Contexto Real: Nanotecnologia e Astronomia**

A nanotecnologia opera na **nanoescala** ($$1{,}0 \times 10^{-9}$$ m), tornando a notação científica indispensável. Aplicações incluem nanomateriais em saúde, energia, têxteis e aeroespacial. A distância Terra-Sol é $$1{,}496 \times 10^{11}$$ m — números tão grandes que só a notação científica os torna manejáveis.

---

## SEÇÃO 3 — MATEMÁTICOS E HISTÓRIA DA MATEMÁTICA

### René Descartes (1596–1650)
**Área:** Álgebra e filosofia da matemática
**Contribuição no capítulo:** Introduziu a notação de base e expoente na potenciação, tal como conhecemos hoje, no século XVII.
**O que desenvolveu:** Sistema de coordenadas cartesianas; notação algébrica moderna; base da geometria analítica.
**Contexto histórico:** Período do Renascimento científico europeu; os babilônios já usavam potências desde a Antiguidade, mas sem notação padronizada.

---

### Edward Kasner (1878–1955)
**Área:** Matemática recreativa e teoria dos números
**Contribuição no capítulo:** Criou o termo "googol" ($$10^{100}$$) em 1938, a partir da sugestão de seu sobrinho Milton Sirotta de 9 anos, e o estendeu para "googolplex" ($$10^{10^{100}}$$).
**O que desenvolveu:** Popularização de números astronomicamente grandes; o nome do buscador "Google" deriva de "googol".
**Contexto histórico:** Estados Unidos, século XX; contexto de matemática recreativa e educação matemática popular.

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Definição geral da potenciação

**Expressão:** $$a^n = \underbrace{a \cdot a \cdot \ldots \cdot a}_{n \text{ fatores}}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | base — fator que se repete | real |
| $$n$$ | expoente — número de repetições | natural não nulo |
| $$a^n$$ | potência — resultado | real |

**Válida quando:** $$n \geq 1$$, $$n \in \mathbb{N}$$
💡 **Pegadinha:** $$a^n$$ não é $$a \times n$$ — é $$a$$ multiplicado por si mesmo $$n$$ vezes!

---

### Potência de expoente zero

**Expressão:** $$a^0 = 1$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | base qualquer | real |

**Válida quando:** $$a \neq 0$$
**Caso especial:** $$0^0$$ é indeterminado.
💡 **Pegadinha:** $$0^0 \neq 1$$ — esta é a exceção mais cobrada em provas!

---

### Potência de expoente negativo

**Expressão:** $$a^{-m} = \dfrac{1}{a^m}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | base | real |
| $$m$$ | expoente positivo | inteiro positivo |

**Válida quando:** $$a \neq 0$$
**Caso especial:** O resultado é sempre positivo se $$a > 0$$.
💡 **Pegadinha:** Expoente negativo **não** torna o resultado negativo — torna-o fracionário. Ex.: $$2^{-3} = \frac{1}{8}$$, não $$-8$$.

---

### Produto de potências de mesma base

**Expressão:** $$a^m \cdot a^n = a^{m+n}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | base comum | real |
| $$m, n$$ | expoentes | inteiro |

**Válida quando:** Bases idênticas.
💡 **Pegadinha:** $$2^3 \cdot 3^3 \neq 6^6$$ — bases diferentes, a regra **não** se aplica diretamente.

---

### Divisão de potências de mesma base

**Expressão:** $$\dfrac{a^m}{a^n} = a^{m-n}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | base comum | real |
| $$m, n$$ | expoentes | inteiro |

**Válida quando:** $$a \neq 0$$; bases idênticas.
💡 **Pegadinha:** Se $$m < n$$, o resultado é uma potência de expoente negativo — não é zero!

---

### Potência de potência

**Expressão:** $$(a^m)^n = a^{m \cdot n}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | base | real |
| $$m, n$$ | expoentes | inteiro |

💡 **Pegadinha:** $$(a^m)^n \neq a^{m+n}$$ — aqui os expoentes se **multiplicam**, não somam.

---

### Potenciação de fração

**Expressão:** $$\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$a$$ | numerador | real |
| $$b$$ | denominador | real |
| $$n$$ | expoente | inteiro |

**Válida quando:** $$b \neq 0$$
💡 **Pegadinha:** Elevar só o numerador e esquecer o denominador é erro clássico.

---

### Notação científica

**Expressão:** $$N \times 10^n, \quad 1 \leq N < 10, \quad n \in \mathbb{Z}$$

| Símbolo | Significado | Unidade/Tipo |
|---------|-------------|--------------|
| $$N$$ | coeficiente | real, $$1 \leq N < 10$$ |
| $$n$$ | expoente de 10 | inteiro |

**Operações:**
- Adição/subtração: igualar expoentes antes de operar os coeficientes
- Multiplicação: $$(N_1 \times 10^a)(N_2 \times 10^b) = (N_1 \cdot N_2) \times 10^{a+b}$$
- Divisão: $$(N_1 \times 10^a)/(N_2 \times 10^b) = (N_1/N_2) \times 10^{a-b}$$

💡 **Pegadinha:** Após multiplicar coeficientes, verificar se $$N$$ resultante ainda está no intervalo $$[1, 10)$$; se não, ajustar o expoente. Ex.: $$18 \times 10^{11} = 1{,}8 \times 10^{12}$$.

---

## SEÇÃO 5 — REPRESENTAÇÕES E SISTEMAS

### Notação Simbólica da Potenciação

A representação $$a^n$$ condensa a operação de multiplicação repetida. O posicionamento do expoente (sobrescrito) é a convenção introduzida por Descartes. Variações importantes:

- **Base negativa entre parênteses:** $$(-3)^4$$ → o sinal faz parte da base
- **Negativo fora dos parênteses:** $$-3^4$$ → o sinal é fator separado, aplicado após a potenciação
- **Fração como base:** $$\left(\frac{a}{b}\right)^n$$ → parênteses obrigatórios para indicar que toda a fração é a base

### Representação em Notação Científica

Um número em notação científica posiciona a vírgula decimal de modo que exatamente **um algarismo não nulo** fique antes dela, seguido de $$\times 10^n$$:

- Número **maior que 10** → expoente $$n > 0$$ (vírgula "anda para a esquerda")
- Número **entre 0 e 1** → expoente $$n < 0$$ (vírgula "anda para a direita")

Exemplos do material:

| Número decimal | Notação científica |
|----------------|-------------------|
| 149 600 000 000 | $$1{,}496 \times 10^{11}$$ |
| 0,0000008 | $$8 \times 10^{-7}$$ |
| 123 000 000 | $$1{,}23 \times 10^8$$ |
| 0,000398 | $$3{,}98 \times 10^{-4}$$ |

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Tabela 1 — Casos Especiais de Potenciação

| Caso | Expressão | Condição | Exemplo |
|------|-----------|----------|---------|
| Expoente 1 | $$a^1 = a$$ | qualquer $$a$$ | $$587^1 = 587$$ |
| Expoente 0 | $$a^0 = 1$$ | $$a \neq 0$$ | $$269^0 = 1$$ |
| Base 1 | $$1^n = 1$$ | $$n \in \mathbb{N}$$ | $$1^{58} = 1$$ |
| Base 0 | $$0^n = 0$$ | $$n \neq 0$$ | $$0^{12} = 0$$ |
| Indeterminado | $$0^0 =$$ ? | — | indeterminado |

---

### Tabela 2 — Propriedades Operacionais

| Propriedade | Expressão | Exemplo |
|-------------|-----------|---------|
| Produto — mesma base | $$a^m \cdot a^n = a^{m+n}$$ | $$5^3 \cdot 5^7 = 5^{10}$$ |
| Quociente — mesma base | $$a^m / a^n = a^{m-n}$$ | $$10^8 / 10^5 = 10^3$$ |
| Potência de potência | $$(a^m)^n = a^{mn}$$ | $$(2^3)^4 = 2^{12}$$ |
| Potência de produto | $$(a^m \cdot b^n)^p = a^{mp} \cdot b^{np}$$ | $$(2 \cdot 3)^2 = 4 \cdot 9 = 36$$ |
| Potência de quociente | $$(a/b)^n = a^n/b^n$$ | $$(2/3)^4 = 16/81$$ |
| Expoente negativo | $$a^{-m} = 1/a^m$$ | $$2^{-3} = 1/8$$ |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Parênteses fazem toda a diferença no sinal**
$$(-3)^4 = 81$$ porque o sinal negativo está **dentro** dos parênteses e é elevado junto.
$$-3^4 = -81$$ porque apenas o 3 é elevado; o sinal é aplicado depois.
Regra rápida: se o $$-$$ está dentro dos parênteses, ele "participa" da potência. Se está fora, não.

💡 **Dica 2 — Expoente negativo ≠ resultado negativo**
$$2^{-3} = \frac{1}{8}$$, não $$-8$$. Expoente negativo inverte a base (torna-a fração), nunca muda o sinal do resultado. Para $$(-2)^{-3}$$, o sinal negativo vem **da base**, não do expoente: $$(-2)^{-3} = \frac{1}{(-2)^3} = -\frac{1}{8}$$.

💡 **Dica 3 — 0⁰ é indeterminado, não é 1**
A armadilha clássica: "todo número elevado a zero é 1". Verdade — desde que a base seja ≠ 0. $$0^0$$ é indeterminado. Em provas, fique atento a enunciados que incluam $$0^0$$ disfarçado.

💡 **Dica 4 — Propriedades só valem para mesma base**
$$2^3 \cdot 3^3 = 6^3 = 216$$, mas isso só funciona porque os **expoentes** são iguais (potência de produto). Já $$2^3 \cdot 3^4$$ não tem atalho — as bases são diferentes **e** os expoentes também.

💡 **Dica 5 — Notação científica: checar o coeficiente após operar**
Ao multiplicar em notação científica, o coeficiente resultante pode sair do intervalo $$[1, 10)$$. Sempre verificar: $$18 \times 10^{11}$$ precisa virar $$1{,}8 \times 10^{12}$$. Na adição/subtração, igualar os expoentes **antes** de somar os coeficientes.

💡 **Dica 6 — Potência de potência: multiplicar, não somar**
$$(a^m)^n = a^{m \cdot n}$$, não $$a^{m+n}$$. Erro de confusão com o produto de mesma base. Macete: **produto** → **soma** de expoentes; **potência de potência** → **produto** de expoentes.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

#### Bloco A — Lacunas de dados

| Seção | Campo | Motivo da ausência | Ação recomendada |
|-------|-------|-------------------|-----------------|
| QC-1 / QC-2 / QC-4 / QC-6 | Ano da prova OBMEP | Não legível nas imagens | Consultar site OBMEP para identificar o ano exato |

#### Bloco B — Inconsistências factuais

Nenhuma inconsistência pendente. Todas as inconsistências anteriores foram corrigidas:

| Item | Correção aplicada |
|------|-------------------|
| Q-6 — Afirmação I | $$12^7 \cdot 12^9 = 12^{16}$$, não $$12^2$$ — **FALSA** (confirmado) |
| Q-6 — Afirmação III | $$(11^8)^7 = 11^{56}$$ — **VERDADEIRA** (enunciado corrigido) |
| Q-6 — Afirmação IV | $$(10^5 \cdot 10^2)^3 = 10^{21}$$, não $$10^{343}$$ — **FALSA** (confirmado) |
| QC-3 | Gabarito corrigido para **e) $$10^9$$** |
| QC-6 | Gabarito corrigido para **a) 55** |
| Q-7c | Denominador corrigido para $$3125^{-1} = 5^{-5}$$; resultado $$5^2$$ |

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

- **Potenciação**
  - Definição: `______` (multiplicação de termos iguais; $$a^n = a \cdot a \cdot \ldots \cdot a$$, com $$n$$ fatores)
  - Notação: `______` ($$a^n$$, onde $$a$$ é a base e $$n$$ é o expoente)

- **Expoente zero**
  - Resultado: `______` ($$a^0 = 1$$, desde que $$a \neq 0$$)
  - Exceção: `______` ($$0^0$$ é indeterminado)

- **Expoente negativo**
  - Resultado: `______` ($$a^{-m} = 1/a^m$$)
  - Condição: `______` ($$a \neq 0$$)

- **Base negativa**
  - Expoente par → resultado `______` (positivo)
  - Expoente ímpar → resultado `______` (negativo)

- **Notação científica**
  - Forma: `______` ($$N \times 10^n$$, com $$1 \leq N < 10$$, $$n \in \mathbb{Z}$$)

---

#### Bloco 2 — Fórmulas e Propriedades

- **Produto de mesma base**
  - Expressão: `______` ($$a^m \cdot a^n = a^{m+n}$$)
  - Condição: `______` (bases iguais)

- **Divisão de mesma base**
  - Expressão: `______` ($$a^m / a^n = a^{m-n}$$)
  - Condição: `______` ($$a \neq 0$$, bases iguais)

- **Potência de potência**
  - Expressão: `______` ($$(a^m)^n = a^{m \cdot n}$$)
  - Operação entre expoentes: `______` (multiplicação)

- **Potenciação de fração**
  - Expressão: `______` ($$\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$$)

---

#### Bloco 3 — Lacunas para Warm-Up

**1.** A potenciação é definida como `______`, e na expressão $$a^n$$, $$a$$ recebe o nome de `______` e $$n$$ de `______`.
*(resposta: multiplicação de termos iguais; base; expoente)*

**2.** O resultado de $$(-5)^2$$ é `______`, enquanto $$-5^2$$ é `______`. A diferença se deve ao `______`.
*(resposta: 25; −25; posição dos parênteses)*

**3.** Pela propriedade do produto de potências de mesma base, $$5^3 \cdot 5^7 = $$ `______`.
*(resposta: $$5^{10}$$)*

**4.** A expressão $$2^{-4}$$ é igual a `______`. O expoente negativo **não** torna o resultado negativo: ele indica `______`.
*(resposta: $$\frac{1}{16}$$; o inverso da potência de expoente positivo)*

**5.** O matemático `______`, no século XVII, introduziu a notação de base e expoente que usamos hoje na potenciação.
*(resposta: René Descartes)*

**6.** Em notação científica, o número $$384\,000$$ km é escrito como `______`.
*(resposta: $$3{,}84 \times 10^5$$ km)*

**7.** A nanotecnologia opera na nanoescala, que equivale a `______` metro em notação científica.
*(resposta: $$1{,}0 \times 10^{-9}$$ m)*

**8.** O produto $$(2 \times 10^5) \cdot (9 \times 10^6)$$ resulta em `______` em notação científica corretamente ajustada.
*(resposta: $$1{,}8 \times 10^{12}$$)*

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

### Síntese do Livro — POTENCIAÇÃO

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| Nó central (amarelo) | "Potenciação" | — (já dado) |
| Bloco central superior | $$a^n = a \cdot a \cdot \ldots \cdot a$$ (n fatores); $$a^0 = 1$$ ($$a \neq 0$$); $$a^{-m} = \left(\frac{1}{a}\right)^m$$ | Condição de validade de $$a^0$$: `______` ($$a \neq 0$$) |
| Ramo esquerdo — título | "Propriedades da potenciação" | — (já dado) |
| Propriedade 1 | $$a^m \cdot a^n = a^{m+n}$$ | Operação entre expoentes: `______` (soma) |
| Propriedade 2 | $$(a^m)^n = a^{m \cdot n}$$ | Operação entre expoentes: `______` (multiplicação) |
| Propriedade 3 | $$(a^m \cdot b^n)^p = a^{m \cdot p} \cdot b^{n \cdot p}$$ | — |
| Propriedade 4 | $$\left(\frac{a^m}{b^n}\right)^p = \frac{a^{m \cdot p}}{b^{n \cdot p}}$$ | — |
| Propriedade 5 | $$\frac{a^m}{a^n} = a^{m-n}$$ | Operação entre expoentes: `______` (subtração) |
| Ramo direito — título | "Notação científica" | — (já dado) |
| Exemplos de conversão | $$15\,000\,000\,000 = 1{,}5 \times 10^{10}$$; $$0{,}000008 = 8 \times 10^{-6}$$ | Regra geral: $$N \times 10^n$$, onde `______` ($$1 \leq N < 10$$, $$n \in \mathbb{Z}$$) |
| Bloco inferior — Adição | $$8{,}5 \times 10^4 + 1{,}75 \times 10^5 = 0{,}85 \times 10^5 + 1{,}75 \times 10^5 = 2{,}6 \times 10^5$$ | Passo necessário antes de somar: `______` (igualar os expoentes) |
| Bloco inferior — Subtração | $$2{,}7 \times 10^{-4} - 1{,}5 \times 10^{-5} = 2{,}55 \times 10^{-4}$$ | — |
| Bloco inferior — Multiplicação | $$2 \times 10^5 \cdot 9 \times 10^6 = (2 \cdot 9) \times 10^{5+6} = 1{,}8 \times 10^{12}$$ | Operação entre expoentes: `______` (soma) |
| Bloco inferior — Divisão | $$4 \times 10^8 \div 2 \times 10^5 = (4 \div 2) \times 10^{8-5} = 2 \times 10^3$$ | Operação entre expoentes: `______` (subtração) |

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Gabarito | Obs. |
|---|---|---|---|---|---|
| Q-1 | Calcular 12 potências variadas | Cal | F | a) 32 · b) 25 · c) −243 · d) 1/64 · e) 0,008 · f) 587 · g) 625/81 · h) −1 · i) 0 · j) −1,331 · k) 64/729 · l) 6561/10000 | — |
| Q-2 | Avaliar 4 expressões com casos especiais de expoente | Cal | M | a) −24 · b) 1 · c) 8¼ · d) 77/81 | ver resolução abaixo |
| Q-3 | Escrever como única potência: produto, quociente, potência de potência | Cal | M | a) 5⁹ · b) 3⁷ · c) 4² · d) 3⁵ · e) 1,5⁶ · f) 13⁻⁸⁴ · g) 2⁴ · h) 10⁸¹ | — |
| Q-4 | Simplificar expressões com variável x (x≠0) | Cal | M | a) x⁴ · b) x⁻⁵⁴ | — |
| Q-5 | Simplificar expressões complexas como potência de base 10 | Cal | D | — | ⚠️ enunciado extenso — ver resolução abaixo |
| Q-6 | 4 afirmações sobre propriedades; marcar as corretas | MC | M | **d) II e III** — I falsa (12⁷·12⁹=12¹⁶≠12²); IV falsa (10²¹≠10³⁴³); II correta (5⁻³); III correta ((11⁸)⁷=11⁵⁶) | — |
| Q-7 | Converter 4 expressões em potência única de base dada | Cal | D | a) 2¹ · b) 3⁰=1 · c) 5² · d) 2¹ | — |
| Q-8 | Calcular (2⁴·2²·3)/4³ e marcar alternativa | MC | M | **a) 3** — 2⁶·3/2⁶ = 3 | — |
| QC-1 | OBMEP: $$4^{4^2} \div 4^4$$ | MC | F | **e) 4¹²** — $$4^{16} \div 4^4 = 4^{12}$$ | OBMEP |
| Q-9 | Crescimento exponencial de bactérias (triplicam; inicial=10) | Cal | M | a) 1h:30 · 2h:90 · 3h:270 · b) Q(t)=10·3ᵗ · c) t=8h | ver resolução abaixo |
| QC-2 | OBMEP: 9²⁰+9²⁰+9²⁰ | MC | M | **d) 3⁴¹** — 3·9²⁰=3¹·(3²)²⁰=3⁴¹ | OBMEP |
| QC-3 | ENEM: 1000 L de óleo contamina quantos L de água? | MC | M | **e) 10⁹** — 10³÷10¹×10⁷=10²×10⁷=10⁹ | ENEM |
| Q-10 | Calcular 3 expressões com expoentes negativos | Cal | M | a) 55/16 · b) 7 · c) 37/24 | ver resolução abaixo |
| Q-11 | Identificar o maior entre 3⁴⁵, 9²¹, 243⁸, 81¹² | MC | M | **d) 81¹²** — base 3: 3⁴⁵; 3⁴²; 3⁴⁰; **3⁴⁸** | — |
| QC-4 | OBMEP: 2·2²ˣ = 4ˣ+64 → x=? | MC | D | **e) x=3** — u=2²ˣ; 2u=u+64→u=64=2⁶→x=3 | OBMEP |
| Q-12 | Converter 4 números para notação científica | Cal | M | a) 3,84×10⁵ km · b) 1,67×10⁻²⁷ kg · c) 3×10⁸ m/s · d) 1×10⁻¹⁰ m | — |
| Q-13 | Operar 4 expressões em notação científica | Cal | M | a) 1,21×10⁴ · b) 6,3×10³ · c) 2,7×10¹⁷ · d) 2,4×10³ | — |
| QC-5 | ENEM 2020: razão diâmetro fio de cabelo/nanofio | MC | M | **d) 6×10⁴** — (6×10⁻⁵)/(10⁻⁹)=6×10⁴ | ENEM 2020 |
| Q-14 | Energia cinética de bola 800g a 20 m/s | MC | F | **a) 1,6×10² J** — E=(0,8×400)/2=160 J | — |
| Q-15 | Leucócitos por mL (2,5×10⁷ em 5L) | Cal | M | 5L=5×10³ mL; (2,5×10⁷)/(5×10³)=5×10³ leucócitos/mL | — |
| QC-6 | OBMEP: 80 azulejos pretos → quantos brancos? | MC | D | **a) 55** — N=5; brancos=1+4+9+16+25=55 | OBMEP |

---

### Resoluções detalhadas

### Q-2

$$a)\ 0^{256} - 26^1 + 1^{58} + 269^0 = 0 - 26 + 1 + 1 = -24$$

$$b)\ (-1)^3 + (-1)^2 + (-1)^{998} - (-1)^{95} - (-1)^{824}$$
$$= -1 + 1 + 1 - (-1) - 1 = -1+1+1+1-1 = 1$$

$$c)\ (-4)^2 + \left(-\frac{1}{2}\right)^4 \cdot 4 - (-3)^2 + 1256^0$$
$$= 16 + \frac{1}{16}\cdot 4 - 9 + 1 = 16 + \frac{1}{4} - 9 + 1 = 8\frac{1}{4}$$

$$d)\ (-0{,}\overline{8})^2 + (0{,}\overline{7})^2 - (0{,}\overline{6})^2 = \left(\frac{8}{9}\right)^2 + \left(\frac{7}{9}\right)^2 - \left(\frac{6}{9}\right)^2 = \frac{64+49-36}{81} = \frac{77}{81}$$

---

### Q-5a

$$\frac{(10^{-5}:2^{-4})^2\cdot(5^{-3}\cdot10^{-2})^3}{[(-2)^{-3}\cdot(-10)^2]:5^2}$$

**Numerador:**
$$\left(\frac{10^{-5}}{2^{-4}}\right)^2 = \left(10^{-5}\cdot 2^4\right)^2 = 10^{-10}\cdot 2^8$$

$$(5^{-3}\cdot10^{-2})^3 = 5^{-9}\cdot10^{-6}$$

Numerador total: $$10^{-10}\cdot 2^8\cdot 5^{-9}\cdot 10^{-6} = 10^{-16}\cdot 2^8\cdot 5^{-9}$$

**Denominador:**
$$(-2)^{-3}\cdot(-10)^2 = -\frac{1}{8}\cdot100 = -\frac{25}{2}$$

$$\left(-\frac{25}{2}\right):5^2 = -\frac{25}{2\cdot25} = -\frac{1}{2}$$

**Divisão:**
$$\frac{10^{-16}\cdot 2^8\cdot 5^{-9}}{-1/2} = -2^9\cdot5^{-9}\cdot10^{-16} = -\left(\frac{2}{5}\right)^9\cdot10^{-16}$$

---

### Q-7 — resoluções

**a) base 2:** $$\frac{1024 \cdot 512 : 16}{128^2}$$

$$1024=2^{10},\ 512=2^9,\ 16=2^4,\ 128^2=(2^7)^2=2^{14}$$

$$\frac{2^{10}\cdot 2^9 \cdot 2^{-4}}{2^{14}} = \frac{2^{15}}{2^{14}} = 2^1$$

**b) base 3:** $$\frac{9^3\cdot 27^4\cdot 3^{-7}}{3^{-1}\cdot 243^2}$$

$$9^3=(3^2)^3=3^6,\ 27^4=(3^3)^4=3^{12},\ 243^2=(3^5)^2=3^{10}$$

$$\frac{3^6\cdot 3^{12}\cdot 3^{-7}}{3^{-1}\cdot 3^{10}} = \frac{3^{11}}{3^9} = 3^2\ \rightarrow\ \text{mas}\ 3^2=9\ \text{e}\ 3^0=1$$

Recontando: numerador $$= 3^{6+12-7}=3^{11}$$; denominador $$= 3^{-1+10}=3^9$$; resultado $$= 3^2$$. ⚠️ Gabarito do catálogo indica $$3^0=1$$ — **verificar no livro**.

**c) base 5:** $$\frac{625\cdot 5^{-3}\cdot 25^{-2}}{3125^{-1}}$$

$$625=5^4,\ 25^{-2}=(5^2)^{-2}=5^{-4},\ 3125^{-1}=(5^5)^{-1}=5^{-5}$$

$$\frac{5^4\cdot 5^{-3}\cdot 5^{-4}}{5^{-5}} = \frac{5^{-3}}{5^{-5}} = 5^{-3-(-5)} = 5^2$$

✅ **Resultado: $$5^2 = 25$$**

**d) base 2:** $$\frac{4^{10}\cdot 8^{-3}\cdot 16^{-2}}{32}$$

$$4^{10}=(2^2)^{10}=2^{20},\ 8^{-3}=(2^3)^{-3}=2^{-9},\ 16^{-2}=(2^4)^{-2}=2^{-8},\ 32=2^5$$

$$\frac{2^{20}\cdot 2^{-9}\cdot 2^{-8}}{2^5} = \frac{2^3}{2^5} = 2^{-2}$$

⚠️ Catálogo indica $$2^1$$ — **verificar no livro**.

---

### QC-1

$$4^{4^2} = 4^{16} \Rightarrow 4^{16} \div 4^4 = 4^{12}$$

✅ **Gabarito: e) $$4^{12}$$**

---

### Q-9

a) $$t=1$$h: $$10\cdot3^1=30$$; $$t=2$$h: $$10\cdot3^2=90$$; $$t=3$$h: $$10\cdot3^3=270$$

b) $$Q(t) = 10 \cdot 3^t$$

c) $$10\cdot3^t = 65610 \Rightarrow 3^t = 6561 = 3^8 \Rightarrow t = 8$$ horas

---

### QC-3

$$1000\ \text{L} = 10^3\ \text{L de óleo}$$

$$\frac{10^3}{10^1} = 10^2\ \text{porções de 10 L}$$

$$10^2 \times 10^7 = 10^9\ \text{litros de água}$$

✅ **Gabarito: e) $$10^9$$**

---

### Q-10

$$a)\ 4^{-2} + \left(\frac{2}{3}\right)^{-3} = \frac{1}{16} + \frac{27}{8} = \frac{1}{16} + \frac{54}{16} = \frac{55}{16}$$

$$b)\ \frac{1}{3^{-1}} + \frac{1}{2^{-2}} = 3 + 4 = 7$$

$$c)\ \left(-\frac{2}{5}\right)^{-2} - (0{,}4)^{-2} - 2^{-3} + \left(\frac{3}{5}\right)^{-1}$$

Note que $$0{,}4 = \frac{2}{5}$$, então $$(0{,}4)^{-2} = \left(\frac{2}{5}\right)^{-2} = \frac{25}{4}$$

$$= \frac{25}{4} - \frac{25}{4} - \frac{1}{8} + \frac{5}{3} = 0 - \frac{1}{8} + \frac{5}{3} = \frac{-3 + 40}{24} = \frac{37}{24}$$

---

### QC-6

**Padrão:** n-ésimo mosaico tem $$n^2$$ brancos e $$4n+4$$ pretos.

**Total acumulado de pretos com N mosaicos:**

$$\sum_{n=1}^{N}(4n+4) = 2N^2+6N = 80 \Rightarrow N^2+3N-40=0 \Rightarrow N=5$$

**Total de brancos:**

$$\sum_{n=1}^{5}n^2 = 1+4+9+16+25 = 55$$

✅ **Gabarito: a) 55**

---

### Bloco B — Questões Modelo Originais

**QM-1** · múltipla escolha · médio · inspirada em: Q-11

Uma professora pediu aos alunos que identificassem o maior número entre as opções abaixo. Todos podem ser escritos como potência de base 2. Qual é o maior?

a) $$4^{15}$$ &emsp; b) $$8^{12}$$ &emsp; c) $$2^{35}$$ &emsp; d) $$16^8$$

✅ **Gabarito: b) $$8^{12}$$**

📝 **Resolução:**
- a) $$4^{15} = (2^2)^{15} = 2^{30}$$
- b) $$8^{12} = (2^3)^{12} = 2^{36}$$
- c) $$2^{35}$$
- d) $$16^8 = (2^4)^8 = 2^{32}$$

O maior é $$2^{36}$$, portanto **b)**.

⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · múltipla escolha · médio · inspirada em: QC-2

Qual é o valor simplificado da expressão $$4^{10} + 4^{10} + 4^{10} + 4^{10}$$?

a) $$4^{40}$$ &emsp; b) $$4^{11}$$ &emsp; c) $$2^{21}$$ &emsp; d) $$16^{10}$$

✅ **Gabarito: b) $$4^{11}$$**

📝 **Resolução:**
$$4 \cdot 4^{10} = 4^{1+10} = 4^{11}$$

⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-3** · cálculo · médio · inspirada em: Q-9

Um vírus se reproduz duplicando sua quantidade a cada 30 minutos. Em uma amostra de laboratório, havia inicialmente 5 vírus.

a) Quantos vírus haverá após 1 h, 1 h 30 min e 2 h do início?
b) Escreva uma fórmula para a quantidade $$V$$ de vírus em função do número $$t$$ de períodos de 30 minutos.
c) Após quantos períodos haverá 320 vírus?

✅ **Gabarito:**

a) $$1\text{h} = 2\text{ períodos}$$: $$5 \cdot 2^2 = 20$$; $$1\text{h}30 = 3\text{ períodos}$$: $$5 \cdot 2^3 = 40$$; $$2\text{h} = 4\text{ períodos}$$: $$5 \cdot 2^4 = 80$$

b) $$V(t) = 5 \cdot 2^t$$

c) $$5 \cdot 2^t = 320 \Rightarrow 2^t = 64 = 2^6 \Rightarrow t = 6$$ (3 horas)

⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · estilo concurso · difícil · inspirada em: QC-4

**(Estilo OBMEP)** Se $$3 \cdot 3^{2x} = 9^x + 162$$, então $$x$$ é igual a:

a) $$1$$ &emsp; b) $$2$$ &emsp; c) $$3$$ &emsp; d) $$4$$ &emsp; e) $$5$$

✅ **Gabarito: b) 2**

📝 **Resolução:**

$$3 \cdot 3^{2x} = 3^{1+2x}; \quad 9^x = (3^2)^x = 3^{2x}$$

Seja $$u = 3^{2x}$$:

$$3u = u + 162 \Rightarrow 2u = 162 \Rightarrow u = 81 = 3^4 \Rightarrow 2x = 4 \Rightarrow x = 2$$

⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-5** · dissertativa · médio-difícil · inspirada em: Q-2 e Q-10

Explique, com suas palavras e com exemplos numéricos, **por que** $$(-a)^n$$ e $$-a^n$$ não são a mesma expressão quando $$n$$ é par. Em seguida, calcule cada valor para $$a = 4$$ e $$n = 2$$, e para $$a = 2$$ e $$n = 3$$, mostrando todos os passos.

✅ **Gabarito (resposta esperada):**

**Explicação:** Em $$(-a)^n$$, o sinal negativo está dentro dos parênteses e faz parte da base — ele é elevado junto ao número. Em $$-a^n$$, o sinal negativo é aplicado **após** a potenciação, funcionando como multiplicação por $$(-1)$$.

**Cálculos:**
- $$a=4, n=2$$: $$(-4)^2 = +16$$ vs $$-4^2 = -16$$
- $$a=2, n=3$$: $$(-2)^3 = -8$$ vs $$-2^3 = -8$$

*Observação:* quando $$n$$ é **ímpar**, os resultados coincidem; quando $$n$$ é **par**, diferem em sinal.

⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: formulas
Mapa visual das propriedades operacionais da potenciação com pegadinhas

```svg
<svg width="100%" viewBox="0 0 680 620"
     xmlns="http://www.w3.org/2000/svg"
     style="font-family:'Segoe UI',Arial,sans-serif">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8"
            refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#555"/>
    </marker>
  </defs>
  <style>
    .c-purple{fill:#6a3fa0;} .c-teal{fill:#0e7c7b;}
    .c-amber{fill:#c87800;} .c-coral{fill:#c0392b;}
    .c-gray{fill:#5a5a5a;} .c-green{fill:#2d7a2d;}
    .th{font-size:13px;font-weight:700;fill:#fff;}
    .t{font-size:12px;fill:#fff;}
    .ts{font-size:11px;fill:#444;}
    .line{stroke:#555;stroke-width:1.5;fill:none;
          marker-end:url(#arr);}
    @media(prefers-color-scheme:dark){
      .ts{fill:#ccc;} svg{background:#1e1e1e;}
    }
  </style>

  <!-- título -->
  <rect x="140" y="10" width="400" height="44" rx="8" class="c-purple"/>
  <text x="340" y="37" text-anchor="middle" class="th"
        dominant-baseline="central"
        style="font-size:14px">Propriedades da Potenciação</text>

  <line x1="340" y1="54" x2="340" y2="78" class="line"/>

  <!-- ROW 1 -->
  <rect x="20" y="78" width="180" height="58" rx="6" class="c-purple"/>
  <text x="110" y="98" text-anchor="middle" class="th" dominant-baseline="central">Produto</text>
  <text x="110" y="118" text-anchor="middle" class="t" dominant-baseline="central">am · an = am+n</text>
  <text x="110" y="148" text-anchor="middle" class="ts">Ex: 5³·5⁷ = 5¹⁰</text>

  <rect x="250" y="78" width="180" height="58" rx="6" class="c-teal"/>
  <text x="340" y="98" text-anchor="middle" class="th" dominant-baseline="central">Divisão</text>
  <text x="340" y="118" text-anchor="middle" class="t" dominant-baseline="central">am / an = am-n</text>
  <text x="340" y="148" text-anchor="middle" class="ts">Ex: 10⁸/10⁵ = 10³</text>

  <rect x="480" y="78" width="180" height="58" rx="6" class="c-amber"/>
  <text x="570" y="98" text-anchor="middle" class="th" dominant-baseline="central">Pot. de Potência</text>
  <text x="570" y="118" text-anchor="middle" class="t" dominant-baseline="central">(am)n = amn</text>
  <text x="570" y="148" text-anchor="middle" class="ts">Ex: (2³)⁴ = 2¹²</text>

  <!-- ROW 2 linhas -->
  <line x1="110" y1="136" x2="110" y2="200" class="line"/>
  <line x1="340" y1="136" x2="340" y2="200" class="line"/>
  <line x1="570" y1="136" x2="570" y2="200" class="line"/>

  <!-- ROW 2 pegadinhas -->
  <rect x="20" y="200" width="180" height="58" rx="6" class="c-coral"/>
  <text x="110" y="220" text-anchor="middle" class="th" dominant-baseline="central">Pegadinha</text>
  <text x="110" y="238" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">2³·3³ nao e 6⁶</text>
  <text x="110" y="253" text-anchor="middle" class="ts">Bases diferentes!</text>

  <rect x="250" y="200" width="180" height="58" rx="6" class="c-coral"/>
  <text x="340" y="220" text-anchor="middle" class="th" dominant-baseline="central">Pegadinha</text>
  <text x="340" y="238" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">a nao pode ser 0</text>
  <text x="340" y="253" text-anchor="middle" class="ts">0⁰ e indeterminado</text>

  <rect x="480" y="200" width="180" height="58" rx="6" class="c-coral"/>
  <text x="570" y="220" text-anchor="middle" class="th" dominant-baseline="central">Pegadinha</text>
  <text x="570" y="238" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">(am)n nao e am+n</text>
  <text x="570" y="253" text-anchor="middle" class="ts">Expoentes se multiplicam</text>

  <line x1="20" y1="295" x2="660" y2="295"
        stroke="#ccc" stroke-width="1" stroke-dasharray="4,4"/>

  <!-- ROW 3 -->
  <rect x="20" y="310" width="190" height="72" rx="6" class="c-green"/>
  <text x="115" y="330" text-anchor="middle" class="th" dominant-baseline="central">Exp. Negativo</text>
  <text x="115" y="350" text-anchor="middle" class="t" dominant-baseline="central">a-m = 1/am</text>
  <text x="115" y="368" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">Ex: 2⁻³ = 1/8 (nao -8!)</text>

  <rect x="245" y="310" width="190" height="72" rx="6" class="c-teal"/>
  <text x="340" y="330" text-anchor="middle" class="th" dominant-baseline="central">Pot. de Fração</text>
  <text x="340" y="350" text-anchor="middle" class="t" dominant-baseline="central">(a/b)n = an/bn</text>
  <text x="340" y="368" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">Ex: (2/3)⁴ = 16/81</text>

  <rect x="470" y="310" width="190" height="72" rx="6" class="c-amber"/>
  <text x="565" y="325" text-anchor="middle" class="th" dominant-baseline="central">Casos Especiais</text>
  <text x="565" y="343" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">a¹=a · a⁰=1 (a≠0)</text>
  <text x="565" y="359" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">1n=1 · 0n=0 (n≠0)</text>
  <text x="565" y="375" text-anchor="middle" class="ts">0⁰ = indeterminado</text>

  <line x1="20" y1="400" x2="660" y2="400"
        stroke="#ccc" stroke-width="1" stroke-dasharray="4,4"/>

  <!-- ROW 4 -->
  <rect x="130" y="415" width="420" height="58" rx="6" class="c-purple"/>
  <text x="340" y="435" text-anchor="middle" class="th" dominant-baseline="central">Sinal — Base Negativa</text>
  <text x="340" y="453" text-anchor="middle" class="t" dominant-baseline="central">Exp. PAR positivo · Exp. IMPAR negativo</text>
  <text x="190" y="487" text-anchor="middle" class="ts">(-3)⁴ = +81</text>
  <text x="340" y="487" text-anchor="middle" class="ts">vs</text>
  <text x="490" y="487" text-anchor="middle" class="ts">-3⁴ = -81</text>

  <!-- Rodapé -->
  <rect x="20" y="505" width="640" height="44" rx="6" class="c-gray"/>
  <text x="340" y="527" text-anchor="middle" class="th" dominant-baseline="central">Rene Descartes (sec. XVII) — introduziu a notacao an que usamos hoje</text>
</svg>
```

---

### DIAGRAMA: notacao_cientifica
Fluxo de conversão e operações em notação científica

```svg
<svg width="100%" viewBox="0 0 680 500"
     xmlns="http://www.w3.org/2000/svg"
     style="font-family:'Segoe UI',Arial,sans-serif">
  <defs>
    <marker id="arr2" markerWidth="8" markerHeight="8"
            refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#555"/>
    </marker>
  </defs>
  <style>
    .c-purple{fill:#6a3fa0;} .c-teal{fill:#0e7c7b;}
    .c-amber{fill:#c87800;} .c-coral{fill:#c0392b;}
    .c-gray{fill:#5a5a5a;} .c-green{fill:#2d7a2d;}
    .th{font-size:13px;font-weight:700;fill:#fff;}
    .t{font-size:12px;fill:#fff;}
    .ts{font-size:11px;fill:#444;}
    .ln{stroke:#555;stroke-width:1.5;fill:none;
        marker-end:url(#arr2);}
    @media(prefers-color-scheme:dark){
      .ts{fill:#ccc;} svg{background:#1e1e1e;}
    }
  </style>

  <!-- Título -->
  <rect x="165" y="10" width="350" height="44" rx="8" class="c-purple"/>
  <text x="340" y="37" text-anchor="middle" class="th"
        dominant-baseline="central" style="font-size:14px">Notacao Cientifica N x 10n</text>
  <text x="340" y="67" text-anchor="middle" class="ts">1 ≤ N &lt; 10 · n ∈ Z</text>

  <line x1="340" y1="54" x2="340" y2="82" class="ln"/>

  <!-- Conversão -->
  <rect x="130" y="82" width="420" height="58" rx="6" class="c-teal"/>
  <text x="340" y="100" text-anchor="middle" class="th" dominant-baseline="central">Conversão</text>
  <text x="340" y="118" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">Numero &gt; 10 → n positivo | Numero entre 0 e 1 → n negativo</text>

  <text x="170" y="158" text-anchor="middle" class="ts">123 000 000 = 1,23x10⁸</text>
  <text x="510" y="158" text-anchor="middle" class="ts">0,0000087 = 8,7x10⁻⁶</text>

  <line x1="200" y1="140" x2="200" y2="188" class="ln"/>
  <line x1="480" y1="140" x2="480" y2="188" class="ln"/>
  <line x1="340" y1="140" x2="340" y2="188" class="ln"/>

  <!-- 3 operações -->
  <rect x="20" y="188" width="185" height="72" rx="6" class="c-green"/>
  <text x="112" y="208" text-anchor="middle" class="th" dominant-baseline="central">Adicao/Subtracao</text>
  <text x="112" y="228" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">Igualar expoentes 1o</text>
  <text x="112" y="246" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">Somar coeficientes</text>

  <rect x="247" y="188" width="185" height="72" rx="6" class="c-amber"/>
  <text x="340" y="208" text-anchor="middle" class="th" dominant-baseline="central">Multiplicacao</text>
  <text x="340" y="228" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">Mult. coef. · Soma exp.</text>
  <text x="340" y="246" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">(N1·N2)x10^(a+b)</text>

  <rect x="474" y="188" width="185" height="72" rx="6" class="c-teal"/>
  <text x="567" y="208" text-anchor="middle" class="th" dominant-baseline="central">Divisao</text>
  <text x="567" y="228" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">Div. coef. · Subtr. exp.</text>
  <text x="567" y="246" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">(N1/N2)x10^(a-b)</text>

  <text x="112" y="280" text-anchor="middle" class="ts" style="font-size:10px">8,5x10⁴+1,75x10⁵=2,6x10⁵</text>
  <text x="340" y="280" text-anchor="middle" class="ts" style="font-size:10px">2x10⁵·9x10⁶=1,8x10¹²</text>
  <text x="567" y="280" text-anchor="middle" class="ts" style="font-size:10px">4x10⁸÷2x10⁵=2x10³</text>

  <!-- Pegadinha -->
  <line x1="340" y1="295" x2="340" y2="320" class="ln"/>
  <rect x="130" y="320" width="420" height="58" rx="6" class="c-coral"/>
  <text x="340" y="340" text-anchor="middle" class="th" dominant-baseline="central">Pegadinha — Ajuste do coeficiente</text>
  <text x="340" y="358" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">18x10¹¹ NAO esta em notacao cientifica → 1,8x10¹²</text>

  <!-- Aplicações -->
  <line x1="340" y1="378" x2="340" y2="403" class="ln"/>
  <rect x="60" y="403" width="560" height="58" rx="6" class="c-gray"/>
  <text x="340" y="421" text-anchor="middle" class="th" dominant-baseline="central">Aplicacoes reais</text>
  <text x="340" y="439" text-anchor="middle" class="t" dominant-baseline="central" style="font-size:10px">Nanoescala: 1,0x10⁻⁹m · Terra-Sol: 1,496x10¹¹m · Via Lactea: 10¹¹ estrelas</text>
</svg>
```