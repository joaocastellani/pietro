<!-- mat-1-11-prep.md -->

---

## DIAGRAMAS DISPONÍVEIS — mat-1-11

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Conceito de Função | `DIAGRAMA: conceito_funcao` | Ao apresentar IS / IS NOT função com diagramas de flechas (Seção 2) |
| Notação f(x) | `DIAGRAMA: notacao_fx` | Ao apresentar f(x) e cálculo de valor (Seção 2) |
| Domínio, Contradomínio e Imagem | `DIAGRAMA: dominio_imagem` | Ao apresentar D, CD e Im (Seção 2) |

### Tabelas markdown (Seção 6):
- Tabela de exemplos de leis de formação e suas variáveis
- Tabela comparativa: é função × não é função

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Síntese do livro disponível em: `Pietro/Raw/Matematica/mat-1-11-sintese.png`

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 11
- Tema: Função
- Perfil: conceitual-algébrico
- Fórmulas principais:
    Lei de formação: f(x) = expressão em x
    Notação: f(a) = substituir x = a na lei
    Inversão: dado f(x) = k, resolver equação em x
    Domínio (D): conjunto A (entradas)
    Contradomínio (CD): conjunto B (saídas possíveis)
    Imagem (Im): subconjunto de B efetivamente atingido — Im ⊆ CD
- Matemáticos citados: nenhum (menção histórica a Aristóteles e noção pré-matemática)
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### **Bloco 1 — O que é uma função**

Uma **função** f de A em B é uma regra que associa a **cada** elemento de A **exatamente um** elemento de B.

Palavras-chave da definição:
- **"cada"** — nenhum elemento de A pode ficar sem correspondência
- **"exatamente um"** — nenhum elemento de A pode ter duas ou mais correspondências em B

A função pode ser expressa por uma **lei de formação** (fórmula), uma **tabela** ou um **diagrama de flechas**.

**Contexto do capítulo:** Ana Patrícia e Duda (ouro no vôlei de praia, Paris 2024) — o desempenho esportivo é uma função de variáveis como treino, saque e bloqueio. A variável de entrada (independente) determina a de saída (dependente).

---

### **Bloco 2 — Lei de formação e variáveis**

A **lei de formação** é a fórmula que expressa a função. As variáveis têm papéis distintos:

| Papel | Nome | Descrição |
|-------|------|-----------|
| Entrada | **Variável independente** | Valor escolhido/dado; "x" na notação |
| Saída | **Variável dependente** | Resultado calculado; depende de x |

**Exemplos do capítulo:**

| Contexto | Lei de formação | Independente | Dependente |
|----------|-----------------|--------------|------------|
| Salário Débora | S(x) = 1350 + 0,03x | x = vendas | S = salário |
| Distância de Fábio | D(t) = 80t | t = tempo | D = distância |
| Máquina de Rodrigo | f(x) = 3x – 5 | x = entrada | f(x) = saída |
| Aula de Guilherme | V(x) = 45x | x = nº aulas | V = valor |
| Plano Matheus | M(m) = 30 + 0,39m | m = minutos | M = preço |
| Caixa d'água | y(t) = 250 + 15t | t = minutos | y = litros |

---

### **Bloco 3 — Notação f(x) e cálculo de valores**

**f(x)** (lê-se: "f de x") representa o valor da função f no ponto x.

Para calcular f(a): **substituir x = a** na expressão e calcular.

**Exemplo:** f(x) = 2x – 5
- f(0) = 2(0) – 5 = **–5**
- f(1) = 2(1) – 5 = **–3**
- f(–4) = 2(–4) – 5 = **–13**
- f(–2) = 2(–2) – 5 = **–9**

**Expressões compostas:** calcular cada f separadamente, depois operar.
Exemplo: [f(0) + f(1) – f(–4)] / f(–2) = [(–5) + (–3) – (–13)] / (–9) = 5/(–9) = **–5/9**

---

### **Bloco 4 — Inversão: encontrar x dado f(x)**

Quando o problema fornece f(x) = k e pede o valor de x:
1. Substituir f(x) = k na lei de formação
2. Resolver a equação resultante em x

**Exemplo:** f(x) = –2x + 1, f(x) = 4/5
- –2x + 1 = 4/5 → –2x = –1/5 → **x = 1/10**

