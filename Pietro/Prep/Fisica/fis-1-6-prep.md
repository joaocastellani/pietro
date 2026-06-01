<!-- fis-1-6-prep.md — gerado automaticamente pelo Prompt de Preparação -->

---

## SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Tipos de movimento | `DIAGRAMA: tipos_movimento` | Ao apresentar progressivo/retrógrado, acelerado/retardado, MU e MUV (Seção 2) |
| Funções horárias | `DIAGRAMA: funcoes_horarias` | Ao trabalhar as fórmulas de MU e MUV (Seção 4) |

### Tabelas markdown (Seção 6):
- Tabela comparativa MU × MUV (Seção 6)
- Tabela de grandezas do capítulo (Seção 5)
- Tabela-catálogo das questões (Seção 11)

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.

---

## SEÇÃO 1 — PERFIL DO CAPÍTULO

# PREPARAÇÃO DE AULA — FÍSICA
- **Unidade:** 1
- **Capítulo:** 6
- **Tema:** Movimentos
- **Perfil:** misto (descritivo-científico + matemático-operacional)
- **Fórmulas principais:** a = Δv/Δt · s = s₀ + v·t · v = v₀ + a·t · s = s₀ + v₀·t + ½·a·t²
- **Cientistas citados:** Galileu Galilei (1564–1642) — contexto histórico da queda livre (Q-10)

---

## SEÇÃO 2 — MAPA DE CONCEITOS

### Classificação dos Movimentos

Um movimento pode ser classificado em dois eixos independentes:

**Eixo 1 — sentido em relação à orientação positiva da trajetória:**
- **Progressivo**: corpo se desloca no mesmo sentido da orientação positiva → v > 0
- **Retrógrado**: corpo se desloca no sentido contrário → v < 0

**Eixo 2 — variação do módulo da velocidade:**
- **Uniforme**: velocidade constante, aceleração nula (a = 0)
- **Variado**: velocidade muda com o tempo (a ≠ 0)
  - **Acelerado**: |v| aumenta — a e v têm o mesmo sentido
  - **Retardado**: |v| diminui — a e v têm sentidos opostos

Os dois eixos são independentes: um movimento pode ser, por exemplo, retrógrado retardado ou progressivo acelerado.

---

### Movimento Uniforme (MU)

Características:
- Velocidade escalar constante (a = 0)
- Distâncias iguais em intervalos de tempo iguais
- Gráfico s × t: **reta inclinada** (inclinação = v; intercepto = s₀)
- Gráfico v × t: **reta horizontal**

**Função horária da posição:**

> **s = s₀ + v · t**

- s₀: posição inicial · v: velocidade escalar (constante) · t: instante
- Inclinação positiva → progressivo; negativa → retrógrado; horizontal → repouso

---

### Aceleração

Quando a velocidade varia, o corpo possui aceleração:

> **a = Δv / Δt = (v − v₀) / (t − t₀)**

- a: m/s² · Δv: variação de velocidade (m/s) · Δt: intervalo de tempo (s)
- a > 0 com v > 0 → acelerado progressivo
- a < 0 com v > 0 → retardado progressivo

Exemplo do livro (peixe — MUV):
- t=0→1s: Δs₁=4m → v₁=4 m/s · t=1→2s: Δs₂=8m → v₂=8 m/s · t=2→3s: Δs₃=12m → v₃=12 m/s
- a = (4−0)/1 = (8−4)/1 = (12−8)/1 = **4 m/s² (constante)** → confirma MUV

---

### Movimento Uniformemente Variado (MUV)

Características:
- Aceleração escalar constante e diferente de zero
- A mesma variação Δv ocorre a cada intervalo Δt igual
- Aceleração média = aceleração instantânea
- Gráfico v × t: **reta inclinada** · Gráfico s × t: **parábola**
- Quando em trajetória reta → **MRUV** (Movimento Retilíneo Uniformemente Variado)

**Função horária da velocidade:**

> **v = v₀ + a · t**

