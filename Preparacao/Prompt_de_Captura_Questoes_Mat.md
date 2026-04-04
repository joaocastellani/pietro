# PROMPT DE CAPTURA DE QUESTÕES — MATEMÁTICA (9º ano)
# Arquivo: mat-[u]-[c]-questoes.md (append — nunca sobrescrever)
# Numeração contínua: Q-1, Q-2... / QC-1, QC-2...
# PADRÃO DAS QUESTÕES: acrescentar apenas na última execução

---

Tarefa: Extraia APENAS as questões da seção Atividades desta
página de Matemática. Siga rigorosamente as regras abaixo.

NÃO CAPTURAR:
- Perguntas retóricas do texto expositivo
- Exercícios de fixação intercalados ao conteúdo (número em caixa
  colorida no meio do texto, antes da seção Atividades)
- Seção "Reflexão" (discussão em grupo, sem gabarito)
- "Questão invertida" (aluno cria a pergunta a partir de uma
  resposta fornecida)

IDENTIFICAÇÃO DE QUESTÕES DE CONCURSO — CRÍTICO:
Se o número da questão vier acompanhado de nome de banca entre
parênteses — ex: 7 (Fatec-SP), 3 (ENEM), 12 (Fuvest 2019) —
capture como QC-N (não Q-N). Extraia banca e ano do marcador.
Se aparecer apenas logotipo sem texto legível: capture como Q-N e
adicione [IMAGEM] (logotipo de banca; necessário para identificar
concurso).

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
> Texto: → APENAS a fonte primária (tabela de dados, trecho de
  problema contextualizado com autoria, citação). Nunca coloque
  a pergunta aqui. Se não há fonte primária: OMITA o campo —
  nunca escreva "> Texto: /" ou variação vazia.
Enunciado: → APENAS a pergunta ou instrução ao aluno.
  Nunca deixe este campo vazio.
  Se o livro mistura enunciado e dados contextuais: separe
  manualmente — dados de contexto no Enunciado:, fonte citada
  no > Texto: apenas se houver autoria explícita.
  Itens a) b) que são perguntas ao aluno → vão no Enunciado:

MÍDIA — CRÍTICO:
Todos os marcadores de mídia são blocos SEPARADOS antes do
Enunciado:. Nunca embutir dentro do Enunciado:.
Campos de mídia sem conteúdo real: OMITIR.

> Figura: — OBRIGATÓRIO o "> " de bloco markdown. Reconstrua em texto:
  tipo de figura (triângulo, gráfico, tabela...) · medidas e cotas
  anotadas · ângulos indicados · variáveis identificadas ·
  relações visíveis (paralelas, perpendiculares, semelhantes).
  NUNCA escreva apenas "Figura:" sem o "> ".
  Se complexa: adicione "(reconstrução parcial — anexar printscreen)"

> Gráfico: — reconstrua SEMPRE em texto:
  título · Eixo X (grandeza + unidade) · Eixo Y (grandeza +
  unidade) · todos os valores nos eixos · pontos ou segmentos
  com coordenadas e comportamento.
  NUNCA [GRÁFICO]. Se complexo: adicione
  "(reconstrução parcial — anexar printscreen para uso na aula)"

[IMAGEM] — use quando irreconstruível (foto, diagrama fora de
  escala, figura geométrica tridimensional complexa).
  Formato obrigatório — bloco único entre parênteses:
  [IMAGEM] (tipo; contexto; o que mostra;
  por que é necessária para responder)

