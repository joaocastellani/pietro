# Prompt 2 — Atualizar `Prompt_Professor_Qui.md`
# Executar via Claude Code no repositório do knowledge base

---

## OBJETIVO
Atualizar o arquivo `Professor/Prompt_Professor_Qui.md` com duas novas regras:
1. Instrução de `image_search` obrigatório para capítulos de tabela periódica
2. Regra de símbolo químico + nome (e vice-versa) em todas as matérias

---

## PASSO 1 — Adicionar regra de image_search na seção ETAPA 1

### Âncora de localização (inserir APÓS esta linha):
```
Máximo 1 imagem por conceito.
```

### Conteúdo a inserir APÓS a âncora:

```markdown

### Tabela periódica — image_search obrigatório
Para qualquer capítulo cujo tema envolva posicionamento na tabela periódica
(períodos, grupos, blocos, classificação de elementos):

1. Buscar via `image_search` com query `"tabela periódica completa elementos grupos períodos"`
   logo no **início do Resumo**, antes de qualquer explicação de posicionamento.
   Máximo 1 imagem — escolher a mais colorida e legível.
2. Usar `DIAGRAMA: blocos_tabela_real` (Seção 12 do prep) via Visualizer
   ao explicar os blocos s, p, d e f — NÃO usar image_search para este diagrama.
3. Usar `DIAGRAMA: grupos_familias` (Seção 12 do prep) via Visualizer
   ao explicar grupos e famílias — NÃO usar image_search para este diagrama.

⚠️ Sem a tabela periódica visual, a aula de posicionamento fica abstrata demais.
```

---

## PASSO 2 — Adicionar regra de símbolo + nome

### Âncora de localização (inserir ANTES desta linha):
```
## ETAPA 2 — WARM-UP
```

### Conteúdo a inserir ANTES da âncora:

```markdown
---

## REGRA GLOBAL — SÍMBOLO QUÍMICO E NOME

Sempre que citar um símbolo químico, incluir o nome entre parênteses:
- Correto: **Hg (mercúrio)**, **Na (sódio)**, **Si (silício)**, **Fe (ferro)**
- Incorreto: apenas "Hg" ou apenas "mercúrio" sem o par

Sempre que citar o nome de um elemento, incluir o símbolo entre parênteses:
- Correto: **mercúrio (Hg)**, **sódio (Na)**, **silício (Si)**
- Incorreto: apenas o nome sem o símbolo

Esta regra se aplica a:
- Resumo da matéria
- Warm-Up e Glossário
- Questões do Teste Progressivo e Teste Final
- Correções e Consolidação

⚠️ Nunca exigir memorização de símbolos isolados — a associação deve acontecer
naturalmente pelo uso repetido do par símbolo ↔ nome ao longo da aula.

---
```

---

## PASSO 3 — Commit

```bash
git add Professor/Prompt_Professor_Qui.md
git commit -m "Prompt_Professor_Qui: adiciona image_search obrigatório tabela periódica + regra símbolo/nome"
```

---

## VERIFICAÇÃO FINAL

Antes do commit, confirmar:
- [ ] Regra de image_search inserida após "Máximo 1 imagem por conceito"
- [ ] Regra de símbolo/nome inserida antes de "## ETAPA 2 — WARM-UP"
- [ ] Nenhuma outra seção do arquivo foi alterada
- [ ] Formatação markdown preservada (headings, listas, negrito)