Exemplo (avião): v = 50 + 10·t → v₀ = 50 m/s · a = 10 m/s²; em t = 7 s → v = 120 m/s

**Função horária da posição:**

> **s = s₀ + v₀ · t + ½ · a · t²**

Conexão com matemática: é uma função do 2º grau — s₀ é o termo independente, v₀ é o coeficiente linear, ½·a é o coeficiente quadrático.

Exemplo (caminhão): s₀=50m · v₀=10 m/s · a=4 m/s²
- Função: s = 50 + 10t + 2t²
- Em t=4s: s = 50+40+32 = **122 m**
- Em t=10s: s = 350 m → espaço percorrido = 350−50 = **300 m** (s₀ ≠ 0!)

---

### Ponto Médio

- **Ponto médio de espaço**: s_m = (s₀ + s_f) / 2
- **Ponto médio de tempo**: t_m = (t₀ + t_f) / 2 — a velocidade instantânea nesse instante é igual à velocidade média do percurso

---

### Encontro de Móveis

Dois móveis se encontram quando ocupam a mesma posição no mesmo instante:

> **s₁(t) = s₂(t)**

1. Escrever funções horárias de cada móvel
2. Igualar e resolver para t
3. Substituir t para obter s do encontro

---

### Queda Livre

- Corpo cai sob ação exclusiva da gravidade (despreza-se resistência do ar)
- É um MRUV com a = g ≈ 10 m/s² (para baixo) e v₀ = 0
- Fórmulas: v = g·t e s = ½·g·t²
- Contexto: observação de Galileu Galilei — todos os corpos caem com a mesma aceleração independente de tamanho ou peso

---

## SEÇÃO 4 — FÓRMULAS, LEIS E PRINCÍPIOS

### Aceleração Escalar Média

| Campo | Valor |
|-------|-------|
| Expressão | a = Δv/Δt = (v − v₀) / (t − t₀) |
| a | aceleração · m/s² · grandeza vetorial |
| v | velocidade final · m/s |
| v₀ | velocidade inicial · m/s |
| Δt | intervalo de tempo · s · sempre positivo |
| Observação | a > 0 e v > 0 → acelerado; a < 0 e v > 0 → retardado |

---

### Função Horária da Posição — MU

| Campo | Valor |
|-------|-------|
| Expressão | s = s₀ + v · t |
| s | posição no instante t · m |
| s₀ | posição inicial · m |
| v | velocidade escalar constante · m/s |
| t | instante · s |
| Gráfico | s × t: reta; inclinação = v; intercepto vertical = s₀ |
| Identificar | dado s = A + B·t → s₀ = A e v = B |

---

### Função Horária da Velocidade — MUV

| Campo | Valor |
|-------|-------|
| Expressão | v = v₀ + a · t |
| v | velocidade no instante t · m/s |
| v₀ | velocidade inicial · m/s |
| a | aceleração constante · m/s² |
| t | instante · s |
| Gráfico | v × t: reta; inclinação = a; intercepto = v₀ |
| Identificar | dado v = A + B·t → v₀ = A e a = B |

---

### Função Horária da Posição — MUV

| Campo | Valor |
|-------|-------|
| Expressão | s = s₀ + v₀ · t + ½ · a · t² |
| s | posição no instante t · m |
| s₀ | posição inicial · m |
| v₀ | velocidade inicial · m/s |
| a | aceleração constante · m/s² |
| t | instante · s |
| Gráfico | s × t: parábola (côncava para cima se a > 0; para baixo se a < 0) |
| Conexão mat. | função do 2º grau: f(x) = ax² + bx + c |

---

## SEÇÃO 5 — GRANDEZAS E SISTEMA INTERNACIONAL

| Grandeza | Símbolo | Unidade SI | Símbolo SI | Tipo |
|----------|---------|-----------|------------|------|
| Posição | s | metro | m | escalar |
| Deslocamento | Δs | metro | m | vetorial |
| Velocidade escalar | v | metro por segundo | m/s | escalar (módulo) |
| Aceleração | a | metro por segundo ao quadrado | m/s² | vetorial |
| Tempo | t | segundo | s | escalar |
| Intervalo de tempo | Δt | segundo | s | escalar |

