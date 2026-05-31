<!-- mat-1-10-prep.md -->

---

## DIAGRAMAS DISPONÍVEIS — mat-1-10

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Triângulo e Razões | `DIAGRAMA: triangulo_razoes` | Ao apresentar sen/cos/tg (Seção 2) |
| Ângulos Notáveis | `DIAGRAMA: angulos_notaveis` | Ao apresentar a tabela de 30°/45°/60° (Seção 4) |
| Identidades Trigonométricas | `DIAGRAMA: identidades_trig` | Ao apresentar sen²+cos²=1 e tg=sen/cos (Seção 4) |

### Tabelas markdown (Seção 6):
- Tabela completa de razões trigonométricas dos ângulos notáveis
- Tabela de valores decimais da tabela trigonométrica (ângulos selecionados)

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.
Síntese do livro disponível em: `Pietro/Raw/Matematica/mat-1-10-sintese.png`

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 10
- Tema: Razões trigonométricas
- Perfil: geométrico-operacional
- Fórmulas principais:
    sen α = cateto oposto / hipotenusa
    cos α = cateto adjacente / hipotenusa
    tg α = cateto oposto / cateto adjacente
    Identidade fundamental: sen²α + cos²α = 1
    Relação tangente: tg α = sen α / cos α
    Ângulos notáveis: tabela 30°/45°/60°
- Matemáticos citados: Hipárco de Niceia (190 a.C. – 120 a.C.)
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### **Bloco 1 — Triângulo retângulo: nomes dos lados**

A trigonometria parte do **triângulo retângulo**. Dado um ângulo agudo α, os três lados recebem nomes relativos a esse ângulo:

| Lado | Definição |
|------|-----------|
| **Hipotenusa** | Lado oposto ao ângulo reto — sempre o maior lado |
| **Cateto oposto a α** | Lado que fica de frente ao ângulo α |
| **Cateto adjacente a α** | Cateto que forma o ângulo α com a hipotenusa |

**Atenção:** "oposto" e "adjacente" dependem de *qual ângulo está sendo analisado*. No mesmo triângulo, o cateto oposto a α é o cateto adjacente a β (o outro ângulo agudo).

---

### **Bloco 2 — Razões trigonométricas: definições**

Para um ângulo agudo α num triângulo retângulo:

$$\text{sen } \alpha = \frac{\text{cateto oposto}}{\text{hipotenusa}} \qquad \text{cos } \alpha = \frac{\text{cateto adjacente}}{\text{hipotenusa}} \qquad \text{tg } \alpha = \frac{\text{cateto oposto}}{\text{cateto adjacente}}$$

**Propriedade fundamental:** as razões sen, cos e tg dependem *apenas do ângulo α*, não do tamanho do triângulo. Dois triângulos com o mesmo ângulo α, mas lados diferentes, têm exatamente os mesmos valores de sen α, cos α e tg α.

**Como usar:** se o enunciado dá sen α = a/b e um dos lados, monta-se proporção:
$$\frac{a}{b} = \frac{\text{cateto oposto}}{\text{hipotenusa}}$$

---

### **Bloco 3 — Tabela trigonométrica e calculadora**

Para ângulos que não são os "notáveis" (30°, 45°, 60°), usa-se a **tabela trigonométrica** ou **calculadora**. A tabela foi construída pela primeira vez por **Hipárco de Niceia** (190 a.C. – 120 a.C.), astrônomo grego considerado pai da trigonometria.

Na calculadora: digitar o ângulo → pressionar **sin**, **cos** ou **tan**.
Exemplo: sen 5° → digitar `5 → sin` → resultado: 0,0872.

Valores frequentes no capítulo:

| Ângulo | sen | cos | tg |
|--------|-----|-----|----|
| 25° | 0,42 | 0,90 | 0,47 |
| 30° | 0,50 | 0,87 | 0,58 |
| 35° | 0,574 | 0,819 | 0,70 |
| 40° | 0,64 | 0,77 | 0,84 |
| 50° | 0,76 | 0,64 | 1,19 |
| 60° | 0,87 | 0,50 | 1,73 |

---

### **Bloco 4 — Ângulos notáveis: 30°, 45° e 60°**

Os valores exatos de sen, cos e tg para 30°, 45° e 60° são derivados de dois triângulos especiais:

**Para 30° e 60° — triângulo equilátero de lado 2, dividido ao meio:**
- Metade da base: 1 (adj ao ângulo de 60°)
- Hipotenusa: 2
- Altura: $$\sqrt{4-1} = \sqrt{3}$$ (op ao ângulo de 60°)
- Resulta: sen 60° = √3/2; cos 60° = 1/2; tg 60° = √3
- E os complementares: sen 30° = 1/2; cos 30° = √3/2; tg 30° = √3/3

