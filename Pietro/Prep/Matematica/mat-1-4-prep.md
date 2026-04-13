
## DIAGRAMAS DISPONÍVEIS — mat-1-4

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Semelhança de polígonos | DIAGRAMA: semelhanca | Ao introduzir razão de semelhança e proporção de lados |
| Casos de semelhança | DIAGRAMA: casos_semelhanca | Ao apresentar AA, LAL e LLL |
| Teorema Fundamental | DIAGRAMA: teorema_fundamental | Ao demonstrar DE ∥ BC → △ADE ~ △ABC |

### Tabelas markdown (Seção 6):
- Tabela de casos de semelhança (AA, LAL, LLL) com condições e expressões

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.

---

## SEÇÃO 1 — METADADOS

# PREPARAÇÃO DE AULA — MATEMÁTICA
- Unidade: 1
- Capítulo: 4
- Tema: Semelhança de Triângulos
- Perfil: geometria
- Fórmulas principais: k = AB/A'B' · a/d = b/e = c/f = k · AD/BD = AE/CE
- Matemáticos citados: nenhum

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### Bloco 1 — Semelhança de Polígonos

Duas figuras são **semelhantes** quando seus lados correspondentes
são proporcionais e seus ângulos correspondentes são congruentes.
O símbolo usado é **~**: escrevemos ABCD ~ A'B'C'D'.

Exemplo concreto do livro: quadrilátero ABCD com lados 12 cm,
15 cm, 9 cm e 6 cm é semelhante a A'B'C'D' com lados 4 cm, 5 cm,
3 cm e 2 cm. Verificando as razões:

$$\frac{12}{4} = \frac{15}{5} = \frac{9}{3} = \frac{6}{2} = 3$$

Todas as razões são iguais a 3 — esse valor é a **razão de
semelhança** k. Dizer k = 3 significa que cada lado da figura
original é o triplo do lado homólogo (correspondente) da redução.
**Homólogo** = de mesma posição, correspondente.

---

### Bloco 2 — Semelhança de Triângulos

Dois triângulos são semelhantes (△ABC ~ △DEF) se e somente se:
1. Os lados correspondentes são proporcionais: a/d = b/e = c/f = k
2. Os ângulos internos correspondentes são congruentes:
   Â ≅ D̂, B̂ ≅ Ê, Ĉ ≅ F̂

Na prática, não é necessário verificar todas as seis condições:
existem os **casos de semelhança de triângulos** que exigem
condições mínimas.

---

### Bloco 3 — Teorema Fundamental da Semelhança

Se uma reta é paralela a um lado de um triângulo e intersecta os
outros dois lados em pontos distintos, o triângulo menor formado é
semelhante ao triângulo original.

Simbolicamente: DE ∥ BC ⇒ △ADE ~ △ABC

A demonstração usa igualdade de áreas dos triângulos BDE e CDE
(mesma base DE, mesma altura), concluindo:

$$\frac{AD}{BD} = \frac{AE}{CE}$$

Aplicação direta (Q-3): DE ∥ BC, AB = 10, AD = 4, BC = 14
→ k = AD/AB = 4/10 = 2/5 → DE = 14 × (2/5) = 5,6 cm

---

### Bloco 4 — Casos de Semelhança

**AA (Ângulo–Ângulo):** basta dois ângulos congruentes.
Raciocínio: se dois ângulos são iguais, o terceiro também é
(soma 180°), então todos os ângulos são congruentes — pelo Bloco 2,
os triângulos são semelhantes.

**LAL (Lado–Ângulo–Lado):** dois lados proporcionais e o ângulo
compreendido entre eles congruente.
Exemplo resolvido 1: BC/EF = 7/10,5 = AC/DF = 6/9 = 1/1,5 e
Ĉ ≅ F̂ → △ABC ~ △DEF por LAL → k = 1,5 → AB = 13,5/1,5 = 9 cm
→ Perímetro ABC = 9 + 6 + 7 = 22 cm.

**LLL (Lado–Lado–Lado):** todos os lados correspondentes
proporcionais. Se AC/A'C' = AB/A'B' = BC/B'C', os triângulos
são semelhantes.

---

### Bloco 5 — Razão de Semelhança e Perímetros/Áreas

Se a razão de semelhança é k:
- Razão entre **perímetros** = k
- Razão entre **áreas** = k²

Isso é fundamental para questões como Q-4 (razão k=7, perímetro
DEF=63 → perímetro ABC = 63/7 = 9 mm) e Q-6 (área com k²).

---

### Bloco 6 — Aplicações Práticas

A semelhança de triângulos aparece em:
- **Sombras e alturas** (QC-3, QC-4): torre/estaca, prédio/poste
  formam triângulos semelhantes pelos raios do sol paralelos.
- **Balestilha portuguesa**: instrumento que media ângulos entre
  astros usando triângulos semelhantes nas Grandes Navegações.
- **Lupa**: a luz desviada forma triângulos semelhantes, tornando a
  imagem proporcionalmente maior.
