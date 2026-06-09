# INSTRUÇÕES VISUAIS — Sistema Professor Master
# Versão 1.0 | 9º ano | Escola particular — Rio de Janeiro
# Aplicável a: Prompt_Professor_Master, Prompt_Professor_Simulado_Edros,
#              Prompt_Professor_[Matéria] (todos os prompts específicos)

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

---

## 10. SVGs DO KNOWLEDGE BASE — NÃO REGENERAR

- Se o prep (Seção 0 ou Seção 12) indicar um diagrama disponível no KB:
  1. Buscar via `project_knowledge_search` com o identificador exato.
  2. Passar o código ao Visualizer para renderizar.
  3. **Nunca regenerar** um SVG que já existe no KB.
  4. **Nunca buscar todos os SVGs de uma vez** — buscar cada um no momento indicado.

---

## 11. REFERÊNCIA CRUZADA

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
*Sistema Professor Master — instrucoes_visuais.md v1.0*
