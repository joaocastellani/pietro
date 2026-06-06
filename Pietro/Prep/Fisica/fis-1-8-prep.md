# PREPARAÇÃO DE AULA — FÍSICA · Capítulo 8 · Energia e Trabalho

---

## SEÇÃO 0 — ÍNDICE DE DIAGRAMAS

```
## DIAGRAMAS DISPONÍVEIS — fis-1-8

| Nome                        | Identificador na Seção 12             | Quando usar na Etapa 1                                      |
|-----------------------------|---------------------------------------|-------------------------------------------------------------|
| Hierarquia da Energia        | DIAGRAMA: hierarquia_energia          | Introdução ao conceito de energia e seus tipos              |
| Fórmulas do Capítulo        | DIAGRAMA: formulas                    | Revisão de fórmulas antes de exercícios                     |
| Tipos de Alavanca           | DIAGRAMA: tipos_alavanca              | Explicação das três classificações de alavanca              |
| Conservação de Energia      | DIAGRAMA: conservacao_energia         | Visualização da troca E_C ↔ E_G ao longo de uma trajetória  |

### Tabelas markdown (Seção 6):
- Tabela de grandezas, símbolos e unidades SI (Seção 5.1)
- Tabela síntese — conceitos e respostas esperadas (Seção 9, Bloco 4)

### Nota ao Professor:
Para cada diagrama: leia o SVG da Seção 12 e passe ao Visualizer para
renderizar inline. Tabelas das Seções 5 e 9 são apresentadas como
markdown no chat.
```

---

## SEÇÃO 1 — METADADOS

```
# PREPARAÇÃO DE AULA — FÍSICA
- Unidade: 1
- Capítulo: 8
- Tema: Energia e Trabalho
- Perfil: misto
- Fórmulas principais:
    E_C = (1/2)·m·v²
    E_G = m·g·h
    E_M = E_C + E_G + E_E
    τ = F·Δs
    P = τ/Δt
    Fr·br = Fp·bp
- Cientistas citados: James Prescott Joule
```

---

## SEÇÃO 2 — RESUMO CONCEITUAL DO CAPÍTULO

### 🔋 O que é Energia?

Energia é a **capacidade de realizar trabalho**. No dia a dia ela aparece o tempo todo: a gasolina que move um carro, o vento que gira um aerogerador, o alimento que nos dá disposição. No SI, a unidade de energia é o **joule (J)**. Um princípio fundamental governa a energia: ela **nunca é criada nem destruída** — apenas transformada de um tipo para outro (lei da conservação de energia).

---

### ⚙️ Tipos de Energia Mecânica

A **energia mecânica (E_M)** é a soma de duas grandes famílias:

**1. Energia cinética (E_C):** associada ao *movimento*. Quanto maior a massa ou a velocidade, maior a E_C. O ponto-chave: a velocidade entra ao quadrado — dobrar a velocidade quadruplica a energia cinética. É por isso que exceder o limite de velocidade no trânsito é tão perigoso.

**2. Energia potencial:** associada a uma condição *armazenada*. Divide-se em:
- **Potencial gravitacional (E_G):** depende da altura. Um objeto suspenso tem energia armazenada pela interação com a gravidade terrestre.
- **Potencial elástica (E_E):** depende da deformação (mola comprimida ou esticada).

$$E_M = E_C + E_G + E_E$$

---

### 🔄 Conservação de Energia Mecânica

Quando a energia mecânica se transforma apenas entre cinética e potencial (sem perdas para calor, som etc.), o total se conserva. O exemplo clássico é o esquiador: no topo (E_M = E_G), na descida (E_M = E_C + E_G), na base (E_M = E_C). A soma nunca muda.

---

### 🔨 Trabalho

Em Física, **trabalho (τ)** é a quantidade de energia transferida a um corpo por uma força que o desloca. Só existe trabalho se houver força *e* deslocamento. O tempo gasto **não importa** para o cálculo do trabalho — importa apenas a força e o deslocamento.

$$\tau = F \cdot \Delta s \quad \text{(força constante, mesma direção do deslocamento)}$$

---

### ⚡ Potência

**Potência (P)** mede a *rapidez* com que o trabalho é realizado. Duas pessoas podem fazer o mesmo trabalho, mas quem termina em menos tempo desenvolve maior potência. A unidade é o **watt (W)** — homenagem ao engenheiro James Watt.

$$P = \frac{\tau}{\Delta t}$$

Conversão prática do cotidiano: motores de carro usam **cavalo-vapor (cv)**, onde 1 cv ≈ 735 W.

---

### 🛠️ Máquinas Simples

Máquinas simples transformam ou transmitem energia para facilitar tarefas. As principais estudadas são:

- **Alavanca:** barra que gira sobre um ponto de apoio. Três tipos conforme a posição do apoio entre as forças:
  - *Interfixa* — apoio no meio (ex.: gangorra, alicate)
  - *Inter-resistente* — resistência no meio (ex.: carrinho de mão)
  - *Interpotente* — potência no meio (ex.: vassoura, pinça)
  - Condição de equilíbrio: $$F_r \cdot b_r = F_p \cdot b_p$$

- **Roldana:** usa cabos para mudar direção da força. Combinada (fixa + móvel), reduz a força necessária à metade.

- **Engrenagem:** rodas dentadas que alteram velocidade ou direção de rotação (bicicletas, relógios, motores).

- **Plano inclinado:** superfície oblíqua que facilita elevar objetos (rampas de acessibilidade, guinchos).

---

## SEÇÃO 3 — CIENTISTAS E HISTÓRIA DA CIÊNCIA

### James Prescott Joule (1818–1889)
**Área:** Física experimental, Termodinâmica
**Contribuição no capítulo:** Determinou uma relação entre o trabalho mecânico e o calor, colaborando decisivamente para o estabelecimento da lei da conservação de energia.
**O que mudou:** Demonstrou que calor e trabalho mecânico são formas equivalentes de energia, unificando conceitos que pareciam independentes e fundando as bases da Termodinâmica moderna.
**Associado a:** Unidade de energia joule (J) — homenagem ao físico.
**Contexto histórico:** Século XIX, Revolução Industrial britânica — época de grande interesse em eficiência de máquinas a vapor e conversão de energia.

---

## SEÇÃO 4 — FÓRMULAS, LEIS E PRINCÍPIOS

### Energia Cinética

