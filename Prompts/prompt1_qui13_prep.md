# Prompt 1 — Atualizar `qui-1-3-prep.md`
# Executar via Claude Code no repositório do knowledge base

---

## OBJETIVO
Atualizar o arquivo `Pietro/Prep/Quimica/qui-1-3-prep.md` com:
1. Nova Seção 0 (DIAGRAMAS DISPONÍVEIS) — adicionar instrução de image_search e dois novos SVGs
2. Dois novos diagramas SVG na Seção 12 — `blocos_tabela_real` e `grupos_familias`

---

## PASSO 1 — Localizar e substituir a Seção 0

### Âncora de início (localizar esta linha exata):
```
## DIAGRAMAS DISPONÍVEIS — qui-1-3
```

### Âncora de fim (substituir até esta linha, inclusive):
```
Tabelas da Seção 6 são apresentadas como markdown no chat.
```

### Substituir TODO o bloco entre as âncoras (inclusive) por:

```markdown
## DIAGRAMAS DISPONÍVEIS — qui-1-3

| Nome | Identificador na Seção 12 | Quando usar na Etapa 1 |
|------|--------------------------|------------------------|
| Linha do tempo — Tabela Periódica | DIAGRAMA: timeline | Ao apresentar Mendeleev e Moseley |
| Classificação dos elementos | DIAGRAMA: classificacao_elementos | Ao explicar metais, não-metais, metaloides e gases nobres |
| Blocos s, p, d, f (tabela real) | DIAGRAMA: blocos_tabela_real | Ao explicar os blocos — exibir ANTES do texto explicativo |
| Grupos e famílias (tabela real) | DIAGRAMA: grupos_familias | Ao explicar períodos e grupos — exibir ANTES do texto |
| Blocos da tabela (esquemático) | DIAGRAMA: blocos_tabela | Fallback — usar apenas se Visualizer falhar |

### Tabelas markdown (Seção 6):
- Tabela 1: Comparação Metais × Não-metais × Metaloides × Gases Nobres
- Tabela 2: Elementos químicos no corpo humano

### image_search obrigatório:
- Quando: logo no início do Resumo, antes de qualquer explicação de posicionamento
- Query: `"tabela periódica completa elementos grupos períodos"`
- Máximo 1 imagem — escolher a mais colorida e legível
- NÃO usar image_search para blocos e grupos — usar os SVGs da Seção 12

### Nota ao Professor:
- DIAGRAMA: blocos_tabela_real e DIAGRAMA: grupos_familias → gerar via Visualizer (show_widget) com o SVG da Seção 12
- Tabela periódica completa → usar image_search (imagem real do material)
- Tabelas da Seção 6 são apresentadas como markdown no chat
```

---

## PASSO 2 — Adicionar dois novos SVGs no final da Seção 12

