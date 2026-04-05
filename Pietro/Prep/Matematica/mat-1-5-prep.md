# PREPARAÇÃO DE AULA — MATEMÁTICA
- **Unidade:** 1
- **Capítulo:** 5
- **Tema:** Relações Métricas no Triângulo Retângulo
- **Perfil:** Geometria
- **Fórmulas principais:** $$a \cdot h = b \cdot c$$ · $$c^2 = a \cdot n$$ · $$b^2 = a \cdot m$$ · $$h^2 = m \cdot n$$ · $$a^2 = b^2 + c^2$$ · $$F_R^2 = F_1^2 + F_2^2$$
- **Matemáticos citados:** nenhum explicitamente

---

## SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

| Nome | Identificador (Seção 12) | Quando usar |
|---|---|---|
| Triângulo com relações métricas | DIAGRAMA: relacoes_metricas | Ao introduzir h, m, n e as 6 relações |
| Três triângulos semelhantes | DIAGRAMA: semelhanca_triangulos | Ao explicar origem AA das relações |
| Síntese das relações | DIAGRAMA: sintese_relacoes | Revisão antes dos exercícios |
| Forças ortogonais | DIAGRAMA: forcas_ortogonais | Contextualização física |

**Tabelas markdown (Seção 6):**
- Tabela das 6 relações métricas com expressão e origem

---

## SEÇÃO 1 — METADADOS

| Campo | Valor |
|---|---|
| Matéria | Matemática |
| Unidade | 1 |
| Capítulo | 5 |
| Tema | Relações Métricas no Triângulo Retângulo |
| Perfil | Geometria |
| Nível | 9º ano |

---

## SEÇÃO 2 — RESUMO CONCEITUAL

### Triângulo Retângulo — estrutura e nomenclatura

Um triângulo retângulo possui exatamente um ângulo de 90°. Os dois lados que formam esse ângulo reto são os **catetos** ($$b$$ e $$c$$); o lado oposto — sempre o maior — é a **hipotenusa** ($$a$$).

Na notação do livro, o triângulo de referência é o **△ABC**, com:
- Ângulo reto em **A**
- Hipotenusa $$a = BC$$
- Cateto $$b = AC$$ · Cateto $$c = AB$$

---

### Altitude relativa à hipotenusa — elementos h, m, n

Ao traçar a altura $$h$$ do vértice A até o ponto H na hipotenusa BC, surgem:

| Elemento | Significado |
|---|---|
| $$h$$ | Altitude do ângulo reto até H |
| $$n$$ | Projeção do cateto $$c$$ sobre a hipotenusa (segmento BH) |
| $$m$$ | Projeção do cateto $$b$$ sobre a hipotenusa (segmento HC) |
| $$a = m + n$$ | Hipotenusa total |

> 💡 **Conexão real:** a altura de uma rampa de skate vista de lado corresponde a $$h$$; a extensão no chão divide-se em $$m$$ e $$n$$.

---

### Semelhança de triângulos — origem das relações métricas

Pelo caso **AA** (dois ângulos iguais), os três triângulos formados são semelhantes:

$$\triangle ABC \sim \triangle HBA \sim \triangle HAC$$

Os ângulos $$\alpha$$ (em B) e $$\beta$$ (em C) aparecem nos três triângulos, garantindo a proporcionalidade dos lados correspondentes.

---

### As 6 Relações Métricas

| Nº | Expressão | Leitura |
|---|---|---|
| (1) | $$a \cdot h = b \cdot c$$ | hipotenusa × altura = produto dos catetos |
| (2) | $$c^2 = a \cdot n$$ | cateto² = hipotenusa × projeção do cateto |
| (3) | $$c \cdot h = b \cdot n$$ | relação cruzada entre lados |
| (4) | $$b^2 = a \cdot m$$ | cateto² = hipotenusa × projeção do cateto |
| (5) | $$b \cdot h = c \cdot m$$ | relação cruzada entre lados |
| (6) | $$h^2 = m \cdot n$$ | altura² = produto das projeções |

