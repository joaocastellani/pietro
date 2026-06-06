# PROMPT DE CAPTURA — Avaliação Edros (9º ano)
# Arquivo gerado: edros-[ano]-[avaliacao]-captura.md
# Destino:        Pietro/Edros/[X]-Avaliação/Raw/

---

Você receberá dois documentos anexados:
1. **PDF da prova** — todas as questões
2. **PDF do gabarito** — respostas oficiais

Tarefa: extraia o conteúdo completo da prova, leia o gabarito
e gere um markdown estruturado com questões + respostas.

---

## REGRAS GERAIS

- Preserve todos os enunciados exatamente como aparecem — não
  resuma, não parafraseie, não omita nenhum trecho
- Transcreva cada alternativa na íntegra, incluindo as letras
  (a., b., c., d., e.)
- Para textos de apoio que precedem a questão (fragmentos,
  poemas, anúncios, tiras, artigos), transcreva o conteúdo
  textual completo antes do enunciado da questão
- Quando houver imagem (charge, mapa, gráfico, tirinha,
  fotografia, anúncio visual), escreva:
  [IMAGEM: descrição objetiva do que é mostrado]
  no lugar onde a imagem aparece — nunca omita a existência
  de uma imagem
- PROIBIDO encerrar com perguntas, sugestões ou próximos passos.
  O output termina na última questão — nada mais.

---

## 1. METADADOS

Extraia do cabeçalho da prova e do gabarito:

- Avaliação: [ex: 2ª Avaliação Edros]
- Ano: [ex: 2024]
- Série: [ex: 9º ano]
- Total de questões: [número]
- Fase: [número, se indicado]

---

## 2. GABARITO

Antes de processar as questões, leia o PDF do gabarito e
monte a tabela completa de respostas:

| Questão | Gabarito |
|---------|----------|
| Q01 | [letra] |
| Q02 | [letra] |
| ... | ... |

---

## 3. QUESTÕES

Para cada questão, use o formato:

**Q[NN]** · [Matéria]
[texto de apoio, se houver — transcrito na íntegra]
[IMAGEM: descrição] ← se houver imagem
Enunciado: [enunciado exato da questão]
a. ( ) [alternativa a completa]
b. ( ) [alternativa b completa]
c. ( ) [alternativa c completa]
d. ( ) [alternativa d completa]
e. ( ) [alternativa e completa]
Gabarito: [letra maiúscula lida do PDF do gabarito]

---

Separe cada questão com uma linha `---`.

### IDENTIFICAÇÃO DE MATÉRIA

A prova está dividida em blocos identificados por cabeçalho
(ex: "LÍNGUA INGLESA", "LÍNGUA PORTUGUESA", "MATEMÁTICA",
"CIÊNCIAS", "HISTÓRIA", "GEOGRAFIA").
Use exatamente o nome do cabeçalho como matéria de cada questão.

Para Ciências, se o bloco for dividido internamente em
subcabeçalhos (Biologia, Química, Física), indique:
**Q[NN]** · Ciências — Biologia
**Q[NN]** · Ciências — Química
**Q[NN]** · Ciências — Física

### TEXTOS COMPARTILHADOS

Se um mesmo texto de apoio servir a mais de uma questão,
transcreva-o ANTES da primeira questão que o usa e, para as
questões seguintes, escreva:
[Texto de apoio: ver Q-NN]

---

## 4. RESUMO FINAL

Ao final, preencha:
- Distribuição por matéria: [Inglês: N | Português: N | Matemática: N | Ciências: N | História: N | Geografia: N]
- Questões com imagem: [lista de números]
- Questões com texto de apoio compartilhado: [lista de grupos]