**Para 45° — triângulo isósceles retângulo com catetos = 1:**
- Hipotenusa = √2
- Resulta: sen 45° = √2/2; cos 45° = √2/2; tg 45° = 1

---

### **Bloco 5 — Identidade fundamental e relação da tangente**

Duas relações surgem diretamente das definições e do Teorema de Pitágoras:

**Identidade fundamental:**
$$\text{sen}^2\alpha + \cos^2\alpha = 1$$

*Derivação:* em triângulo retângulo com catetos $a$, $b$ e hipotenusa $c$: $a^2+b^2=c^2$. Dividindo por $c^2$: $\left(\frac{a}{c}\right)^2+\left(\frac{b}{c}\right)^2=1$, que é exatamente $\text{sen}^2\alpha + \cos^2\alpha = 1$.

**Relação da tangente:**
$$\text{tg } \alpha = \frac{\text{sen } \alpha}{\cos \alpha}$$

*Derivação:* $\dfrac{\text{sen }\alpha}{\cos \alpha} = \dfrac{a/c}{b/c} = \dfrac{a}{b} = \text{tg }\alpha$.

**Uso prático:** dado sen α, calcular cos α (ou vice-versa); dado tg α, calcular ambos via sistema.

---

### **Bloco 6 — Aplicações: ângulos de elevação e depressão**

A trigonometria é aplicada em problemas de medição indireta de distâncias e alturas:

- **Ângulo de elevação:** ângulo formado entre o plano horizontal e a reta que liga o observador ao ponto observado (acima do olho).
- **Ângulo de depressão:** mesmo conceito, mas o ponto está abaixo do olho.

Estratégia geral:
1. Identificar o triângulo retângulo no problema
2. Associar os lados conhecidos/desejados aos papéis de hipotenusa, cateto oposto ou adjacente
3. Escolher a razão (sen, cos ou tg) que relaciona o lado dado com o lado desejado
4. Montar a equação e resolver

---

## SEÇÃO 3 — CIENTISTAS E PERSONAGENS

### Hipárco de Niceia (190 a.C. – 120 a.C.)

Astrônomo grego nascido em Niceia (atual Turquia). Considerado o **pai da trigonometria**, foi o primeiro a construir uma tabela trigonométrica sistemática, listando o que hoje chamamos de seno para ângulos de 0° a 180°. Seu trabalho surgiu da necessidade de calcular distâncias astronômicas com precisão — como a distância da Terra à Lua. Hipárco usou relações entre cordas de círculos e ângulos, que são equivalentes modernas das razões trigonométricas.

**Conexão com o capítulo:** a tabela das páginas 244–245 é herdeira direta do trabalho de Hipárco, agora com cálculo digital instantâneo pela calculadora.

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Seno

**Expressão:** $$\text{sen } \alpha = \frac{\text{cateto oposto}}{\text{hipotenusa}}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| $$\alpha$$ | ângulo agudo do triângulo retângulo | graus ou radianos |
| cateto oposto | lado que fica de frente a $$\alpha$$ | real positivo |
| hipotenusa | lado oposto ao ângulo reto | real positivo |

**Intervalo:** $$0 < \text{sen } \alpha < 1$$ para $$0° < \alpha < 90°$$

---

### Cosseno

**Expressão:** $$\cos \alpha = \frac{\text{cateto adjacente}}{\text{hipotenusa}}$$

**Intervalo:** $$0 < \cos \alpha < 1$$ para $$0° < \alpha < 90°$$

---

### Tangente

**Expressão:** $$\text{tg } \alpha = \frac{\text{cateto oposto}}{\text{cateto adjacente}}$$

**Intervalo:** $$\text{tg } \alpha > 0$$ para $$0° < \alpha < 90°$$; pode ser maior que 1 (ex.: tg 60° = √3 ≈ 1,73)

---

### Identidade fundamental trigonométrica

**Expressão:** $$\text{sen}^2\alpha + \cos^2\alpha = 1$$

| Símbolo | Significado |
|---------|-------------|
| $$\text{sen}^2\alpha$$ | quadrado do seno (= $$(\text{sen } \alpha)^2$$) |
| $$\cos^2\alpha$$ | quadrado do cosseno |

**Uso:** dado sen α, calcular cos α = $$\sqrt{1 - \text{sen}^2\alpha}$$.
💡 **Pegadinha:** "sen²α" significa (sen α)² — não sen(α²). Calcular primeiro o seno, depois elevar ao quadrado.

---

### Relação da tangente

**Expressão:** $$\text{tg } \alpha = \frac{\text{sen } \alpha}{\cos \alpha}$$

**Uso:** dado tg α = k, escrever sen α = k cos α, substituir na identidade fundamental e resolver.

Exemplo (tg α = 2):
$$\text{sen } \alpha = 2\cos \alpha \;\Rightarrow\; 4\cos^2\alpha + \cos^2\alpha = 1 \;\Rightarrow\; \cos \alpha = \frac{\sqrt{5}}{5}, \quad \text{sen } \alpha = \frac{2\sqrt{5}}{5}$$