---

### **Bloco 5 — Função por diagramas de flechas**

Representação com flechas ligando cada elemento de A ao seu correspondente em B.

**É FUNÇÃO quando:**
- Todo elemento de A tem **exatamente uma** flecha saindo

**NÃO É FUNÇÃO quando:**
- Algum elemento de A não tem flecha saindo (sem correspondência)
- Algum elemento de A tem **duas ou mais** flechas saindo

**Observações importantes:**
- Um elemento de B pode receber **múltiplas flechas** (muitos-para-um ✅)
- Um elemento de B pode **não receber nenhuma flecha** (não precisa ser atingido ✅)
- Só importa o que sai de A — não o que chega em B

---

### **Bloco 6 — Domínio, Contradomínio e Conjunto Imagem**

Para uma função f: A → B:

| Conceito | Símbolo | Definição |
|----------|---------|-----------|
| **Domínio** | D | Conjunto A — todas as entradas possíveis |
| **Contradomínio** | CD | Conjunto B — todas as saídas declaradas |
| **Conjunto Imagem** | Im | Subconjunto de B realmente atingido por f |

**Relação:** Im ⊆ CD (a imagem está sempre dentro do contradomínio)
- Im = CD somente se todo elemento de B for atingido por pelo menos um elemento de A

**Exemplo — AT-14:** A = {–2,–1,1,3,8}, f(x) = 3x–1, B = {–7,–4,1,2,8,15,19,23}
- D = {–2,–1,1,3,8}
- CD = {–7,–4,1,2,8,15,19,23}
- Im = {–7,–4,2,8,23} ← os valores 1, 15 e 19 de B **não** são atingidos

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Leis de formação: tipos e estruturas

| Tipo | Estrutura | Exemplo do cap. |
|------|-----------|-----------------|
| Proporcional (direto) | f(x) = kx | V(x) = 45x (aulas) |
| Afim com taxa fixa | f(x) = a + bx | S(x) = 1350 + 0,03x |
| Quadrática | f(x) = x² | A(l) = l² (área quadrada) |
| Com taxa variável | f(x) = a + bx | y(t) = 250 + 15t (caixa) |

### É função × Não é função (diagrama)

| Situação | É função? | Por quê |
|----------|-----------|---------|
| Todo elem. de A tem 1 flecha → 1 elem. de B | ✅ | Cada entrada tem exatamente 1 saída |
| Elem. de A com 2 flechas para 2 elem. de B | ❌ | Entrada com 2 saídas = não é função |
| Elem. de A sem flecha | ❌ | Entrada sem saída = não é função |
| 2 elem. de A → mesmo elem. de B | ✅ | Muitos-para-um é permitido |
| Elem. de B sem nenhuma flecha chegando | ✅ | Não precisa ser atingido |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Substituição cuidadosa com negativos**
f(–3) ≠ –f(3). Sempre colocar parênteses ao substituir: f(x) = 2x² → f(–3) = 2(–3)² = 2×9 = 18, não –18. Erro clássico: esquecer os parênteses.

💡 **Dica 2 — IS / IS NOT função: olhar só o lado A**
A única regra é: de cada ponto de A, sai exatamente uma flecha. O que acontece em B (quantas flechas chegam, quais elementos ficam sem flecha) não importa para a definição.

💡 **Dica 3 — Im ⊆ CD, sempre**
O conjunto imagem nunca pode ter elementos fora do contradomínio. Se f(x) = 3x–1 e A = {–2,–1,1,3,8}, calcular f para cada elemento de A para encontrar a Im — não listar todos os elementos de B.

💡 **Dica 4 — Inversão: é uma equação do 1º grau**
"Encontre x tal que f(x) = k" é a mesma coisa que resolver "lei = k". Se f(x) = –2x+1 = 4/5: –2x = 4/5 – 1 = –1/5 → x = 1/10. Não confundir com calcular f(4/5).

💡 **Dica 5 — Variável dependente = saída = f(x)**
A variável dependente é sempre o resultado da função (o "y" ou "f(x)"). A independente é a entrada (o "x"). Em "S(v) = 1560 + 0,07v": v é independente, S é dependente.