- **Arte**: obra de Tatsuya Tanaka usa máscara 180 mm × 90 mm para
  representar piscinas olímpicas 50 m × 25 m — preservação da
  proporção original.

---

## SEÇÃO 3 — MATEMÁTICOS E HISTÓRIA DA MATEMÁTICA

*Nenhum matemático histórico é citado nominalmente neste capítulo.*

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

---

### Razão de semelhança entre dois polígonos

**Expressão:**
$$k = \frac{AB}{A'B'} = \frac{BC}{B'C'} = \frac{CD}{C'D'} = \frac{DA}{D'A'}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| k | razão de semelhança | real positivo |
| AB, BC… | lados do polígono original | comprimento (real > 0) |
| A'B', B'C'… | lados homólogos do polígono semelhante | comprimento (real > 0) |

**Válida quando:** os polígonos são semelhantes (lados proporcionais
e ângulos congruentes).
**Caso especial:** k = 1 → figuras congruentes (iguais em tamanho).
💡 **Pegadinha:** Confundir k com k² — a razão dos **perímetros** é k,
mas a razão das **áreas** é k². Se k = 3, a área cresce 9 vezes!

---

### Semelhança de triângulos — expressão geral

**Expressão:**
$$\frac{a}{d} = \frac{b}{e} = \frac{c}{f} = k$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| a, b, c | lados do triângulo ABC | comprimento (real > 0) |
| d, e, f | lados homólogos do triângulo DEF | comprimento (real > 0) |
| k | razão de semelhança | real positivo |

**Válida quando:** △ABC ~ △DEF (confirmado por AA, LAL ou LLL).
💡 **Pegadinha:** A **ordem** das letras na semelhança importa!
△ABC ~ △DEF significa A↔D, B↔E, C↔F. Trocar a ordem muda quais
lados são homólogos e gera proporções erradas.

---

### Proporcionalidade do Teorema Fundamental

**Expressão:**
$$\frac{AD}{BD} = \frac{AE}{CE}$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| AD, BD | segmentos do lado AB determinados por D | comprimento (real > 0) |
| AE, CE | segmentos do lado AC determinados por E | comprimento (real > 0) |

**Válida quando:** DE ∥ BC, com D em AB e E em AC.
**Caso especial:** Se D e E são pontos médios, k = 1/2 e DE = BC/2.
💡 **Pegadinha:** O teorema relaciona os **segmentos parciais** entre si
(AD/BD), não o segmento parcial com o total (AD/AB). Ambas as formas
são corretas, mas a confusão entre elas gera erros de proporção.

---

### Razão de semelhança e razão de áreas

**Expressão:**
$$\frac{\text{Área}_{ABC}}{\text{Área}_{DEF}} = k^2$$

| Símbolo | Significado | Tipo |
|---------|-------------|------|
| k | razão de semelhança entre △ABC e △DEF | real positivo |

**Válida quando:** △ABC ~ △DEF com razão k.
💡 **Pegadinha:** Ao dobrar os lados (k=2), a área quadruplica (k²=4),
não dobra. Erro muito comum em questões de concurso.

---

## SEÇÃO 5 — REPRESENTAÇÕES E SISTEMAS

*Não aplicável — o capítulo é de geometria pura sem representações
em plano cartesiano, reta numérica ou conjuntos numéricos.*

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Casos de Semelhança de Triângulos

| Caso | Nome | Condição mínima | Expressão simbólica |
|------|------|-----------------|---------------------|
| AA | Ângulo–Ângulo | Dois ângulos congruentes | Â ≅ Â' e B̂ ≅ B̂' |
| LAL | Lado–Ângulo–Lado | Dois lados proporcionais + ângulo compreendido congruente | AB/A'B' = BC/B'C' e B̂ ≅ B̂' |
| LLL | Lado–Lado–Lado | Todos os lados proporcionais | AC/A'C' = AB/A'B' = BC/B'C' |

### Razões em figuras semelhantes (razão de semelhança k)

| Elemento | Razão |
|----------|-------|
| Lados correspondentes | k |
| Perímetros | k |
| Áreas | k² |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — A ordem na semelhança não é decorativa**
△ABC ~ △DEF indica correspondência direta: A↔D, B↔E, C↔F.
Se o livro escrever △ABC ~ △EFD, então A↔E, B↔F, C↔D. Montar a
proporção com a ordem errada garante resultado errado.

💡 **Dica 2 — Perímetro × k, Área × k²**
Se dois triângulos semelhantes têm razão k = 3, o perímetro
cresce 3 vezes mas a área cresce 9 vezes. Nunca confundir as duas
razões. (Q-4: k=7, perímetro DEF=63 → perímetro ABC = 9 mm)

💡 **Dica 3 — Teorema Fundamental: segmento parcial vs. total**
AD/BD = AE/CE (parcial/parcial) é equivalente a AD/AB = AE/AC
(parcial/total), mas NÃO a AD/AB = BD/AC. Escolha UMA forma e
mantenha a consistência na proporção.