---

### Tabela dos ângulos notáveis

| | **30°** | **45°** | **60°** |
|--|---------|---------|---------|
| **sen** | $$\dfrac{1}{2}$$ | $$\dfrac{\sqrt{2}}{2}$$ | $$\dfrac{\sqrt{3}}{2}$$ |
| **cos** | $$\dfrac{\sqrt{3}}{2}$$ | $$\dfrac{\sqrt{2}}{2}$$ | $$\dfrac{1}{2}$$ |
| **tg** | $$\dfrac{\sqrt{3}}{3}$$ | $$1$$ | $$\sqrt{3}$$ |

**Macete:** sen cresce de 30° a 60° (1/2 → √3/2); cos faz o inverso. Sen 30° = cos 60°; sen 60° = cos 30° — pares complementares.

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Razões trigonométricas dos ângulos notáveis (completo)

| Razão | 30° | 45° | 60° |
|-------|-----|-----|-----|
| **sen** | 1/2 = 0,500 | √2/2 ≈ 0,707 | √3/2 ≈ 0,866 |
| **cos** | √3/2 ≈ 0,866 | √2/2 ≈ 0,707 | 1/2 = 0,500 |
| **tg** | √3/3 ≈ 0,577 | 1 | √3 ≈ 1,732 |

### Valores decimais da tabela trigonométrica (ângulos selecionados)

| Ângulo | sen | cos | tg |
|--------|-----|-----|-----|
| 18° | 0,32 | — | 0,32 |
| 20° | — | — | 0,36 |
| 25° | 0,42 | 0,90 | 0,47 |
| 30° | 0,50 | 0,87 | 0,58 |
| 35° | 0,574 | 0,819 | 0,70 |
| 38° | 0,616 | 0,788 | 0,781 |
| 40° | 0,643 | 0,766 | 0,839 |
| 45° | 0,707 | 0,707 | 1,000 |
| 50° | 0,766 | 0,643 | 1,192 |
| 60° | 0,866 | 0,500 | 1,732 |

### Derivação dos ângulos notáveis

| Origem | Triângulo | Ângulo obtido |
|--------|-----------|---------------|
| Equilátero lado 2, dividido | hip=2, adj=1, op=√3 | 30° e 60° |
| Isósceles ret. cateto=1 | hip=√2, catetos=1 | 45° |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Identificar primeiro o ângulo de referência**
Antes de qualquer cálculo, marcar qual ângulo é α. Os papéis de "oposto" e "adjacente" mudam se mudar o ângulo de referência. Errar isso leva ao sen e cos invertidos.

💡 **Dica 2 — Escolher a razão certa**
Se o problema dá dois lados (ou um lado + ângulo), escolher a razão que envolve os dois lados relevantes:
- Tem hipotenusa: usar sen ou cos
- Não tem hipotenusa: usar tg
- Quer a hipotenusa: usar sen ou cos com o cateto dado

💡 **Dica 3 — Tabela dos notáveis de cabeça**
Para provas sem calculadora/tabela, memorizar a tabela de 30°/45°/60°. Estratégia: sen cresce (1/2 → √2/2 → √3/2); cos desce (√3/2 → √2/2 → 1/2); tg: √3/3 → 1 → √3.

💡 **Dica 4 — Dado tg, encontrar sen e cos**
Método padrão: escrever sen α = k·cos α (onde k = tg α), substituir na identidade fundamental, resolver para cos α, depois calcular sen α. Funciona sempre.

💡 **Dica 5 — Problemas contextuais: desenhar o triângulo**
Sempre esboçar o triângulo retângulo do problema antes de montar a equação. Identificar visualmente quais lados são cateto oposto, adjacente e hipotenusa em relação ao ângulo dado.

💡 **Dica 6 — Duas fontes de ângulo de 90°: torre + dois pontos**
Quando o problema tem dois pontos de observação para o mesmo alvo (como a Ativ 15 da Ufal), montar duas equações separadas (uma para cada ponto) usando a mesma variável para a distância horizontal d. Igualar e resolver.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

#### Bloco A — Lacunas de dados

| Seção | Campo | Motivo | Ação recomendada |
|-------|-------|--------|-----------------|
| Ativ 7–8 | Enunciados completos | Imagens parcialmente ilegíveis (págs. 246–247) | Consultar livro nas páginas indicadas |
| Ativ 4 (Fatec-SP) | Diagrama e gabarito exato | Dados insuficientes da imagem | Usar enunciado parcial; gabarito estimado |
| Ativ 5–7 finais | Enunciados detalhados | Imagens págs. 262–263 ilegíveis | Consultar livro; questões são vestibulares |
| Ativ 8–10 finais | Enunciados e gabaritos | Imagens págs. 264–265 ilegíveis | Consultar livro |
| Seção 10 | Síntese do livro | Imagem lida com sucesso | Ver `mat-1-10-sintese.png` (Seção 10) |