> As relações **(1), (2), (4) e (6)** são as mais cobradas em avaliações.

---

### Teorema de Pitágoras

Somando as relações (2) e (4):

$$c^2 + b^2 = a \cdot n + a \cdot m = a(m+n) = a^2$$

$$\boxed{a^2 = b^2 + c^2}$$

**Recíproca:** se os lados de um triângulo satisfazem $$a^2 = b^2 + c^2$$, então ele é retângulo.

> Exemplo: **8, 15, 17** → $$8^2 + 15^2 = 64 + 225 = 289 = 17^2$$ ✔

---

### Aplicação: Forças Ortogonais

Quando $$\vec{F_1} \perp \vec{F_2}$$, a força resultante é a hipotenusa do triângulo que elas formam:

$$F_R^2 = F_1^2 + F_2^2$$

---

### Aplicação: Distância Terra–Lua (Paralaxe Estelar)

Usando semelhança de triângulos com ângulo $$2P = 2°$$:

$$\frac{1{,}4}{6400} = \frac{80}{d} \Rightarrow d \approx 365.714 \text{ km}$$

---

## SEÇÃO 3 — MATEMÁTICOS E HISTÓRIA

> O livro não cita matemáticos nominalmente. **Seção não gerada.**
>
> **Recomendação:** mencionar Pitágoras de Samos (c. 570–495 a.C.) e a Escola Pitagórica ao introduzir o teorema.

---

## SEÇÃO 4 — FÓRMULAS, PROPRIEDADES E LEIS

### Relação (1) — Produto da hipotenusa pela altura

**Expressão:** $$a \cdot h = b \cdot c$$

| Símbolo | Significado | Tipo |
|---|---|---|
| $$a$$ | Hipotenusa | real positivo |
| $$h$$ | Altura relativa à hipotenusa | real positivo |
| $$b, c$$ | Catetos | real positivo |

**Válida quando:** existe altitude $$h$$ traçada do ângulo reto até H na hipotenusa.

💡 **Pegadinha:** esta relação **não é** o Teorema de Pitágoras. Envolve a **altura**, não a soma dos quadrados.

---

### Relação (2) — Quadrado do cateto c

**Expressão:** $$c^2 = a \cdot n$$

| Símbolo | Significado | Tipo |
|---|---|---|
| $$c$$ | Cateto (lado AB) | real positivo |
| $$a$$ | Hipotenusa | real positivo |
| $$n$$ | Projeção de $$c$$ sobre a hipotenusa | real positivo |

💡 **Pegadinha:** $$n$$ é a projeção de **c**, não de **b**. Inverter $$m$$ e $$n$$ é o erro mais frequente.

---

### Relação (4) — Quadrado do cateto b

**Expressão:** $$b^2 = a \cdot m$$

| Símbolo | Significado | Tipo |
|---|---|---|
| $$b$$ | Cateto (lado AC) | real positivo |
| $$a$$ | Hipotenusa | real positivo |
| $$m$$ | Projeção de $$b$$ sobre a hipotenusa | real positivo |

💡 **Pegadinha:** $$m$$ fica do lado do ângulo $$\beta$$ (em C). Associe: **"cateto b projeta m, ambos do lado C"**.

---

### Relação (6) — Quadrado da altura

**Expressão:** $$h^2 = m \cdot n$$

| Símbolo | Significado | Tipo |
|---|---|---|
| $$h$$ | Altura relativa à hipotenusa | real positivo |
| $$m$$ | Projeção do cateto $$b$$ | real positivo |
| $$n$$ | Projeção do cateto $$c$$ | real positivo |

💡 **Pegadinha:** válida **apenas** para a altura relativa à hipotenusa, não para qualquer altura.

---

### Teorema de Pitágoras

**Expressão:** $$a^2 = b^2 + c^2$$

