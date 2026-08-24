## SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

## DIAGRAMAS DISPONÍVEIS — fis-2-2

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| graficos_muv | DIAGRAMA: graficos_muv | Ao comparar os gráficos S×t (parábola) e v×t (reta) do MUV |
| conservacao_energia | DIAGRAMA: conservacao_energia | Ao apresentar o princípio da conservação da energia mecânica |

### Tabelas markdown (Seção 6):
- Tabela 2 — tempo × distância (MUV, a = 2,00 m/s²)
- Tabela 3 — tempo × velocidade (MUV)
- Tabela 4 — conversão graus ↔ radianos
- Tabela 5 — tempo de queda para diferentes distâncias
- Tabela 6 — experimento do pêndulo simples (cálculo de g)

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer.
Tabelas da Seção 6 são apresentadas como markdown no chat.

---

## SEÇÃO 1 — PERFIL DO CAPÍTULO

```
# PREPARAÇÃO DE AULA — FÍSICA
- Unidade: 2
- Capítulo (parte): 2
- Tema: Mecânica — MUV completo, Movimento Circular, Forças (queda livre, pêndulo, atrito), Trabalho e Energia
- Perfil: misto
- Fórmulas principais: S = S₀+v₀t+½at² · acp = v²/R · T = 2π√(l/g) · W = F·cosθ·d · P = W/t · Ec = ½mv² · Epg = mgh · Emec = Ep+Ec
```

📚 **Glossário do Capítulo**

| Termo | Definição |
|-------|-----------|
| Aceleração centrípeta | Aceleração sempre dirigida ao centro da trajetória circular; muda a direção da velocidade, não seu módulo (acp = v²/R). |
| Energia | Capacidade de realizar trabalho; não se cria nem se perde, apenas se transforma. |
| Energia cinética | Energia associada à massa e à velocidade de um corpo (Ec = ½mv²). |
| Energia mecânica | Soma da energia cinética e potencial de um sistema (Emec = Ep + Ec). |
| Energia potencial gravitacional | Energia associada à posição de um corpo em relação a um nível de referência (Epg = mgh). |
| Frequência | Número de vezes que um fenômeno periódico se repete por unidade de tempo (f = 1/T). |
| MCU | Movimento Circular e Uniforme — velocidade tangencial de módulo constante numa trajetória circular. |
| Período | Tempo mínimo para um fenômeno periódico se repetir (T = 1/f). |
| Peso | Força de atração gravitacional sobre um corpo (P = mg); varia conforme o local. |
| Potência | Taxa de realização de trabalho no tempo (P = W/t). |
| Queda livre | Movimento de um corpo sob ação exclusiva da aceleração da gravidade. |
| Radiano | Unidade SI de ângulo — arco de circunferência com comprimento igual ao raio. |
| Trabalho | Energia transferida por uma força ao longo de um deslocamento (W = F·cosθ·d). |
| Velocidade angular | Razão entre o deslocamento angular e o intervalo de tempo (ω = Δα/Δt). |

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

**Completando o MUV.** A Parte 1 introduziu a aceleração e a
velocidade do MUV (v = v₀ + at); esta parte completa a descrição
com a equação de posição: S = S₀ + v₀·t + ½·a·t² — uma função do
2º grau em t. Isso muda a forma dos gráficos: enquanto v(t) e a(t)
continuam sendo retas (funções do 1º grau), o gráfico S×t do MUV é
uma parábola, não mais uma reta como no MRU. A inclinação da reta
v×t corresponde à aceleração constante do movimento.

**Movimento circular.** Quando a trajetória é uma circunferência, é
útil medir o deslocamento em ângulo (radianos) em vez de distância
linear. O radiano é definido de forma elegante: é o ângulo cujo
arco tem comprimento igual ao raio. No Movimento Circular e
Uniforme (MCU), a velocidade tangencial tem módulo constante, mas
sua direção muda a cada instante — e é justamente essa mudança de
direção que exige uma aceleração, a aceleração centrípeta
(acp = v²/R), sempre apontando para o centro da trajetória. Período
e frequência são grandezas inversas (T = 1/f) que descrevem quanto
tempo leva uma volta completa e quantas voltas ocorrem por segundo.