### Conversões frequentes neste capítulo

| De | Para | Operação | Exemplo do livro |
|----|------|----------|-----------------|
| km/h | m/s | ÷ 3,6 | 10,8 km/h = 3 m/s (Q-3) |
| km/h | m/s | ÷ 3,6 | 72 km/h = 20 m/s (Q-10) |
| km/h | m/s | ÷ 3,6 | 252 km/h = 70 m/s (Q-4) |
| min | s | × 60 | 2 min = 120 s |

---

## SEÇÃO 6 — TABELAS DE DADOS

### Comparativo: MU × MUV

| Característica | MU | MUV |
|---------------|-----|-----|
| Aceleração (a) | Zero (a = 0) | Constante ≠ 0 |
| Velocidade (v) | Constante | Varia |
| Δs em Δt iguais | Constante | Varia |
| Gráfico s × t | Reta inclinada | Parábola |
| Gráfico v × t | Reta horizontal | Reta inclinada |
| Função da posição | s = s₀ + v·t | s = s₀ + v₀·t + ½·a·t² |
| Função da velocidade | v = constante | v = v₀ + a·t |
| Quando usar | Δs constante entre medidas | Δs crescente ou decrescente |

---

### Questões de concurso — dados-chave

| Questão | Banca/Ano | Dados principais | Resposta |
|---------|-----------|-----------------|---------|
| Q-1 | IFCMCSP 2024 | Esteira 45 m · v_esteira=0,80 m/s · v_pessoa/esteira=1,0 m/s | d) 25 s |
| Q-2 | Fuvest | v_EM=3,0×10⁵ km/s · d=3,24×10⁸ km | 18 min |
| Q-3a | Unicamp-SP | 8×(1 km correr + 2 min caminhar a 7,2 km/h) | 9,92 km |
| Q-3b | Unicamp-SP | v₀=0 · v=10,8 km/h=3 m/s · Δs=3 m | a=1,5 m/s² |
| Q-4 | — | v₀=0 · v=252 km/h=70 m/s · t=3 s | ≈23,3 m/s² |
| Q-8 | UCS-RS | Δs=2 m · t=4 s · v₀_relativa=0 | a) 0,25 m/s² |
| Q-10 | Ufam | v=72 km/h=20 m/s · g=10 m/s² · v₀=0 | a) 20 m; 2 s |

---

## SEÇÃO 7 — DICAS DE OURO

**Dica 1 — Identificar MU ou MUV pelo enunciado antes de escolher a fórmula**
Se o enunciado diz "velocidade constante" ou "a = 0" → MU → s = s₀ + v·t. Se diz "aceleração constante", "parte do repouso e acelera", "desacelera até parar" → MUV → v = v₀ + a·t e/ou s = s₀ + v₀·t + ½·a·t².

**Dica 2 — Converter km/h para m/s antes de substituir nas fórmulas**
As fórmulas do capítulo operam em m/s e m. 10,8 km/h = 3 m/s · 72 km/h = 20 m/s · 252 km/h = 70 m/s. Fazer a conversão primeiro evita cascata de erros.

**Dica 3 — Sinal negativo em v indica sentido, não "lentidão"**
v = −2 m/s significa que o corpo se move no sentido negativo (retrógrado) com rapidez 2 m/s. Q-6 (garota): s₀=50 m, v=−2 m/s → função s = 50 − 2t, movimento retrógrado.

**Dica 4 — Deslocamento ≠ posição final**
Q-7 item b): s(3) = 152 m é a **posição** no instante 3 s. O deslocamento é s(3) − s₀ = 152 − 2 = 150 m. Questões de V/F exploram exatamente essa confusão.