| Símbolo | Significado | Tipo |
|---|---|---|
| $$a$$ | Hipotenusa (oposta ao ângulo reto) | real positivo |
| $$b, c$$ | Catetos | real positivo |

**Recíproca:** se $$a^2 = b^2 + c^2$$ → triângulo é retângulo.

💡 **Pegadinha:** o maior lado é **sempre** a hipotenusa. Aplicar $$a^2 = b^2 + c^2$$ com um cateto no lugar de $$a$$ gera resultado negativo sob raiz.

---

### Força Resultante

**Expressão:** $$F_R^2 = F_1^2 + F_2^2$$

| Símbolo | Significado | Tipo |
|---|---|---|
| $$F_R$$ | Força resultante | escalar (módulo) |
| $$F_1, F_2$$ | Forças perpendiculares entre si | escalar (módulo) |

**Válida quando:** ângulo de 90° entre $$\vec{F_1}$$ e $$\vec{F_2}$$.

---

## SEÇÃO 5 — REPRESENTAÇÕES E SISTEMAS

> Não aplicável a este capítulo. **Seção não gerada.**

---

## SEÇÃO 6 — TABELAS DE REFERÊNCIA

### Relações Métricas — conjunto completo

| Nº | Expressão | Semelhança de origem |
|---|---|---|
| (1) | $$a \cdot h = b \cdot c$$ | $$\triangle ABC \sim \triangle HBA$$ |
| (2) | $$c^2 = a \cdot n$$ | $$\triangle ABC \sim \triangle HBA$$ |
| (3) | $$c \cdot h = b \cdot n$$ | $$\triangle ABC \sim \triangle HBA$$ |
| (4) | $$b^2 = a \cdot m$$ | $$\triangle ABC \sim \triangle HAC$$ |
| (5) | $$b \cdot h = c \cdot m$$ | $$\triangle ABC \sim \triangle HAC$$ |
| (6) | $$h^2 = m \cdot n$$ | $$\triangle HBA \sim \triangle HAC$$ |

**Condição geral:** triângulo ABC retângulo em A, com H = pé da altitude $$h$$ sobre BC.

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Identifique m e n pelo lado do ângulo**
$$m$$ fica do lado de C (projeção de $$b$$); $$n$$ fica do lado de B (projeção de $$c$$). Macete: *"n vem antes de m no alfabeto, assim como B vem antes de C"*.

💡 **Dica 2 — A hipotenusa é sempre o maior lado**
Antes de qualquer cálculo, identifique o ângulo reto e o lado oposto a ele. Nunca aplique $$a^2 = b^2 + c^2$$ com um cateto no lugar de $$a$$.

💡 **Dica 3 — h² = m·n não é Pitágoras**
São fórmulas diferentes: uma envolve a **altura e as projeções**; a outra envolve **catetos e hipotenusa**. Não confundir.

💡 **Dica 4 — Recíproca do Teorema de Pitágoras**
Para verificar se é retângulo: eleve o **maior lado** ao quadrado e compare com a soma dos quadrados dos outros dois. Ex: lados 10, 40, 42 → $$42^2 = 1764 \neq 10^2 + 40^2 = 1700$$ → **não é retângulo**.

💡 **Dica 5 — Relação (1) como atalho para h**
Quando conhecer os dois catetos e a hipotenusa, use $$h = \dfrac{b \cdot c}{a}$$ diretamente. Ex: catetos 6 e 8, hipotenusa 10 → $$h = \dfrac{48}{10} = 4{,}8$$ cm.

💡 **Dica 6 — Pitágoras em dois passos para figuras 3D**
Em blocos retangulares, calcule primeiro a diagonal da base e depois use esse resultado como cateto para a diagonal espacial — nunca tente fazer tudo em uma única equação.

---

## SEÇÃO 8 — ALERTAS E LACUNAS

### Bloco A — Lacunas de dados