💡 **Dica 4 — Dois ângulos bastam (caso AA)**
Em concursos, basta encontrar dois ângulos iguais para concluir
semelhança — não é preciso calcular lados. Ângulo reto explícito
+ um ângulo agudo comum já garantem AA.

💡 **Dica 5 — Congruência ≠ Semelhança**
Triângulos congruentes são sempre semelhantes (k=1), mas semelhantes
NÃO são necessariamente congruentes. A questão QC-2 (UEM-PR 2016)
explora exatamente essa distinção — item cuidado.

💡 **Dica 6 — Sombras e alturas: atenção às unidades**
Em problemas com sombras (QC-3), todos os dados devem estar na
mesma unidade antes de montar a proporção. A sombra da estaca
é 50 cm = 0,5 m. Misturar metros e centímetros é o erro mais
frequente nesse tipo de questão.

---

## SEÇÃO 8 — ALERTAS E LACUNAS
```
✅ ALERTA RESOLVIDO — Q-7
Dados corretos confirmados pela figura:
AD=12 m · DE=8 m · EC=20 m · BC=16 m
Resolução: k=1/2 → AE=20 m → P(ADE) = 40 m
Remover ⚠️ do catálogo.

✅ ALERTA RESOLVIDO — Q-11
Lado do quadrado não numerado — resolução em função de ℓ.
M confirmado como ponto médio de BA.
Resolução: coordenadas → I=(2ℓ/5, 4ℓ/5) → Área(NIC) = ℓ²/20
Remover ⚠️ do catálogo.
```

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

### Bloco 1 — Conceitos e Definições

- **Semelhança**
  - Definição: figuras com lados correspondentes `______` e ângulos correspondentes `______` *(proporcionais; congruentes)*
  - Notação: símbolo `______` *(~)*

- **Razão de semelhança**
  - Definição: valor constante obtido ao dividir `______` de figuras semelhantes *(quaisquer dois lados correspondentes)*
  - k = 3 significa: cada lado da figura original é `______` do lado homólogo *(o triplo)*

- **Homólogo**
  - Significado: `______` *(de mesma posição; correspondente)*

- **Teorema Fundamental da Semelhança**
  - Enunciado: se uma reta é `______` a um lado de um triângulo e intersecta os outros dois lados em pontos distintos, o triângulo determinado é `______` ao triângulo inicial *(paralela; semelhante)*

- **Caso AA**
  - Condição: dois triângulos são semelhantes se possuem `______` *(dois ângulos congruentes)*

- **Caso LAL**
  - Condição: dois lados correspondentes `______` e o ângulo `______` entre eles congruente *(proporcionais; compreendido)*

- **Caso LLL**
  - Condição: `______` os lados correspondentes proporcionais *(todos)*

### Bloco 2 — Fórmulas e Propriedades

- **Razão de semelhança**
  - Expressão: `______` *(k = AB/A'B' = BC/B'C' = …)*
  - Variável k: `______` *(razão de semelhança)*
  - Condição: `______` *(figuras semelhantes)*

- **Expressão geral de triângulos semelhantes**
  - Expressão: `______` *(a/d = b/e = c/f = k)*
  - Condição: `______` *(△ABC ~ △DEF)*

- **Proporcionalidade do Teorema Fundamental**
  - Expressão: `______` *(AD/BD = AE/CE)*
  - Condição: `______` *(DE ∥ BC)*

- **Razão de áreas**
  - Se a razão de semelhança é k, a razão das áreas é `______` *(k²)*

### Bloco 3 — Lacunas para Warm-Up

1. Dois polígonos são semelhantes se seus lados correspondentes são `______` e seus ângulos correspondentes são `______`.
*(proporcionais; congruentes)*

2. Se △ABC ~ △DEF com k = 4, o perímetro de DEF é `______` vezes o perímetro de ABC e a área de DEF é `______` vezes a área de ABC.
*(4 vezes; 16 vezes)*

3. Pelo Teorema Fundamental da Semelhança, se DE ∥ BC com D em AB e E em AC, então △ADE ~ `______`.
*(△ABC)*

4. Para provar semelhança pelo caso LAL é preciso mostrar que dois lados são `______` e que o ângulo `______` entre eles é congruente.
*(proporcionais; compreendido)*

5. A balestilha portuguesa usava a semelhança de triângulos para medir `______` entre astros durante as `______`.
*(ângulos; Grandes Navegações)*

6. Na obra de Tatsuya Tanaka, uma máscara de 180 mm × 90 mm representa uma piscina olímpica de 50 m × 25 m. Para que a representação seja semelhante, os lados devem ser `______`.
*(proporcionais — a razão 180mm/50m = 90mm/25m deve ser constante)*

7. Em problemas de sombra (torre e estaca), os triângulos formados são semelhantes porque os raios solares são `______`, criando ângulos iguais.
*(paralelos)*

8. Se dois triângulos congruentes têm razão de semelhança k = `______`, pois congruência é um caso particular de semelhança.
*(1)*

#### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Definição de semelhança | Lados correspondentes `______` e ângulos correspondentes `______` → proporcionais; congruentes |
| Notação de semelhança | Símbolo `______` → ~ |
| Razão de semelhança k | Constante igual à razão entre `______` → lados homólogos correspondentes |
| Teorema Fundamental | Reta paralela a um lado cria triângulo `______` ao original → semelhante |
| Caso AA | Dois ângulos `______` garantem semelhança → congruentes |
| Caso LAL | Dois lados `______` e ângulo `______` entre eles congruente → proporcionais; compreendido |
| Caso LLL | `______` os lados correspondentes proporcionais → todos |
| Razão das áreas | Se k é a razão de semelhança, a razão das áreas é `______` → k² |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

### Síntese do Livro — SEMELHANÇA DE TRIÂNGULOS

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| Caixa central (pílula amarela) | Semelhança | — |
| Caixa de definição (topo, borda vermelha) | Polígonos semelhantes: lados correspondentes proporcionais e ângulos correspondentes congruentes. Se k é razão de semelhança: razão entre perímetros = k, razão entre áreas = k² | — |
| Dois triângulos ABC e DEF com ângulos e lados rotulados | Â = D̂, B̂ = Ê, Ĉ = F̂ e a/d = b/e = c/f = k | △ABC ~ △DEF |
| Ramo esquerdo (borda vermelha) | Teorema fundamental da semelhança | — |
| Texto do ramo esquerdo | Se uma reta é paralela a um dos lados de um triângulo, intersectando os outros dois lados em pontos distintos, então o triângulo que essa reta determina é semelhante ao triângulo inicial | — |
| Ramo direito (borda vermelha) | Casos de semelhança de triângulos | — |
| Subnós do ramo direito | Ângulo – Ângulo (AA) · Lado – Ângulo – Lado (LAL) · Lado – Lado – Lado (LLL) | Lacuna possível: enunciar a condição mínima de cada caso |
| Lacuna warm-up 1 | "Dois triângulos são semelhantes se possuem dois ângulos `______`" | congruentes (caso AA) |
| Lacuna warm-up 2 | "A razão entre as áreas de dois triângulos semelhantes com razão k é `______`" | k² |
| Lacuna warm-up 3 | "O símbolo de semelhança é `______`" | ~ |

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Gabarito | Obs. |
|---|---|---|---|---|---|
| QC-1 | Ampliação de △ABC: qual elemento conserva medida? | MC | F | **d) os ângulos** — em semelhança, ângulos são congruentes; lados, perímetros e áreas mudam proporcionalmente | Prova Brasil |
| Q-1 | Verificar semelhança em 3 pares de triângulos | Dis | M | a) LLL: 9/4,5=2; 12/6=2; 13/6,5=2 → sim, k=2. b) LLL: 12/30=16/40=20/50=2/5 → sim (unidades diferentes: converter mm→cm). c) LAL: ângulo 45° igual, MN/PQ=7/16 ≠ MO/PR=8/15 → **não semelhantes** | — |
| Q-2 | Determinar x e y em triângulos semelhantes | Cal | M | k = 35/14 = 2,5 → x = 12×2,5 = **30 mm** · y = 10×2,5 = **25 mm** | — |
| QC-2 | UEM-PR: afirmações sobre congruência e semelhança (soma) | Cal | D | Itens corretos: **02** (congruentes têm mesma área) + **08** (congruentes são semelhantes) + **16** (caso LAL de congruência → AC=DF). Soma = 02+08+16 = **26** | UEM-PR 2016 |
| QC-3 | Altura da torre por semelhança com estaca | MC | M | estaca: 1 m alto, 0,5 m sombra; torre: ? alto, 12 m sombra. k = 12/0,5 = 24 → altura = 1×24 = **24 m** → **b)** | Unemat-MT 2015 |
| Q-3 | DE ∥ BC; calcular DE | Cal | M | k = AD/AB = 4/10 = 2/5 → DE = BC×k = 14×(2/5) = **5,6 cm** | — |
| QC-4 | Altura do prédio por sombra | MC | F | 5/3 = h/15 → h = **25 m** → **a)** | Unesp |
| Q-4 | Razão k=7, perímetro DEF=63 mm → perímetro ABC | Cal | F | P_ABC = 63/7 = **9 mm** | — |
| Q-5 | Triângulo lados 10, 14, 12 cm; semelhante perímetro 54 cm | Cal | M | Perímetro original = 36 cm; k = 54/36 = 1,5 → lados: **15 cm, 21 cm, 18 cm** | — |
| Q-6 | △ABC área 300 cm², semelhante a △DEF catetos 5 e 7,5 cm; hipotenusa de ABC | Cal | D | Área DEF = (5×7,5)/2 = 18,75 cm²; k² = 300/18,75 = 16 → k=4; hipotenusa DEF = √(5²+7,5²) = √81,25 = √(325/4) = (√325)/2; hip_ABC = k × hip_DEF = 4 × (√325)/2 = **2√325 ≈ 36,1 cm** | — |
| # | Enunciado resumido | Tipo | Dif. | Gabarito | Obs. |
| # | Enunciado resumido | Tipo | Dif. | Gabarito | Obs. |
| Q-7 | Perímetro do △ADE com DE ∥ BC | Cal | M | 40 m · k = DE/BC = 8/16 = 1/2 → AB = 2×AD = 2×12 = 24 m → AE: AE/(AE+20) = 1/2 → AE = 20 m → P = 12+8+20 = 40 m | — |
ℓ/2) → DN: y=2x · CM: y=−x/2+ℓ → I=(2ℓ/5, 4ℓ/5) → Área = (1/2) | ℓ/2·(−ℓ/5) |
| QC-5 | Segmento CE em triângulo com DE ∥ BC | Cal | M | AD/DB = 2/3 → AD = 6 cm, DB = 9 cm, AB = 15 cm ✓; k = AD/AB = 6/15 = 2/5; AE/AC = 2/5 → AC = AE/(2/5) = 8/(2/5) = 20 cm → CE = 20−8 = **12 cm** | UEG-GO |
| Q-8 | Quadrado BDEF inscrito em △ABC retângulo (AB=1, BC=3); perímetro | Cal | D | Seja l o lado do quadrado. Por semelhança: △ADE ~ △ABC → (1−l)/l = 1/3 → 3−3l = l → l = 3/4; perímetro = 4×(3/4) = **3 cm** | — |
| Q-9 | Área do quadrilátero ABDE (△ retângulo, AB=20, BD=16, BE=12) | Cal | D | △BDE: BE=12, BD=16 → área = (12×16)/2 = 96 cm². △ABC: AB=20, BC=BD+DC; pelo teorema de Pitágoras aplicado ao triângulo e à altura BE: AB×BC = BE × AC (relação da altura sobre hipotenusa não se aplica diretamente). Usando área △ABE + △BDE: área ABDE = (AB×BE)/2 = (20×12)/2 = **120 cm²** | ⚠️ figura parcial |
| Q-10 | Três lotes; qual tem maior área? | Dis | D | Os lotes têm a mesma altura (determinada pela diagonal comum); lote I tem frente 50 m (maior) → **lote I tem maior área** | — |
| Q-11 | Área do △NIC em quadrado ABCD com N e M midpoints | Cal | D | ℓ²/20 · Sistema de coord.: D=(0,0), C=(0,ℓ), B=(ℓ,ℓ), A=(ℓ,0) → N=(ℓ/2, ℓ), M=(ℓ, 
| QC-6 | Haste EF entre postes 4 m e 6 m (harmônica) | MC | D | Fórmula da média harmônica: 1/EF = 1/4 + 1/6 = 5/12 → EF = **12/5 = 2,4 m** → **c)** | ENEM |
| QC-7 | Porta de garagem: distância de C ao trilho; altura de Y constante | Dis | D | a) Triângulos semelhantes: CX/AX = distância_C/distância_X → por semelhança CY/XY e BC=CY=0,5; razão = 0,5/1 = 1/2 → dist_C = 0,2×(1/2) = **0,1 m**. b) YD = YA + AD; como AC=BC=CY=0,5 e semelhança, YD é constante. | Obmep (Adapt.) |
| QC-8 | Dobras em folha 10×20 cm; área colorida visível | MC | D | Diagonal BD = √(10²+20²) = √500 = 10√5; área total = 200 cm²; dobras simétricas → área visível = área do losango central = **100 cm²** → **d)** | Obmep 2022 |