**Dica 5 — Ler a função horária como equação do 1º ou 2º grau**
v = 9 − 3t → v₀ = 9 m/s, a = −3 m/s². s = 2 + 50t → MRU, s₀ = 2 m, v = 50 m/s. Identificar os coeficientes diretamente é mais rápido que montar o sistema.

**Dica 6 — Queda livre é MUV com g = 10 m/s²**
Aplique as mesmas fórmulas: v = g·t e s = ½·g·t² (com v₀ = 0). Q-9 e Q-10 testam exatamente isso. Se a velocidade final vier em km/h, converta para m/s antes.

**Dica 7 — Espaço percorrido ≠ posição quando s₀ ≠ 0**
Exemplo do caminhão (pág. 114): em t=10s, posição = 350 m, mas espaço percorrido = 350 − 50 = 300 m. Sempre subtrair s₀ quando a posição inicial não é zero.

---

## SEÇÃO 8 — ALERTAS E PEGADINHAS

**ALERTA 1 — Retrógrado não significa "mais lento"**
Movimento retrógrado é definido pelo sentido, não pela velocidade. Um corpo pode ser rápido e retrógrado simultaneamente. Sempre verificar o sinal de v, não o módulo.

**ALERTA 2 — a < 0 não implica obrigatoriamente "retardado"**
A classificação acelerado/retardado depende de |v| crescer ou decrescer, não do sinal de a isolado. Se a = −3 m/s² e o movimento é retrógrado (v₀ < 0), o corpo pode estar acelerando (em módulo). Verificar sempre o sentido relativo de a e v.

**ALERTA 3 — Q-7b: confundir posição com deslocamento**
s(3) = 152 m é posição (onde o corpo está), não deslocamento (quanto andou). Como s₀ = 2 m ≠ 0, o deslocamento é 152 − 2 = 150 m. O item afirma "deslocou 152 m" → FALSO.

**ALERTA 4 — Q-8 (UCS-RS): o referencial é relativo entre as duas pessoas**
No início, ambas têm a mesma velocidade → velocidade relativa entre elas = 0. A moça precisa percorrer Δs = 2 m em relação à outra em t = 4 s partindo do repouso relativo. Usar s = ½·a·t², não s = v₀·t + ½·a·t² com a velocidade absoluta.

**ALERTA 5 — Q-1 (esteira): velocidade relativa ao chão = soma das velocidades**
A pessoa anda a 1,0 m/s *em relação à esteira*, que por sua vez move-se a 0,80 m/s em relação ao chão. Velocidade em relação ao chão = 1,0 + 0,80 = 1,80 m/s. Usar apenas 1,0 ou apenas 0,80 são erros típicos.

**ALERTA 6 — Tabela de posições: verificar se Δs é constante antes de classificar**
Para identificar MU ou MUV numa tabela: calcular Δs em intervalos Δt iguais. Se Δs constante → MU. Se Δs crescente → MUV acelerado. Se Δs decrescente → MUV retardado. Não classificar "na intuição" sem calcular.

---

## SEÇÃO 9 — SÍNTESE COM LACUNAS

### Bloco 1 — Classificação

1. Movimento no mesmo sentido da orientação positiva: `______`. *(progressivo)*
2. Movimento no sentido contrário: `______`. *(retrógrado)*
3. No progressivo, v é `______` (positivo/negativo). *(positivo)*
4. Movimento em que a velocidade não varia: `______`. *(uniforme — MU)*
5. Movimento em que a aceleração é constante e ≠ 0: `______`. *(uniformemente variado — MUV)*
6. No MUV, a `______` varia e a `______` é constante. *(velocidade / aceleração)*
7. |v| crescente → `______`; |v| decrescente → `______`. *(acelerado / retardado)*
8. MUV em trajetória reta: `______`. *(MRUV)*

### Bloco 2 — Fórmulas