**Expressão:** $$E_C = \frac{1}{2} \cdot m \cdot v^2$$

| Símbolo | Grandeza | Unidade SI | Tipo |
|---|---|---|---|
| E_C | Energia cinética | J | derivada / escalar |
| m | Massa do objeto | kg | fundamental / escalar |
| v | Velocidade escalar | m/s | derivada / escalar |

**Válida quando:** o corpo está em movimento com velocidade escalar v.
**Caso especial:** se v = 0, então E_C = 0.
💡 **Pegadinha:** a velocidade entra ao quadrado — muitos alunos dobram v e dobram E_C, quando na verdade E_C quadruplica. Sempre elevar v ao quadrado antes de multiplicar pela massa.

---

### Energia Potencial Gravitacional

**Expressão:** $$E_G = m \cdot g \cdot h$$

| Símbolo | Grandeza | Unidade SI | Tipo |
|---|---|---|---|
| E_G | Energia potencial gravitacional | J | derivada / escalar |
| m | Massa do objeto | kg | fundamental / escalar |
| g | Aceleração gravitacional local | m/s² | derivada / escalar |
| h | Altura em relação ao chão | m | fundamental / escalar |

**Válida quando:** objeto próximo à superfície terrestre; h medida a partir da referência definida (geralmente h = 0 no ponto mais baixo).
**Caso especial:** se h = 0, então E_G = 0 — o valor depende da referência escolhida.
💡 **Pegadinha:** confundir a referência de h = 0. E_G é relativa — sempre verificar qual ponto foi definido como chão.

---

### Energia Mecânica

**Expressão:** $$E_M = E_C + E_G + E_E$$

| Símbolo | Grandeza | Unidade SI | Tipo |
|---|---|---|---|
| E_M | Energia mecânica | J | derivada / escalar |
| E_C | Energia cinética | J | derivada / escalar |
| E_G | Energia potencial gravitacional | J | derivada / escalar |
| E_E | Energia potencial elástica | J | derivada / escalar |

**Válida quando:** sistema conservativo (sem perdas por atrito ou resistência do ar).
💡 **Pegadinha:** em provas que mencionam "energia mecânica conservada", assume-se que E_E = 0 (sem mola), logo E_M = E_C + E_G — cuidado para não incluir E_E sem necessidade.

---

### Trabalho

**Expressão:** $$\tau = F \cdot \Delta s$$

| Símbolo | Grandeza | Unidade SI | Tipo |
|---|---|---|---|
| τ | Trabalho | J | derivada / escalar |
| F | Força | N | derivada / vetorial |
| Δs | Deslocamento | m | fundamental / escalar (módulo) |

**Válida quando:** força de intensidade constante com mesma direção do deslocamento.
**Caso especial:** se não há deslocamento (Δs = 0), o trabalho é zero — mesmo que a força seja enorme.
💡 **Pegadinha:** segurar um objeto parado no ar não realiza trabalho físico, mesmo exigindo esforço muscular. Trabalho em Física exige deslocamento.

---

### Potência

**Expressão:** $$P = \frac{\tau}{\Delta t}$$

| Símbolo | Grandeza | Unidade SI | Tipo |
|---|---|---|---|
| P | Potência | W | derivada / escalar |
| τ | Trabalho | J | derivada / escalar |
| Δt | Intervalo de tempo | s | fundamental / escalar |

**Válida quando:** trabalho realizado de forma uniforme no intervalo Δt.
💡 **Pegadinha:** o tempo não altera o *trabalho* — mas altera a *potência*. Fazer o mesmo trabalho em menos tempo = maior potência.

---

### Equilíbrio da Alavanca

**Expressão:** $$F_r \cdot b_r = F_p \cdot b_p$$

| Símbolo | Grandeza | Unidade SI | Tipo |
|---|---|---|---|
| Fr | Força resistente | N | derivada / escalar (módulo) |
| br | Braço da força resistente | m | fundamental / escalar |
| Fp | Força potente | N | derivada / escalar (módulo) |
| bp | Braço da força potente | m | fundamental / escalar |

**Válida quando:** alavanca em equilíbrio estático.
💡 **Pegadinha:** aumentar o braço potente (bp) *diminui* Fp — muitos alunos invertem a relação e acham que braço maior exige mais força.

---

## SEÇÃO 5 — GRANDEZAS E SISTEMA INTERNACIONAL

#### 5.1 — Grandezas do capítulo

| Grandeza | Símbolo | Unidade SI | Símbolo | Tipo |
|---|---|---|---|---|
| Energia mecânica | E_M | joule | J | derivada / escalar |
| Energia cinética | E_C | joule | J | derivada / escalar |
| Energia pot. gravitacional | E_G | joule | J | derivada / escalar |
| Energia pot. elástica | E_E | joule | J | derivada / escalar |
| Massa | m | quilograma | kg | fundamental / escalar |
| Velocidade escalar | v | metro por segundo | m/s | derivada / escalar |
| Aceleração gravitacional | g | metro por segundo ao quadrado | m/s² | derivada / escalar |
| Altura | h | metro | m | fundamental / escalar |
| Trabalho | τ | joule | J | derivada / escalar |
| Força | F | newton | N | derivada / vetorial |
| Deslocamento | Δs | metro | m | fundamental / escalar |
| Potência | P | watt | W | derivada / escalar |
| Intervalo de tempo | Δt | segundo | s | fundamental / escalar |

#### 5.2 — Conversões importantes

```
Joule (unidades fundamentais):
  1 J = 1 kg·m²/s²
  Fator: derivado de E_C = (1/2)·m·v²
  ⚠️ Pegadinha: não confundir J com N — newton é kg·m/s², não kg·m²/s²

Joule ↔ Newton·metro:
  1 J = 1 N·m
  Fator: τ = F·Δs → [N]·[m] = [J]
  ⚠️ Pegadinha: lembrar que 1 N·m (de trabalho) = 1 J,
     mas 1 N·m (de torque) NÃO é a mesma grandeza física.

Watt ↔ Joule/segundo:
  1 W = 1 J/s
  Fator: P = τ/Δt

Cavalo-vapor ↔ Watt:
  1 cv ≈ 735 W
  Exemplo: motor de 70 cv → 70 × 735 = 51.450 W
  ⚠️ Pegadinha: cv não é unidade SI — converter sempre antes de operar.

Quilotons de TNT ↔ Joules:
  16 quilotons de TNT ≈ 6,7 × 10¹³ J
  (referência: bomba Little Boy, Hiroshima, 1945)
```