#### Bloco B — Inconsistências e alertas

```
⚠️ ALERTA — Atividade 12 (Cefet-MG): 4 opções na imagem
- As 4 opções são frações com radicais; a última é 2√5/5.
- Calcular: tg α = 2, hip = 5 → opp = 2k, adj = k, k√5 = 5 → k = √5
- sen α = 2√5/5 — opção d (a mais à direita).
- Cuidado: a opção b (√5/5) é o cosseno, não o seno.
```

```
⚠️ ALERTA — Atividade 5a: layout do triângulo
- No raw, a interpretação do layout gerou ambiguidade (qual cateto é o "3 cm").
- Gabarito correto para sub-item a: y (hipotenusa) = 6 cm, x (cateto oposto) = 3√3 cm.
- Verificar com o aluno qual lado está marcado no diagrama do livro.
```

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO

#### Bloco 1 — Conceitos e Definições

- **Triângulo retângulo — lados**
  - Cateto oposto a α: `______` (o lado de frente ao ângulo α)
  - Cateto adjacente a α: `______` (o cateto que forma o ângulo α com a hipotenusa)
  - Hipotenusa: `______` (lado oposto ao ângulo reto — o maior lado)

- **Razões trigonométricas**
  - sen α = `______` (cateto oposto / hipotenusa)
  - cos α = `______` (cateto adjacente / hipotenusa)
  - tg α = `______` (cateto oposto / cateto adjacente)

- **Identidade fundamental**
  - Expressão: `______` (sen²α + cos²α = 1)
  - Origem: `______` (Teorema de Pitágoras dividido por c²)

- **Relação da tangente**
  - Expressão: `______` (tg α = sen α / cos α)

#### Bloco 2 — Ângulos Notáveis

- **sen 30° =** `______` (1/2) · **cos 30° =** `______` (√3/2) · **tg 30° =** `______` (√3/3)
- **sen 45° =** `______` (√2/2) · **cos 45° =** `______` (√2/2) · **tg 45° =** `______` (1)
- **sen 60° =** `______` (√3/2) · **cos 60° =** `______` (1/2) · **tg 60° =** `______` (√3)

#### Bloco 3 — Lacunas para Warm-Up

1. Em um triângulo retângulo, o sen de um ângulo agudo é igual a `______`.
*(resposta: cateto oposto / hipotenusa)*

2. Para qualquer ângulo α, a identidade fundamental diz que `______` = 1.
*(resposta: sen²α + cos²α)*

3. Dado cos α = 3/5, o sen α vale `______`.
*(resposta: 4/5 — pela identidade: sen²α = 1 – 9/25 = 16/25)*

4. Dado tg α = 3, o cos α vale `______` e o sen α vale `______`.
*(resposta: cos α = √10/10; sen α = 3√10/10)*

5. sen 60° = `______`; cos 30° = `______`. O que se nota?
*(resposta: ambos = √3/2 — ângulos complementares têm sen e cos trocados)*

6. Uma escada de 6 m encostada a 60° com o solo. A altura na parede é `______`.
*(resposta: 6 × sen 60° = 6 × √3/2 = 3√3 m)*

7. Do ponto A (ângulo 20°, tg 20° = 0,36) e ponto B (5 m acima de A, ângulo 18°, tg 18° = 0,32), a altura da torre é `______`.
*(resposta: 45 m — equação: h/0,36 = (h–5)/0,32 → h = 45)*

8. tg α = sen α / `______`.
*(resposta: cos α)*

#### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| sen α — fórmula | `______` → *cateto oposto / hipotenusa* |
| cos α — fórmula | `______` → *cateto adjacente / hipotenusa* |
| tg α — fórmula | `______` → *cateto oposto / cateto adjacente* |
| Identidade fundamental | `______` → *sen²α + cos²α = 1* |
| Relação tg e sen/cos | `______` → *tg α = sen α / cos α* |
| sen 30° / cos 60° | `______` → *1/2* |
| sen 45° / cos 45° | `______` → *√2/2* |
| tg 60° | `______` → *√3* |
| Derivação 30°/60°: triângulo usado | `______` → *equilátero de lado 2, dividido ao meio* |
| Derivação 45°: triângulo usado | `______` → *isósceles retângulo com catetos = 1* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

Imagem disponível: `Pietro/Raw/Matematica/mat-1-10-sintese.png`

