# Prompt 4 — Atualizar `Prompt_Professor_Master.md`
# Migrar relatório de sessão de HTML para Markdown
# Executar via Claude Code no repositório do knowledge base

---

## OBJETIVO
Substituir o template de relatório de sessão (Seção 5.3) no arquivo
`Professor/Prompt_Professor_Master.md`, migrando de HTML para Markdown.

Motivação:
- Arquivos HTML grandes (>9KB base64) excedem o limite de parâmetro da ferramenta MCP do Drive
- Arquivos Markdown são ~2KB de base64 — cabem folgados no limite
- Markdown é legível diretamente no Google Drive sem renderização especial

---

## PASSO 1 — Localizar e substituir o bloco de parâmetros do Drive

### Âncora de início (localizar esta linha exata):
```
**Parâmetros:**
```

### Âncora de fim (substituir até esta linha inclusive):
```
⚠️ base64 obrigatório: `base64.b64encode(html.encode()).decode()`
```

### Substituir TODO o bloco entre as âncoras (inclusive) por:

```markdown
**Parâmetros:**
```
title:    "Relatório U[X]C[Y] — Pietro — [YYYY-MM-DD].md"
mimeType: "text/markdown"
parentId: "[parentId da subpasta da matéria]"
content:  [Markdown em base64]
disableConversionToGoogleType: true
```

⚠️ base64 obrigatório: `base64.b64encode(markdown.encode()).decode()`
⚠️ Usar base64 em linha única (sem quebras): `base64 -w 0` ou equivalente Python
```

---

## PASSO 2 — Localizar e substituir o template HTML pelo template Markdown

### Âncora de início (localizar esta linha exata):
```
#### Geração do HTML
```

### Âncora de fim (localizar o fechamento do bloco HTML — esta linha):
```
→ Não bloquear o encerramento da aula.
```

### Substituir TODO o bloco entre as âncoras (inclusive) por:

```markdown
#### Geração do Markdown

**Nível de desempenho** (média dos 3 placares):
- ≥ 90%: "Excelente" · 75–89%: "Bom desempenho"
- 60–74%: "Regular" · < 60%: "A reforçar"

**Estrelas:** 5=Excelente · 4=Bom · 3=Regular · 1–2=Reforçar
(representar como: ⭐⭐⭐⭐⭐ / ⭐⭐⭐⭐ / ⭐⭐⭐ / ⭐⭐)

**Template Markdown:**

```markdown
# Relatório de Aula — [Matéria] U[X]C[Y]
**[Nome do Capítulo]** · Pietro · [DD/MM/AAAA]

---

## Resultado: [N]/10 [estrelas]

---

## Assuntos dominados

- ✅ [Tópico 1]
- ✅ [Tópico 2]
- ✅ [Tópico N]

---

## Para reforçar

### [Tópico com erro 1]
**[Descrição do erro]**
[Explicação do conceito correto em 1-2 linhas]
[Regra ou macete para fixar]

### [Tópico com erro 2]
**[Descrição do erro]**
[Explicação do conceito correto em 1-2 linhas]

---

*Gerado pelo Sistema de Tutoria · [Matéria] U[X]C[Y] · [DD/MM/AAAA]*
```

**Salvamento via MCP:**
```python
import base64
md_content = "..."  # conteúdo markdown
b64 = base64.b64encode(md_content.encode()).decode()
```

Chamar `Google Drive:create_file` com:
- `title`: `"Relatório U[X]C[Y] — Pietro — [YYYY-MM-DD].md"`
- `mimeType`: `"text/markdown"`
- `parentId`: ID da subpasta da matéria (ver tabela acima)
- `content`: base64 do markdown em linha única
- `disableConversionToGoogleType`: `true`

Se o Drive MCP não estiver disponível:
→ "⚠️ Relatório gerado mas não salvo no Drive. Baixe o arquivo."
→ Não bloquear o encerramento da aula.
```

---

## PASSO 3 — Commit

```bash
git add Professor/Prompt_Professor_Master.md
git commit -m "Prompt_Professor_Master: migra relatório de sessão de HTML para Markdown"
```

---

## VERIFICAÇÃO FINAL

Antes do commit, confirmar:
- [ ] Parâmetros atualizados: `mimeType` = `text/markdown`, título com `.md`
- [ ] Template HTML removido e substituído pelo template Markdown
- [ ] Template Markdown contém: cabeçalho, resultado+estrelas, dominados, para reforçar, rodapé
- [ ] Instrução de base64 em linha única preservada (`-w 0`)
- [ ] Fallback "Drive MCP não disponível" preservado
- [ ] Tabela de IDs das pastas preservada intacta
- [ ] Nenhuma outra seção do arquivo foi alterada