| Seção | Campo | Motivo | Ação recomendada |
|---|---|---|---|
| Q-1 | Figuras individuais dos itens b)–h) | Não capturadas individualmente | Usar printscreen da pág. 113 em aula |
| Q-13 | Comprimento dos cabos de aço | Ausente na descrição | Verificar no livro físico |
| Q-15 | Relação geométrica BD/CD com BC | Reconstrução parcial da figura | Verificar no livro físico |
| QC-9 | Posição exata do ponto E | Descrito como ambíguo | Anexar printscreen da pág. 122 |

### Bloco B — Inconsistências factuais

> ⚠️ **ALERTA — Q-6: classificação de dificuldade**
> - **Dado no material:** classificação "fácil"
> - **Problema:** lados 10, 40 e 42 → $$10^2 + 40^2 = 1700 \neq 42^2 = 1764$$. Exige aplicação da recíproca e interpretação do resultado.
> - **Correto:** classificação → **médio**
> - **Impacto:** não tratar como exercício trivial; explorar a diferença entre terna pitagórica e trio qualquer.

> ⚠️ **ALERTA — QC-5: configuração geométrica do balão**
> - **Dado no material:** "ângulo reto em João"
> - **Problema:** o ângulo reto está entre a vertical (balão–chão) e o chão, não necessariamente em João.
> - **Impacto:** apresentar o diagrama antes de resolver; não assumir o gabarito sem montar o triângulo explicitamente.

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (warm-up)

### Bloco 1 — Conceitos e Definições

- **Triângulo Retângulo**
  - Definição: triângulo que possui `______` *(um ângulo de 90°)*
  - Os lados que formam o ângulo reto chamam-se `______` *(catetos)*
  - O lado oposto ao ângulo reto chama-se `______` *(hipotenusa)*

- **Elementos após traçar a altitude h**
  - H é o `______` da altitude relativa à hipotenusa *(pé da altitude)*
  - m é a projeção do cateto `______` sobre a hipotenusa *(b)*
  - n é a projeção do cateto `______` sobre a hipotenusa *(c)*
  - Relação entre m, n e a: `______` *(a = m + n)*

- **Semelhança**
  - Os três triângulos são semelhantes pelo caso: `______` *(AA)*
  - Cadeia: `______` *(△ABC ~ △HBA ~ △HAC)*

### Bloco 2 — Fórmulas e Propriedades

- **Relação (1):** `______` *(a·h = b·c)* — envolve hipotenusa, `______` e dois catetos *(altura h)*
- **Relação (6):** `______` *(h² = m·n)* — h é a `______` relativa à hipotenusa *(altitude)*
- **Teorema de Pitágoras:** `______` *(a² = b² + c²)* — a é sempre a `______` *(hipotenusa)*
- **Força Resultante:** `______` *(F²R = F²₁ + F²₂)* — válida quando o ângulo entre as forças é `______` *(90°)*

### Bloco 3 — Lacunas para Warm-Up

1. O lado oposto ao ângulo reto em um triângulo retângulo chama-se `______`. *(hipotenusa)*

2. Ao traçar a altitude relativa à hipotenusa em △ABC, formam-se `______` triângulos semelhantes. *(três — △ABC, △HBA e △HAC)*

3. A relação métrica que relaciona apenas a altura com as projeções dos catetos é `______`. *(h² = m·n)*

4. Para verificar se um triângulo de lados 10, 40 e 42 é retângulo, calculamos $$42^2 = \text{______}$$ e comparamos com $$10^2 + 40^2 = \text{______}$$. *(1764 e 1700 → não é retângulo)*

5. Em um triângulo com catetos 6 cm e 8 cm, a hipotenusa mede `______`. *(10 cm, pois 36 + 64 = 100)*

6. A altura relativa à hipotenusa desse mesmo triângulo mede `______`, usando $$a \cdot h = b \cdot c$$. *(4,8 cm)*

7. A distância Terra–Lua estimada pelo método da paralaxe foi de aproximadamente `______` km. *(365.714 km)*

8. Quando $$\vec{F_1} \perp \vec{F_2}$$, a força resultante satisfaz `______`. *(F²R = F²₁ + F²₂)*

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