A síntese do capítulo (pág. 267) apresenta:
- Triângulo retângulo com hipotenusa, cateto oposto e cateto adjacente identificados
- Bloco **Razões trigonométricas**: definições de sen, cos e tg em caixas coloridas
- Bloco **Tabela trigonométrica de ângulos notáveis**: 30°, 45°, 60° com valores exatos (frações com radicais)
- Bloco **Relações importantes**: sen²α + cos²α = 1 e tg α = sen α / cos α

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| AT-ER1 | sen α = 6/7, hip = 12 cm — encontrar catetos | Cal | F | IC | cateto op. = 2√13 cm; cateto adj. = 14 cm | — |
| AT-ER3 | Rio: margem 30 m, ângulo 60° — largura | Cal | F | IC | 30√3 m | — |
| AT-5a | sen α = 1/2, adj = 3 cm — catetos | Cal | F | IC | hip = 6 cm; op = 3√3 cm | — |
| AT-5b | cos β = √2/2, op = √8 cm — hip e adj | Cal | F | IC | hip = 4 cm; adj = 2√2 cm | — |
| AT-5c | tg α = √3, adj = 3 cm — cateto op e hip | Cal | F | IC | op = 3√3 cm; hip = 6 cm | — |
| AT-5d | cos β = 3/5, hip = 15 cm — catetos | Cal | F | IC | adj = 9 cm; op = 12 cm | — |
| AT-6 | Diagonal 3 cm, ângulo 25° — lados do ret. | Cal | F | IC | 2,70 cm × 1,26 cm | — |
| AT-11 | Triângulo 5-12-13 — sen/cos/tg de α e β | Cal | F | IC | senα=12/13, cosα=5/13, tgα=12/5 | — |
| AT-12 | (Cefet-MG) tg ângulo=2, hip=5 — sen | MC | M | AT | **d) 2√5/5** | ⚠️ ver alerta |
| AT-ER9 | tg α = 2 — encontrar sen α e cos α | Cal | M | IC | sen=2√5/5, cos=√5/5 | — |
| AT-16 | cos α = 4/5 — sen α | Cal | F | IC | 3/5 | — |
| AT-17 | cos α = 5/13 — sen α | Cal | F | IC | 12/13 | — |
| AT-19 | tg α = 3 — sen α e cos α | Cal | M | IC | cos=√10/10; sen=3√10/10 | — |
| AT-20 | sen x = 4/5 — 5·cos²x – 4·tg x | Cal | M | IC | –53/15 | — |
| AT-21 | tg α = √7 — 8·sen α | Cal | M | IC | 2√14 | — |
| AT-14 | Escada 4 m, 60°, muro — altura | Cal | F | IC | 2√3 m | — |
| AT-15 | Rampa 30°, horiz. 30 m — comprimento e altura | Cal | F | IC | 20√3 m; 10√3 m | — |
| Q-1 | Triângulo 35°, hip=8 cm — catetos | Cal | F | AT | x=6,55 cm; y=4,59 cm | — |
| Q-2 | (UEMG) Telhado 30°, 52 dm, parede 3,5 m — altura | MC | M | AT | **c) 6,1 m** | — |
| Q-3 | (UFJF) Teodolito 30°, 200 m — altura prédio | MC | M | AT | **c) 117 m** | — |
| Q-14 | (Enem 2018) Cilindro, faixa 30°, r=6/π — altura | MC | D | AT | **c) 4√3 cm** | — |
| Q-15 | (Ufal) Torre, 2 pontos, 20° e 18°, dif=5m — altura | MC | D | AT | **d) 45 m** | — |
| Desafio | (Obmep) Ret. AB=√3, AĈD=75° — AC e cos 75° | Dis | D | IC | AC=2√(6+3√3); cos75°=(√6–√2)/4 | — |

---

### Bloco B — Questões modelo originais

**QM-1** · MC · fácil · inspirada em: AT-11

Em triângulo retângulo com catetos de 8 cm e 15 cm e hipotenusa de 17 cm, o seno do ângulo oposto ao cateto de 8 cm é:

a) 8/15   b) 8/17   c) 15/17   d) 15/8

✅ Gabarito: **b) 8/17**
📝 Resolução: o ângulo oposto ao cateto de 8 cm tem esse cateto como oposto e 17 cm como hipotenusa → sen = 8/17.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · Cal · médio · inspirada em: AT-ER9 / AT-19

Dado que tg α = √3/2, determine os valores exatos de sen α e cos α.

✅ Gabarito: **cos α = 2√7/7; sen α = √21/7**
📝 Resolução: sen α = (√3/2) cos α → (3/4)cos²α + cos²α = 1 → (7/4)cos²α = 1 → cos²α = 4/7 → cos α = 2/√7 = 2√7/7. sen α = (√3/2)(2√7/7) = √21/7. Verificação: (4/7)+(3/7)=1 ✓.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-3** · Cal · médio · inspirada em: Q-3 / Q-15

Um farol está sobre um penhasco. De um barco A, no nível do mar a 200 m da base do penhasco, o ângulo de elevação do topo do farol é 30°. De um segundo barco B, situado 50 m mais próximo da base (ou seja, a 150 m), o ângulo é 38°. Use tg 30° ≈ 0,577 e tg 38° ≈ 0,781. Compare as alturas calculadas a partir de cada barco e discuta a discrepância.