9. Fórmula da aceleração: `______`. *(a = Δv/Δt = (v − v₀)/(t − t₀))*
10. Função horária da posição no MU: `______`. *(s = s₀ + v·t)*
11. Função horária da velocidade no MUV: `______`. *(v = v₀ + a·t)*
12. Função horária da posição no MUV: `______`. *(s = s₀ + v₀·t + ½·a·t²)*
13. Gráfico s × t no MU: `______`. No MUV: `______`. *(reta / parábola)*
14. Encontro de móveis: condição `______`. *(s₁(t) = s₂(t))*
15. Queda livre é `______` com a = `______`. *(MRUV / g ≈ 10 m/s²)*

### Bloco 3 — Tabela síntese

| Conceito | Lacuna | Resposta |
|----------|--------|---------|
| MU | a = `___` | 0 |
| MUV | a = `___` | constante ≠ 0 |
| MU | Δs em Δt iguais é `___` | constante |
| MUV | Δs em Δt iguais `___` | varia |
| Gráfico v×t — MU | `___` | reta horizontal |
| Gráfico v×t — MUV | `___` | reta inclinada |
| Gráfico s×t — MUV | `___` | parábola |
| s = s₀ + v·t | válida para `___` | MU |
| v = v₀ + a·t | válida para `___` | MUV |
| Queda livre | a = `___ m/s²` | 10 (ou g) |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

Imagem disponível: `Pietro/Raw/Fisica/fis-1-6-sintese.png` (pág. 122)

O diagrama de síntese do livro mostra:
- Raiz: **Tipos de movimento** (4 ramos)
- **Progressivo**: mesmo sentido da orientação positiva
- **Retrógrado**: sentido oposto
- **Acelerado**: aumenta a velocidade no decorrer do tempo
- **Retardado**: diminui a velocidade no decorrer do tempo
- **Movimento Uniforme (MU)**: corpo percorre distâncias iguais em Δt iguais; velocidade constante; s = s₀ + v·t
- **Aceleração**: a = Δv/Δt
- **Movimento variado**: velocidade muda com o tempo
- **Movimento Uniformemente Variado (MUV)**: mesma variação Δv a cada Δt igual; v = v₀ + a·t e s = s₀ + v₀·t + ½·a·t²

Lacunas do diagrama (para Pietro preencher):
- Ramo esquerdo sem nome → mesmo sentido da orientação positiva: `______` *(progressivo)*
- Terceiro ramo → aumenta a velocidade: `______` *(acelerado)*
- Três grandezas constantes no MU: `______`, `______`, `______` *(Δt / v / a = 0)*
- Duas grandezas constantes no MUV: `______` e `______` *(Δt / a)*

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo

| # | Enunciado resumido | Tipo | Dif. | Gabarito | Fonte |
|---|---|---|---|---|---|
| Q-1 | Esteira 45 m · v_rel=1,0 m/s · v_esteira=0,80 m/s → tempo | MC | médio | d) 25 s | IFCMCSP 2024 |
| Q-2 | Sonda em Marte · ondas EM 3,0×10⁵ km/s · d=3,24×10⁸ km → Δt | Cálculo | médio | 18 min | Fuvest |
| Q-3a | Maratona 8 sequências (1 km + 2 min caminhar) → distância total | Cálculo | difícil | 9,92 km | Unicamp-SP |
| Q-3b | v₀=0 · v=10,8 km/h · Δs=3 m → aceleração | Cálculo | difícil | 1,5 m/s² | Unicamp-SP |
| Q-4 | Foguete · v₀=0 · v=252 km/h · t=3 s → aceleração | Cálculo | médio | ≈23,3 m/s² | — |
| Q-5 | 3 situações com v e a → identificar MU/acelerado/retardado | Identif. | médio | II→MU · I→acel. · III→retard. | — |
| Q-6 | Garota s₀=50m v=−2m/s → função horária, sentido, tempo para 20 m | Dis./Cálc. | médio | s=50−2t · retrógrado · t=10s | — |
| Q-7 | MRU s=2+50t → 4 assertivas V/F | V/F | médio | V·F·V·V | — |
| Q-8 | Moça acelera 2 m à frente em 4 s (ref. relativa, v₀=0) | MC | difícil | a) 0,25 m/s² | UCS-RS |
| Q-9 | Queda livre — tipo de movimento e justificativa | Dis. | médio | MRUV acelerado, a = g | — |
| Q-10 | Galileu · martelo · v=72 km/h · g=10 m/s² → altura e tempo | MC | difícil | a) 20 m; 2 s | Ufam |