---

### Bloco B — Questões Modelo Originais

---

**QM-1** · múltipla escolha · médio · inspirada em: QC-4

Uma régua de 30 cm, posicionada verticalmente no chão, projeta uma
sombra de 20 cm no mesmo instante em que uma árvore projeta uma
sombra de 5 m. Qual é a altura da árvore?

a) 3,5 m  
b) 6,5 m  
c) 7,5 m  
d) 10 m  

✅ Gabarito: c) 7,5 m  
📝 Resolução:
Converter: régua = 30 cm = 0,30 m; sombra régua = 20 cm = 0,20 m.
Triângulos semelhantes (raios solares paralelos):
altura_régua / sombra_régua = altura_árvore / sombra_árvore
0,30/0,20 = h/5 → h = 5 × 1,5 = **7,5 m**

⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-2** · múltipla escolha · médio · inspirada em: Q-5

Os lados de um triângulo medem 8 cm, 15 cm e 17 cm. Um triângulo
semelhante a ele tem perímetro de 80 cm. Qual é a medida do maior
lado do triângulo semelhante?

a) 25 cm  
b) 32 cm  
c) 34 cm  
d) 40 cm  

✅ Gabarito: c) 34 cm  
📝 Resolução:
Perímetro original = 8 + 15 + 17 = 40 cm.
k = 80/40 = 2.
Maior lado = 17 × 2 = **34 cm**.

⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-3** · cálculo · médio · inspirada em: Q-3

No triângulo PQR, traça-se ST ∥ QR com S sobre PQ e T sobre PR.
Sabe-se que PS = 6 cm, SQ = 9 cm e QR = 20 cm. Calcule ST e PT,
dado que PR = 25 cm.