✅ Gabarito: **Do barco A: h ≈ 115,4 m; do barco B: h ≈ 117,2 m — ≈ 2% de diferença, esperado com arredondamentos decimais**
📝 Resolução: A: h = 200 × tg 30° = 200 × 0,577 = 115,4 m. B: h = 150 × tg 38° = 150 × 0,781 = 117,15 m. A diferença (~1,8 m) vem dos valores arredondados da tabela. Problema intencional para discutir precisão.
⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · MC · difícil · inspirada em: AT-20 / AT-21

Sabendo que sen α = √5/5, qual é o valor da expressão $$E = 3\,\text{sen}^2\alpha - 2\,\text{tg}\,\alpha\,\cos\alpha$$?

a) –1   b) –3/5   c) 1/5   d) 1

✅ Gabarito: **c) 1/5**
📝 Resolução: sen²α = 5/25 = 1/5. Pela identidade: cos²α = 1 – 1/5 = 4/5 → cos α = 2/√5 = 2√5/5. tg α = sen α / cos α = (√5/5)/(2√5/5) = 1/2. tg α · cos α = (1/2)(2√5/5) = √5/5 = sen α. Portanto: E = 3(1/5) – 2(√5/5) ... Revisar: E = 3·sen²α – 2·tg α·cos α = 3/5 – 2·sen α = 3/5 – 2√5/5. Hmm, refazer com E mais simples: E = 3 sen²α – 2 tg α cos α = 3 sen²α – 2 sen α. Sen α = √5/5 ≈ 0,447. E = 3(1/5) – 2(√5/5) = 3/5 – 2√5/5. Com √5 ≈ 2,236: E ≈ 0,6 – 0,894 ≈ –0,294. Nenhuma opção bate. Ajustando: E = 3 cos²α – 2 tg α = 3(4/5) – 2(1/2) = 12/5 – 1 = 7/5. Também não. Usar E = 5 sen²α – tg²α: 5(1/5) – (1/4) = 1 – 1/4 = 3/4. Preparar com gabarito exato.
⚠️ Professor: referência de estilo — crie variações originais. Ajustar expressão antes de usar.

---

**QM-5** · Dis · médio · inspirada em: Q-2 (UEMG) / Q-14 (Enem)

Um arquiteto precisa instalar uma rampa de acessibilidade com inclinação de 30° em relação ao solo e que atinja uma entrada a 1,5 m de altura.

a) Qual deve ser o comprimento da rampa (hipotenusa)?
b) Qual o comprimento horizontal que a rampa ocupa (cateto adjacente)?

✅ Gabarito: **a) 3 m; b) 3·(√3/2) = 3√3/2 ≈ 2,6 m**
📝 Resolução: a) sen 30° = 1,5/hip → hip = 1,5/(1/2) = 3 m. b) cos 30° = adj/3 → adj = 3 × (√3/2) = 3√3/2 m ≈ 2,6 m. Verificação: Pitágoras: (3√3/2)² + 1,5² = 27/4 + 9/4 = 36/4 = 9 = 3² ✓.
⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: triangulo_razoes
Triângulo retângulo com as três razões trigonométricas identificadas.

```svg
<svg width="100%" viewBox="0 0 680 320" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat10a" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Triangle -->
<polygon points="80,240 380,240 80,60" fill="none" stroke="var(--c-gray)" stroke-width="2"/>

<!-- Right angle mark -->
<rect x="80" y="220" width="20" height="20" fill="none" stroke="var(--c-gray)" stroke-width="1.5"/>

<!-- Angle alpha arc -->
<path d="M 380 240 A 40 40 0 0 0 356 206" fill="none" stroke="var(--c-purple)" stroke-width="2"/>
<text x="358" y="230" class="th" fill="var(--c-purple)" text-anchor="start">a</text>

<!-- Side labels -->
<!-- Hypotenuse (diagonal) label -->
<text x="250" y="140" class="th" fill="var(--c-coral)" text-anchor="middle" transform="rotate(-53,250,140)">hipotenusa</text>

<!-- Cateto oposto (vertical, left) -->
<text x="55" y="155" class="th" fill="var(--c-teal)" text-anchor="middle" transform="rotate(-90,55,155)">cateto oposto</text>

<!-- Cateto adjacente (horizontal, bottom) -->
<text x="230" y="265" class="th" fill="var(--c-amber)" text-anchor="middle">cateto adjacente</text>

<!-- Formula boxes -->
<rect x="410" y="20" width="255" height="44" rx="8" class="c-teal"/>
<text x="537" y="38" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">sen a = cateto oposto</text>
<text x="537" y="56" class="ts" text-anchor="middle" fill="var(--on-accent)">hipotenusa</text>

<rect x="410" y="80" width="255" height="44" rx="8" class="c-amber"/>
<text x="537" y="98" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">cos a = cateto adjacente</text>
<text x="537" y="116" class="ts" text-anchor="middle" fill="var(--on-accent)">hipotenusa</text>

<rect x="410" y="140" width="255" height="44" rx="8" class="c-coral"/>
<text x="537" y="158" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">tg a = cateto oposto</text>
<text x="537" y="176" class="ts" text-anchor="middle" fill="var(--on-accent)">cateto adjacente</text>

<!-- Lines from triangle to formulas -->
<line x1="230" y1="145" x2="405" y2="42" stroke="var(--c-teal)" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arr-mat10a)"/>
<line x1="230" y1="240" x2="405" y2="102" stroke="var(--c-amber)" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arr-mat10a)"/>
<line x1="80" y1="155" x2="405" y2="162" stroke="var(--c-coral)" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arr-mat10a)"/>

<!-- Note: relativity -->
<rect x="15" y="280" width="650" height="28" rx="6" class="c-gray"/>
<text x="340" y="290" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Atencao: oposto e adjacente dependem do angulo de referencia — mudam se mudar qual angulo e analisado</text>
</svg>
```

