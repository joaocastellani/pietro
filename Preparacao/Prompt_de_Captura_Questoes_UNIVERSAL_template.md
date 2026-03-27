# PROMPT DE CAPTURA DE QUESTÕES — UNIVERSAL (template)
# NÃO usar diretamente — derivar para cada disciplina
# Variáveis a substituir ao derivar:
#   {{MATERIA}}   → Biologia / Física / Química / Geografia / História
#   {{PREFIXO}}   → bio / fis / qui / geo / his
#   {{TIPOS}}     → lista de tipos válidos da disciplina
#   {{MIDIA}}     → regras de mídia específicas da disciplina
#   {{EXEMPLOS}}  → 2-3 exemplos representativos da disciplina

# PROMPT DE CAPTURA DE QUESTÕES — {{MATERIA}} (9º ano)
# Arquivo: {{PREFIXO}}-[u]-[c]-questoes.md (append — nunca sobrescrever)
# Numeração contínua: Q-1, Q-2... / QC-1, QC-2...
# PADRÃO DAS QUESTÕES: acrescentar apenas na última execução

---

Tarefa: Extraia APENAS as questões da seção Atividades desta
página de {{MATERIA}}. Siga rigorosamente as regras abaixo.

NÃO CAPTURAR:
- Perguntas retóricas do texto expositivo
- Questões intercaladas ao conteúdo (número em caixa colorida
  no meio do texto, antes da seção Atividades)
- "Questão invertida" (aluno cria a pergunta a partir de
  uma resposta fornecida)

NUMERAÇÃO — CRÍTICO:
Use sequência própria do arquivo — NUNCA a numeração do livro.
Q-N e QC-N são independentes entre si.
Nunca salte números: após Q-3 vem Q-4, após QC-2 vem QC-3.

ANTI-DUPLICATA — CRÍTICO:
Aplica-se APENAS dentro do material enviado nesta execução.
Se na mesma página o livro apresenta uma questão sem banca
e a mesma questão aparece com banca (mesmo texto + mesmo
enunciado): capture APENAS a versão de banca (QC-N).
NUNCA inferir que uma questão já foi capturada em execução
anterior — você não tem acesso ao arquivo gerado. Capture
tudo que estiver no material enviado agora.

ANTI-PARTIÇÃO — CRÍTICO:
Enunciado com itens a) b) c) = UMA questão.
Nunca gere Q-N e Q-N+1 para itens do mesmo enunciado.
Todos os itens vão dentro do mesmo campo Enunciado:.

TEXTO vs ENUNCIADO — CRÍTICO:
> Texto: → APENAS a fonte primária (citação, documento, trecho
  de autor). Nunca coloque a pergunta aqui.
  Se não há fonte primária: OMITA o campo — nunca escreva
  "> Texto: /" ou variação vazia.
Enunciado: → APENAS a pergunta ou instrução ao aluno.
  Nunca deixe este campo vazio.
  Se o livro mistura os dois: separe manualmente.
  Itens a) b) que são perguntas ao aluno → vão no Enunciado:
  Contexto introdutório do livro NÃO é parte do enunciado
  — descarte.

MÍDIA — CRÍTICO:
Todos os marcadores de mídia são blocos SEPARADOS antes do
Enunciado:. Nunca embutir dentro do Enunciado:.
Campos de mídia sem conteúdo real: OMITIR.

{{MIDIA}}

TIPO — use um único valor. Nunca combine com "/":
{{TIPOS}}
  · Gráfico/Esquema + alternativas → múltipla escolha
  · Texto de fonte primária + alternativas → múltipla escolha
  · Texto introdutório do livro → dissertativa

GABARITO: sempre vazio — o livro não traz gabarito.
NUNCA invente ou infira.

Output termina na seção PADRÃO DAS QUESTÕES. Nada depois.
PROIBIDO encerrar com perguntas, opções ou sugestões.

---

FORMATO:
Inclua APENAS os campos que têm conteúdo real.

**Q-[N]** · pág. [X]
[> Texto: APENAS se houver fonte primária]
[marcadores de mídia APENAS se houver]
Enunciado: [APENAS a pergunta, com todos os itens a) b) c)]
Alternativas: (dissertativa) ou lista de opções
Gabarito:
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

**QC-[N]** · [Banca] · [Ano] · pág. [X]
[> Texto: APENAS se houver fonte primária]
[marcadores de mídia APENAS se houver]
Enunciado: [APENAS a pergunta, com todos os itens a) b) c)]
Alternativas: lista de opções
Gabarito:
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

---

EXEMPLOS:

{{EXEMPLOS}}

---

Na ÚLTIMA execução do capítulo, acrescente ao final:

## PADRÃO DAS QUESTÕES
- Estilo predominante: [múltipla escolha / dissertativa / misto / ...]
- Foco: [causas-consequências / cálculo / identificação / análise de fonte / ...]
- Nível de dificuldade médio: [fácil / médio / difícil]
- Tópicos mais cobrados: [lista]
- Total: [N] questões do capítulo + [N] questões de concurso