**Forças que atuam sobre os corpos.** A queda livre é um caso
particular de MUV em que a aceleração é a da gravidade
(g ≈ 9,8 m/s²) — Galileu já havia demonstrado que, no vácuo, todos
os corpos caem com a mesma aceleração, independentemente da massa.
O pêndulo simples oferece uma forma experimental elegante de medir
g, a partir do período de oscilação (T = 2π√(l/g)). É importante
não confundir massa (quantidade de matéria, constante em qualquer
lugar) com peso (força gravitacional P = mg, que varia conforme o
local — menor na Lua, por exemplo). Já o atrito é a força que se
opõe ao movimento relativo entre superfícies em contato: às vezes
queremos reduzi-lo (lubrificação), às vezes ele é essencial
(freios, pneus).

**Trabalho e energia.** Trabalho é realizado por uma força quando
há deslocamento na direção dessa força (W = F·cosθ·d) — se a força
for perpendicular ao deslocamento, o trabalho é nulo (por isso
carregar uma mochila nas costas, andando na horizontal, não realiza
trabalho sobre ela, mesmo com esforço muscular envolvido). O
trabalho da força peso tem uma propriedade notável: depende apenas
da altura percorrida, não do caminho (W = mgh, independente da
trajetória). Energia é a capacidade de realizar trabalho, e se
apresenta principalmente como energia cinética (Ec = ½mv²,
associada ao movimento) e energia potencial (associada à posição,
como a Epg = mgh). O princípio da conservação da energia mecânica
amarra tudo isso: na ausência de forças dissipativas, a soma
Ep + Ec permanece constante — um corpo em queda livre troca energia
potencial por cinética ao longo da queda, sem nunca perder o total.

---

## SEÇÃO 4 — FÓRMULAS, LEIS E PRINCÍPIOS

### Equação de posição do MUV

**Expressão:** S = S₀ + v₀·t + ½·a·t²

| Símbolo | Grandeza | Unidade SI | Tipo |
|---------|----------|------------|------|
| S | posição no instante t | m | escalar |
| S₀ | posição inicial | m | escalar |
| v₀ | velocidade inicial | m/s | vetorial |
| a | aceleração (constante) | m/s² | vetorial |
| t | tempo | s | escalar |

💡 **Pegadinha:** o gráfico S×t desta equação é uma parábola — muitos alunos esperam uma reta, como no MRU.

### Velocidade angular e velocidade linear (MCU)

**Expressão:** ω = Δα/Δt = 2π/T = 2πf  ·  v = ω·R

| Símbolo | Grandeza | Unidade SI |
|---------|----------|------------|
| ω | velocidade angular | rad/s |
| T | período | s |
| f | frequência | Hz |
| v | velocidade linear (tangencial) | m/s |
| R | raio da trajetória | m |

### Aceleração centrípeta

**Expressão:** acp = v²/R = ω²R

**Válida quando:** o movimento é circular (uniforme ou não — a
centrípeta descreve só a variação de direção da velocidade).
💡 **Pegadinha:** a aceleração centrípeta NÃO altera o módulo da velocidade, só sua direção.

### Queda livre (a partir do repouso)

**Expressão:** S = ½·g·t²

| Símbolo | Grandeza | Unidade SI |
|---------|----------|------------|
| S | altura de queda | m |
| g | aceleração da gravidade | m/s² (≈ 9,8 ao nível do mar) |
| t | tempo de queda | s |

**Caso especial:** caso particular do MUV, com v₀ = 0 e S₀ = 0.

### Período do pêndulo simples

**Expressão:** T = 2π√(l/g)  ⟺  g = 4π²l/T²

| Símbolo | Grandeza | Unidade SI |
|---------|----------|------------|
| T | período de oscilação | s |
| l | comprimento do fio | m |
| g | aceleração da gravidade | m/s² |

### Peso

**Expressão:** P = m·g
💡 **Pegadinha:** massa não muda de local para local; peso sim, porque depende de g.

### Trabalho de uma força

**Expressão:** W = F·d (força paralela)  ·  W = F·cosθ·d (força em ângulo θ)