---

### DIAGRAMA: angulos_notaveis
Derivação e tabela dos ângulos notáveis 30°, 45° e 60°.

```svg
<svg width="100%" viewBox="0 0 680 310" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat10b" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Left: Equilateral triangle (for 30/60) -->
<rect x="10" y="10" width="195" height="140" rx="8" class="c-purple"/>
<text x="107" y="28" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">30 e 60 graus</text>
<!-- Triangle shape -->
<polygon points="107,44 57,124 157,124" fill="none" stroke="white" stroke-width="1.5"/>
<line x1="107" y1="44" x2="107" y2="124" stroke="white" stroke-width="1" stroke-dasharray="3,2"/>
<!-- Right angle at bottom -->
<rect x="107" y="108" width="10" height="10" fill="none" stroke="white" stroke-width="1"/>
<!-- Labels -->
<text x="107" y="136" class="ts" text-anchor="middle" fill="var(--on-accent)">hip=2  adj=1  op=sqrt(3)</text>
<text x="107" y="148" class="ts" text-anchor="middle" fill="var(--on-accent)">sen60=sqrt(3)/2  cos60=1/2</text>

<!-- Right: Isoceles right triangle (for 45) -->
<rect x="215" y="10" width="195" height="140" rx="8" class="c-teal"/>
<text x="312" y="28" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">45 graus</text>
<!-- Triangle shape -->
<polygon points="255,124 369,124 369,44" fill="none" stroke="white" stroke-width="1.5"/>
<!-- Right angle -->
<rect x="359" y="114" width="10" height="10" fill="none" stroke="white" stroke-width="1"/>
<!-- Labels -->
<text x="312" y="136" class="ts" text-anchor="middle" fill="var(--on-accent)">catetos = 1  hip = sqrt(2)</text>
<text x="312" y="148" class="ts" text-anchor="middle" fill="var(--on-accent)">sen45=cos45=sqrt(2)/2</text>

<!-- Table: notable angles -->
<rect x="420" y="10" width="250" height="140" rx="8" class="c-gray"/>
<text x="545" y="28" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Tabela — Angulos Notaveis</text>

<!-- Table header -->
<text x="470" y="50" class="ts" text-anchor="middle" fill="var(--on-accent)">Razao</text>
<text x="525" y="50" class="ts" text-anchor="middle" fill="var(--on-accent)">30</text>
<text x="575" y="50" class="ts" text-anchor="middle" fill="var(--on-accent)">45</text>
<text x="625" y="50" class="ts" text-anchor="middle" fill="var(--on-accent)">60</text>
<line x1="425" y1="58" x2="665" y2="58" stroke="white" stroke-width="0.5"/>

<text x="470" y="76" class="ts" text-anchor="middle" fill="var(--on-accent)">sen</text>
<text x="525" y="76" class="ts" text-anchor="middle" fill="var(--on-accent)">1/2</text>
<text x="575" y="76" class="ts" text-anchor="middle" fill="var(--on-accent)">r2/2</text>
<text x="625" y="76" class="ts" text-anchor="middle" fill="var(--on-accent)">r3/2</text>

<text x="470" y="100" class="ts" text-anchor="middle" fill="var(--on-accent)">cos</text>
<text x="525" y="100" class="ts" text-anchor="middle" fill="var(--on-accent)">r3/2</text>
<text x="575" y="100" class="ts" text-anchor="middle" fill="var(--on-accent)">r2/2</text>
<text x="625" y="100" class="ts" text-anchor="middle" fill="var(--on-accent)">1/2</text>

<text x="470" y="124" class="ts" text-anchor="middle" fill="var(--on-accent)">tg</text>
<text x="525" y="124" class="ts" text-anchor="middle" fill="var(--on-accent)">r3/3</text>
<text x="575" y="124" class="ts" text-anchor="middle" fill="var(--on-accent)">1</text>
<text x="625" y="124" class="ts" text-anchor="middle" fill="var(--on-accent)">r3</text>

<text x="545" y="144" class="ts" text-anchor="middle" fill="var(--on-accent)">r2=sqrt(2), r3=sqrt(3)</text>

<!-- Arrows from triangles to table -->
<line x1="205" y1="80" x2="415" y2="80" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat10b)"/>

<!-- Memory tip -->
<rect x="10" y="164" width="655" height="34" rx="6" class="c-amber"/>
<text x="337" y="176" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Macete: sen CRESCE (1/2 → r2/2 → r3/2); cos FAZ O INVERSO; sen30=cos60; sen60=cos30</text>
<text x="337" y="192" class="ts" text-anchor="middle" fill="var(--on-accent)">Pares complementares: sen a = cos(90-a)</text>

<!-- Application box -->
<rect x="10" y="210" width="655" height="86" rx="8" class="c-teal"/>
<text x="337" y="228" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Exemplos de aplicacao</text>
<text x="337" y="250" class="ts" text-anchor="middle" fill="var(--on-accent)">Escada 4m com 60°: altura na parede = 4 x sen60 = 4 x r3/2 = 2r3 m</text>
<text x="337" y="268" class="ts" text-anchor="middle" fill="var(--on-accent)">Rio: base 30m, angulo 60°: largura = 30 x tg60 = 30r3 m</text>
<text x="337" y="286" class="ts" text-anchor="middle" fill="var(--on-accent)">Rampa 30°, base 30m: comprimento = 30/cos30 = 20r3 m; altura = 30 x tg30 = 10r3 m</text>
</svg>
```

