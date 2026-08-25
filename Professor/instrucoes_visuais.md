# INSTRUÇÕES VISUAIS — Sistema Professor Master
# Versão 1.3 | 9º ano | Escola particular — Rio de Janeiro
# Aplicável a: Prompt_Professor_Master, Prompt_Professor_Simulado_Edros,
#              Prompt_Professor_[Matéria] (todos os prompts específicos)
# Patch 1.1: fecha lacuna de QA — gráfico/diagrama mencionado no texto
#            sem SVG catalogado no prep (Seção 11 nova)
# Patch 1.2: fecha lacuna simétrica em image_search — sem catálogo prévio
#            no prep (diferente dos SVGs), a regra dependia só de
#            percepção espontânea durante a narração (Seção 9.1 nova)
# Patch 1.3: QA real (Marcela, fis-2-2) — cientista citado só em prosa
#            corrida (sem bloco dedicado na Seção 3) não foi detectado;
#            9.1 agora cobre explicitamente esse caso (item 3)

---

## 1. PRINCÍPIO GERAL

Estas regras se aplicam a **todos os SVGs e visualizações** gerados
em qualquer etapa de qualquer prompt do sistema Professor Master:
resumos, warm-ups, testes progressivos, testes finais, simulados
Edros e revisões.

---

## 2. CONTRASTE DE TEXTO — REGRA OBRIGATÓRIA

| Cor de fundo do elemento | Cor do texto |
|---|---|
| Fundo **escuro** (fills escuros, ex: `c-purple`, `c-teal`, `c-blue`, `c-coral`, `c-red`, `c-green` no stop 600–900) | Texto **branco** (`fill="white"` ou `#ffffff`) |
| Fundo **claro** (fills claros, ex: stop 50–200, `#E6F1FB`, `#f1f5f9`, cinzas claros) | Texto **preto/escuro** (`fill="#042C53"`, `fill="#0C447C"` ou similar do mesmo ramp 800–900) |
| Fundo **transparente** (sem fill, sobre o background da página) | Usar `class="t"`, `class="th"` ou `class="ts"` — herdam a cor do tema automaticamente |

**Regra de ouro:** antes de finalizar qualquer SVG, verificar mentalmente:
*"Se o fundo fosse preto, este texto ainda seria legível?"*
*"Se o fundo fosse branco, este texto ainda seria legível?"*

---

## 3. ENTREGA DE SVGs — VISUALIZER OBRIGATÓRIO

- Todo SVG deve ser passado ao **Visualizer** (`visualize:show_widget`) para renderizar inline.
- **NUNCA** colocar código SVG diretamente no markdown — não renderiza no chat.
- O SVG aparece **antes** do enunciado ou do texto explicativo correspondente.
- Um SVG por chamada ao Visualizer — nunca empilhar dois SVGs na mesma chamada.

---

## 4. ESPECIFICAÇÕES TÉCNICAS DO SVG

```
width="100%"
viewBox="0 0 680 H"   ← H = altura real do conteúdo + 40px de margem
```

- ViewBox **sempre** com largura 680 — nunca reduzir.
- Conteúdo seguro: x=40 a x=640, y=40 a y=(H−40).
- Fundo transparente — nunca adicionar `<rect>` de fundo na raiz.
- Sem texto rotacionado.
- Sem emojis dentro do SVG.
- `fill="none"` obrigatório em todo `<path>` ou `<polyline>` usado como linha/conector.

---

## 5. CONVENÇÕES GEOMÉTRICAS (Matemática e Física)

| Elemento | Representação |
|---|---|
| Ângulo reto | Quadradinho no vértice (`<rect>` pequeno) |
| Lados iguais | Traços perpendiculares sobre o lado |
| Ângulo genérico | Arco com valor em graus |
| Retas paralelas | Setas no mesmo sentido sobre as retas |
| Medidas | Sempre anotadas na figura, próximas ao elemento |

---

## 6. PALETA DE CORES — SVGs GERADOS MANUALMENTE