#### 5.3 — Notação científica

- Regra: $$a \times 10^n$$, onde $$1 \leq |a| < 10$$ e n é inteiro
- Exemplo do capítulo: $$6{,}7 \times 10^{13} \text{ J}$$ (energia da bomba de Hiroshima)
- Erro clássico: confundir o sinal de n — $$10^{13}$$ é muito grande; $$10^{-13}$$ é minúsculo. Verificar sempre se o número original é maior ou menor que 1.

---

## SEÇÃO 6 — DADOS FACTUAIS DENSOS

| Tipo de alavanca | Posição do ponto de apoio (P) | Posição da força resistente (Fr) | Posição da força potente (Fp) | Exemplos |
|---|---|---|---|---|
| Interfixa | Entre Fr e Fp | Extremidade | Extremidade | Gangorra, alicate, tesoura |
| Inter-resistente | Extremidade | Entre P e Fp | Extremidade oposta | Carrinho de mão, abridor de garrafas |
| Interpotente | Extremidade | Extremidade oposta | Entre P e Fr | Vassoura, pinça |

| Tipo de roldana | Reduz a força? | Relação força × peso | Muda direção? |
|---|---|---|---|
| Fixa | Não | F₁ = P | Sim |
| Fixa + Móvel combinadas | Sim | F₂ = P/2 | Sim |

---

## SEÇÃO 7 — DICAS DE OURO

💡 **Dica 1 — Velocidade ao quadrado muda tudo**
A energia cinética é proporcional a v². Se a velocidade dobra, E_C quadruplica. Se triplica, E_C fica 9× maior. Nunca multiplique apenas por 2 ao dobrar v.
$$E_C = \frac{1}{2} \cdot m \cdot v^2 \Rightarrow \text{dobrar } v \Rightarrow E_C \times 4$$

💡 **Dica 2 — Trabalho zero sem deslocamento**
Segurar um objeto parado, empurrar uma parede, carregar uma mochila andando em nível constante na direção perpendicular à força — todos têm trabalho físico nulo. A definição exige força *e* deslocamento *na mesma direção*.

💡 **Dica 3 — h = 0 é uma escolha sua**
A energia potencial gravitacional depende da referência de altura. Sempre defina qual ponto é h = 0 antes de calcular. Em problemas de conservação, o que importa é a *variação* de altura, não o valor absoluto.

💡 **Dica 4 — Potência e trabalho são grandezas diferentes**
Dois motores podem realizar o mesmo trabalho — o mais potente é simplesmente o que termina mais rápido. Não confundir "maior trabalho" com "maior potência". A fórmula $$P = \tau / \Delta t$$ deixa claro que o tempo é o fator que diferencia potências iguais.

💡 **Dica 5 — Alavanca: braço maior = menos força**
Na equação $$F_r \cdot b_r = F_p \cdot b_p$$, aumentar o braço potente (bp) reduz Fp necessária. É o princípio por trás de ferramentas como chaves de roda e pedais longos de bicicleta.

💡 **Dica 6 — Conservação de energia: identifique o que é zero**
Em problemas de conservação, identifique o ponto onde E_C = 0 (repouso) e o ponto onde E_G = 0 (h = 0). Isso simplifica a equação e elimina incógnitas. No topo em repouso: E_M = E_G. Na base (h = 0): E_M = E_C.

---

## SEÇÃO 8 — ALERTAS DE INCONSISTÊNCIA

```
# GAPS — fis-1-8
# Gerado automaticamente pelo Prompt de Preparação

## INFERÊNCIAS USADAS NO PREP

| Seção | Campo | Valor inferido | Fonte da inferência |
|---|---|---|---|
| Seção 3 | Período de vida de Joule | 1818–1889 | Conhecimento histórico geral |
| Seção 3 | Contexto histórico de Joule | Revolução Industrial / Termodinâmica séc. XIX | Conhecimento histórico geral |
| Seção 4 | Tipo "vetorial" para Força (F) | vetorial | Definição física padrão — não explicitado no .md |
| QI-1 | Gabarito (não fornecido no .md) | Inferido: sim, bola de futebol causa mais estrago (E_C maior pela massa); sim, 30 m/s causa 9× mais E_C | Aplicação de E_C = (1/2)mv² |
| QI-2 | Gabarito (não fornecido no .md) | 5m: 3.000 J · 10m: 6.000 J · 20m: 12.000 J | Aplicação de E_G = m·g·h com m=60, g=10 |
| QI-3 | Gabarito (não fornecido no .md) | Fp = 20 N | Fr·br = Fp·bp → 30·0,8 = Fp·1,2 → Fp = 20 N |
| QC-1 | Gabarito PUC-RJ 2023 | e) 15 J | τ = F·Δx = 5·3 = 15 J (força orientada em x, deslocamento em x de 0 a 3) |
| QC-2 | Gabarito Uerj 2024 | a) W | Maior inclinação no gráfico E_G×h → maior g (E_G = m·g·h, m fixo) |
| QC-3 | Gabarito FMP-RJ | d) somente cinética e potencial gravitacional | Na vara: sem contato com a vara → sem E_E; v ≈ 0 horizontal mas existe → E_C residual + E_G por estar em h máxima |

## DADOS AUSENTES — AÇÃO NECESSÁRIA

| Seção | Campo | Motivo da ausência | Ação recomendada |
|---|---|---|---|
| Bloco B | Unidade SI de Fr, br, Fp, bp na fórmula de alavanca | Não capturado no .md | Adicionar: Fr e Fp em N; br e bp em m |
| Seção Atividades Q-1 | Gabarito oficial | Não fornecido no livro capturado | Confirmar com gabarito do professor: A e B têm trabalho (queda com força gravitacional + deslocamento; empurrar com deslocamento); C não tem (sem deslocamento das sacolas) |
```

⚠️ **ALERTA — QC-3 (FMP-RJ) — Velocidade "da ordem de 1 cm/s"**
- Dado no material: "ultrapassou o sarrafo com uma velocidade horizontal da ordem de 1 cm/s"
- Observação: a velocidade de 1 cm/s é extremamente pequena mas não nula, portanto existe E_C residual mínima. O gabarito mais defensável é **(d) somente cinética e potencial gravitacional**, pois o atleta já perdeu contato com a vara (E_E = 0) e ainda tem v ≠ 0. Verificar com gabarito oficial da banca antes de apresentar ao aluno.