---

### Análise detalhada — Q-1 (IFCMCSP 2024)

v_esteira = 0,80 m/s (relação ao chão) · v_pessoa/esteira = 1,0 m/s (mesmo sentido)
v_pessoa/chão = 0,80 + 1,0 = **1,80 m/s**
t = Δs / v = 45 / 1,80 = **25 s** → alternativa **d)**

---

### Análise detalhada — Q-2 (Fuvest)

v = 3,0 × 10⁵ km/s · d = 3,24 × 10⁸ km
Δt = d / v = 3,24 × 10⁸ / 3,0 × 10⁵ = 1 080 s ÷ 60 = **18 min**

---

### Análise detalhada — Q-3 (Unicamp-SP)

**a)** v_caminhada = 7,2 km/h · t_caminhada = 2 min = 1/30 h
d_caminhada = 7,2 × (1/30) = 0,24 km por sequência
d_total = 8 × (1 + 0,24) = 8 × 1,24 = **9,92 km**

**b)** v = 10,8 km/h ÷ 3,6 = 3 m/s · v₀ = 0 · Δs = 3 m
v² = v₀² + 2·a·Δs → 9 = 0 + 2·a·3 = 6a → **a = 1,5 m/s²**

---

### Análise detalhada — Q-6

s₀ = 50 m · v = −2 m/s (sentido contrário ao positivo)
**a)** s = 50 + (−2)·t = **50 − 2t**
**b)** v < 0 → movimento **retrógrado**
**c)** Δs = 20 m → t = 20 / |v| = 20 / 2 = **10 s**

---

### Análise detalhada — Q-7

s = 2 + 50·t → s₀ = 2 m · v = 50 m/s
- a) **V** — v = 50 m/s (coeficiente de t) ✓
- b) **F** — s(3) = 2 + 150 = 152 m é a posição; deslocamento = 152 − 2 = **150 m** ≠ 152 m
- c) **V** — s₀ = 2 m (termo independente) ✓
- d) **V** — 102 = 2 + 50t → t = 2 s ✓

---

### Análise detalhada — Q-8 (UCS-RS)

Referencial relativo (moça em relação à desconhecida): v₀_rel = 0 · Δs = 2 m · t = 4 s
s = ½·a·t² → 2 = ½·a·16 = 8a → **a = 0,25 m/s²** → alternativa **a)**

---

### Análise detalhada — Q-10 (Ufam)

v = 72 km/h ÷ 3,6 = 20 m/s · v₀ = 0 · g = 10 m/s²
v = g·t → t = 20 / 10 = **2 s**
s = ½·g·t² = ½ · 10 · 4 = **20 m** → alternativa **a)**

---

### Bloco B — Questões modelo originais

**QM-1** · múltipla escolha · fácil · inspirada em Q-7

Um móvel em MRU segue a função horária s = 10 + 30·t (SI). Qual afirmativa está CORRETA?

a) A velocidade do móvel é 10 m/s.
b) Em t = 4 s, o móvel está na posição 130 m.
c) O deslocamento em 4 s é 130 m.
d) O móvel estava na posição 70 m no instante t = 1 s.

✅ **Gabarito:** b)
📝 **Resolução:** s(4) = 10 + 120 = 130 m ✓ · a) v = 30 m/s, não 10 · c) Δs = 130 − 10 = 120 m · d) s(1) = 10 + 30 = 40 m ≠ 70 m
⚠️ Professor: referência de estilo — crie variações originais, nunca reproduza diretamente.

---

**QM-2** · cálculo · médio · inspirada em Q-4

Um ciclista parte do repouso e, em 8 segundos, atinge a velocidade de 72 km/h. Qual é sua aceleração média?