✅ Gabarito: ST = 8 cm · PT = 10 cm  
📝 Resolução:
PQ = PS + SQ = 6 + 9 = 15 cm.
k = PS/PQ = 6/15 = 2/5.
ST = QR × k = 20 × (2/5) = **8 cm**.
PT = PR × k = 25 × (2/5) = **10 cm**.

⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-4** · estilo concurso · difícil · inspirada em: QC-6

*(Estilo ENEM/Fuvest)*

Dois postes verticais estão fincados no solo plano. O poste da
esquerda tem 10 m de altura e o da direita tem 6 m. Um cabo vai do
topo do poste esquerdo ao pé do direito, e outro cabo vai do topo do
direito ao pé do esquerdo. No ponto de cruzamento dos cabos, uma
haste vertical é instalada. Qual é a altura dessa haste?

a) 3,0 m  
b) 3,75 m  
c) 4,0 m  
d) 5,0 m  
e) 6,0 m  

✅ Gabarito: b) 3,75 m  
📝 Resolução:
Fórmula da média harmônica para a haste entre dois postes a e b:
$$\frac{1}{h} = \frac{1}{a} + \frac{1}{b} = \frac{1}{10} + \frac{1}{6} = \frac{3+5}{30} = \frac{8}{30}$$
$$h = \frac{30}{8} = \frac{15}{4} = \textbf{3,75 m}$$

⚠️ Professor: referência de estilo — crie variações originais.

---

**QM-5** · dissertativa · médio-difícil · inspirada em: QC-5

No triângulo ABC, o ponto D está sobre AB e DE é paralela a BC,
com E sobre AC. Sabe-se que AD = 4 cm, DB = 8 cm e AE = 5 cm.

a) Determine a razão de semelhança k entre △ADE e △ABC.
b) Calcule EC.
c) Se BC = 18 cm, qual é o comprimento de DE?
d) Qual é a razão entre as áreas de △ADE e △ABC?

✅ Gabarito:
a) k = AD/AB = 4/12 = **1/3**
b) AE/AC = 1/3 → AC = 15 cm → EC = 15−5 = **10 cm**
c) DE = 18 × (1/3) = **6 cm**
d) Razão das áreas = k² = (1/3)² = **1/9**

📝 Resolução completa:
AB = AD + DB = 4 + 8 = 12 cm.
k = 4/12 = 1/3.
AC = AE/k = 5/(1/3) = 15 → EC = 10 cm.
DE = BC × k = 18/3 = 6 cm.
Área: (1/3)² = 1/9 — a área de △ADE é um nono da área de △ABC.

⚠️ Professor: referência de estilo — crie variações originais.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: semelhanca
Dois triângulos semelhantes com razão k indicada entre lados homólogos.

```svg
<svg width="100%" viewBox="0 0 680 260"
     xmlns="http://www.w3.org/2000/svg"
     style="font-family:'Inter',sans-serif">
  <defs>
    <style>
      .c-purple{fill:#6B48FF;}
      .c-teal{fill:#0D9488;}
      .c-amber{fill:#D97706;}
      .c-coral{fill:#EF4444;}
      .c-gray{fill:#6B7280;}
      .c-green{fill:#16A34A;}
      .t{font-size:14px;fill:#1e293b;dominant-baseline:central;}
      .ts{font-size:11px;fill:#64748b;dominant-baseline:central;}
      .th{font-size:13px;font-weight:700;fill:#ffffff;dominant-baseline:central;}
    </style>
    <marker id="arr" markerWidth="8" markerHeight="8"
            refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#6B48FF"/>
    </marker>
  </defs>

  <!-- Triângulo ABC (menor) -->
  <polygon points="60,200 160,200 110,80"
           fill="#e0e7ff" stroke="#6B48FF" stroke-width="2"/>
  <text x="105" y="72" class="t" font-weight="700">A</text>
  <text x="48" y="210" class="t" font-weight="700">B</text>
  <text x="162" y="210" class="t" font-weight="700">C</text>
  <!-- lados -->
  <text x="68" y="148" class="ts" transform="rotate(-56,68,148)">c</text>
  <text x="148" y="148" class="ts" transform="rotate(56,148,148)">b</text>
  <text x="102" y="215" class="ts">a</text>
  <!-- rótulo triângulo -->
  <text x="100" y="230" class="ts" text-anchor="middle">△ABC</text>

  <!-- Seta de semelhança -->
  <line x1="200" y1="140" x2="270" y2="140"
        stroke="#6B48FF" stroke-width="2" marker-end="url(#arr)"/>
  <text x="235" y="128" class="ts" text-anchor="middle">k =</text>
  <text x="235" y="145" class="ts" text-anchor="middle">a/d = b/e = c/f</text>

  <!-- Triângulo DEF (maior) -->
  <polygon points="300,210 460,210 380,60"
           fill="#ccfbf1" stroke="#0D9488" stroke-width="2"/>
  <text x="374" y="50" class="t" font-weight="700">D</text>
  <text x="286" y="222" class="t" font-weight="700">E</text>
  <text x="462" y="222" class="t" font-weight="700">F</text>
  <!-- lados -->
  <text x="310" y="142" class="ts" transform="rotate(-52,310,142)">f</text>
  <text x="445" y="142" class="ts" transform="rotate(52,445,142)">e</text>
  <text x="375" y="228" class="ts">d</text>
  <!-- rótulo triângulo -->
  <text x="380" y="245" class="ts" text-anchor="middle">△DEF</text>

  <!-- Caixa de razão -->
  <rect x="505" y="60" width="155" height="140" rx="10"
        fill="#f1f5f9" stroke="#6B48FF" stroke-width="1.5"/>
  <text x="582" y="90" class="t" text-anchor="middle"
        font-weight="700">△ABC ~ △DEF</text>
  <line x1="515" y1="103" x2="650" y2="103"
        stroke="#cbd5e1" stroke-width="1"/>
  <text x="582" y="123" class="ts" text-anchor="middle">Â ≅ D̂</text>
  <text x="582" y="141" class="ts" text-anchor="middle">B̂ ≅ Ê</text>
  <text x="582" y="159" class="ts" text-anchor="middle">Ĉ ≅ F̂</text>
  <text x="582" y="182" class="ts" text-anchor="middle">a/d = b/e = c/f = k</text>
</svg>
```