### Síntese do Livro — RELAÇÕES MÉTRICAS NO TRIÂNGULO RETÂNGULO

| Nó / Posição | Já dado na síntese | Lacuna — resposta esperada |
|---|---|---|
| Título central (amarelo) | "Em um triângulo retângulo, são válidas as relações métricas:" | — |
| Caixa superior esquerda | $$a \cdot h = b \cdot c$$ | Qual grandeza relaciona a hipotenusa com os dois catetos? → **altitude h** |
| Caixa superior direita | $$c \cdot h = b \cdot n$$ | Esta é a relação nº `______` → **(3)** |
| Caixa esquerda | $$b^2 = a \cdot m$$ | m representa `______` → **projeção do cateto b** |
| Caixa direita | $$c^2 = a \cdot n$$ | n representa `______` → **projeção do cateto c** |
| Caixa inferior esquerda | $$a^2 = b^2 + c^2$$ | Esta relação é o `______` → **Teorema de Pitágoras** |
| Caixa inferior central | $$h^2 = m \cdot n$$ | Quais grandezas aparecem? → **altitude h e projeções m e n** |
| Caixa inferior direita | $$b \cdot h = c \cdot m$$ | Esta é a relação nº `______` → **(5)** |

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Gabarito / Resolução resumida | Obs. |
|---|---|---|---|---|---|
| Q-1 | Encontrar incógnita em 8 triângulos | Cal | M | a) x=9,6 · b) x=√12 · c) x=4 · d) x=16 · e) x=32 · f) x=3√7 · g) x=144/25 · h) x=1/3 | ⚠️ figuras b–h sem descrição |
| Q-2 | V ou F: 3 afirmações sobre relações métricas | Dis | M | a) F · b) V (h²=36→h=6) · c) V (h=4,8) | — |
| Q-3 | Catetos em proporção 2:1, hipotenusa 8√5 | Cal | D | Catetos: 16 cm e 8 cm | — |
| Q-4 | Incógnita em 6 triângulos (Pitágoras) | Cal | M | a) 70 · b) 3√21 · c) √271 · d) 12 · e) 4√2 · f) 4√5 | ⚠️ figuras sem descrição |
| Q-5 | 8, 15, 17 é retângulo? | Dis | F | Sim: $$8^2+15^2=289=17^2$$ ✔ | — |
| Q-6 | 10, 40, 42 é retângulo? | Dis | **M** | Não: $$1700 \neq 1764$$ | ⚠️ dif. corrigida |
| Q-7 | Catetos 4x+4 e 3x−8, hipotenusa 5x; perímetro | Cal | M | x=12 → P=140 cm | — |
| Q-8 | Soma das áreas das semicircunferências | Cal | D | Pelo Teorema de Hipócrates: soma = $$200\pi$$ | ⚠️ BC ausente na figura |
| Q-9 | Perímetro do triângulo AHC no bloco retangular | Cal | D | AC=13, AH=15, HC=√106 → P = $$28 + \sqrt{106}$$ cm | — |
| Q-10 | Lados do triângulo isósceles (base=altura=50 cm) | Cal | M | $$l = 25\sqrt{5}$$ cm | — |
| Q-11 | Diagonal da TV 64×36 cm em polegadas | Cal | M | $$\approx 28{,}3$$ polegadas | — |
| Q-12 | Diagonal do quadrado sobre a hipotenusa | Cal | M | 6 cm | — |
| Q-13 | Altura h do cabo na árvore (6 m e 13,5 m) | Cal | M | Dados insuficientes sem comprimento dos cabos | ⚠️ verificar livro |
| Q-14 | Altura do muro (OB=40, OP=32) | Cal | D | $$x = \dfrac{160}{3} \approx 53{,}3$$ dm | — |
| Q-15 | BC, x e área do quadrilátero ABDC | Cal | D | x=25; BC=112 mm | ⚠️ figura parcial |
| QC-1 | Distância entre 2 circunferências no quadriculado | MC | D | **a) $$2\sqrt{2}-1$$** | Canguru 2016 |
| QC-2 | Altura relativa à hipotenusa; catetos 6 e 8 | MC | M | **b) 4,8 cm** | Ifal 2017 |
| QC-3 | Área do quadrado interno (4 triângulos congruentes) | MC | M | **b) $$a^2+b^2$$** | UFRGS |
| QC-4 | Valores de x, y, z com projeções 9 e 16 | Cal | M | z=15, x=20, y=12 | Obmep |
| QC-5 | Altura do balão (8, 15, 17 km) | MC | M | A confirmar com diagrama | ⚠️ CPII-RJ 2017 |
| QC-6 | Área do triângulo AMN | MC | D | **a) 3,36 cm²** | ITA-SP 2017 |
| QC-7 | Área do terreno irregular | MC | D | A confirmar com figura completa | ⚠️ ESPM-SP 2016 |
| QC-8 | Comprimento da trepadeira (5 voltas) | MC | D | **c) 1,25 m** (cada volta=25 cm) | Canguru 2016 |
| QC-9 | Área do triângulo ABE | MC | D | **d) 60 cm²** | ⚠️ CPII-RJ 2017 |
| QC-10 | Localização ideal para conexão das rodovias | MC | D | **c) III** (reflexão minimiza soma) | ENEM 2022 |