---

## SEÇÃO 9 — SÍNTESE DO CAPÍTULO (para warm-up)

#### Bloco 1 — Conceitos e Definições

- **Energia**
  - Definição: `______` (*capacidade de realizar trabalho*)
  - Exemplo: `______` (*gasolina movendo um carro; vento girando aerogerador*)

- **Energia cinética**
  - Definição: `______` (*energia associada ao movimento de um corpo*)
  - Exemplo: `______` (*bola em movimento, carro em velocidade*)

- **Energia potencial gravitacional**
  - Definição: `______` (*energia armazenada devido à posição do corpo em um campo gravitacional*)
  - Exemplo: `______` (*bloco suspenso, atleta em plataforma de salto*)

- **Trabalho**
  - Definição: `______` (*quantidade de energia transferida por uma força que provoca deslocamento*)
  - Exemplo: `______` (*empurrar uma geladeira que se desloca 1,5 m*)

- **Potência**
  - Definição: `______` (*rapidez com que o trabalho é realizado*)
  - Exemplo: `______` (*motor de 70 cv = 51.450 W*)

- **Alavanca interfixa**
  - Definição: `______` (*ponto de apoio localizado entre as forças resistente e potente*)
  - Exemplo: `______` (*gangorra, alicate*)

- **Alavanca inter-resistente**
  - Definição: `______` (*força resistente entre o ponto de apoio e a força potente*)
  - Exemplo: `______` (*carrinho de mão*)

- **Alavanca interpotente**
  - Definição: `______` (*força potente entre o ponto de apoio e a força resistente*)
  - Exemplo: `______` (*vassoura, pinça*)

---

#### Bloco 2 — Fórmulas

- **Energia cinética**
  - Expressão: `______` ($$E_C = \frac{1}{2} \cdot m \cdot v^2$$)
  - v representa: `______` (*velocidade escalar do objeto, em m/s*)

- **Energia potencial gravitacional**
  - Expressão: `______` ($$E_G = m \cdot g \cdot h$$)
  - h representa: `______` (*altura em relação ao ponto de referência, em m*)

- **Trabalho**
  - Expressão: `______` ($$\tau = F \cdot \Delta s$$)
  - τ representa: `______` (*trabalho, em joules*)

- **Potência**
  - Expressão: `______` ($$P = \tau / \Delta t$$)
  - Δt representa: `______` (*intervalo de tempo, em segundos*)

- **Equilíbrio de alavanca**
  - Expressão: `______` ($$F_r \cdot b_r = F_p \cdot b_p$$)
  - bp representa: `______` (*braço da força potente, em m*)

---

#### Bloco 3 — Lacunas para Warm-Up

1. A energia é definida em Física como a capacidade de realizar `______`.
*(resposta: trabalho)*

2. A unidade de energia no SI é o `______`, equivalente a 1 kg·m²/s².
*(resposta: joule — J)*

3. Se a velocidade de um corpo triplica, sua energia cinética fica `______` vezes maior.
*(resposta: 9 vezes — porque v entra ao quadrado)*

4. A energia potencial gravitacional de um corpo depende de sua `______` em relação a um ponto de referência.
*(resposta: altura — h)*

5. Em uma alavanca, quanto maior o braço potente (bp), `______` será a força potente necessária para o equilíbrio.
*(resposta: menor)*

6. A grandeza que mede a rapidez com que o trabalho é realizado chama-se `______`, e sua unidade no SI é o `______`.
*(resposta: potência; watt — W)*

7. Para haver trabalho em Física, são necessários obrigatoriamente dois elementos: `______` e `______`.
*(resposta: força; deslocamento)*

8. Na conservação de energia mecânica, quando um esquiador atinge o ponto mais baixo da pista (h = 0), toda a energia potencial gravitacional se transforma em energia `______`.
*(resposta: cinética)*

---

#### Bloco 4 — Tabela Síntese

| Conceito | Lacuna — resposta esperada |
|---|---|
| Definição de energia | `______` → *capacidade de realizar trabalho* |
| Fórmula da energia cinética | `______` → *E_C = (1/2)·m·v²* |
| Fórmula da energia potencial gravitacional | `______` → *E_G = m·g·h* |
| Fórmula do trabalho | `______` → *τ = F·Δs* |
| Fórmula da potência | `______` → *P = τ/Δt* |
| Condição de equilíbrio da alavanca | `______` → *Fr·br = Fp·bp* |
| Efeito de dobrar a velocidade sobre E_C | `______` → *E_C quadruplica* |
| Aplicação prática: roldana fixa + móvel | `______` → *reduz a força necessária à metade: F = P/2* |
| Pegadinha: trabalho sem deslocamento | `______` → *trabalho = zero (τ = F·0 = 0)* |
| Unidade de potência e equivalência | `______` → *watt (W); 1 cv ≈ 735 W* |

---

## SEÇÃO 10 — SÍNTESE DO LIVRO

### Síntese do Livro — ENERGIA E TRABALHO

| Nó / Posição | Já dado | Lacuna — resposta esperada |
|---|---|---|
| Nó central | **Energia** | — (dado) |
| Ramo superior esquerdo | **Energia cinética** — "Energia que o corpo tem devido ao seu movimento" | Fórmula: `______` → *E_C = (1/2)·m·v²* |
| Ramo superior direito | **Energia potencial** | Definição: `______` → *Energia armazenada capaz de realizar trabalho* |
| Ramo intermediário esquerdo | **Energia potencial gravitacional** | Fórmula: `______` → *E_G = m·g·h* |
| Ramo intermediário direito | **Energia mecânica** — "Energia do movimento" | Fórmula: `______` → *E_M = E_C + E_Pot* |
| Nó central inferior 1 | **Conservação de energia mecânica** | Definição: `______` → *A soma das energias cinética e potencial será igual para qualquer instante* |
| Nó central inferior 2 | **Trabalho** | Unidade: `______` → *joule (J)*; Fórmula: `______` → *τ = F·Δs* |
| Texto abaixo de Trabalho | "Quando uma forma de energia é alterada devido a uma força que age sobre um corpo que é deslocado" | — (dado) |
| Nó base | **Máquinas simples** | Função: `______` → *facilitam a execução de tarefas, promovendo conforto ou reduzindo o esforço* |
| Ramo base esquerdo | **Alavanca — Interfixa** | Definição: `______` → *Ponto de apoio entre os pontos nos quais são aplicadas as forças resistente e potente* |
| Ramo base central | **Alavanca — Inter-resistente** | Definição: `______` → *A parte na qual é aplicada a força resistente fica entre o ponto de apoio e o ponto no qual é aplicada a força potente* |
| Ramo base direito | **Alavanca — Interpotente** | Definição: `______` → *A parte na qual é aplicada a força potente fica entre o ponto de apoio e o ponto no qual é aplicada a força resistente* |