| Símbolo | Grandeza | Unidade SI |
|---------|----------|------------|
| W | trabalho | J (joule) |
| F | intensidade da força | N |
| d | módulo do deslocamento | m |
| θ | ângulo entre a força e o deslocamento | — |

**Caso especial:** θ = 90° → W = 0.

### Trabalho da força peso

**Expressão:** W = P·h = m·g·h

**Válida quando:** sempre, independente da trajetória — h é o deslocamento vertical.

### Potência

**Expressão:** P = W/t = F·v

| Símbolo | Grandeza | Unidade SI |
|---------|----------|------------|
| P | potência | W (watt) |
| W | trabalho | J |
| t | tempo | s |
| v | velocidade | m/s |

### Energia cinética

**Expressão:** Ec = ½·m·v²

### Teorema da energia cinética

**Expressão:** W = ΔEc = EcB − EcA

### Energia potencial gravitacional

**Expressão:** Epg = P·h = m·g·h

### Conservação da energia mecânica

**Expressão:** Emec = Ep + Ec (constante, na ausência de forças dissipativas)

---

## SEÇÃO 5 — GRANDEZAS E SISTEMA INTERNACIONAL

#### 5.1 — Grandezas do capítulo

| Grandeza | Símbolo | Unidade SI | Tipo (escalar/vetorial) |
|----------|---------|------------|--------------------------|
| Ângulo | α | radiano (rad) | escalar |
| Período | T | segundo (s) | escalar |
| Frequência | f | hertz (Hz) | escalar |
| Velocidade angular | ω | rad/s | vetorial |
| Aceleração centrípeta | acp | m/s² | vetorial |
| Peso | P | newton (N) | vetorial |
| Trabalho | W | joule (J) | escalar |
| Potência | P | watt (W) | escalar |
| Energia | Ec, Ep | joule (J) | escalar |

#### 5.2 — Conversões importantes

```
Ângulo: graus → radianos
Fator: 360° = 2π rad
Exemplo: 90° = π/2 rad (Tabela 4 do material)
⚠️ Pegadinha: usar graus diretamente numa fórmula que exige radianos (ex.: ω = Δα/Δt)
```

```
Potência: watt e seus múltiplos/unidades especiais
Fator: 1 kW = 1000 W · 1 CV = 735 W · 1 HP = 746 W · 1 kWh = 3,6×10⁶ J
Exemplo: motor de 1 CV ≈ 735 W
⚠️ Pegadinha: confundir CV (cavalo-vapor, métrico) com HP (horse-power, imperial) — não são numericamente iguais
```

---

## SEÇÃO 6 — DADOS FACTUAIS DENSOS

**Tabela 2 — tempo × distância (MUV, corpo partindo do repouso, a = 2,00 m/s²):**

| Tempo (s) | Distância (m) |
|-----------|----------------|
| 0,00 | 0,00 |
| 1,00 | 1,00 |
| 2,00 | 4,00 |
| 3,00 | 9,00 |
| 4,00 | 16,00 |
| 5,00 | 25,00 |

**Tabela 3 — tempo × velocidade (MUV):**

| Tempo (s) | Velocidade (m/s) |
|-----------|-------------------|
| 0,00 | 0,00 |
| 1,00 | 2,00 |
| 2,00 | 4,00 |
| 3,00 | 6,00 |
| 4,00 | 8,00 |
| 5,00 | 10,0 |

**Tabela 4 — conversão de graus em radianos:**

| Graus | Radianos |
|-------|----------|
| 360° | 2π rad |
| 180° | π rad |
| 90° | π/2 rad |
| 60° | π/3 rad |
| 45° | π/4 rad |
| 30° | π/6 rad |

**Tabela 5 — tempo de queda para diferentes distâncias (g = 9,8 m/s²):**

| Distância (m) | Velocidade (m/s) | Tempo (s) |
|----------------|-------------------|-----------|
| 2,00 | 6,36 | 0,64 |
| 3,00 | 7,67 | 0,78 |
| 6,00 | 10,8 | 1,1 |
| 10,0 | 14,0 | 1,4 |

**Tabela 6 — experimento do pêndulo simples (cálculo de g):**