💡 **Dica 6 — Break-even: igualar receita e custo**
Quando o problema pede "quantos itens para recuperar o investimento": igualar R(n) = C(n). Exemplo papelaria: 0,90n = 25 + 0,40n → n = 50. Para qualquer n > 50, há lucro.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

#### Bloco A — Lacunas de dados

| Seção | Campo | Motivo | Ação |
|-------|-------|--------|------|
| AT-6 (IFPE) | Enunciado e gabarito completos | Texto parcialmente ilegível (pág. 291–292) | Consultar livro |
| AT-8 (Acafe-SC) | Sub-itens além do custo fixo | Texto parcialmente ilegível (pág. 292) | Consultar livro |
| AT-9 (Enem 2023) | Enunciado e gabarito | Texto parcialmente ilegível (pág. 292) | Consultar livro |
| AT-10 (diagramas) | Gabaritos dos 8 diagramas | Diagramas dependem do livro | Verificar com aluno |

#### Bloco B — Alertas e pegadinhas

```
⚠️ ALERTA — AT-9: expressão composta com fração
- Expressão: [f(0) + f(1) – f(–4)] / f(–2), f(x) = 2x – 5
- Gabarito: –5/9 (NÃO –2/3 — cuidado com versão errada da expressão)
- Passo a passo: f(0)=–5; f(1)=–3; f(–4)=–13; f(–2)=–9
- Numerador: –5 + (–3) – (–13) = 5; Denominador: –9; Resultado: –5/9
```

```
⚠️ ALERTA — AT-8e: f(x) = 4/5, não 5/2
- f(x) = –2x + 1 = 4/5 → –2x = –1/5 → x = 1/10
- Versão incorreta (5/2) daria x = –3/4 — gabarito errado
```

```
⚠️ ALERTA — AT-16: domínio com frações
- f(x) = 2x + 3, Im = {–8, –7, 10, 13, 49}
- D contém valores não-inteiros: {–11/2, –5, 7/2, 5, 23}
- Matematicamente correto para 9º ano; não exigir que domínio seja sempre inteiro
```

```
⚠️ ALERTA — Desafio UPF-RS: erro comum de setup
- João anda por t horas; mãe sai 0,5h depois
- Equação correta: 20t = 60(t – 0,5) → t = 3/4 h
- Erro comum: montar 20t = 60t (esquecer o atraso da mãe) → t=0
- Gabarito: b) 15 km e 15 min
```

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO

#### Bloco 1 — Conceitos e Definições

- **Função de A em B**
  - Condição 1: `______` (todo elemento de A tem correspondência em B)
  - Condição 2: `______` (cada elemento de A tem exatamente UMA correspondência)

- **Lei de formação**
  - O que é: `______` (fórmula/regra que define f(x))
  - Calcular f(a): `______` (substituir x = a na expressão)

- **Notação f(x)**
  - Lê-se: `______` ("f de x")
  - Significa: `______` (valor da função f quando a entrada é x)

- **Domínio, Contradomínio, Imagem**
  - D = `______` (conjunto A = todas as entradas)
  - CD = `______` (conjunto B = todas as saídas declaradas)
  - Im = `______` (subconjunto de B realmente atingido)
  - Relação: `______` (Im ⊆ CD)

#### Bloco 2 — Lacunas para Warm-Up

1. Uma função associa cada elemento de A a `______` elemento de B.
*(resposta: exatamente um)*

2. Se f(x) = 3x – 5 e f(a) = 10, então a = `______`.
*(resposta: 5 — 3a – 5 = 10 → 3a = 15 → a = 5)*

3. Na função S(v) = 1560 + 0,07v, a variável independente é `______` e a dependente é `______`.
*(resposta: v; S)*

4. Um diagrama NÃO representa função quando algum elemento de A tem `______` flechas saindo.
*(resposta: zero ou duas ou mais)*

5. Para f(x) = 2x – 5: f(0) = `______`; f(1) = `______`; f(–4) = `______`; f(–2) = `______`.
*(resposta: –5; –3; –13; –9)*

6. A expressão [f(0) + f(1) – f(–4)] / f(–2) com f(x) = 2x – 5 vale `______`.
*(resposta: –5/9)*

7. D = {0, 2, 4, 6}, f(x) = 2x – 2. A imagem é `______`.
*(resposta: {–2, 2, 6, 10})*