✅ **Gabarito:** 2,5 m/s²
📝 **Resolução:** v = 72 km/h ÷ 3,6 = 20 m/s · v₀ = 0 · a = Δv/Δt = 20/8 = **2,5 m/s²**
⚠️ Professor: referência de estilo — crie variações originais, nunca reproduza diretamente.

---

**QM-3** · múltipla escolha · difícil · inspirada em Q-8 (UCS-RS)

Dois patinadores percorrem uma pista lado a lado com a mesma velocidade. Um deles acelera uniformemente a partir desse instante. Após 5 segundos, está 10 metros à frente do outro. Qual é a aceleração do patinador que acelerou?

a) 0,4 m/s²
b) 0,8 m/s²
c) 1,0 m/s²
d) 2,0 m/s²

✅ **Gabarito:** b) 0,8 m/s²
📝 **Resolução:** Referencial relativo ao segundo patinador: v₀_rel = 0 · Δs = 10 m · t = 5 s · s = ½·a·t² → 10 = ½·a·25 = 12,5a → a = 0,8 m/s²
⚠️ Professor: referência de estilo — crie variações originais, nunca reproduza diretamente.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: tipos_movimento
Classificação dos tipos de movimento, MU e MUV com funções horárias.

```svg
<svg width="100%" viewBox="0 0 680 370" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr1" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Raiz -->
<rect x="230" y="16" width="220" height="44" rx="8" class="c-purple"/>
<text x="340" y="38" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Tipos de Movimento</text>

<!-- Flechas nível 2 -->
<line x1="280" y1="60" x2="120" y2="100" stroke="var(--c-gray-border)" stroke-width="1.5" marker-end="url(#arr1)"/>
<line x1="320" y1="60" x2="260" y2="100" stroke="var(--c-gray-border)" stroke-width="1.5" marker-end="url(#arr1)"/>
<line x1="370" y1="60" x2="440" y2="100" stroke="var(--c-gray-border)" stroke-width="1.5" marker-end="url(#arr1)"/>
<line x1="410" y1="60" x2="580" y2="100" stroke="var(--c-gray-border)" stroke-width="1.5" marker-end="url(#arr1)"/>

<!-- Progressivo -->
<rect x="20" y="100" width="190" height="52" rx="8" class="c-teal"/>
<text x="115" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Progressivo</text>
<text x="115" y="140" class="ts" text-anchor="middle" fill="var(--on-accent)">v &gt; 0  mesmo sentido +</text>

<!-- Retrogrado -->
<rect x="180" y="100" width="160" height="52" rx="8" class="c-coral"/>
<text x="260" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Retrogrado</text>
<text x="260" y="140" class="ts" text-anchor="middle" fill="var(--on-accent)">v &lt; 0  sentido oposto</text>

<!-- Acelerado -->
<rect x="360" y="100" width="160" height="52" rx="8" class="c-amber"/>
<text x="440" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Acelerado</text>
<text x="440" y="140" class="ts" text-anchor="middle" fill="var(--on-accent)">|v| cresce com o tempo</text>

<!-- Retardado -->
<rect x="500" y="100" width="160" height="52" rx="8" class="c-amber"/>
<text x="580" y="120" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Retardado</text>
<text x="580" y="140" class="ts" text-anchor="middle" fill="var(--on-accent)">|v| decresce com o tempo</text>

<!-- Separador -->
<line x1="40" y1="184" x2="640" y2="184" stroke="var(--c-gray-border)" stroke-width="1" stroke-dasharray="5 4"/>

<!-- Flecha MU -->
<line x1="180" y1="184" x2="180" y2="210" stroke="var(--c-gray-border)" stroke-width="1.5" marker-end="url(#arr1)"/>

<!-- MU box -->
<rect x="30" y="210" width="290" height="80" rx="8" class="c-teal"/>
<text x="175" y="232" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Movimento Uniforme (MU)</text>
<text x="175" y="254" class="ts" text-anchor="middle" fill="var(--on-accent)">a = 0  |  v constante</text>
<text x="175" y="274" class="ts" text-anchor="middle" fill="var(--on-accent)">s = s0 + v · t</text>

<!-- Flecha MUV -->
<line x1="500" y1="184" x2="500" y2="210" stroke="var(--c-gray-border)" stroke-width="1.5" marker-end="url(#arr1)"/>

<!-- MUV box -->
<rect x="360" y="210" width="290" height="80" rx="8" class="c-amber"/>
<text x="505" y="232" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Mov. Unif. Variado (MUV)</text>
<text x="505" y="254" class="ts" text-anchor="middle" fill="var(--on-accent)">a = constante ≠ 0</text>
<text x="505" y="274" class="ts" text-anchor="middle" fill="var(--on-accent)">v = v0 + a·t</text>

<!-- Aceleração box -->
<rect x="220" y="316" width="240" height="44" rx="8" class="c-purple"/>
<text x="340" y="334" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Aceleracao</text>
<text x="340" y="350" class="ts" text-anchor="middle" fill="var(--on-accent)">a = Δv / Δt</text>
</svg>
```