---

## SEÇÃO 11 — QUESTÕES DE REFERÊNCIA

#### Bloco A — Catálogo das questões

| # | Enunciado resumido | Tipo | Dif. | Origem | Gabarito inferido | Obs. |
|---|---|---|---|---|---|---|
| QI-1a | Bola de futebol (0,50 kg) vs. pingue-pongue (0,02 kg) a 10 m/s — mais estrago? | Calc | F | IC | Sim: E_C(fut)=12,5 J >> E_C(ping)=1 J | — |
| QI-1b | Pingue-pongue a 30 m/s vs. 10 m/s — mais estrago? | Calc | F | IC | Sim: E_C(30)=9 J >> E_C(10)=1 J; 9× maior | — |
| QI-2 | E_G atleta 60 kg nas plataformas 5 m, 10 m, 20 m | Calc | F | IC | 3.000 J / 6.000 J / 12.000 J | — |
| QI-3 | Fp em alavanca: Fr=30N, br=0,8m, bp=1,2m | Calc | F | IC | Fp = 20 N | — |
| Q-1 | Identificar situações com trabalho (queda, carrinho, sacolas paradas) | Dis | F | AT | A e B têm trabalho; C não tem | ⚠️ gabarito não fornecido |
| Q-2 | τ: F=40N, Δs=1,5m | Calc | F | AT | τ = 60 J | — |
| QC-1 | Trabalho de F=5N (eixo x) sobre partícula de x=0 a x=3 | MC | D | AT | e) 15 J | — |
| QC-2 | Gráfico E_G × h — planeta com maior g | MC | M | AT | a) W | — |
| Q-3 | P: F=50N, Δs=2m, Δt=4s | Calc | F | AT | τ=100J; P=25W | — |
| Q-4 | 70 cv em watts | Calc | F | AT | 51.450 W | — |
| Q-5 | E_G: m=50kg, h=8m, g=10 | Calc | F | AT | 4.000 J | — |
| Q-6a | E_G: m=50kg, h=20m, g=10 | Calc | M | AT | 10.000 J | — |
| Q-6b | v no ponto 2 por conservação (E_M=10.000J, h=0) | Calc | M | AT | v = 20 m/s | — |
| Q-7 | E_G sistema 300 kg nos pontos A(12m), B(0m), C(4m) | Calc | M | AT | A:36.000J / B:0J / C:12.000J | — |
| Q-8a | Fp: m=52kg, br=2,5m, bp=1,0m | Calc | M | AT | Fr=520N; Fp=1.300N | — |
| Q-8b | Fp com br=1m, bp=2,5m — maior ou menor? | Calc | M | AT | Fp=208N — menor | — |
| QC-3 | Energia do saltador com vara no ponto mais alto | MC | M | AT | d) cinética e potencial gravitacional | ⚠️ ver Seção 8 |

---

#### Bloco B — Questões modelo originais

---

**QM-1** · múltipla escolha · médio · inspirada em: QI-1

Um ciclista de 80 kg pedala a 5 m/s. Ao descer uma rampa sem pedalar, sua velocidade aumenta para 10 m/s. Qual é a razão entre a energia cinética final e a energia cinética inicial do ciclista?

a) 2  
b) 4  
c) 8  
d) 16

✅ **Gabarito:** b) 4
📝 **Resolução:** $$\frac{E_{C_f}}{E_{C_i}} = \frac{v_f^2}{v_i^2} = \frac{10^2}{5^2} = \frac{100}{25} = 4$$. A massa cancela. A velocidade dobrou, logo E_C quadruplicou.
⚠️ **Professor:** referência de estilo — crie variações originais, nunca reproduza diretamente.

---

**QM-2** · múltipla escolha · médio · inspirada em: Q-3

Dois operários empurram uma mesma caixa com a mesma força de 60 N por 4 m. O operário A leva 10 s; o operário B leva 20 s. Qual afirmativa é CORRETA?

a) A realizou maior trabalho e maior potência que B.
b) A e B realizaram o mesmo trabalho, mas A desenvolveu maior potência.
c) B realizou maior trabalho porque levou mais tempo.
d) A e B desenvolveram a mesma potência porque a força foi igual.

✅ **Gabarito:** b)
📝 **Resolução:** τ = 60 × 4 = 240 J (igual para ambos). P_A = 240/10 = 24 W; P_B = 240/20 = 12 W. O tempo não altera o trabalho, mas diferencia as potências.
⚠️ **Professor:** referência de estilo — crie variações originais, nunca reproduza diretamente.

---

**QM-3** · dissertativa · médio · inspirada em: Q-1

Um estudante afirma: *"Quando seguro minha mochila de 5 kg parado na fila do banco, estou realizando um trabalho físico enorme, pois meus músculos estão se esforçando muito."*
Explique, com base no conceito científico de trabalho, se a afirmativa está correta, apresentando a expressão matemática adequada.

✅ **Gabarito:**
📝 **Resolução:** A afirmativa está incorreta. Trabalho em Física exige força *e* deslocamento: $$\tau = F \cdot \Delta s$$. Como Δs = 0 (mochila parada), τ = F × 0 = 0 J. O esforço muscular é real, mas não configura trabalho no sentido físico.
⚠️ **Professor:** referência de estilo — crie variações originais, nunca reproduza diretamente.

---

**QM-4** · múltipla escolha estilo concurso · difícil · inspirada em: QC-2

Um objeto de massa m é levado a diferentes alturas em quatro planetas (I, II, III, IV) com acelerações gravitacionais $$g_I > g_{II} > g_{III} > g_{IV}$$. Um gráfico mostra a energia potencial gravitacional em função da massa (E_G × m) para h = 10 m constante em cada planeta. A reta de maior coeficiente angular corresponde ao planeta com:

a) menor aceleração gravitacional, pois o eixo x representa a massa.
b) maior aceleração gravitacional, pois E_G = m·g·h e o coeficiente angular é g·h.
c) maior massa do objeto, independente de g.
d) menor altura, pois h determina a inclinação da reta.
e) aceleração gravitacional igual à terrestre, pois g é constante.

✅ **Gabarito:** b)
📝 **Resolução:** Com h = 10 m fixo, $$E_G = m \cdot g \cdot h = m \cdot (g \cdot 10)$$. O gráfico E_G × m é uma reta de coeficiente angular igual a $$g \times 10$$. Maior inclinação → maior g → planeta I.
⚠️ **Professor:** referência de estilo — crie variações originais, nunca reproduza diretamente.

---

**QM-5** · cálculo/aplicação · médio-difícil · inspirada em: Q-6 e Q-8

Uma pedra de 2 kg é solta do repouso de uma altura de 45 m. Considere g = 10 m/s² e energia mecânica conservada.

a) Qual é a energia potencial gravitacional da pedra no ponto de lançamento?
b) Qual é a velocidade da pedra imediatamente antes de atingir o solo?
c) A que altura a energia cinética da pedra é igual à metade da energia mecânica total?

✅ **Gabarito:**
📝 **Resolução:**

a) $$E_G = m \cdot g \cdot h = 2 \cdot 10 \cdot 45 = 900 \text{ J}$$

b) No solo h = 0, logo E_M = E_C:
$$900 = \frac{1}{2} \cdot 2 \cdot v^2 \Rightarrow v^2 = 900 \Rightarrow v = 30 \text{ m/s}$$

c) $$E_C = \frac{E_M}{2} = 450 \text{ J} \Rightarrow E_G = 450 \text{ J} \Rightarrow h = \frac{450}{2 \cdot 10} = 22{,}5 \text{ m}$$

⚠️ **Professor:** referência de estilo — crie variações originais, nunca reproduza diretamente.

---

## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO

### DIAGRAMA: hierarquia_energia
Hierarquia dos tipos de energia mecânica com fórmulas principais.

```svg
<svg width="100%" viewBox="0 0 680 420">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- NÍVEL 0: Energia Mecânica -->
<rect x="240" y="20" width="200" height="48" rx="8" class="c-purple"/>
<text x="340" y="40" text-anchor="middle" class="th" dominant-baseline="central">Energia Mecânica</text>
<text x="340" y="58" text-anchor="middle" class="ts" dominant-baseline="central">E_M = E_C + E_G + E_E</text>

<!-- Seta para E_C -->
<line x1="270" y1="68" x2="130" y2="138"
  stroke="#a78bfa" stroke-width="2" marker-end="url(#arrow)"/>

<!-- Seta para E_Pot -->
<line x1="410" y1="68" x2="550" y2="138"
  stroke="#a78bfa" stroke-width="2" marker-end="url(#arrow)"/>

<!-- NÍVEL 1 esquerdo: Energia Cinética -->
<rect x="40" y="138" width="180" height="58" rx="8" class="c-teal"/>
<text x="130" y="157" text-anchor="middle" class="th" dominant-baseline="central">Energia Cinética</text>
<text x="130" y="178" text-anchor="middle" class="ts" dominant-baseline="central">E_C = ½ · m · v²</text>

<!-- NÍVEL 1 direito: Energia Potencial -->
<rect x="460" y="138" width="180" height="58" rx="8" class="c-teal"/>
<text x="550" y="157" text-anchor="middle" class="th" dominant-baseline="central">Energia Potencial</text>
<text x="550" y="178" text-anchor="middle" class="ts" dominant-baseline="central">armazenada no sistema</text>

<!-- Seta E_Pot → E_G -->
<line x1="510" y1="196" x2="390" y2="266"
  stroke="#5eead4" stroke-width="2" marker-end="url(#arrow)"/>

<!-- Seta E_Pot → E_E -->
<line x1="590" y1="196" x2="590" y2="266"
  stroke="#5eead4" stroke-width="2" marker-end="url(#arrow)"/>

<!-- NÍVEL 2 centro: E_G -->
<rect x="270" y="266" width="200" height="58" rx="8" class="c-amber"/>
<text x="370" y="284" text-anchor="middle" class="th" dominant-baseline="central">Pot. Gravitacional</text>
<text x="370" y="305" text-anchor="middle" class="ts" dominant-baseline="central">E_G = m · g · h</text>

<!-- NÍVEL 2 direito: E_E -->
<rect x="490" y="266" width="160" height="58" rx="8" class="c-amber"/>
<text x="570" y="284" text-anchor="middle" class="th" dominant-baseline="central">Pot. Elástica</text>
<text x="570" y="305" text-anchor="middle" class="ts" dominant-baseline="central">E_E (mola/elástico)</text>

<!-- Pegadinha -->
<rect x="40" y="230" width="180" height="58" rx="8" class="c-coral"/>
<text x="130" y="252" text-anchor="middle" class="ts" dominant-baseline="central">⚠ Dobrar v →</text>
<text x="130" y="272" text-anchor="middle" class="ts" dominant-baseline="central">E_C quadruplica (v²)</text>

<!-- Seta de observação -->
<line x1="130" y1="228" x2="130" y2="197"
  stroke="#f87171" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#arrow)"/>

<!-- Conservação -->
<rect x="180" y="352" width="320" height="48" rx="8" class="c-gray"/>
<text x="340" y="370" text-anchor="middle" class="th" dominant-baseline="central">Conservação de E_M</text>
<text x="340" y="388" text-anchor="middle" class="ts" dominant-baseline="central">E_C + E_G + E_E = constante</text>

<!-- Seta para conservação -->
<line x1="340" y1="324" x2="340" y2="352"
  stroke="#94a3b8" stroke-width="1.5" marker-end="url(#arrow)"/>
</svg>
```

---

### DIAGRAMA: formulas
Painel de fórmulas do capítulo com variáveis e pegadinhas.