Para SVGs gerados do zero (não provenientes do prep), usar:

| Papel | Cor |
|---|---|
| Roxo (destaque principal) | `#6c63ff` |
| Laranja (destaque secundário) | `#e67e22` |
| Verde (positivo / correto) | `#27ae60` |
| Cinza (neutro / estrutural) | `#7f8c8d` |
| Vermelho (alerta / erro) | `#c0392b` |
| Azul (informativo) | `#185FA5` |

Alternativa: usar as classes de ramp do Visualizer (`c-purple`, `c-teal`,
`c-blue`, `c-coral`, `c-amber`, `c-gray`) que gerenciam light/dark
automaticamente — preferir quando disponíveis.

---

## 7. QUANDO GERAR SVG POR MATÉRIA

### Matemática e Física — SVG obrigatório quando a questão/aula envolver:
- Figura geométrica (triângulo, círculo, polígono, sólido)
- Reta numérica com pontos ou intervalos
- Gráfico (função, dados, velocidade × tempo)
- Diagrama de forças ou vetores
- Qualquer representação visual mencionada no enunciado

### Química e Biologia — SVG para:
- Ciclos (ciclo do carbono, ciclo celular, cadeia alimentar)
- Esquemas de reação com reagentes e produtos
- Diagramas de estrutura (célula, molécula, cadeia)

### Geografia — SVG para:
- Mapas esquemáticos de distribuição espacial, regiões ou fluxos
- **Nunca** reproduzir mapas reais com fronteiras detalhadas

### História e Artes — SVG não obrigatório.

### Simulado Edros — SVG obrigatório em questões de Matemática e Física
que envolvam qualquer elemento geométrico ou visual descrito no enunciado.

---

## 8. TABELAS MARKDOWN

- Tabelas do conteúdo (comparativos, classificações, fórmulas) → **sempre markdown**, nunca converter para SVG.
- Nunca usar o Visualizer para exibir tabelas de conteúdo.

---

## 9. IMAGE_SEARCH

- Usar para conceitos visuais do mundo real sem diagrama no prep.
- **Máximo 1 imagem por conceito.**
- Apresentar **antes** do texto explicativo correspondente.
- Casos obrigatórios por matéria definidos nos prompts específicos
  (ex: tabela periódica em Química, retratos de cientistas em aulas históricas).

### 9.1 Sem catálogo prévio — auditoria obrigatória, não só percepção espontânea

Diferença estrutural em relação aos SVGs: o prep cataloga os diagramas
disponíveis (Seção 0/12) e o Passo 5 do Master registra essa lista
*antes* da aula começar — existe um índice para conferir contra. Para
image_search não existe índice equivalente: a decisão de buscar uma
imagem depende inteiramente do professor perceber, no meio da
narração do Resumo ou do Glossário, que acabou de citar algo que se
encaixa nos casos listados no prompt específico da matéria. Isso
falha com mais frequência do que uma checagem mecânica pós-texto.

Para reduzir essa dependência:

1. **Ao final da Etapa 1 (Resumo) e da Etapa 3A (Glossário)**, releia
   internamente o que acabou de apresentar procurando qualquer menção
   aos casos listados no prompt específico da matéria (aplicação
   real, retrato de personagem histórico, obra, objeto ou lugar do
   mundo real etc.). Para cada menção sem imagem apresentada:
   busque agora, antes de avançar para a próxima etapa.
2. A lista de casos por matéria nos prompts específicos é
   **ilustrativa, não exaustiva** — mesmo princípio da Seção 1
   (Princípio Geral): um exemplo listado decide apenas COMO
   reconhecer o caso, nunca SE ele se aplica. Um conceito visual do
   mundo real que não se encaixa em nenhum exemplo dado ainda assim
   exige image_search.