| Experimento | l (m) | T (s) | g (m/s²) |
|-------------|-------|-------|----------|
| 1 | 0,57 | 1,51 | 9,77 |
| 2 | 0,49 | 1,38 | 10,16 |
| 3 | 0,36 | 1,21 | 9,61 |
| 4 | 0,72 | 1,71 | 9,76 |
| 5 | 1,14 | 2,15 | 9,69 |
| **Média** | — | — | **9,79** |

⚠️ Pegadinha: a medida 2 (g=10,16) se afasta mais do valor teórico
(9,8) que as demais — bom exemplo de erro experimental para discutir
precisão de medidas com fio curto (menor l amplifica erro relativo
de medição do tempo).

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — S×t do MUV é parábola, não reta**
Só o MRU tem gráfico S×t linear. No MUV, por causa do termo ½at²,
a posição cresce (ou decresce) como uma parábola.

💡 **Dica 2 — Aceleração centrípeta muda direção, não módulo**
Num MCU, a velocidade tem módulo constante, mas está sempre
mudando de direção — e é essa mudança de direção que a aceleração
centrípeta descreve. Não pense nela como algo que "acelera ou freia"
o corpo no sentido do movimento.

💡 **Dica 3 — Massa não é peso**
Massa é propriedade do corpo (kg, igual em qualquer lugar); peso é
uma força (N, P = mg) que depende da gravidade local. Na Lua, a
massa de um objeto não muda, mas seu peso cai bastante.

💡 **Dica 4 — Força perpendicular ao deslocamento não trabalha**
Sempre que θ = 90° entre a força e o deslocamento, W = 0 — mesmo
que a força seja grande e o deslocamento também.

💡 **Dica 5 — Trabalho do peso só depende da altura**
W = mgh vale para QUALQUER trajetória entre os pontos inicial e
final — reta, curva, sinuosa — desde que a variação de altura h
seja a mesma.

💡 **Dica 6 — Energia mecânica se conserva, mas troca de forma**
Em queda livre sem resistência do ar, a energia potencial que o
corpo perde é exatamente a energia cinética que ele ganha — a soma
Ep + Ec não muda.

---

## SEÇÃO 8 — ALERTAS DE INCONSISTÊNCIA

⚠️ ALERTA — Desenvolvimento do exemplo de força de frenagem (energia cinética)
- Dado no material: a equação é apresentada como
  "F × 8m = ½ × 800kg × (10m/s)² = 5000", seguida da conclusão
  "F = 5000 N".
- Problema: ½ × 800 × (10)² = 40.000 J, não 5.000 — a forma como a
  equação está impressa no material salta a etapa de divisão por
  8 m, fazendo parecer que o produto ½×800×10² já vale 5.000
  diretamente, o que é matematicamente incorreto.
- Dado correto: ΔEc = ½ × 800 kg × (10 m/s)² = 40.000 J.
  F = ΔEc / d = 40.000 J / 8 m = 5.000 N. O resultado final
  (F = 5000 N) está certo — só a equação intermediária impressa no
  material está com um erro de formatação/digitação.
- Impacto na aula: ao apresentar este exemplo (Etapa 1 ou
  Progressivo), mostrar o desenvolvimento completo e correto
  (40.000 J antes de dividir pelos 8 m), sem repetir a equação como
  aparece no material, para não confundir a aluna.

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

- **Movimento Circular e Uniforme (MCU)**
  - Definição: `______` (trajetória circular com velocidade tangencial de módulo constante)
  - Exemplo: `______` (roda gigante, Terra em órbita quase circular)

- **Queda livre**
  - Definição: `______` (movimento sob ação exclusiva da aceleração da gravidade)
  - Exemplo: `______` (S = ½gt², g ≈ 9,8 m/s²)

- **Energia potencial gravitacional**
  - Definição: `______` (energia associada à posição/altura de um corpo, Epg = mgh)
  - Exemplo: `______` (água represada numa hidrelétrica)

#### Bloco 2 — Fórmulas

- **Equação de posição do MUV**
  - Expressão: `______` (S = S₀ + v₀t + ½at²)
  - a representa: `______` (aceleração, em m/s²)

- **Energia cinética**
  - Expressão: `______` (Ec = ½mv²)
  - v representa: `______` (velocidade, em m/s)

#### Bloco 3 — Lacunas para Warm-Up