```svg
<svg width="100%" viewBox="0 0 680 500">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Título -->
<text x="340" y="28" text-anchor="middle" class="th" dominant-baseline="central">FÓRMULAS DO CAPÍTULO</text>

<!-- F1: Energia Cinética -->
<rect x="40" y="50" width="140" height="44" rx="6" class="c-purple"/>
<text x="110" y="72" text-anchor="middle" class="th" dominant-baseline="central">Energia Cinética</text>

<rect x="196" y="50" width="180" height="44" rx="6" class="c-teal"/>
<text x="286" y="72" text-anchor="middle" class="t" dominant-baseline="central">E_C = ½ · m · v²</text>

<text x="400" y="58" text-anchor="start" class="ts" dominant-baseline="central">m: massa (kg)</text>
<text x="400" y="76" text-anchor="start" class="ts" dominant-baseline="central">v: velocidade (m/s) · E_C: joule</text>

<rect x="40" y="102" width="336" height="36" rx="6" class="c-coral"/>
<text x="208" y="120" text-anchor="middle" class="ts" dominant-baseline="central">⚠ Dobrar v → E_C × 4 (não × 2)</text>

<!-- F2: Energia Pot. Gravitacional -->
<rect x="40" y="152" width="140" height="44" rx="6" class="c-purple"/>
<text x="110" y="167" text-anchor="middle" class="ts" dominant-baseline="central">Energia Pot.</text>
<text x="110" y="185" text-anchor="middle" class="ts" dominant-baseline="central">Gravitacional</text>

<rect x="196" y="152" width="180" height="44" rx="6" class="c-teal"/>
<text x="286" y="174" text-anchor="middle" class="t" dominant-baseline="central">E_G = m · g · h</text>

<text x="400" y="160" text-anchor="start" class="ts" dominant-baseline="central">g: acel. grav. (m/s²)</text>
<text x="400" y="178" text-anchor="start" class="ts" dominant-baseline="central">h: altura (m) · E_G: joule</text>

<rect x="40" y="204" width="336" height="36" rx="6" class="c-coral"/>
<text x="208" y="222" text-anchor="middle" class="ts" dominant-baseline="central">⚠ h = 0 depende da referência escolhida</text>

<!-- F3: Trabalho -->
<rect x="40" y="254" width="140" height="44" rx="6" class="c-purple"/>
<text x="110" y="276" text-anchor="middle" class="th" dominant-baseline="central">Trabalho</text>

<rect x="196" y="254" width="180" height="44" rx="6" class="c-teal"/>
<text x="286" y="276" text-anchor="middle" class="t" dominant-baseline="central">τ = F · Δs</text>

<text x="400" y="262" text-anchor="start" class="ts" dominant-baseline="central">F: força (N)</text>
<text x="400" y="280" text-anchor="start" class="ts" dominant-baseline="central">Δs: deslocamento (m) · τ: joule</text>

<rect x="40" y="306" width="336" height="36" rx="6" class="c-coral"/>
<text x="208" y="324" text-anchor="middle" class="ts" dominant-baseline="central">⚠ Sem deslocamento → τ = 0, mesmo com força</text>

<!-- F4: Potência -->
<rect x="40" y="356" width="140" height="44" rx="6" class="c-purple"/>
<text x="110" y="378" text-anchor="middle" class="th" dominant-baseline="central">Potência</text>

<rect x="196" y="356" width="180" height="44" rx="6" class="c-teal"/>
<text x="286" y="378" text-anchor="middle" class="t" dominant-baseline="central">P = τ / Δt</text>

<text x="400" y="364" text-anchor="start" class="ts" dominant-baseline="central">τ: trabalho (J)</text>
<text x="400" y="382" text-anchor="start" class="ts" dominant-baseline="central">Δt: tempo (s) · P: watt (W)</text>

<!-- F5: Alavanca -->
<rect x="40" y="416" width="140" height="44" rx="6" class="c-purple"/>
<text x="110" y="431" text-anchor="middle" class="ts" dominant-baseline="central">Equilíbrio</text>
<text x="110" y="449" text-anchor="middle" class="ts" dominant-baseline="central">Alavanca</text>

<rect x="196" y="416" width="180" height="44" rx="6" class="c-teal"/>
<text x="286" y="438" text-anchor="middle" class="t" dominant-baseline="central">Fr·br = Fp·bp</text>

<text x="400" y="424" text-anchor="start" class="ts" dominant-baseline="central">br/bp: braços (m)</text>
<text x="400" y="442" text-anchor="start" class="ts" dominant-baseline="central">Fr/Fp: forças (N)</text>
</svg>
```

---

### DIAGRAMA: tipos_alavanca
Classificação visual dos três tipos de alavanca com exemplos e posição dos elementos.