---

### Bloco B — Questões Modelo Originais

---

**QM-1** · Múltipla escolha · Médio · inspirada em: QC-2

Em um triângulo retângulo, os catetos medem 5 cm e 12 cm. Qual é a medida da altura relativa à hipotenusa?

- a) 4,2 cm
- b) 4,6 cm
- c) $$\dfrac{60}{13}$$ cm
- d) 5 cm

✅ **Gabarito: c)**

📝 **Resolução:**
- Hipotenusa: $$a = \sqrt{5^2 + 12^2} = \sqrt{169} = 13$$ cm
- Pela relação (1): $$13 \cdot h = 5 \times 12 = 60 \Rightarrow h = \dfrac{60}{13}$$ cm

⚠️ **Professor:** a alternativa b) é distratora (60/13 arredondado). Valorize a forma exata.

---

**QM-2** · Múltipla escolha · Médio · inspirada em: Q-5 e Q-6

Qual dos seguintes conjuntos forma um triângulo retângulo?

- a) 7, 24, 26
- b) 9, 40, 41
- c) 11, 60, 62
- d) 5, 11, 13

✅ **Gabarito: b)**

📝 **Resolução:**
- a) $$7^2+24^2=625 \neq 676$$ ✗
- b) $$9^2+40^2=1681=41^2$$ ✔
- c) $$11^2+60^2=3721 \neq 3844$$ ✗
- d) $$5^2+11^2=146 \neq 169$$ ✗

⚠️ **Professor:** reforce que sempre se testa o **maior lado** como hipotenusa.

---

**QM-3** · Cálculo · Médio · inspirada em: Q-10

Uma treliça metálica tem formato de triângulo isósceles com base de 80 cm e altura de 30 cm. Qual é o comprimento de cada lado congruente?

✅ **Gabarito: 50 cm**

📝 **Resolução:**
- Semi-base = 40 cm
- $$l = \sqrt{40^2 + 30^2} = \sqrt{1600 + 900} = \sqrt{2500} = 50$$ cm

⚠️ **Professor:** erro comum é usar a base inteira (80) em vez da semi-base (40).

---

**QM-4** · Estilo concurso · Difícil · inspirada em: Q-14 e QC-4

*(Estilo CPII-RJ)* Em um triângulo retângulo PQR com ângulo reto em P, a altitude relativa à hipotenusa QR tem pé S, com QS = 4 cm e SR = 9 cm. Determine a área do triângulo PQR.

- a) 39 cm²
- b) 32,5 cm²
- c) 30 cm²
- d) 26 cm²