1. A equação de posição do MUV é S = `______`
   *(resposta: S₀ + v₀t + ½at²)*
2. O gráfico S×t do MUV tem forma de: `______`
   *(resposta: parábola)*
3. A fórmula da aceleração centrípeta é acp = `______`
   *(resposta: v²/R (ou ω²R))*
4. A relação entre frequência e período é f = `______`
   *(resposta: 1/T)*
5. Segundo Galileu, no vácuo todos os corpos caem com a mesma `______`, independente da massa
   *(resposta: aceleração (g))*
6. A fórmula do período do pêndulo simples é T = `______`
   *(resposta: 2π√(l/g))*
7. A fórmula da energia cinética é Ec = `______`
   *(resposta: ½mv²)*
8. Na ausência de forças dissipativas, a energia mecânica total permanece: `______`
   *(resposta: constante)*

#### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Equação de posição do MUV | `______` → *S = S₀ + v₀t + ½at²* |
| Gráfico S×t do MUV | `______` → *parábola* |
| Aceleração centrípeta | `______` → *acp = v²/R* |
| Trabalho da força peso | `______` → *W = mgh, independe da trajetória* |
| Energia cinética | `______` → *Ec = ½mv²* |
| Conservação da energia mecânica | `______` → *Emec = Ep + Ec = constante* |
| Pegadinha: força perpendicular ao deslocamento | `______` → *trabalho = zero* |

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

**Fontes:** "Exercícios Propostos" do `fis-2-2.md` (associados à
fórmula v = v₀ + at, introduzida ao final da Parte 1).

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito | Obs. |
|---|---|---|---|---|---|---|
| Q-1 | Aeroplano desacelera de 250 a 200 m/s em 10,0s — aceleração? | Cálculo | F | AT | 5,00 m/s² | — |
| Q-2 | Carro a 18,0m/s acelera 0,25m/s² por 20s — velocidade final? | Cálculo | F | AT | 23 m/s | — |
| Q-3 | Carro a 16m/s freia em 8,0s — aceleração e distância? | Cálculo | M | AT | (a) −2,0 m/s²; (b) 64 m | — |

#### Bloco B — Questões modelo originais

**QM-1** · múltipla escolha · médio

Uma ave de rapina de 1,2 kg mergulha em direção à presa atingindo
15 m/s no momento do ataque. Qual é sua energia cinética nesse
instante?

a) 9,0 J   b) 18 J   c) 90 J   d) 135 J

✅ Gabarito: d
📝 Resolução: Ec = ½·m·v² = ½ × 1,2 × 15² = ½ × 1,2 × 225 = 135 J.

**QM-2** · dissertativa · médio

Um pesquisador caminha 50 m carregando uma mochila de 8 kg nas
costas, em terreno plano e horizontal. O peso da mochila realiza
trabalho sobre ela durante essa caminhada? Justifique.

✅ Gabarito: Não.
📝 Resolução: o peso da mochila atua na direção vertical, enquanto
o deslocamento do pesquisador é horizontal — força e deslocamento
são perpendiculares (θ = 90°), logo W = F·cosθ·d = F·cos90°·d = 0.

**QM-3** · múltipla escolha estilo concurso · difícil

Um satélite descreve uma órbita circular de raio R em torno da
Terra, com velocidade tangencial de módulo constante v. Sobre esse
movimento, é correto afirmar que:

a) a velocidade do satélite é constante em módulo e em direção
b) a aceleração centrípeta é nula, pois o módulo da velocidade não muda
c) a aceleração centrípeta aponta sempre para o centro da órbita e é responsável apenas pela mudança de direção da velocidade
d) não há aceleração atuando sobre o satélite, pois o movimento é uniforme
e) a aceleração centrípeta é proporcional a R e inversamente proporcional a v²

✅ Gabarito: c
📝 Resolução: acp = v²/R é sempre dirigida ao centro e responsável
apenas por mudar a direção da velocidade — não seu módulo. As
demais alternativas confundem "velocidade constante em módulo"
(MCU) com "velocidade constante em direção" (que não ocorre no
movimento circular).

**QM-4** · cálculo/aplicação · médio-difícil