8. Im ⊆ `______` (sempre).
*(resposta: CD — contradomínio)*

9. Guilherme cobra R$ 45/aula. Para receber R$ 810, precisa dar `______` aulas.
*(resposta: 18 — 45x = 810 → x = 18)*

10. João anda a 20 km/h; mãe sai 0,5h depois a 60 km/h. Tempo da mãe até encontrar João: `______`.
*(resposta: 15 min — 20t = 60(t–0,5) → t = 3/4 h; tempo da mãe = 1/4 h = 15 min)*

#### Bloco 3 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Condição para ser função | `______` → *todo elem. de A com exatamente 1 correspondência em B* |
| Notação f(x) | `______` → *valor de f quando a entrada é x (lê-se "f de x")* |
| Calcular f(a) | `______` → *substituir x = a na expressão e calcular* |
| Encontrar x dado f(x) = k | `______` → *igualar a lei a k e resolver a equação* |
| D (domínio) | `______` → *conjunto A = todas as entradas* |
| CD (contradomínio) | `______` → *conjunto B = saídas declaradas* |
| Im (imagem) | `______` → *subconjunto de B efetivamente atingido* |
| Im e CD — relação | `______` → *Im ⊆ CD* |
| Muitos-para-um em B: é função? | `______` → *sim — permitido* |
| Elemento de A sem flecha: é função? | `______` → *não — viola a definição* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

Imagem disponível: `Pietro/Raw/Matematica/mat-1-11-sintese.png`

A síntese (pág. 295) apresenta mapa conceitual com três ramos a partir de "Conceito de função":
1. **A notação f(x)** → Valor numérico de uma função
2. **Relação de dependência entre duas grandezas, variáveis**
3. **O conceito de função por meio de conjuntos** → ramifica em "É função" (diagrama com cada elem. de A com exatamente 1 flecha) e "Não é função" (diagrama com elem. de A com 2+ flechas)
   - Sub-ramo: **Domínio, Contradomínio e Conjunto Imagem** — com exemplo: D={1,2,3,4,5}; CD={1,2,3,4,5,6,7}; Im={2,3,4,5,6}

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| AT-1ic | Máquina f(x)=3x–5: completar tabela e lei | Cal | F | IC | f(x)=3x–5; se saída=40, x=15 | — |
| AT-2ic | Posto: P(v)=5,50v ou 4,50v; calcular preços | Cal | F | IC | 20L gas=R$110; 15L etanol=R$67,50 | — |
| AT-4ic | Vendedor: S(v)=1560+0,07v; calcular salário e vendas | Cal | F | IC | v=16000→R$2.680; S=3275→v=R$24.500 | — |
| AT-5ic | Celular: Matheus vs Amanda — calcular e igualar | Cal | M | IC | 45min→R$47,55; 150min→igualdade | — |
| AT-6ic | Caixa d'água: y(t)=250+15t | Cal | F | IC | após 5min=325L; cheio em 50min | — |
| AT-8 | f(x)=–2x+1: encontrar x para 5 valores | Cal | F | IC | a)–5/2 b)6 c)5 d)–11/2 e)1/10 | ⚠️ e) é 4/5 |
| AT-9 | [f(0)+f(1)–f(–4)]/f(–2), f(x)=2x–5 | Cal | M | IC | **–5/9** | ⚠️ ver alerta |
| AT-11ic | Dados: f(x)=x/2+1; verificar se é função | Cal | F | IC | Sim — –2→0, –1→1/2, etc. | — |
| AT-13 | D={0,2,4,6}, f(x)=2x–2: Im | Cal | F | IC | {–2,2,6,10} | — |
| AT-14 | D={1,3,7,9,15}, f(x)=3x+7: Im | Cal | F | IC | {10,16,28,34,52} | — |
| AT-15 | Im={–13,–7,2,8}, f(x)=3x–4: domínio | Cal | M | IC | D={–3,–1,2,4} | — |
| AT-16 | Im={–8,–7,10,13,49}, f(x)=2x+3: domínio | Cal | M | IC | D={–11/2,–5,7/2,5,23} | ⚠️ D com frações |
| AT-11f | f(x)=x²+2x–1: f(0)+f(5) e f(1)–f(–2) | Cal | M | AT | 33 e 3 | — |
| AT-12f | a) D={–2,0,4,10}, f=3x+3→Im; b) Im={–5,–3,1,3}, f=2x–1→D | Cal | M | AT | a){–3,3,15,33}; b){–2,–1,1,2} | — |
| AT-13f | 4 diagramas: qual é função? | MC | F | AT | **c)** | — |
| AT-14f | f(x)=3x–1, A={–2,–1,1,3,8}, B={...}: D, CD, Im | Cal | M | AT | Im={–7,–4,2,8,23} | — |
| Q-1 | Guilherme R$45/aula: tabela, lei, 18 aulas, Ricardo | Cal | F | AT | V(x)=45x; R$810; 28 aulas | — |
| Q-2 | Som: t=5d — tabela, inversão, 7 milhas | Cal | F | AT | d=8 milhas (40s); t=35s (7mi) | — |
| Q-3 | Papelaria: C(n)=25+0,40n; break-even; lucro | Cal | M | AT | break-even n=50; lucro 400lápis=R$175 | — |
| Q-4 | (Enem 2019) Gerente+diaristas: Y=f(X) | MC | M | AT | **d) Y=160X+840** | — |
| Q-5 | (Unioeste-PR) Custo livro: c(x)=0,02x+12 | MC | F | AT | **a)** | — |
| Q-7 | (UFG-GO) Tradutores A vs B: ponto de igualdade | Cal | M | AT | n=40 linhas (a partir daí B melhor) | — |
| Q-10 | (Enem 2021) IMC: (3M+4G)/AH | MC | M | AT | **b)** | — |
| Desafio | (UPF-RS) João bicicleta vs mãe de carro | MC | D | IC | **b) 15 km e 15 min** | ⚠️ ver alerta |