3. **Cientista/personagem histórico citado só de passagem, sem
   bloco dedicado na Seção 3, ainda exige imagem.** A existência (ou
   não) de uma Seção 3 no prep não é o critério — é só onde o prep
   costuma concentrar essas citações quando o papel histórico é
   central ao capítulo. Uma menção nominal dentro da prosa corrida do
   Resumo (ex.: "Galileu já havia demonstrado que...") aciona a
   mesma regra de retrato de cientista da Seção 9, mesmo sem Seção 3
   nenhuma no prep. QA real: fis-2-2 (Marcela) mencionou Galileu em
   uma frase do Resumo, sem Seção 3, e a imagem não foi buscada.

---

## 10. SVGs DO KNOWLEDGE BASE — NÃO REGENERAR

- Se o prep (Seção 0 ou Seção 12) indicar um diagrama disponível no KB:
  1. Buscar via `project_knowledge_search` com o identificador exato.
  2. Passar o código ao Visualizer para renderizar.
  3. **Nunca regenerar** um SVG que já existe no KB.
  4. **Nunca buscar todos os SVGs de uma vez** — buscar cada um no momento indicado.

---

## 11. GRÁFICOS E DIAGRAMAS SEM SVG NO PREP — GERAR NA HORA

Regra crítica que fecha a lacuna entre a Seção 7 (quando gerar) e a
Seção 10 (SVGs do KB): a Seção 7 lista os casos que EXIGEM SVG —
mas nem todo caso desses tem uma entrada pronta no prep. O gatilho
"gráfico/figura/diagrama mencionado" não pode ficar condicionado a
existir SVG catalogado — a existência do SVG só decide COMO obtê-lo,
nunca SE ele deve ser renderizado.

**Sempre que o resumo, uma explicação, uma resposta a pergunta do
aluno ou uma questão original mencionar ou exigir um dos elementos
da Seção 7** (gráfico, figura geométrica, diagrama de forças,
esquema, ciclo, mapa esquemático etc.):

1. Verificar primeiro a Seção 0 do prep. Se o diagrama já existir
   ali: seguir a Seção 10 (buscar no KB, nunca regenerar).
2. Se NÃO existir entrada correspondente: gerar o SVG do zero,
   seguindo as mesmas especificações deste documento — Seção 2
   (contraste), Seção 4 (specs técnicas: viewBox, largura 680, sem
   fundo, sem rotação), Seção 5 (convenções geométricas, quando
   aplicável) e Seção 6 (paleta para SVGs gerados do zero).
3. Passar ao Visualizer e apresentar **antes** do parágrafo ou
   enunciado que faz a menção — nunca descrever o gráfico em texto,
   mesmo quando a geração é improvisada e não há tempo de preparo.

Isso vale em **qualquer etapa da aula**, não só na Etapa 1 do
resumo — inclui explicações espontâneas, respostas a perguntas fora
do fluxo e questões originais criadas pelo professor. Exemplo
típico: gráficos S×t e v×t explicando Cinemática em Física — quase
nunca estão catalogados como diagrama do capítulo na Seção 12 do
prep (são ilustrações da fórmula, não do conteúdo narrativo), mas a
menção ao gráfico no meio da explicação exige a mesma disciplina de
renderização — e as mesmas regras de qualidade (Seções 2, 4, 5, 6)
— dos SVGs catalogados. O mesmo vale para gráficos de dados em
Geografia/Economia, esquemas de reação em Química etc.

---

## 12. REFERÊNCIA CRUZADA

Este arquivo é referenciado por:
- `Prompt_Professor_Master.md`
- `Prompt_Professor_Simulado_Edros.md`
- `Prompt_Professor_Simulado.md`
- `Prompt_Professor_Mat.md`
- `Prompt_Professor_Fis.md`
- `Prompt_Professor_Qui.md`
- `Prompt_Professor_Bio.md`
- `Prompt_Professor_Geo.md`
- `Prompt_Professor_His.md`
- `Prompt_Professor_Por.md`
- `Prompt_Professor_Ingles.md`
- `Prompt_Professor_Artes.md`

Quando houver conflito entre este arquivo e uma regra de prompt específico,
**este arquivo tem precedência** para questões visuais.

---
*Sistema Professor Master — instrucoes_visuais.md v1.3*