✅ **Gabarito: b)**

📝 **Resolução:**
- $$QR = 4 + 9 = 13$$ cm
- $$h^2 = 4 \times 9 = 36 \Rightarrow h = 6$$ cm
- $$\text{Área} = \dfrac{1}{2} \times 13 \times 6 = 39 \div 2 = 32{,}5 \text{ cm}^2$$

---

**QM-5** · Dissertativa · Médio-difícil · inspirada em: Q-2 e Q-3

A hipotenusa de um triângulo retângulo mede 26 cm e um cateto mede 10 cm.

- **a)** Calcule o outro cateto.
- **b)** Calcule a altura relativa à hipotenusa.
- **c)** Calcule as projeções dos catetos sobre a hipotenusa.
- **d)** Verifique se $$h^2 = m \cdot n$$.

✅ **Gabarito:**

**a)** $$b = \sqrt{26^2 - 10^2} = \sqrt{576} = 24$$ cm

**b)** $$h = \dfrac{24 \times 10}{26} = \dfrac{120}{13} \approx 9{,}23$$ cm

**c)** $$n = \dfrac{c^2}{a} = \dfrac{100}{26} = \dfrac{50}{13}$$ cm · $$m = \dfrac{b^2}{a} = \dfrac{576}{26} = \dfrac{288}{13}$$ cm

**d)** $$h^2 = \dfrac{14400}{169}$$ · $$m \cdot n = \dfrac{288}{13} \times \dfrac{50}{13} = \dfrac{14400}{169}$$ ✔

⚠️ **Professor:** o item d) demonstra a consistência das relações métricas — excelente para fechamento da aula.

---

## SEÇÃO 12 — DIAGRAMAS SVG

### DIAGRAMA: sintese_relacoes
Tabela visual das 6 relações métricas organizadas por grupo de semelhança.

```svg
<svg width="100%" viewBox="0 0 680 310" xmlns="http://www.w3.org/2000/svg" style="font-family:sans-serif">
  <defs>
    <style>
      .th{font-size:13px;font-weight:700;fill:#1a3a5c;text-anchor:middle;dominant-baseline:central}
      .wt{fill:#fff;font-size:12px;font-weight:700;text-anchor:middle;dominant-baseline:central}
      .ts{font-size:11px;fill:#6b7280;text-anchor:middle;dominant-baseline:central}
    </style>
  </defs>
  <rect x="10" y="10" width="660" height="36" rx="8" fill="#1a3a5c"/>
  <text x="340" y="28" class="wt" style="font-size:14px">Relações Métricas no Triângulo Retângulo</text>
  <rect x="10" y="56" width="210" height="26" rx="6" fill="#7c3aed"/>
  <text x="115" y="69" class="wt">△ABC ~ △HBA</text>
  <rect x="10" y="88" width="210" height="36" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.2"/>
  <text x="115" y="106" class="th">(1) a · h = b · c</text>
  <rect x="10" y="130" width="210" height="36" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.2"/>
  <text x="115" y="148" class="th">(2) c² = a · n</text>
  <rect x="10" y="172" width="210" height="36" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.2"/>
  <text x="115" y="190" class="th">(3) c · h = b · n</text>
  <rect x="235" y="56" width="210" height="26" rx="6" fill="#0d9488"/>
  <text x="340" y="69" class="wt">△ABC ~ △HAC</text>
  <rect x="235" y="88" width="210" height="36" rx="6" fill="#d1fae5" stroke="#059669" stroke-width="1.2"/>
  <text x="340" y="106" class="th">(4) b² = a · m</text>
  <rect x="235" y="130" width="210" height="36" rx="6" fill="#d1fae5" stroke="#059669" stroke-width="1.2"/>
  <text x="340" y="148" class="th">(5) b · h = c · m</text>
  <rect x="460" y="56" width="210" height="26" rx="6" fill="#16a34a"/>
  <text x="565" y="69" class="wt">△HBA ~ △HAC</text>
  <rect x="460" y="88" width="210" height="36" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.2"/>
  <text x="565" y="106" class="th">(6) h² = m · n</text>
  <rect x="10" y="220" width="660" height="40" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="340" y="240" class="th" style="font-size:14px">Teorema de Pitágoras: a² = b² + c²</text>
  <text x="340" y="255" class="ts">(derivado de (2)+(4): c²+b² = a·n+a·m = a²)</text>
  <rect x="10" y="272" width="660" height="28" rx="6" fill="#fee2e2" stroke="#e11d48" stroke-width="1.2"/>
  <text x="340" y="286" class="th" style="fill:#be123c;font-size:12px">⚠ m = projeção de b · n = projeção de c · nunca inverter!</text>
</svg>
```