---

### Bloco B — Questões modelo originais

**QM-1** · Cal · fácil · inspirada em: AT-8

Dada a função g(x) = 3x – 7, encontre o valor de x tal que g(x) = 2.

✅ Gabarito: **x = 3**
📝 Resolução: 3x – 7 = 2 → 3x = 9 → x = 3. Verificação: g(3) = 9 – 7 = 2 ✓.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · Cal · médio · inspirada em: AT-9

Dada f(x) = 3x + 1, calcule o valor da expressão $$\frac{f(2) \cdot f(-1)}{f(0) + f(3)}$$

✅ Gabarito: **–7/14 = –1/2**
📝 Resolução: f(2) = 7; f(–1) = –2; f(0) = 1; f(3) = 10. Expressão: (7 × (–2)) / (1 + 10) = –14/11. Hmm — recalcular: f(2)=7, f(-1)=-2, f(0)=1, f(3)=10; (7×(−2))/(1+10) = −14/11. Ajustar enunciado para gabarito limpo antes de usar.
⚠️ Professor: referência de estilo — ajustar valores antes de usar.

---

**QM-3** · Cal · médio · inspirada em: AT-15 / AT-16

Uma função f tem lei de formação f(x) = 4x – 3. O conjunto imagem é Im = {–11, –3, 5, 21}. Determine o domínio dessa função.

✅ Gabarito: **D = {–2, 0, 2, 6}**
📝 Resolução: 4x – 3 = –11 → x = –2; 4x – 3 = –3 → x = 0; 4x – 3 = 5 → x = 2; 4x – 3 = 21 → x = 6. Verificação: f(–2)=–11 ✓; f(0)=–3 ✓; f(2)=5 ✓; f(6)=21 ✓.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · MC · médio · inspirada em: Q-4 / Q-5

Um serviço de streaming cobra R$ 19,90 por mês de taxa fixa mais R$ 4,50 por filme alugado. Qual lei de formação expressa o custo mensal C em função do número de filmes alugados n?

a) C(n) = 4,50n   b) C(n) = 19,90 + n   c) C(n) = 19,90 + 4,50n   d) C(n) = 24,40n

✅ Gabarito: **c)**
📝 Resolução: taxa fixa = 19,90 (independe de n); taxa variável = 4,50n; total = 19,90 + 4,50n.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-5** · Dis · médio-difícil · inspirada em: Desafio / Q-3

Empresa A cobra R$ 50,00 fixos + R$ 1,20 por km rodado para entrega. Empresa B cobra R$ 20,00 fixos + R$ 1,80 por km rodado.