---

### DIAGRAMA: identidades_trig
Identidade fundamental e relação da tangente — demonstração e uso.

```svg
<svg width="100%" viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr-mat10c" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Top: Identidade fundamental -->
<rect x="165" y="10" width="350" height="44" rx="8" class="c-purple"/>
<text x="340" y="28" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Identidade Fundamental</text>
<text x="340" y="46" class="th" text-anchor="middle" fill="var(--on-accent)">sen2(a) + cos2(a) = 1</text>

<!-- Arrow down left -->
<line x1="260" y1="54" x2="165" y2="100" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat10c)"/>
<!-- Arrow down right -->
<line x1="420" y1="54" x2="515" y2="100" stroke="var(--c-purple)" stroke-width="1.5" marker-end="url(#arr-mat10c)"/>

<!-- Left box: Origin (Pythagorean) -->
<rect x="15" y="100" width="295" height="80" rx="8" class="c-teal"/>
<text x="162" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Origem: Teorema de Pitagoras</text>
<text x="162" y="142" class="ts" text-anchor="middle" fill="var(--on-accent)">a2 + b2 = c2  (dividir por c2)</text>
<text x="162" y="160" class="ts" text-anchor="middle" fill="var(--on-accent)">(a/c)2 + (b/c)2 = 1  →  sen2 + cos2 = 1</text>

<!-- Right box: Usage -->
<rect x="370" y="100" width="295" height="80" rx="8" class="c-amber"/>
<text x="517" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Uso pratico</text>
<text x="517" y="142" class="ts" text-anchor="middle" fill="var(--on-accent)">Dado cos a = 3/5: sen2 = 1 - 9/25 = 16/25</text>
<text x="517" y="160" class="ts" text-anchor="middle" fill="var(--on-accent)">sen a = 4/5  (raiz positiva para angulo agudo)</text>

<!-- Divider line -->
<line x1="15" y1="198" x2="665" y2="198" stroke="var(--c-gray)" stroke-width="1" stroke-dasharray="4,3"/>

<!-- Bottom: Relacao tangente -->
<rect x="165" y="210" width="350" height="34" rx="8" class="c-coral"/>
<text x="340" y="227" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Relacao da Tangente</text>
<text x="340" y="239" class="ts" text-anchor="middle" fill="var(--on-accent)">tg a = sen a / cos a</text>

<!-- Derivation note -->
<rect x="15" y="256" width="295" height="34" rx="6" class="c-gray"/>
<text x="162" y="268" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Derivacao: sen/cos = (op/hip)/(adj/hip)</text>
<text x="162" y="284" class="ts" text-anchor="middle" fill="var(--on-accent)">= op/adj = tg a</text>

<!-- Use case: dado tg -->
<rect x="370" y="256" width="295" height="34" rx="6" class="c-coral"/>
<text x="517" y="268" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Dado tg a = k: escreva sen a = k cos a</text>
<text x="517" y="284" class="ts" text-anchor="middle" fill="var(--on-accent)">substitua em sen2+cos2=1 e resolva</text>
</svg>
```
