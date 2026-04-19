# Prompt 4 — Checklist de cobertura visual no EXECUÇÃO
# Executar via Claude Code no repositório do knowledge base

---

## OBJETIVO

Adicionar verificação automática de cobertura visual em todos os 9 prompts
de preparação: após gerar a Seção 12, o Claude confirma que cada tópico
da Seção 2 tem ao menos um recurso visual. Gaps são registrados na Seção 8
como instruções para image_search na aula — nunca surpresas silenciosas.

---

## EDIÇÃO — Expandir passo 4 no EXECUÇÃO de todos os prompts

### Arquivos padrão (Fis, Mat, Bio, Qui, Geo, His, Por, Art)

Substituir:

```
4. Antes de gerar a Seção 12, varra todas as imagens anexadas:
   identifique diagramas visuais (esquemas, fluxos, tabelas
   estruturais, mapas, gráficos) e decida para cada um:
   SVG embutido na Seção 12 · markdown na Seção 6 · ou registrar
   na Seção 8 como ausente (para image_search na aula).
   Depois gere a Seção 12 com todos os SVGs identificados.
```

Por:

```
4. Antes de gerar a Seção 12:
   a) Varra todas as imagens anexadas: identifique diagramas
      visuais (esquemas, fluxos, tabelas estruturais, mapas,
      gráficos) e decida para cada um: SVG na Seção 12 ·
      markdown na Seção 6 · registrar na Seção 8 como ausente.
   b) Gere a Seção 12 com todos os SVGs identificados.
   c) Verifique cobertura visual: para cada bloco temático
      da Seção 2, confirme se há ao menos um recurso visual
      (SVG na Seção 12 · tabela na Seção 6 · image_search).
      Tópicos sem cobertura → adicionar à Seção 8:
      ⚠️ VISUAL AUSENTE — [tópico]
      - Sugestão: [image_search query ou tipo de SVG]
      - Ação: usar image_search na aula / gerar SVG na revisão
```

### Inglês (Prompt_de_Preparacao_Ing.md)

Substituir:

```
3.5. Antes de finalizar a Seção 12, varra todas as imagens anexadas:
   identifique diagramas visuais (esquemas, fluxos, tabelas
   estruturais, mapas, gráficos) e decida para cada um:
   SVG embutido na Seção 12 · markdown na Seção 6 · ou registrar
   na Seção 8 como ausente (para image_search na aula).
```

Por:

```
3.5. Antes de finalizar a Seção 12:
   a) Varra todas as imagens anexadas: identifique diagramas
      visuais (esquemas, fluxos, tabelas estruturais, mapas,
      gráficos) e decida para cada um: SVG na Seção 12 ·
      markdown na Seção 6 · registrar na Seção 8 como ausente.
   b) Gere a Seção 12 com todos os SVGs identificados.
   c) Verifique cobertura visual: para cada bloco temático
      da Seção 2, confirme se há ao menos um recurso visual
      (SVG na Seção 12 · tabela na Seção 6 · image_search).
      Tópicos sem cobertura → adicionar à Seção 8:
      ⚠️ VISUAL AUSENTE — [tópico]
      - Sugestão: [image_search query ou tipo de SVG]
      - Ação: usar image_search na aula / gerar SVG na revisão
```

---

## COMMIT

```bash
git add Preparacao/
git commit -m "feat(prep): checklist de cobertura visual por tópico no EXECUÇÃO (todos os prompts)"
git push
```