```svg
<svg width="100%" viewBox="0 0 680 360">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Título -->
<text x="340" y="24" text-anchor="middle" class="th" dominant-baseline="central">TIPOS DE ALAVANCA</text>

<!-- ===== INTERFIXA ===== -->
<rect x="40" y="50" width="180" height="44" rx="6" class="c-purple"/>
<text x="130" y="72" text-anchor="middle" class="th" dominant-baseline="central">INTERFIXA</text>

<!-- Barra -->
<line x1="60" y1="128" x2="200" y2="128" stroke="#a78bfa" stroke-width="4"/>
<!-- P centro -->
<polygon points="130,128 118,150 142,150" class="c-purple"/>
<text x="130" y="162" text-anchor="middle" class="ts" dominant-baseline="central">P</text>
<!-- Fr esquerda -->
<line x1="75" y1="128" x2="75" y2="100" stroke="#5eead4" stroke-width="2" marker-end="url(#arrow)"/>
<text x="75" y="96" text-anchor="middle" class="ts" dominant-baseline="central">Fr</text>
<!-- Fp direita -->
<line x1="185" y1="128" x2="185" y2="100" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow)"/>
<text x="185" y="96" text-anchor="middle" class="ts" dominant-baseline="central">Fp</text>

<rect x="40" y="172" width="180" height="44" rx="6" class="c-gray"/>
<text x="130" y="190" text-anchor="middle" class="ts" dominant-baseline="central">Ex.: gangorra,</text>
<text x="130" y="208" text-anchor="middle" class="ts" dominant-baseline="central">alicate, tesoura</text>

<!-- ===== INTER-RESISTENTE ===== -->
<rect x="250" y="50" width="180" height="44" rx="6" class="c-teal"/>
<text x="340" y="64" text-anchor="middle" class="ts" dominant-baseline="central">INTER-</text>
<text x="340" y="82" text-anchor="middle" class="ts" dominant-baseline="central">RESISTENTE</text>

<!-- Barra -->
<line x1="270" y1="128" x2="410" y2="128" stroke="#5eead4" stroke-width="4"/>
<!-- P esquerda -->
<polygon points="275,128 263,150 287,150" class="c-teal"/>
<text x="275" y="162" text-anchor="middle" class="ts" dominant-baseline="central">P</text>
<!-- Fr centro -->
<line x1="340" y1="128" x2="340" y2="100" stroke="#5eead4" stroke-width="2" marker-end="url(#arrow)"/>
<text x="340" y="96" text-anchor="middle" class="ts" dominant-baseline="central">Fr</text>
<!-- Fp direita -->
<line x1="395" y1="128" x2="395" y2="100" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow)"/>
<text x="395" y="96" text-anchor="middle" class="ts" dominant-baseline="central">Fp</text>

<rect x="250" y="172" width="180" height="44" rx="6" class="c-gray"/>
<text x="340" y="190" text-anchor="middle" class="ts" dominant-baseline="central">Ex.: carrinho de mão,</text>
<text x="340" y="208" text-anchor="middle" class="ts" dominant-baseline="central">abridor de garrafas</text>

<!-- ===== INTERPOTENTE ===== -->
<rect x="460" y="50" width="180" height="44" rx="6" class="c-amber"/>
<text x="550" y="64" text-anchor="middle" class="ts" dominant-baseline="central">INTER-</text>
<text x="550" y="82" text-anchor="middle" class="ts" dominant-baseline="central">POTENTE</text>

<!-- Barra -->
<line x1="480" y1="128" x2="620" y2="128" stroke="#fbbf24" stroke-width="4"/>
<!-- P esquerda -->
<polygon points="485,128 473,150 497,150" class="c-amber"/>
<text x="485" y="162" text-anchor="middle" class="ts" dominant-baseline="central">P</text>
<!-- Fp centro -->
<line x1="550" y1="128" x2="550" y2="100" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow)"/>
<text x="550" y="96" text-anchor="middle" class="ts" dominant-baseline="central">Fp</text>
<!-- Fr direita -->
<line x1="605" y1="128" x2="605" y2="100" stroke="#5eead4" stroke-width="2" marker-end="url(#arrow)"/>
<text x="605" y="96" text-anchor="middle" class="ts" dominant-baseline="central">Fr</text>

<rect x="460" y="172" width="180" height="44" rx="6" class="c-gray"/>
<text x="550" y="190" text-anchor="middle" class="ts" dominant-baseline="central">Ex.: vassoura,</text>
<text x="550" y="208" text-anchor="middle" class="ts" dominant-baseline="central">pinça</text>

<!-- Equilíbrio -->
<rect x="180" y="242" width="320" height="44" rx="8" class="c-coral"/>
<text x="340" y="258" text-anchor="middle" class="th" dominant-baseline="central">Condição de equilíbrio</text>
<text x="340" y="276" text-anchor="middle" class="t" dominant-baseline="central">Fr · br = Fp · bp</text>

<!-- Dica -->
<rect x="100" y="302" width="480" height="44" rx="6" class="c-gray"/>
<text x="340" y="320" text-anchor="middle" class="ts" dominant-baseline="central">⚠ Maior bp → menor Fp necessária para o equilíbrio</text>
<text x="340" y="338" text-anchor="middle" class="ts" dominant-baseline="central">Princípio de todas as alavancas</text>
</svg>
```

---

### DIAGRAMA: conservacao_energia
Transformação de energia ao longo da trajetória de um esquiador (E_C ↔ E_G).

```svg
<svg width="100%" viewBox="0 0 680 340">
<defs>
  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
    markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke"
      stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>

<!-- Título -->
<text x="340" y="22" text-anchor="middle" class="th" dominant-baseline="central">CONSERVAÇÃO DE ENERGIA MECÂNICA</text>

<!-- Perfil de montanha simplificado -->
<polyline points="60,240 200,100 400,240 580,120"
  fill="none" stroke="#94a3b8" stroke-width="3"/>

<!-- Linha h=0 -->
<line x1="40" y1="240" x2="640" y2="240"
  stroke="#94a3b8" stroke-width="1" stroke-dasharray="6,4"/>
<text x="644" y="244" class="ts" dominant-baseline="central">h=0</text>

<!-- PONTO A -->
<circle cx="200" cy="100" r="7" class="c-purple"/>
<text x="200" y="82" text-anchor="middle" class="th" dominant-baseline="central">A</text>
<rect x="105" y="48" width="190" height="44" rx="6" class="c-purple"/>
<text x="200" y="63" text-anchor="middle" class="ts" dominant-baseline="central">E_M = E_G (repouso)</text>
<text x="200" y="81" text-anchor="middle" class="ts" dominant-baseline="central">E_C = 0 · E_G = máx</text>

<!-- PONTO B (meio da descida) -->
<circle cx="300" cy="170" r="7" class="c-teal"/>
<text x="300" y="156" text-anchor="middle" class="th" dominant-baseline="central">B</text>
<rect x="205" y="118" width="190" height="44" rx="6" class="c-teal"/>
<text x="300" y="133" text-anchor="middle" class="ts" dominant-baseline="central">E_M = E_C + E_G</text>
<text x="300" y="151" text-anchor="middle" class="ts" dominant-baseline="central">ambas presentes</text>

<!-- PONTO C -->
<circle cx="400" cy="240" r="7" class="c-amber"/>
<text x="400" y="258" text-anchor="middle" class="th" dominant-baseline="central">C</text>
<rect x="305" y="262" width="190" height="44" rx="6" class="c-amber"/>
<text x="400" y="277" text-anchor="middle" class="ts" dominant-baseline="central">E_M = E_C (h=0)</text>
<text x="400" y="295" text-anchor="middle" class="ts" dominant-baseline="central">E_G = 0 · v = máx</text>

<!-- PONTO D -->
<circle cx="580" cy="120" r="7" class="c-purple"/>
<text x="580" y="104" text-anchor="middle" class="th" dominant-baseline="central">D</text>
<rect x="490" y="68" width="170" height="44" rx="6" class="c-purple"/>
<text x="575" y="83" text-anchor="middle" class="ts" dominant-baseline="central">E_M = E_G</text>
<text x="575" y="101" text-anchor="middle" class="ts" dominant-baseline="central">repouso novamente</text>

<!-- E_M constante -->
<rect x="180" y="308" width="320" height="24" rx="6" class="c-gray"/>
<text x="340" y="320" text-anchor="middle" class="ts" dominant-baseline="central">E_M total = constante em todos os pontos</text>
</svg>
```