TIPO — use um único valor. Nunca combine com "/":
  REGRA DE PRECEDÊNCIA — CRÍTICO:
  Tem alternativas listadas (a. b. c. / a) b) c))?
  → SEMPRE múltipla escolha. Independente do conteúdo pedir
    justificativa, raciocínio ou análise de afirmações.
  Afirmações I II III + alternativas de combinação
  (ex: "II e III são verdadeiras") → múltipla escolha.
  V-F = APENAS quando cada item recebe (V) ou (F) individualmente,
  sem alternativas de escolha.
  Sem alternativas: aplique a regra abaixo:
  Pede cálculo numérico?                              → cálculo
  Pede dissertar, justificar ou explicar?             → dissertativa
  Associar colunas ou completar tabela?               → associação
  Pede marcar/dispor pontos em reta ou construção
  geométrica?                                         → construção
  Figura + alternativas → múltipla escolha.
  Figura + cálculo → cálculo.
  Dados tabulares + cálculo → cálculo.

GABARITO: sempre vazio — o livro não traz gabarito.
NUNCA invente ou infira.

Output termina na seção PADRÃO DAS QUESTÕES. Nada depois.
PROIBIDO encerrar com perguntas, opções ou sugestões.

---

FORMATO — inclua APENAS campos com conteúdo real:

**Q-[N]** · pág. [X]
[> Texto:] [> Figura:] [> Gráfico:] [se houver]
Enunciado: [pergunta com todos os itens a) b) c)]
Alternativas: (dissertativa / cálculo / construção) ou lista
Gabarito:
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

**QC-[N]** · [Banca] · [Ano] · pág. [X]
[> Texto:] [> Figura:] [> Gráfico:] [se houver]
Enunciado: [pergunta com todos os itens a) b) c)]
Alternativas: lista
Gabarito:
Tipo: [valor único]
Classificação: [fácil / médio / difícil]

---

EXEMPLOS:

**Q-1** · pág. 35
Enunciado: Calcule o valor de cada potência:
a) 3⁴   b) (−2)³   c) 5⁰   d) (1/2)²
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: fácil

**Q-2** · pág. 37
> Figura: Triângulo ABC retângulo em C · cateto AC = 6 cm ·
>   cateto BC = 8 cm · hipotenusa AB sem medida anotada.
Enunciado: Determine o valor da hipotenusa AB.
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

**Q-3** · pág. 40
> Gráfico: título "Crescimento populacional" · Eixo X: anos
>   (2000, 2005, 2010, 2015, 2020) · Eixo Y: habitantes (×10³)
>   (0, 20, 40, 60, 80) · curva crescente de 10 a 75 mil hab.
Enunciado: Com base no gráfico, determine a variação percentual
da população entre 2000 e 2020.
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: médio

**QC-1** · ENEM · 2018 · pág. 42
> Texto: "Em uma cidade, o número de habitantes dobra a cada
>   10 anos." (Adaptado de: IBGE, 2018)
Enunciado: Considerando que em 2000 a cidade tinha 5.000
habitantes, qual será a população em 2030?
Alternativas:
  a) 15.000   b) 20.000   c) 30.000   d) 40.000   e) 50.000
Gabarito:
Tipo: múltipla escolha
Classificação: médio

**Q-4** · pág. 45
> Figura: Dois triângulos semelhantes ABC e A'B'C' ·
>   triângulo ABC com lados 3 cm, 4 cm e 5 cm ·
>   triângulo A'B'C' com lado correspondente a 3 cm igual a 6 cm
>   · demais lados sem medidas anotadas.
Enunciado: a) Determine a razão de semelhança k entre os dois
triângulos. b) Calcule os lados desconhecidos do triângulo A'B'C'.
c) Qual é a razão entre os perímetros? E entre as áreas?
Alternativas: (cálculo)
Gabarito:
Tipo: cálculo
Classificação: difícil

---

Na ÚLTIMA execução do capítulo, acrescente ao final:

## PADRÃO DAS QUESTÕES
- Estilo predominante: [múltipla escolha / cálculo / dissertativa / misto]
- Foco: [memorização de propriedades / cálculo algébrico /
  geometria / aplicação contextualizada]
- Nível de dificuldade médio: [fácil / médio / difícil]
- Tópicos mais cobrados: [lista]
- Total: [N] questões do capítulo + [N] questões de concurso