---

### DIAGRAMA: casos_semelhanca
Três casos de semelhança de triângulos: AA, LAL e LLL.

```svg
<svg width="100%" viewBox="0 0 680 320"
     xmlns="http://www.w3.org/2000/svg"
     style="font-family:'Inter',sans-serif">
  <defs>
    <style>
      .c-purple{fill:#6B48FF;}
      .c-teal{fill:#0D9488;}
      .c-amber{fill:#D97706;}
      .c-coral{fill:#EF4444;}
      .c-gray{fill:#6B7280;}
      .t{font-size:14px;fill:#1e293b;dominant-baseline:central;}
      .ts{font-size:11px;fill:#64748b;dominant-baseline:central;}
      .th{font-size:13px;font-weight:700;fill:#ffffff;dominant-baseline:central;}
    </style>
  </defs>

  <!-- Título -->
  <rect x="190" y="10" width="300" height="44" rx="8" fill="#6B48FF"/>
  <text x="340" y="32" class="th" text-anchor="middle"
        font-size="15">Casos de Semelhança de Triângulos</text>

  <!-- CARD AA -->
  <rect x="20" y="75" width="195" height="210" rx="10"
        fill="#f1f5f9" stroke="#6B48FF" stroke-width="2"/>
  <rect x="20" y="75" width="195" height="44" rx="10" fill="#6B48FF"/>
  <text x="117" y="97" class="th" text-anchor="middle">AA</text>
  <text x="117" y="115" class="th" text-anchor="middle"
        font-size="11">Ângulo – Ângulo</text>
  <text x="117" y="148" class="ts" text-anchor="middle">Condição:</text>
  <text x="117" y="166" class="t" text-anchor="middle"
        font-weight="700">2 ângulos</text>
  <text x="117" y="184" class="t" text-anchor="middle"
        font-weight="700">congruentes</text>
  <text x="117" y="210" class="ts" text-anchor="middle">Â ≅ Â'  e  B̂ ≅ B̂'</text>
  <text x="117" y="232" class="ts" text-anchor="middle">⇒ Ĉ ≅ Ĉ' (automático)</text>
  <rect x="52" y="252" width="130" height="26" rx="6" fill="#0D9488"/>
  <text x="117" y="265" class="th" text-anchor="middle"
        font-size="12">△ABC ~ △A'B'C'</text>

  <!-- CARD LAL -->
  <rect x="242" y="75" width="195" height="210" rx="10"
        fill="#f1f5f9" stroke="#0D9488" stroke-width="2"/>
  <rect x="242" y="75" width="195" height="44" rx="10" fill="#0D9488"/>
  <text x="339" y="97" class="th" text-anchor="middle">LAL</text>
  <text x="339" y="115" class="th" text-anchor="middle"
        font-size="11">Lado – Ângulo – Lado</text>
  <text x="339" y="148" class="ts" text-anchor="middle">Condição:</text>
  <text x="339" y="166" class="t" text-anchor="middle"
        font-weight="700">2 lados proporcionais</text>
  <text x="339" y="184" class="t" text-anchor="middle"
        font-weight="700">+ ângulo entre eles ≅</text>
  <text x="339" y="210" class="ts" text-anchor="middle">AB/A'B' = BC/B'C'</text>
  <text x="339" y="228" class="ts" text-anchor="middle">e  B̂ ≅ B̂'</text>
  <rect x="274" y="252" width="130" height="26" rx="6" fill="#0D9488"/>
  <text x="339" y="265" class="th" text-anchor="middle"
        font-size="12">△ABC ~ △A'B'C'</text>

  <!-- CARD LLL -->
  <rect x="464" y="75" width="195" height="210" rx="10"
        fill="#f1f5f9" stroke="#D97706" stroke-width="2"/>
  <rect x="464" y="75" width="195" height="44" rx="10" fill="#D97706"/>
  <text x="561" y="97" class="th" text-anchor="middle">LLL</text>
  <text x="561" y="115" class="th" text-anchor="middle"
        font-size="11">Lado – Lado – Lado</text>
  <text x="561" y="148" class="ts" text-anchor="middle">Condição:</text>
  <text x="561" y="166" class="t" text-anchor="middle"
        font-weight="700">todos os lados</text>
  <text x="561" y="184" class="t" text-anchor="middle"
        font-weight="700">proporcionais</text>
  <text x="561" y="210" class="ts" text-anchor="middle">AC/A'C' = AB/A'B'</text>
  <text x="561" y="228" class="ts" text-anchor="middle">= BC/B'C'</text>
  <rect x="496" y="252" width="130" height="26" rx="6" fill="#D97706"/>
  <text x="561" y="265" class="th" text-anchor="middle"
        font-size="12">△ABC ~ △A'B'C'</text>
</svg>
```