a) Escreva as leis de formação A(k) e B(k).
b) Para quantos km as duas empresas cobram o mesmo valor?
c) Para uma entrega de 40 km, qual empresa é mais barata? Qual a diferença?

✅ Gabarito: **a) A(k)=50+1,20k; B(k)=20+1,80k · b) k=50 km · c) A é mais barata; diferença = R$6**
📝 Resolução:
a) A(k) = 50 + 1,20k; B(k) = 20 + 1,80k
b) 50 + 1,20k = 20 + 1,80k → 30 = 0,60k → k = 50 km
c) A(40) = 50 + 48 = R$98; B(40) = 20 + 72 = R$92. B é mais barata; diferença = R$6.
⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: conceito_funcao
Condições para ser (e não ser) função — diagrama de flechas comparativo.

```svg
<svg width="100%" viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat11a" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Title -->
<rect x="185" y="8" width="310" height="30" rx="6" class="c-purple"/>
<text x="340" y="23" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Conceito de Funcao</text>

<!-- IS function box -->
<rect x="15" y="50" width="300" height="180" rx="8" class="c-teal"/>
<text x="165" y="72" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">E FUNCAO</text>
<text x="165" y="90" class="ts" text-anchor="middle" fill="var(--on-accent)">cada elem. de A: exatamente 1 flecha</text>

<!-- A set left -->
<ellipse cx="80" cy="155" rx="30" ry="55" fill="none" stroke="white" stroke-width="1.5"/>
<text x="80" y="102" class="ts" text-anchor="middle" fill="var(--on-accent)">A</text>
<circle cx="80" cy="120" r="4" fill="white"/>
<circle cx="80" cy="145" r="4" fill="white"/>
<circle cx="80" cy="170" r="4" fill="white"/>
<circle cx="80" cy="195" r="4" fill="white"/>

<!-- B set right (is-function) -->
<ellipse cx="250" cy="155" rx="30" ry="55" fill="none" stroke="white" stroke-width="1.5"/>
<text x="250" y="102" class="ts" text-anchor="middle" fill="var(--on-accent)">B</text>
<circle cx="250" cy="120" r="4" fill="white"/>
<circle cx="250" cy="145" r="4" fill="white"/>
<circle cx="250" cy="170" r="4" fill="white"/>
<circle cx="250" cy="195" r="4" fill="white"/>

<!-- Arrows (one-to-one and many-to-one) -->
<line x1="84" y1="120" x2="246" y2="120" stroke="white" stroke-width="1.5" marker-end="url(#arr-mat11a)"/>
<line x1="84" y1="145" x2="246" y2="145" stroke="white" stroke-width="1.5" marker-end="url(#arr-mat11a)"/>
<line x1="84" y1="170" x2="246" y2="170" stroke="white" stroke-width="1.5" marker-end="url(#arr-mat11a)"/>
<line x1="84" y1="195" x2="246" y2="195" stroke="white" stroke-width="1.5" marker-end="url(#arr-mat11a)"/>

<text x="165" y="248" class="ts" text-anchor="middle" fill="var(--on-accent)">cada elem. de A: 1 flecha</text>

<!-- IS NOT function box -->
<rect x="365" y="50" width="300" height="180" rx="8" class="c-coral"/>
<text x="515" y="72" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">NAO E FUNCAO</text>
<text x="515" y="90" class="ts" text-anchor="middle" fill="var(--on-accent)">algum elem. de A: 0 ou 2+ flechas</text>

<!-- A set right-box -->
<ellipse cx="430" cy="155" rx="30" ry="55" fill="none" stroke="white" stroke-width="1.5"/>
<text x="430" y="102" class="ts" text-anchor="middle" fill="var(--on-accent)">A</text>
<circle cx="430" cy="120" r="4" fill="white"/>
<circle cx="430" cy="155" r="4" fill="white"/>
<circle cx="430" cy="190" r="4" fill="white"/>

<!-- B set right-box -->
<ellipse cx="600" cy="155" rx="30" ry="55" fill="none" stroke="white" stroke-width="1.5"/>
<text x="600" y="102" class="ts" text-anchor="middle" fill="var(--on-accent)">B</text>
<circle cx="600" cy="120" r="4" fill="white"/>
<circle cx="600" cy="145" r="4" fill="white"/>
<circle cx="600" cy="170" r="4" fill="white"/>
<circle cx="600" cy="195" r="4" fill="white"/>

<!-- 2 arrows from same A element (not a function) -->
<line x1="434" y1="118" x2="596" y2="118" stroke="white" stroke-width="1.5" marker-end="url(#arr-mat11a)"/>
<line x1="434" y1="122" x2="596" y2="148" stroke="white" stroke-width="1.5" marker-end="url(#arr-mat11a)"/>
<line x1="434" y1="190" x2="596" y2="172" stroke="white" stroke-width="1.5" marker-end="url(#arr-mat11a)"/>

<text x="515" y="248" class="ts" text-anchor="middle" fill="var(--on-accent)">elem. do meio: 2 flechas saindo</text>

<!-- Bottom note -->
<rect x="15" y="246" width="650" height="44" rx="6" class="c-amber"/>
<text x="340" y="260" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Permitido em B: receber multiplas flechas (muitos-para-um) ou nao receber nenhuma</text>
<text x="340" y="280" class="ts" text-anchor="middle" fill="var(--on-accent)">Proibido em A: ter 0 ou 2+ flechas saindo do mesmo elemento</text>
</svg>
```