---

### DIAGRAMA: semelhanca_triangulos
Os três triângulos semelhantes com ângulos α e β identificados.

```svg
<svg width="100%" viewBox="0 0 680 260" xmlns="http://www.w3.org/2000/svg" style="font-family:sans-serif">
  <defs>
    <style>
      .th{font-size:13px;font-weight:700;fill:#1a3a5c;text-anchor:middle;dominant-baseline:central}
      .t{font-size:12px;fill:#1a3a5c;text-anchor:middle;dominant-baseline:central}
      .ts{font-size:11px;fill:#6b7280;text-anchor:middle;dominant-baseline:central}
      .wt{fill:#fff;font-size:11px;font-weight:700;text-anchor:middle;dominant-baseline:central}
    </style>
  </defs>
  <rect x="10" y="6" width="80" height="26" rx="13" fill="#7c3aed"/>
  <text x="50" y="19" class="wt">△ABC</text>
  <polygon points="100,20 10,200 210,200" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <rect x="93" y="24" width="10" height="10" fill="none" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="100" y="12" class="th">A</text>
  <text x="4" y="212" class="th">B</text>
  <text x="216" y="212" class="th">C</text>
  <text x="42" y="218" class="ts">α</text>
  <text x="192" y="218" class="ts">β</text>
  <text x="48" y="115" class="t">c</text>
  <text x="160" y="115" class="t">b</text>
  <text x="110" y="215" class="t">a</text>
  <rect x="235" y="6" width="80" height="26" rx="13" fill="#059669"/>
  <text x="275" y="19" class="wt">△HBA</text>
  <polygon points="330,20 240,200 330,200" fill="#d1fae5" stroke="#059669" stroke-width="2"/>
  <rect x="323" y="24" width="10" height="10" fill="none" stroke="#059669" stroke-width="1.5"/>
  <rect x="323" y="188" width="10" height="10" fill="none" stroke="#059669" stroke-width="1.5"/>
  <text x="330" y="12" class="th">A</text>
  <text x="234" y="212" class="th">B</text>
  <text x="336" y="212" class="th">H</text>
  <text x="252" y="218" class="ts">α</text>
  <text x="278" y="115" class="t">c</text>
  <text x="342" y="115" class="t">h</text>
  <text x="285" y="215" class="t">n</text>
  <rect x="455" y="6" width="80" height="26" rx="13" fill="#d97706"/>
  <text x="495" y="19" class="wt">△HAC</text>
  <polygon points="495,20 440,200 580,200" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <rect x="488" y="24" width="10" height="10" fill="none" stroke="#d97706" stroke-width="1.5"/>
  <rect x="433" y="188" width="10" height="10" fill="none" stroke="#d97706" stroke-width="1.5"/>
  <text x="495" y="12" class="th">A</text>
  <text x="434" y="212" class="th">H</text>
  <text x="586" y="212" class="th">C</text>
  <text x="562" y="218" class="ts">β</text>
  <text x="458" y="115" class="t">h</text>
  <text x="548" y="115" class="t">b</text>
  <text x="513" y="215" class="t">m</text>
  <text x="340" y="248" class="ts">Pelo caso AA: △ABC ~ △HBA ~ △HAC</text>
</svg>
```

---

