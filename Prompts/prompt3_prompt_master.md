# Prompt 3 — Atualizar `Prompt_Professor_Master.md`
# Executar via Claude Code no repositório do knowledge base

---

## OBJETIVO
Atualizar o arquivo `Professor/Prompt_Professor_Master.md` removendo o campo
de cronograma/duração das etapas do template do Mapa de Desempenho (_perf.html).
O campo foi removido pois não há como capturar a duração real das etapas
de forma confiável dentro do claude.ai.

---

## PASSO 1 — Localizar e remover a tabela de cronograma do template HTML

### Âncora de início (localizar este bloco exato):
```
  <div class="section">
    <div class="section-title">Cronograma</div>
    <table>
      <tr><th>Etapa</th><th>Duração</th></tr>
      <tr><td>Resumo</td><td>[XX min]</td></tr>
      <tr><td>Glossário</td><td>[XX min]</td></tr>
      <tr><td>Warm-Up</td><td>[XX min]</td></tr>
      <tr><td>Progressivo</td><td>[XX min]</td></tr>
      <tr><td>Teste final</td><td>[XX min]</td></tr>
      <tr><td><strong>Total</strong></td><td><strong>[XX min]</strong></td></tr>
    </table>
  </div>
```

### Ação: remover TODO o bloco acima (do `<div class="section">` até o `</div>` de fechamento, inclusive)

---

## PASSO 2 — Commit

```bash
git add Professor/Prompt_Professor_Master.md
git commit -m "Prompt_Professor_Master: remove cronograma de etapas do relatório _perf.html"
```

---

## VERIFICAÇÃO FINAL

Antes do commit, confirmar:
- [ ] Bloco de cronograma removido do template HTML do _perf
- [ ] As demais seções do template (Assuntos dominados, Para reforçar, Erros específicos) preservadas intactas
- [ ] Nenhuma outra seção do arquivo foi alterada
- [ ] O arquivo fecha corretamente o HTML (verificar que não ficou tag aberta/solta)