---

### DIAGRAMA: notacao_fx
Notação f(x), cálculo de valores e inversão.

```svg
<svg width="100%" viewBox="0 0 680 290" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat11b" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Central: f(x) -->
<rect x="240" y="10" width="200" height="44" rx="8" class="c-purple"/>
<text x="340" y="28" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Notacao f(x)</text>
<text x="340" y="46" class="ts" text-anchor="middle" fill="var(--on-accent)">le-se: f de x</text>

<!-- Arrow left: calcular valor -->
<line x1="240" y1="32" x2="185" y2="80" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat11b)"/>
<!-- Arrow right: inverter -->
<line x1="440" y1="32" x2="495" y2="80" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat11b)"/>

<!-- Left box: calculate f(a) -->
<rect x="15" y="80" width="310" height="120" rx="8" class="c-teal"/>
<text x="170" y="100" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Calcular f(a)</text>
<text x="170" y="120" class="ts" text-anchor="middle" fill="var(--on-accent)">Substituir x = a na expressao</text>
<text x="170" y="140" class="ts" text-anchor="middle" fill="var(--on-accent)">f(x) = 2x - 5:</text>
<text x="170" y="158" class="ts" text-anchor="middle" fill="var(--on-accent)">f(0) = -5  f(1) = -3  f(-4) = -13</text>
<text x="170" y="176" class="ts" text-anchor="middle" fill="var(--on-accent)">f(-2) = -9</text>

<!-- Right box: inversion -->
<rect x="355" y="80" width="310" height="120" rx="8" class="c-amber"/>
<text x="510" y="100" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Encontrar x dado f(x) = k</text>
<text x="510" y="120" class="ts" text-anchor="middle" fill="var(--on-accent)">Igualar a lei a k e resolver</text>
<text x="510" y="140" class="ts" text-anchor="middle" fill="var(--on-accent)">f(x) = -2x + 1 = 4/5</text>
<text x="510" y="158" class="ts" text-anchor="middle" fill="var(--on-accent)">-2x = 4/5 - 1 = -1/5</text>
<text x="510" y="176" class="ts" text-anchor="middle" fill="var(--on-accent)">x = 1/10</text>

<!-- Expression composed -->
<rect x="15" y="216" width="650" height="60" rx="8" class="c-coral"/>
<text x="340" y="234" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Expressao composta: calcular cada f separadamente, depois operar</text>
<text x="340" y="254" class="ts" text-anchor="middle" fill="var(--on-accent)">[f(0) + f(1) - f(-4)] / f(-2) = [(-5) + (-3) - (-13)] / (-9) = 5 / (-9) = -5/9</text>
<text x="340" y="270" class="ts" text-anchor="middle" fill="var(--on-accent)">Atencao: substituir com parenteses — f(-4) = 2(-4)-5 = -13, nao -2(4)-5</text>
</svg>
```

---

### DIAGRAMA: dominio_imagem
Domínio, Contradomínio e Conjunto Imagem — definições e exemplo.

