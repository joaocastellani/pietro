# Prompt 3 — Varredura de imagens + SVGs de tabela periódica
# Executar via Claude Code no repositório do knowledge base

---

## OBJETIVO

Dois problemas a corrigir para evitar geração manual de SVGs em conteúdos futuros:

1. **Todos os 9 prompts de preparação** — adicionar etapa de varredura
   de imagens antes de gerar a Seção 12, para que diagramas visuais
   presentes nas imagens sejam automaticamente identificados e convertidos.

2. **`Prompt_de_Preparacao_Qui.md`** — adicionar tipos de SVG específicos
   para tabela periódica no perfil `descritivo-científico` da Seção 12.

---

## PARTE 1 — Todos os 9 prompts de preparação

### Edição: expandir passo 4 no EXECUÇÃO

Em cada um dos arquivos abaixo, substituir:

```
3. Gere Seções 1–11 (conteúdo textual)
4. Gere Seção 12 (SVGs embutidos no prep)
5. Gere Seção 0 (índice) e posicione no início do arquivo
```

Por:

```
3. Gere Seções 1–11 (conteúdo textual)
4. Antes de gerar a Seção 12, varra todas as imagens anexadas:
   identifique diagramas visuais (esquemas, fluxos, tabelas
   estruturais, mapas, gráficos) e decida para cada um:
   SVG embutido na Seção 12 · markdown na Seção 6 · ou registrar
   na Seção 8 como ausente (para image_search na aula).
   Depois gere a Seção 12 com todos os SVGs identificados.
5. Gere Seção 0 (índice) e posicione no início do arquivo
```

Arquivos:
- `Preparacao/Prompt_de_Preparacao_Fis.md`
- `Preparacao/Prompt_de_Preparacao_Mat.md`
- `Preparacao/Prompt_de_Preparacao_Bio.md`
- `Preparacao/Prompt_de_Preparacao_Qui.md`
- `Preparacao/Prompt_de_Preparacao_Geo.md`
- `Preparacao/Prompt_de_Preparacao_His.md`
- `Preparacao/Prompt_de_Preparacao_Por.md`
- `Preparacao/Prompt_de_Preparacao_Art.md`
- `Preparacao/Prompt_de_Preparacao_Ing.md` (passos são 1–9, adaptar)

---

## PARTE 2 — `Prompt_de_Preparacao_Qui.md` — tipos de SVG para tabela periódica

### Edição: adicionar após o bloco `descritivo-científico → DIAGRAMA: transformacao_[tema]`

Após esta linha:
```
NÃO usar SVG para tabelas densas de dados — usar markdown na Seção 6.
```

Inserir:

```markdown
**Descritivo-científico → DIAGRAMA: blocos_tabela_real**
[gerar se o capítulo tratar de blocos s, p, d, f da tabela periódica]
Tabela periódica real com os quatro blocos coloridos nas posições corretas.
Usar formato HTML+SVG (show_widget) — ver template em qui-1-3-prep.md Seção 12.
Legenda obrigatória abaixo do SVG identificando cada bloco e os grupos correspondentes.

**Descritivo-científico → DIAGRAMA: grupos_familias**
[gerar se o capítulo tratar de grupos A/B ou famílias de elementos]
Tabela periódica real diferenciando grupos A (representantes), grupos B (transição)
e grupo 8A (gases nobres) por cor. Usar formato HTML+SVG (show_widget).
Ver template em qui-1-3-prep.md Seção 12.
```

---

## PARTE 3 — Inglês (tratamento especial)

O `Prompt_de_Preparacao_Ing.md` tem numeração diferente (passos 1–9).
A varredura de imagens deve ser inserida antes do passo de geração da Seção 12.
Localizar:
```
3. Gere Seções 1–11 (conteúdo textual)
```
e expandir da mesma forma que os demais.

---

## PARTE 4 — Commit

```bash
git add Preparacao/Prompt_de_Preparacao_Fis.md \
        Preparacao/Prompt_de_Preparacao_Mat.md \
        Preparacao/Prompt_de_Preparacao_Bio.md \
        Preparacao/Prompt_de_Preparacao_Qui.md \
        Preparacao/Prompt_de_Preparacao_Geo.md \
        Preparacao/Prompt_de_Preparacao_His.md \
        Preparacao/Prompt_de_Preparacao_Por.md \
        Preparacao/Prompt_de_Preparacao_Art.md \
        Preparacao/Prompt_de_Preparacao_Ing.md

git commit -m "feat(prep): varredura de imagens antes da Seção 12 + SVGs tabela periódica (Qui)"
git push
```