---

### DIAGRAMA: funcoes_horarias
Comparativo das funções horárias do MU e do MUV.

```svg
<svg width="100%" viewBox="0 0 680 310" xmlns="http://www.w3.org/2000/svg">
<defs>
  <marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- MU header -->
<rect x="20" y="20" width="290" height="44" rx="8" class="c-teal"/>
<text x="165" y="42" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Movimento Uniforme (MU)</text>

<!-- MU: condicao -->
<rect x="20" y="80" width="290" height="38" rx="6" class="c-gray"/>
<text x="165" y="99" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--fg)">a = 0  |  v = constante  |  Δs = constante</text>

<!-- MU: funcao horaria posicao -->
<rect x="20" y="134" width="290" height="58" rx="8" class="c-teal"/>
<text x="165" y="154" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Funcao horaria da posicao</text>
<text x="165" y="178" class="ts" text-anchor="middle" fill="var(--on-accent)">s = s0 + v · t</text>

<!-- MU: graficos -->
<rect x="20" y="208" width="290" height="38" rx="6" class="c-gray"/>
<text x="165" y="227" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--fg)">s×t: reta  |  v×t: reta horizontal</text>

<!-- MUV header -->
<rect x="370" y="20" width="290" height="44" rx="8" class="c-amber"/>
<text x="515" y="42" class="th" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">Mov. Unif. Variado (MUV)</text>

<!-- MUV: condicao -->
<rect x="370" y="80" width="290" height="38" rx="6" class="c-gray"/>
<text x="515" y="99" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--fg)">a = constante ≠ 0  |  v varia</text>

<!-- MUV: funcao velocidade -->
<rect x="370" y="134" width="290" height="38" rx="8" class="c-amber"/>
<text x="515" y="153" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">v = v0 + a · t</text>

<!-- MUV: funcao posicao -->
<rect x="370" y="188" width="290" height="38" rx="8" class="c-amber"/>
<text x="515" y="207" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">s = s0 + v0·t + (1/2)·a·t²</text>

<!-- MUV: graficos -->
<rect x="370" y="242" width="290" height="38" rx="6" class="c-gray"/>
<text x="515" y="261" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--fg)">v×t: reta inclinada  |  s×t: parabola</text>

<!-- Aceleracao central -->
<rect x="256" y="148" width="168" height="38" rx="8" class="c-purple"/>
<text x="340" y="167" class="ts" text-anchor="middle" dominant-baseline="central" fill="var(--on-accent)">a = Δv / Δt  (m/s²)</text>
<line x1="310" y1="148" x2="310" y2="118" stroke="var(--c-gray-border)" stroke-width="1.5" marker-end="url(#arr2)"/>
<line x1="370" y1="167" x2="370" y2="148" stroke="var(--c-gray-border)" stroke-width="1.5" marker-end="url(#arr2)"/>
</svg>
```