### Âncora de localização (inserir APÓS este bloco):
```
### DIAGRAMA: blocos_tabela
```
(inserir após o fechamento do bloco SVG de blocos_tabela, ou seja, após o ``` que fecha aquele diagrama)

### Conteúdo a inserir:

```markdown

---

### DIAGRAMA: blocos_tabela_real
Tabela periódica real com os quatro blocos s, p, d e f coloridos nas posições corretas.
Bordas pretas finas (#333) para delimitar as células. Gerar via show_widget (HTML).

```html
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font-sans)}
.wrap{padding:12px}
.legend{display:flex;gap:16px;flex-wrap:wrap;margin-top:10px;font-size:11px;color:var(--color-text-secondary)}
.leg-item{display:flex;align-items:center;gap:5px}
.leg-dot{width:12px;height:12px;border-radius:2px;flex-shrink:0}
</style>
<div class="wrap">
<svg width="100%" viewBox="0 0 680 280" role="img">
<title>Blocos da tabela periódica</title>
<desc>Tabela periódica mostrando os blocos s, p, d e f com posições reais</desc>
<defs><style>
.cell{stroke:#333;stroke-width:0.5}
.bs{fill:#FAEEDA}.bp{fill:#EAF3DE}.bd{fill:#E6F1FB}.bf{fill:#EEEDFE}
.blk{font-size:18px;font-weight:700;text-anchor:middle;dominant-baseline:central;opacity:0.3}
.blk-s{fill:#854F0B}.blk-p{fill:#3B6D11}.blk-d{fill:#0C447C}.blk-f{fill:#3C3489}
.per{font-size:6px;fill:#888;text-anchor:middle;dominant-baseline:central}
.grp{font-size:5.5px;fill:#888;text-anchor:middle;dominant-baseline:central}
</style></defs>
<text class="grp" x="42" y="24">1</text><text class="grp" x="76" y="24">2</text>
<text class="grp" x="110" y="24">3</text><text class="grp" x="144" y="24">4</text>
<text class="grp" x="178" y="24">5</text><text class="grp" x="212" y="24">6</text>
<text class="grp" x="246" y="24">7</text><text class="grp" x="280" y="24">8</text>
<text class="grp" x="314" y="24">9</text><text class="grp" x="348" y="24">10</text>
<text class="grp" x="382" y="24">11</text><text class="grp" x="416" y="24">12</text>
<text class="grp" x="450" y="24">13</text><text class="grp" x="484" y="24">14</text>
<text class="grp" x="518" y="24">15</text><text class="grp" x="552" y="24">16</text>
<text class="grp" x="586" y="24">17</text><text class="grp" x="620" y="24">18</text>
<text class="per" x="14" y="43">1</text><text class="per" x="14" y="69">2</text>
<text class="per" x="14" y="95">3</text><text class="per" x="14" y="121">4</text>
<text class="per" x="14" y="147">5</text><text class="per" x="14" y="173">6</text>
<text class="per" x="14" y="199">7</text>
<!-- Bloco s -->
<rect class="cell bs" x="25" y="30" width="34" height="26"/>
<rect class="cell bs" x="603" y="30" width="34" height="26"/>
<rect class="cell bs" x="25" y="56" width="34" height="26"/><rect class="cell bs" x="59" y="56" width="34" height="26"/>
<rect class="cell bs" x="25" y="82" width="34" height="26"/><rect class="cell bs" x="59" y="82" width="34" height="26"/>
<rect class="cell bs" x="25" y="108" width="34" height="26"/><rect class="cell bs" x="59" y="108" width="34" height="26"/>
<rect class="cell bs" x="25" y="134" width="34" height="26"/><rect class="cell bs" x="59" y="134" width="34" height="26"/>
<rect class="cell bs" x="25" y="160" width="34" height="26"/><rect class="cell bs" x="59" y="160" width="34" height="26"/>
<rect class="cell bs" x="25" y="186" width="34" height="26"/><rect class="cell bs" x="59" y="186" width="34" height="26"/>
<text class="blk blk-s" x="42" y="130">s</text>
<!-- Bloco p -->
<rect class="cell bp" x="433" y="56" width="34" height="26"/><rect class="cell bp" x="467" y="56" width="34" height="26"/>
<rect class="cell bp" x="501" y="56" width="34" height="26"/><rect class="cell bp" x="535" y="56" width="34" height="26"/>
<rect class="cell bp" x="569" y="56" width="34" height="26"/><rect class="cell bp" x="603" y="56" width="34" height="26"/>
<rect class="cell bp" x="433" y="82" width="34" height="26"/><rect class="cell bp" x="467" y="82" width="34" height="26"/>
<rect class="cell bp" x="501" y="82" width="34" height="26"/><rect class="cell bp" x="535" y="82" width="34" height="26"/>
<rect class="cell bp" x="569" y="82" width="34" height="26"/><rect class="cell bp" x="603" y="82" width="34" height="26"/>
<rect class="cell bp" x="433" y="108" width="34" height="26"/><rect class="cell bp" x="467" y="108" width="34" height="26"/>
<rect class="cell bp" x="501" y="108" width="34" height="26"/><rect class="cell bp" x="535" y="108" width="34" height="26"/>
<rect class="cell bp" x="569" y="108" width="34" height="26"/><rect class="cell bp" x="603" y="108" width="34" height="26"/>
<rect class="cell bp" x="433" y="134" width="34" height="26"/><rect class="cell bp" x="467" y="134" width="34" height="26"/>
<rect class="cell bp" x="501" y="134" width="34" height="26"/><rect class="cell bp" x="535" y="134" width="34" height="26"/>
<rect class="cell bp" x="569" y="134" width="34" height="26"/><rect class="cell bp" x="603" y="134" width="34" height="26"/>
<rect class="cell bp" x="433" y="160" width="34" height="26"/><rect class="cell bp" x="467" y="160" width="34" height="26"/>
<rect class="cell bp" x="501" y="160" width="34" height="26"/><rect class="cell bp" x="535" y="160" width="34" height="26"/>
<rect class="cell bp" x="569" y="160" width="34" height="26"/><rect class="cell bp" x="603" y="160" width="34" height="26"/>
<rect class="cell bp" x="433" y="186" width="34" height="26"/><rect class="cell bp" x="467" y="186" width="34" height="26"/>
<rect class="cell bp" x="501" y="186" width="34" height="26"/><rect class="cell bp" x="535" y="186" width="34" height="26"/>
<rect class="cell bp" x="569" y="186" width="34" height="26"/><rect class="cell bp" x="603" y="186" width="34" height="26"/>
<text class="blk blk-p" x="520" y="130">p</text>
<!-- Bloco d -->
<rect class="cell bd" x="93" y="108" width="34" height="26"/><rect class="cell bd" x="127" y="108" width="34" height="26"/>
<rect class="cell bd" x="161" y="108" width="34" height="26"/><rect class="cell bd" x="195" y="108" width="34" height="26"/>
<rect class="cell bd" x="229" y="108" width="34" height="26"/><rect class="cell bd" x="263" y="108" width="34" height="26"/>
<rect class="cell bd" x="297" y="108" width="34" height="26"/><rect class="cell bd" x="331" y="108" width="34" height="26"/>
<rect class="cell bd" x="365" y="108" width="34" height="26"/><rect class="cell bd" x="399" y="108" width="34" height="26"/>
<rect class="cell bd" x="93" y="134" width="34" height="26"/><rect class="cell bd" x="127" y="134" width="34" height="26"/>
<rect class="cell bd" x="161" y="134" width="34" height="26"/><rect class="cell bd" x="195" y="134" width="34" height="26"/>
<rect class="cell bd" x="229" y="134" width="34" height="26"/><rect class="cell bd" x="263" y="134" width="34" height="26"/>
<rect class="cell bd" x="297" y="134" width="34" height="26"/><rect class="cell bd" x="331" y="134" width="34" height="26"/>
<rect class="cell bd" x="365" y="134" width="34" height="26"/><rect class="cell bd" x="399" y="134" width="34" height="26"/>
<rect class="cell bd" x="93" y="160" width="34" height="26"/><rect class="cell bd" x="127" y="160" width="34" height="26"/>
<rect class="cell bd" x="161" y="160" width="34" height="26"/><rect class="cell bd" x="195" y="160" width="34" height="26"/>
<rect class="cell bd" x="229" y="160" width="34" height="26"/><rect class="cell bd" x="263" y="160" width="34" height="26"/>
<rect class="cell bd" x="297" y="160" width="34" height="26"/><rect class="cell bd" x="331" y="160" width="34" height="26"/>
<rect class="cell bd" x="365" y="160" width="34" height="26"/><rect class="cell bd" x="399" y="160" width="34" height="26"/>
<rect class="cell bd" x="93" y="186" width="34" height="26"/><rect class="cell bd" x="127" y="186" width="34" height="26"/>
<rect class="cell bd" x="161" y="186" width="34" height="26"/><rect class="cell bd" x="195" y="186" width="34" height="26"/>
<rect class="cell bd" x="229" y="186" width="34" height="26"/><rect class="cell bd" x="263" y="186" width="34" height="26"/>
<rect class="cell bd" x="297" y="186" width="34" height="26"/><rect class="cell bd" x="331" y="186" width="34" height="26"/>
<rect class="cell bd" x="365" y="186" width="34" height="26"/><rect class="cell bd" x="399" y="186" width="34" height="26"/>
<text class="blk blk-d" x="246" y="165">d</text>
<!-- Bloco f -->
<rect class="cell bf" x="93" y="222" width="34" height="20"/><rect class="cell bf" x="127" y="222" width="34" height="20"/>
<rect class="cell bf" x="161" y="222" width="34" height="20"/><rect class="cell bf" x="195" y="222" width="34" height="20"/>
<rect class="cell bf" x="229" y="222" width="34" height="20"/><rect class="cell bf" x="263" y="222" width="34" height="20"/>
<rect class="cell bf" x="297" y="222" width="34" height="20"/><rect class="cell bf" x="331" y="222" width="34" height="20"/>
<rect class="cell bf" x="365" y="222" width="34" height="20"/><rect class="cell bf" x="399" y="222" width="34" height="20"/>
<rect class="cell bf" x="433" y="222" width="34" height="20"/><rect class="cell bf" x="467" y="222" width="34" height="20"/>
<rect class="cell bf" x="501" y="222" width="34" height="20"/><rect class="cell bf" x="535" y="222" width="34" height="20"/>
<rect class="cell bf" x="93" y="244" width="34" height="20"/><rect class="cell bf" x="127" y="244" width="34" height="20"/>
<rect class="cell bf" x="161" y="244" width="34" height="20"/><rect class="cell bf" x="195" y="244" width="34" height="20"/>
<rect class="cell bf" x="229" y="244" width="34" height="20"/><rect class="cell bf" x="263" y="244" width="34" height="20"/>
<rect class="cell bf" x="297" y="244" width="34" height="20"/><rect class="cell bf" x="331" y="244" width="34" height="20"/>
<rect class="cell bf" x="365" y="244" width="34" height="20"/><rect class="cell bf" x="399" y="244" width="34" height="20"/>
<rect class="cell bf" x="433" y="244" width="34" height="20"/><rect class="cell bf" x="467" y="244" width="34" height="20"/>
<rect class="cell bf" x="501" y="244" width="34" height="20"/><rect class="cell bf" x="535" y="244" width="34" height="20"/>
<text class="blk blk-f" x="314" y="254">f</text>
<text style="font-size:6px;fill:#888;text-anchor:end;dominant-baseline:central" x="88" y="232">6*</text>
<text style="font-size:6px;fill:#888;text-anchor:end;dominant-baseline:central" x="88" y="254">7**</text>
<text style="font-size:6px;fill:#534AB7;text-anchor:middle;dominant-baseline:central" x="110" y="173">*</text>
<text style="font-size:6px;fill:#534AB7;text-anchor:middle;dominant-baseline:central" x="110" y="199">**</text>
</svg>
<div class="legend">
  <div class="leg-item"><div class="leg-dot" style="background:#FAEEDA;border:0.5px solid #333"></div><span style="color:#854F0B;font-weight:500">Bloco s</span> — grupos 1 e 2</div>
  <div class="leg-item"><div class="leg-dot" style="background:#EAF3DE;border:0.5px solid #333"></div><span style="color:#3B6D11;font-weight:500">Bloco p</span> — grupos 13 a 18</div>
  <div class="leg-item"><div class="leg-dot" style="background:#E6F1FB;border:0.5px solid #333"></div><span style="color:#0C447C;font-weight:500">Bloco d</span> — grupos 3 a 12</div>
  <div class="leg-item"><div class="leg-dot" style="background:#EEEDFE;border:0.5px solid #333"></div><span style="color:#3C3489;font-weight:500">Bloco f</span> — lantanídeos e actinídeos</div>
</div>
</div>
```

---

### DIAGRAMA: grupos_familias
Tabela periódica real mostrando grupos A (representantes), grupos B (transição) e grupo 8A (gases nobres).
Bordas pretas finas (#333). Gerar via show_widget (HTML).

```html
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font-sans)}
.wrap{padding:12px}
.legend{display:flex;gap:16px;flex-wrap:wrap;margin-top:10px;font-size:11px;color:var(--color-text-secondary)}
.leg-item{display:flex;align-items:center;gap:5px}
.leg-dot{width:12px;height:12px;border-radius:2px;flex-shrink:0}
</style>
<div class="wrap">
<svg width="100%" viewBox="0 0 680 260" role="img">
<title>Grupos e famílias da tabela periódica</title>
<desc>Estrutura de grupos A e B da tabela periódica</desc>
<defs><style>
.cell{stroke:#333;stroke-width:0.5}
.ga{fill:#E6F1FB}.gb{fill:#FAEEDA}.g18{fill:#EAF3DE}
.grp{font-size:6px;fill:#0C447C;text-anchor:middle;dominant-baseline:central;font-weight:500}
.grpb{font-size:6px;fill:#854F0B;text-anchor:middle;dominant-baseline:central;font-weight:500}
.grp18{font-size:6px;fill:#3B6D11;text-anchor:middle;dominant-baseline:central;font-weight:500}
.per{font-size:6px;fill:#888;text-anchor:middle;dominant-baseline:central}
.num{font-size:5.5px;fill:#888;text-anchor:middle;dominant-baseline:central}
</style></defs>
<text class="num" x="42" y="18">1</text><text class="num" x="76" y="18">2</text>
<text class="num" x="110" y="18">3</text><text class="num" x="144" y="18">4</text>
<text class="num" x="178" y="18">5</text><text class="num" x="212" y="18">6</text>
<text class="num" x="246" y="18">7</text><text class="num" x="280" y="18">8</text>
<text class="num" x="314" y="18">9</text><text class="num" x="348" y="18">10</text>
<text class="num" x="382" y="18">11</text><text class="num" x="416" y="18">12</text>
<text class="num" x="450" y="18">13</text><text class="num" x="484" y="18">14</text>
<text class="num" x="518" y="18">15</text><text class="num" x="552" y="18">16</text>
<text class="num" x="586" y="18">17</text><text class="num" x="620" y="18">18</text>
<text class="grp" x="42" y="30">1A</text><text class="grp" x="76" y="30">2A</text>
<text class="grpb" x="110" y="30">3B</text><text class="grpb" x="144" y="30">4B</text>
<text class="grpb" x="178" y="30">5B</text><text class="grpb" x="212" y="30">6B</text>
<text class="grpb" x="246" y="30">7B</text><text class="grpb" x="280" y="30">8B</text>
<text class="grpb" x="314" y="30">8B</text><text class="grpb" x="348" y="30">8B</text>
<text class="grpb" x="382" y="30">1B</text><text class="grpb" x="416" y="30">2B</text>
<text class="grp" x="450" y="30">3A</text><text class="grp" x="484" y="30">4A</text>
<text class="grp" x="518" y="30">5A</text><text class="grp" x="552" y="30">6A</text>
<text class="grp" x="586" y="30">7A</text><text class="grp18" x="620" y="30">8A</text>
<text class="per" x="14" y="56">1</text><text class="per" x="14" y="82">2</text>
<text class="per" x="14" y="108">3</text><text class="per" x="14" y="134">4</text>
<text class="per" x="14" y="160">5</text><text class="per" x="14" y="186">6</text>
<text class="per" x="14" y="212">7</text>
<rect class="cell ga" x="25" y="43" width="34" height="26"/>
<rect class="cell g18" x="603" y="43" width="34" height="26"/>
<rect class="cell ga" x="25" y="69" width="34" height="26"/><rect class="cell ga" x="59" y="69" width="34" height="26"/>
<rect class="cell ga" x="433" y="69" width="34" height="26"/><rect class="cell ga" x="467" y="69" width="34" height="26"/>
<rect class="cell ga" x="501" y="69" width="34" height="26"/><rect class="cell ga" x="535" y="69" width="34" height="26"/>
<rect class="cell ga" x="569" y="69" width="34" height="26"/><rect class="cell g18" x="603" y="69" width="34" height="26"/>
<rect class="cell ga" x="25" y="95" width="34" height="26"/><rect class="cell ga" x="59" y="95" width="34" height="26"/>
<rect class="cell ga" x="433" y="95" width="34" height="26"/><rect class="cell ga" x="467" y="95" width="34" height="26"/>
<rect class="cell ga" x="501" y="95" width="34" height="26"/><rect class="cell ga" x="535" y="95" width="34" height="26"/>
<rect class="cell ga" x="569" y="95" width="34" height="26"/><rect class="cell g18" x="603" y="95" width="34" height="26"/>
<rect class="cell ga" x="25" y="121" width="34" height="26"/><rect class="cell ga" x="59" y="121" width="34" height="26"/>
<rect class="cell gb" x="93" y="121" width="34" height="26"/><rect class="cell gb" x="127" y="121" width="34" height="26"/>
<rect class="cell gb" x="161" y="121" width="34" height="26"/><rect class="cell gb" x="195" y="121" width="34" height="26"/>
<rect class="cell gb" x="229" y="121" width="34" height="26"/><rect class="cell gb" x="263" y="121" width="34" height="26"/>
<rect class="cell gb" x="297" y="121" width="34" height="26"/><rect class="cell gb" x="331" y="121" width="34" height="26"/>
<rect class="cell gb" x="365" y="121" width="34" height="26"/><rect class="cell gb" x="399" y="121" width="34" height="26"/>
<rect class="cell ga" x="433" y="121" width="34" height="26"/><rect class="cell ga" x="467" y="121" width="34" height="26"/>
<rect class="cell ga" x="501" y="121" width="34" height="26"/><rect class="cell ga" x="535" y="121" width="34" height="26"/>
<rect class="cell ga" x="569" y="121" width="34" height="26"/><rect class="cell g18" x="603" y="121" width="34" height="26"/>
<rect class="cell ga" x="25" y="147" width="34" height="26"/><rect class="cell ga" x="59" y="147" width="34" height="26"/>
<rect class="cell gb" x="93" y="147" width="34" height="26"/><rect class="cell gb" x="127" y="147" width="34" height="26"/>
<rect class="cell gb" x="161" y="147" width="34" height="26"/><rect class="cell gb" x="195" y="147" width="34" height="26"/>
<rect class="cell gb" x="229" y="147" width="34" height="26"/><rect class="cell gb" x="263" y="147" width="34" height="26"/>
<rect class="cell gb" x="297" y="147" width="34" height="26"/><rect class="cell gb" x="331" y="147" width="34" height="26"/>
<rect class="cell gb" x="365" y="147" width="34" height="26"/><rect class="cell gb" x="399" y="147" width="34" height="26"/>
<rect class="cell ga" x="433" y="147" width="34" height="26"/><rect class="cell ga" x="467" y="147" width="34" height="26"/>
<rect class="cell ga" x="501" y="147" width="34" height="26"/><rect class="cell ga" x="535" y="147" width="34" height="26"/>
<rect class="cell ga" x="569" y="147" width="34" height="26"/><rect class="cell g18" x="603" y="147" width="34" height="26"/>
<rect class="cell ga" x="25" y="173" width="34" height="26"/><rect class="cell ga" x="59" y="173" width="34" height="26"/>
<rect class="cell gb" x="93" y="173" width="34" height="26"/><rect class="cell gb" x="127" y="173" width="34" height="26"/>
<rect class="cell gb" x="161" y="173" width="34" height="26"/><rect class="cell gb" x="195" y="173" width="34" height="26"/>
<rect class="cell gb" x="229" y="173" width="34" height="26"/><rect class="cell gb" x="263" y="173" width="34" height="26"/>
<rect class="cell gb" x="297" y="173" width="34" height="26"/><rect class="cell gb" x="331" y="173" width="34" height="26"/>
<rect class="cell gb" x="365" y="173" width="34" height="26"/><rect class="cell gb" x="399" y="173" width="34" height="26"/>
<rect class="cell ga" x="433" y="173" width="34" height="26"/><rect class="cell ga" x="467" y="173" width="34" height="26"/>
<rect class="cell ga" x="501" y="173" width="34" height="26"/><rect class="cell ga" x="535" y="173" width="34" height="26"/>
<rect class="cell ga" x="569" y="173" width="34" height="26"/><rect class="cell g18" x="603" y="173" width="34" height="26"/>
<rect class="cell ga" x="25" y="199" width="34" height="26"/><rect class="cell ga" x="59" y="199" width="34" height="26"/>
<rect class="cell gb" x="93" y="199" width="34" height="26"/><rect class="cell gb" x="127" y="199" width="34" height="26"/>
<rect class="cell gb" x="161" y="199" width="34" height="26"/><rect class="cell gb" x="195" y="199" width="34" height="26"/>
<rect class="cell gb" x="229" y="199" width="34" height="26"/><rect class="cell gb" x="263" y="199" width="34" height="26"/>
<rect class="cell gb" x="297" y="199" width="34" height="26"/><rect class="cell gb" x="331" y="199" width="34" height="26"/>
<rect class="cell gb" x="365" y="199" width="34" height="26"/><rect class="cell gb" x="399" y="199" width="34" height="26"/>
<rect class="cell ga" x="433" y="199" width="34" height="26"/><rect class="cell ga" x="467" y="199" width="34" height="26"/>
<rect class="cell ga" x="501" y="199" width="34" height="26"/><rect class="cell ga" x="535" y="199" width="34" height="26"/>
<rect class="cell ga" x="569" y="199" width="34" height="26"/><rect class="cell g18" x="603" y="199" width="34" height="26"/>
</svg>
<div class="legend">
  <div class="leg-item"><div class="leg-dot" style="background:#E6F1FB;border:0.5px solid #333"></div><span style="color:#0C447C;font-weight:500">Grupos A</span> — elementos representantes (1A a 7A)</div>
  <div class="leg-item"><div class="leg-dot" style="background:#FAEEDA;border:0.5px solid #333"></div><span style="color:#854F0B;font-weight:500">Grupos B</span> — metais de transição (3B a 8B, 1B, 2B)</div>
  <div class="leg-item"><div class="leg-dot" style="background:#EAF3DE;border:0.5px solid #333"></div><span style="color:#3B6D11;font-weight:500">Grupo 8A</span> — gases nobres</div>
</div>
</div>
```
```

---

## PASSO 3 — Commit

```bash
git add Pietro/Prep/Quimica/qui-1-3-prep.md
git commit -m "qui-1-3: adiciona image_search obrigatório + SVGs blocos_tabela_real e grupos_familias"
```

---

## VERIFICAÇÃO FINAL

Antes do commit, confirmar:
- [ ] Seção 0 atualizada com as 5 linhas de diagrama + instrução de image_search
- [ ] DIAGRAMA: blocos_tabela_real presente na Seção 12
- [ ] DIAGRAMA: grupos_familias presente na Seção 12
- [ ] DIAGRAMA: blocos_tabela original preservado (não removido, apenas rebaixado para fallback)
- [ ] Nenhuma outra seção do arquivo foi alterada