---

### DIAGRAMA: teorema_fundamental
Teorema Fundamental da Semelhança: DE ∥ BC ⇒ △ADE ~ △ABC.

```svg
<svg width="100%" viewBox="0 0 680 300"
     xmlns="http://www.w3.org/2000/svg"
     style="font-family:'Inter',sans-serif">
  <defs>
    <style>
      .t{font-size:14px;fill:#1e293b;dominant-baseline:central;}
      .ts{font-size:11px;fill:#64748b;dominant-baseline:central;}
      .th{font-size:13px;font-weight:700;fill:#ffffff;dominant-baseline:central;}
    </style>
    <marker id="arr2" markerWidth="8" markerHeight="8"
            refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#6B48FF"/>
    </marker>
  </defs>

  <!-- Triângulo ABC grande -->
  <polygon points="200,40 60,250 340,250"
           fill="#e0e7ff" stroke="#6B48FF" stroke-width="2"/>

  <!-- Triângulo ADE menor (interno, destacado) -->
  <polygon points="200,40 137,155 263,155"
           fill="#ccfbf1" stroke="#0D9488" stroke-width="2"/>

  <!-- Rótulos vértices -->
  <text x="196" y="30" class="t" font-weight="700">A</text>
  <text x="44" y="258" class="t" font-weight="700">B</text>
  <text x="342" y="258" class="t" font-weight="700">C</text>
  <text x="122" y="167" class="t" font-weight="700">D</text>
  <text x="260" y="167" class="t" font-weight="700">E</text>

  <!-- Indicação DE ∥ BC -->
  <line x1="137" y1="155" x2="263" y2="155"
        stroke="#0D9488" stroke-width="2.5" stroke-dasharray="6,3"/>
  <text x="185" y="148" class="ts" fill="#0D9488"
        font-weight="700">DE ∥ BC</text>

  <!-- Seta de implicação -->
  <line x1="380" y1="145" x2="430" y2="145"
        stroke="#6B48FF" stroke-width="2" marker-end="url(#arr2)"/>

  <!-- Caixa de conclusão -->
  <rect x="440" y="60" width="220" height="170" rx="10"
        fill="#f8fafc" stroke="#6B48FF" stroke-width="1.5"/>
  <rect x="440" y="60" width="220" height="44" rx="10" fill="#6B48FF"/>
  <text x="550" y="82" class="th" text-anchor="middle"
        font-size="13">Teorema Fundamental</text>
  <text x="550" y="105" class="t" text-anchor="middle">△ADE ~ △ABC</text>
  <line x1="450" y1="118" x2="650" y2="118"
        stroke="#e2e8f0" stroke-width="1"/>
  <text x="550" y="138" class="ts" text-anchor="middle">AD/BD = AE/CE</text>
  <text x="550" y="158" class="ts" text-anchor="middle">AD/AB = AE/AC = DE/BC</text>
  <text x="550" y="180" class="ts" text-anchor="middle">= k (razão de semelhança)</text>
  <rect x="470" y="200" width="160" height="26" rx="6"
        fill="#EF4444"/>
  <text x="550" y="213" class="th" text-anchor="middle"
        font-size="12">Cuidado: AD/BD ≠ AD/AB</text>

  <!-- Proporcionalidade indicada na figura -->
  <text x="88" y="200" class="ts" fill="#6B48FF">AD</text>
  <text x="88" y="222" class="ts" fill="#0D9488">DB</text>
  <line x1="84" y1="208" x2="108" y2="208"
        stroke="#64748b" stroke-width="1"/>
  <text x="116" y="210" class="ts">=</text>
  <text x="130" y="200" class="ts" fill="#6B48FF">AE</text>
  <text x="130" y="222" class="ts" fill="#0D9488">CE</text>
  <line x1="126" y1="208" x2="154" y2="208"
        stroke="#64748b" stroke-width="1"/>
</svg>
```

---