Uma pedra de 0,50 kg é abandonada (v₀ = 0) do alto de um penhasco de
20 m de altura. Desprezando a resistência do ar, calcule a
velocidade da pedra ao atingir o solo, usando conservação de
energia mecânica (g = 10 m/s²).

✅ Gabarito: v ≈ 20 m/s
📝 Resolução: no topo, Emec = Epg = mgh = 0,50 × 10 × 20 = 100 J
(Ec = 0, pois v₀ = 0). No solo, h = 0, então Emec = Ec = ½mv².
Por conservação: ½ × 0,50 × v² = 100 → v² = 400 → v = 20 m/s.

**QM-5** · dissertativa · difícil

Um pêndulo simples de 1,0 m de comprimento tem período de 2,0 s
medido experimentalmente num laboratório. Usando T = 2π√(l/g),
estime o valor de g obtido nesse experimento e compare com o valor
teórico de referência (9,8 m/s²). O resultado é consistente com os
dados da Tabela 6 do capítulo?

✅ Gabarito: g ≈ 9,87 m/s² — consistente com a Tabela 6 (valores entre 9,6 e 10,2 m/s²).
📝 Resolução: de T = 2π√(l/g), isolando g: g = 4π²l/T² =
4 × (3,14)² × 1,0 / (2,0)² = 4 × 9,86 × 1,0 / 4,0 ≈ 9,87 m/s².
Valor próximo do teórico (9,8 m/s²) e dentro da faixa de erro
experimental observada na Tabela 6 do capítulo.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: graficos_muv
Gráficos S×t (parábola) e v×t (reta) do MUV

<svg width="100%" viewBox="0 0 680 300">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
stroke-width="1.5" stroke-linecap="round"
stroke-linejoin="round"/></marker></defs>
<text x="40" y="30" class="th">S × t — parábola</text>
<line x1="70" y1="240" x2="70" y2="55" class="c-gray" stroke="currentColor" stroke-width="1.5"/>
<line x1="70" y1="240" x2="310" y2="240" class="c-gray" stroke="currentColor" stroke-width="1.5"/>
<path d="M70 240 Q 190 235 310 80" fill="none" class="c-purple" stroke="currentColor" stroke-width="3" marker-end="url(#arrow)"/>
<text x="45" y="60" class="t">S</text>
<text x="300" y="258" class="t">t</text>
<text x="45" y="255" class="ts">0</text>
<text x="390" y="30" class="th">v × t — reta (inclinação = aceleração)</text>
<line x1="390" y1="240" x2="390" y2="55" class="c-gray" stroke="currentColor" stroke-width="1.5"/>
<line x1="390" y1="240" x2="630" y2="240" class="c-gray" stroke="currentColor" stroke-width="1.5"/>
<line x1="390" y1="200" x2="630" y2="80" class="c-teal" stroke="currentColor" stroke-width="3" marker-end="url(#arrow)"/>
<text x="365" y="60" class="t">v</text>
<text x="620" y="258" class="t">t</text>
<text x="360" y="205" class="ts">v0</text>
</svg>

### DIAGRAMA: conservacao_energia
Conservação da energia mecânica — queda livre de A até B

<svg width="100%" viewBox="0 0 680 300">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
stroke-width="1.5" stroke-linecap="round"
stroke-linejoin="round"/></marker></defs>
<text x="40" y="30" class="th">Emec = Ep + Ec = constante (sem forças dissipativas)</text>
<rect x="80" y="60" width="80" height="160" class="c-purple" fill="currentColor"/>
<text x="100" y="245" class="t">A (v=0)</text>
<rect x="300" y="60" width="80" height="80" class="c-purple" fill="currentColor"/>
<rect x="300" y="140" width="80" height="80" class="c-teal" fill="currentColor"/>
<text x="320" y="245" class="t">C</text>
<rect x="520" y="60" width="80" height="160" class="c-teal" fill="currentColor"/>
<text x="500" y="245" class="t">B (h=0)</text>
<rect x="40" y="270" width="16" height="16" class="c-purple" fill="currentColor"/>
<text x="62" y="283" class="ts">Ep (energia potencial)</text>
<rect x="260" y="270" width="16" height="16" class="c-teal" fill="currentColor"/>
<text x="282" y="283" class="ts">Ec (energia cinética)</text>
</svg>