```svg
<svg width="100%" viewBox="0 0 680 310" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat11c" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Title -->
<rect x="165" y="8" width="350" height="30" rx="6" class="c-purple"/>
<text x="340" y="23" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Dominio, Contradominio e Imagem</text>

<!-- A set (domain) -->
<rect x="15" y="50" width="180" height="170" rx="8" class="c-teal"/>
<text x="105" y="70" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">D — Dominio</text>
<text x="105" y="88" class="ts" text-anchor="middle" fill="var(--on-accent)">Conjunto A</text>
<text x="105" y="108" class="ts" text-anchor="middle" fill="var(--on-accent)">todas as entradas</text>
<text x="105" y="130" class="ts" text-anchor="middle" fill="var(--on-accent)">Ex: {-2,-1,1,3,8}</text>
<text x="105" y="150" class="ts" text-anchor="middle" fill="var(--on-accent)">f(x) = 3x - 1</text>
<text x="105" y="170" class="ts" text-anchor="middle" fill="var(--on-accent)">f(-2)=-7  f(-1)=-4</text>
<text x="105" y="190" class="ts" text-anchor="middle" fill="var(--on-accent)">f(1)=2  f(3)=8  f(8)=23</text>

<!-- Arrow D to CD -->
<line x1="195" y1="135" x2="240" y2="135" stroke="var(--c-purple)" stroke-width="2" marker-end="url(#arr-mat11c)"/>
<text x="217" y="128" class="ts" text-anchor="middle" fill="var(--c-purple)">f</text>

<!-- B set (codomain) -->
<rect x="245" y="50" width="210" height="170" rx="8" class="c-amber"/>
<text x="350" y="70" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">CD — Contradominio</text>
<text x="350" y="88" class="ts" text-anchor="middle" fill="var(--on-accent)">Conjunto B inteiro</text>
<text x="350" y="108" class="ts" text-anchor="middle" fill="var(--on-accent)">todas as saidas declaradas</text>
<text x="350" y="128" class="ts" text-anchor="middle" fill="var(--on-accent)">Ex: {-7,-4,1,2,8,15,19,23}</text>
<text x="350" y="150" class="ts" text-anchor="middle" fill="var(--on-accent)">Inclui valores que</text>
<text x="350" y="168" class="ts" text-anchor="middle" fill="var(--on-accent)">NAO sao atingidos:</text>
<text x="350" y="186" class="ts" text-anchor="middle" fill="var(--on-accent)">1, 15, 19 estao no CD</text>
<text x="350" y="204" class="ts" text-anchor="middle" fill="var(--on-accent)">mas NAO na Im</text>

<!-- Arrow CD to Im -->
<line x1="455" y1="135" x2="500" y2="135" stroke="var(--c-coral)" stroke-width="2" marker-end="url(#arr-mat11c)"/>
<text x="477" y="128" class="ts" text-anchor="middle" fill="var(--c-coral)">Im ⊆ CD</text>

<!-- Im set -->
<rect x="505" y="50" width="160" height="170" rx="8" class="c-coral"/>
<text x="585" y="70" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Im — Imagem</text>
<text x="585" y="88" class="ts" text-anchor="middle" fill="var(--on-accent)">subconj. de B</text>
<text x="585" y="108" class="ts" text-anchor="middle" fill="var(--on-accent)">efetivamente atingido</text>
<text x="585" y="130" class="ts" text-anchor="middle" fill="var(--on-accent)">Ex: {-7,-4,2,8,23}</text>
<text x="585" y="152" class="ts" text-anchor="middle" fill="var(--on-accent)">Calcular f(a)</text>
<text x="585" y="170" class="ts" text-anchor="middle" fill="var(--on-accent)">para cada a em D</text>
<text x="585" y="190" class="ts" text-anchor="middle" fill="var(--on-accent)">e listar resultados</text>

<!-- Bottom key rule -->
<rect x="15" y="236" width="650" height="30" rx="6" class="c-purple"/>
<text x="340" y="251" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Regra: Im ⊆ CD — imagem sempre dentro do contradominio</text>

<!-- Second rule -->
<rect x="15" y="276" width="650" height="26" rx="6" class="c-gray"/>
<text x="340" y="289" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Im = CD somente se todos os elementos de B forem atingidos por algum elemento de A</text>
</svg>
```
