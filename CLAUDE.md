# Projeto Professor Particular

Sistema de tutoria IA para geração e validação de material
pedagógico para uso no Claude.ai (Knowledge Base). Multi-aluno:
cada aluno tem sua própria pasta, seu próprio pipeline e seu
próprio Project/Knowledge Base no Claude.ai — desacoplados entre si.

## Alunos ativos

| Aluno | Nível | Pasta | Doc |
|-------|-------|-------|-----|
| Pietro | 9º ano (Fundamental) | `Pietro/` | este arquivo (seções abaixo) |
| Marcela | Ensino Superior — Biologia | `Marcela/` | `Marcela/CLAUDE.md` |

O restante deste arquivo documenta especificamente o pipeline do
**Pietro** (o mais antigo e mais completo). A Marcela tem seu
próprio `CLAUDE.md` com estrutura equivalente, adaptada ao nível
dela — consulte `Marcela/CLAUDE.md` antes de mexer em arquivos
dela. Scripts de manutenção (`Pietro/Scripts/validate_preps.py`)
são agnósticos de aluno e reaproveitados por ambos.

---

## Estrutura de pastas

```
~/Projects/Professor/
├── CLAUDE.md                  ← este arquivo
├── Pietro/
│   ├── Prep/                  ← preps prontos, organizados por matéria
│   │   ├── Artes/
│   │   ├── Biologia/
│   │   ├── Fisica/
│   │   ├── Geografia/
│   │   ├── Historia/
│   │   ├── Ingles/
│   │   ├── Matematica/
│   │   ├── Portugues/
│   │   └── Quimica/
│   ├── Raw/                   ← conteúdo bruto capturado
│   │   ├── Artes/
│   │   │   └── imagens/       ← screenshots individuais prontos para Claude.ai
│   │   ├── Biologia/
│   │   │   └── imagens/
│   │   ├── Fisica/
│   │   │   └── imagens/
│   │   ├── Geografia/
│   │   │   └── imagens/
│   │   ├── Historia/
│   │   │   └── imagens/
│   │   ├── Matematica/
│   │   │   └── imagens/
│   │   ├── Portugues/
│   │   │   └── imagens/
│   │   └── Quimica/
│   │       └── imagens/
│   ├── Transcricoes/          ← transcrições .md geradas pelo Prompt de Transcrição
│   │   ├── Artes/
│   │   ├── Biologia/
│   │   ├── Fisica/
│   │   ├── Geografia/
│   │   ├── Historia/
│   │   ├── Ingles/
│   │   ├── Matematica/
│   │   ├── Portugues/
│   │   └── Quimica/
│   ├── Edros/                 ← pipeline de provas Edros
│   │   ├── Prompt_Captura_Edros.md     ← genérico (qualquer prova)
│   │   ├── Prompt_Preparacao_Edros.md  ← genérico (qualquer prova)
│   │   ├── 1-Avaliação/
│   │   │   ├── Raw/           ← captura bruta da prova (fonte primária)
│   │   │   ├── BancoQuestoes/ ← bancos de revisão + banco da prova
│   │   │   ├── Revisão/       ← PDFs de revisão por matéria
│   │   │   └── Simulado/      ← PDFs da prova, gabarito e resolução
│   │   └── 2-Avaliação/
│   │       ├── Raw/
│   │       ├── BancoQuestoes/
│   │       ├── Revisão/
│   │       └── Simulado/
│   ├── Scripts/               ← scripts de automação (agnósticos de aluno)
│   │   ├── validate_preps.py  ← validador de preps
│   │   ├── gerar_relatorio.js ← template do Relatório de Sessão
│   │   │                        (usado pelo Professor via bash, Etapa 5.3)
│   │   └── concat_screenshots.sh ← deprecado (não usar)
│   └── temp/                  ← arquivos temporários de trabalho
├── Marcela/                    ← pipeline da Marcela (ver Marcela/CLAUDE.md)
│   ├── CLAUDE.md
│   ├── Raw/Fisica/
│   ├── Prep/Fisica/
│   └── Prompts/                ← prompts próprios, desacoplados dos do Pietro
├── Preparacao/                ← prompts de preparação por matéria (Pietro)
│   ├── Prompt_de_Preparacao_Fis.md
│   ├── Prompt_de_Preparacao_Qui.md
│   └── ...
└── Professor/                 ← prompts do professor por matéria (Pietro)
    ├── Prompt_Professor_Master.md
    ├── Prompt_Professor_Fis.md
    ├── Prompt_Professor_Simulado.md
    ├── Prompt_Professor_Simulado_Edros.md
    └── ...
```

---

## Convenção de nomenclatura dos preps

Padrão: `[materia]-[unidade]-[capitulo]-prep.md`

| Prefixo | Matéria     | Pasta Raw     |
|---------|-------------|---------------|
| fis     | Física      | Fisica        |
| qui     | Química     | Quimica       |
| bio     | Biologia    | Biologia      |
| geo     | Geografia   | Geografia     |
| his     | História    | Historia      |
| mat     | Matemática  | Matematica    |
| por     | Português   | Portugues     |
| ing     | Inglês      | Ingles        |
| art     | Artes       | Artes         |

Exemplo: `fis-1-3-prep.md` → Física, Unidade 1, Capítulo 3

Para a Marcela, ver a convenção específica (unidade = capítulo do
material dela, capítulo = parte) em `Marcela/CLAUDE.md`.

---

## Convenção de nomenclatura dos arquivos Edros

| Arquivo | Padrão | Destino | Deletar? |
|---------|--------|---------|----------|
| Captura bruta da prova | `edros-[ano]-[Xav]-captura.md` | `Pietro/Edros/[X]-Avaliação/Raw/` | Não |
| Banco da prova Edros | `banco_edros_[ano]_[Xav].md` | `Pietro/Edros/[X]-Avaliação/BancoQuestoes/` | Não |
| Banco de revisão por matéria | `banco_revisao_[mat].md` | `Pietro/Edros/[X]-Avaliação/BancoQuestoes/` | Não |

Exemplos:
- `edros-2024-2av-captura.md` → captura da 2ª Avaliação Edros 2024
- `banco_edros_2024_2av.md` → banco de questões da 2ª Avaliação Edros 2024
- `banco_revisao_fis.md` → banco de revisão de Física

---

## Pipeline Edros — geração do banco de questões

```
1. CAPTURA      — Claude.ai com Prompt_Captura_Edros.md
                  Anexar: PDF da prova + PDF do gabarito
                  Gera: edros-[ano]-[Xav]-captura.md
                  Salvar em: Pietro/Edros/[X]-Avaliação/Raw/

2. PREPARAÇÃO   — Claude.ai com Prompt_Preparacao_Edros.md
                  Anexar: edros-[ano]-[Xav]-captura.md
                  Gera: banco_edros_[ano]_[Xav].md
                  Salvar em: Pietro/Edros/[X]-Avaliação/BancoQuestoes/

3. COMMIT       — Commitar Raw + BancoQuestoes juntos

4. SIMULADO     — Claude.ai com Prompt_Professor_Simulado_Edros.md
                  Lê banco_edros_*.md do KB
                  Aluno escolhe qual prova simular
```

---

## Convenção de nomenclatura das transcrições

Padrão: `[materia]-[unidade]-[capitulo]-trans.md`

O arquivo de transcrição é o `.md` consolidado (todos os lotes
concatenados) gerado pelo Prompt de Transcrição antes do Prompt
de Captura. Arquivos de lote intermediários (`-trans-01.md` etc.)
são gerados em `Pietro/temp/` e deletados após concatenação.

Exemplo: `his-1-7-trans.md` → transcrição consolidada de História, Unidade 1, Capítulo 7

---

## Estrutura obrigatória de cada prep.md

Todo arquivo `*-prep.md` deve conter estas seções na ordem:

| Seção    | Conteúdo                        | Obrigatória? |
|----------|---------------------------------|-------------|
| SEÇÃO 0  | Índice de diagramas disponíveis | ✅ Sim      |
| SEÇÃO 1  | Perfil do capítulo              | ✅ Sim      |
| SEÇÃO 2  | Mapa de conceitos               | ✅ Sim      |
| SEÇÃO 3  | Cientistas / personagens        | ⬜ Se histórico |
| SEÇÃO 4  | Fórmulas                        | ⬜ Se mat-operacional |
| SEÇÃO 5  | Conteúdo específico por matéria | ⬜ Condicional |
| SEÇÃO 6  | Tabelas de dados (markdown)     | ✅ Sim      |
| SEÇÃO 7  | Dicas de ouro                   | ✅ Sim      |
| SEÇÃO 8  | Alertas e pegadinhas            | ✅ Sim      |
| SEÇÃO 9  | Síntese (tabela com lacunas)    | ✅ Sim      |
| SEÇÃO 10 | Síntese do livro (imagem)       | ⬜ Se imagem disponível |
| SEÇÃO 11 | Questões de referência          | ✅ Sim      |
| SEÇÃO 12 | Diagramas SVG embutidos         | ✅ Sim      |

A SEÇÃO 1 também inclui o bloco **"Glossário do Capítulo"**
(termos e definições, gerado uma vez na Preparação). O Professor
lê esse bloco direto na Etapa 3A da aula, sem reprocessar — preps
antigos sem o bloco caem no fallback de extração ao vivo.

Regras dos SVGs (Seção 12):
- `width="100%"` e `viewBox="0 0 680 H"` obrigatórios
- Classes de cor: `c-purple`, `c-teal`, `c-amber`, `c-coral`, `c-gray`
- `<defs>` com marker de seta em cada SVG
- Sem emojis, sem hardcode de hex para texto, sem texto rotacionado

Esta estrutura é a mesma para qualquer aluno — `validate_preps.py`
não distingue Pietro de Marcela, só olha o nome do arquivo e as
seções.

---

## Script de validação

```bash
# Validar um prep específico
python3 Pietro/Scripts/validate_preps.py Pietro/Prep/Fisica/fis-1-3-prep.md

# Validar todos os preps de todas as matérias
python3 Pietro/Scripts/validate_preps.py Pietro/Prep/

# Validar uma matéria específica
python3 Pietro/Scripts/validate_preps.py Pietro/Prep/Biologia/

# Funciona igual para a Marcela:
python3 Pietro/Scripts/validate_preps.py Marcela/Prep/Fisica/fis-2-1-prep.md
```

Exit code 0 = tudo válido. Exit code 1 = há erros.

---

## Pipeline de geração de conteúdo (Pietro)

### Pipeline A — direto com imagens (Claude.ai)

```
1. CAPTURA      — Print Screen manual no leitor Poliedro (browser)
                  Joao tira screenshots página a página
                  Screenshots salvos em: ~/Pictures/Screenshots/

2. ORGANIZAÇÃO  — Claude Code organiza os screenshots:
                  - Move cada screenshot diretamente (sem concatenação)
                  - Descarta o primeiro (capa) e separa o último como síntese
                  - Move para: Pietro/Raw/[Materia]/imagens/[mat]-[u]-[c]-NN.png
                  - Deleta os screenshots originais de ~/Pictures/Screenshots/

3. PREPARAÇÃO   — Claude.ai com Prompt de Preparação + imagens do KB
                  Gera: Pietro/Prep/[Materia]/[mat]-[u]-[c]-prep.md
                        Pietro/Prep/[Materia]/mindmap_[mat][u][c].html

4. VALIDAÇÃO    — python3 Pietro/Scripts/validate_preps.py [arquivo]
                  Verificar antes de subir ao Knowledge Base

5. AULA         — Claude.ai com Prompt Professor Master + prep no KB
                  Aluno: Pietro (9º ano)
```

### Pipeline B — via transcrição .md (MyHub.ia + Sonnet)

Usar quando o limite de upload de imagens do Claude.ai for um problema.

```
1. CAPTURA      — igual ao Pipeline A

2. ORGANIZAÇÃO  — igual ao Pipeline A

3. TRANSCRIÇÃO  — MyHub.ia com Prompt_de_Transcricao_[mat].md
                  Anexar lotes de screenshots (ex: 4–5 por run)
                  Copiar output de cada lote para Pietro/temp/:
                    [mat]-[u]-[c]-trans-01.md, -02.md, ...
                  Pedir ao Claude Code para concatenar:
                    "Concatena os lotes his-1-7-trans-*.md de Pietro/temp/
                     e salva como Pietro/Transcricoes/Historia/his-1-7-trans.md"
                  Claude Code deleta os arquivos de lote de Pietro/temp/

4. PREPARAÇÃO   — MyHub.ia com Prompt_de_Captura_[mat]_txt.md
                  Anexar Pietro/Transcricoes/[Materia]/[mat]-[u]-[c]-trans.md
                  Copiar output e salvar como:
                    Pietro/Prep/[Materia]/[mat]-[u]-[c]-prep.md

5. VALIDAÇÃO    — python3 Pietro/Scripts/validate_preps.py [arquivo]

6. AULA         — igual ao Pipeline A

Síntese: o último screenshot continua sendo salvo como
[mat]-[u]-[c]-sintese.png em Pietro/Raw/[Materia]/ e
subido diretamente ao KB como imagem — não passa pela transcrição.
```

### Pipeline C — PDF de texto nativo direto (Marcela)

Ver `Marcela/CLAUDE.md`. Usado quando o material já chega como PDF
de texto nativo (não escaneado) — pula Captura por screenshot e
Transcrição, vai direto do PDF para a Preparação.

---

## Tarefas comuns — como pedir ao Claude Code

**Organizar screenshots após captura manual:**
```
Acabei de tirar screenshots do capítulo 3 de Biologia unidade 1.
Organiza, move para Pietro/Raw/Biologia/imagens/ com
prefixo bio-1-3 e deleta os originais de ~/Pictures/Screenshots/.
```

**Concatenar lotes de transcrição:**
```
Concatena os lotes his-1-7-trans-*.md de Pietro/temp/ em ordem
e salva como Pietro/Transcricoes/Historia/his-1-7-trans.md.
Deleta os arquivos de lote de Pietro/temp/ após concatenar.
```

**Validar todos os preps:**
```
Roda o validate_preps.py em Pietro/Prep/ e me diz quais arquivos
têm erro, listando o que está faltando em cada um.
```

**Verificar prep recém-gerado:**
```
Acabei de salvar o bio-2-1-prep.md em Pietro/Prep/Biologia/.
Valida ele e me diz se está pronto para subir ao KB.
```

**Salvar relatório:**
```
Valida todos os preps e salva o resultado em Pietro/temp/relatorio.txt
com a lista dos arquivos com erro e o que falta em cada um.
```

**Listar preps pendentes (Raw sem Prep correspondente):**
```
Compara os arquivos em Pietro/Raw/ com os em Pietro/Prep/.
Me diz quais captures ainda não têm prep gerado.
```

**Listar transcrições sem prep correspondente:**
```
Compara os arquivos em Pietro/Transcricoes/ com os em Pietro/Prep/.
Me diz quais transcrições ainda não têm prep gerado.
```

**Contar cobertura por matéria:**
```
Conta quantos preps existem em cada subpasta de Pietro/Prep/
e me mostra uma tabela com a cobertura atual.
```

---

## Organização de screenshots — regras para Claude Code

Quando pedido para organizar screenshots:

1. Verificar se existem arquivos `Screenshot_*.png` em `~/Pictures/Screenshots/`
2. Ordenar por nome (cronológico)
3. Separar os screenshots especiais:
   - **Primeiro screenshot** → descartar (capa do capítulo — só título e imagem decorativa)
     - **Exceção Inglês**: o primeiro screenshot tem conteúdo relevante — NÃO descartar
   - **Último screenshot** → síntese do capítulo (exceto Artes)
   - **Demais screenshots** → conteúdo, mover diretamente (sem concatenação)
4. Verificar se a pasta `Pietro/Raw/[Materia]/imagens/` existe — criar se não existir
5. Mover cada screenshot de conteúdo diretamente para a pasta de imagens com numeração sequencial:
   `Pietro/Raw/[Materia]/imagens/[mat]-[u]-[c]-NN.png` (01, 02, 03, ...)
6. Copiar o último screenshot como síntese (exceto Artes):
   `Pietro/Raw/[Materia]/[mat]-[u]-[c]-sintese.png`
7. Deletar todos os screenshots originais de `~/Pictures/Screenshots/`
8. Confirmar quantos arquivos foram gerados e onde estão

**Regra da síntese:**
- Todas as matérias EXCETO Artes: último screenshot → `[mat]-[u]-[c]-sintese.png`
- Artes: todos os screenshots vão para imagens, sem síntese separada

**Por que sem concatenação:**
- Cada screenshot corresponde a uma página inteira em resolução total
- Textos de atividades e questões ficam legíveis sem precisar de zoom complementar
- Elimina o risco de misturar zooms com screenshots de conteúdo na mesma sessão

Mapeamento prefixo → pasta:
- bio → Biologia
- fis → Fisica
- qui → Quimica
- geo → Geografia
- his → Historia
- mat → Matematica
- por → Portugues
- ing → Ingles
- art → Artes

---

## Git

Repositório: https://github.com/joaocastellani/pietro
Branch principal: main

Após qualquer operação que crie, mova ou modifique arquivos,
faça commit e push automaticamente.

Convenção de mensagens:

| Tipo de mudança          | Prefixo                                          |
|--------------------------|--------------------------------------------------|
| Novo prep                | `feat(mat): adiciona prep mat-u-c`               |
| Correção em prep         | `fix(mat): corrige prep mat-u-c`                 |
| Nova transcrição         | `feat(trans): adiciona transcrição mat-u-c`      |
| Relatório de validação   | `chore: relatório de validação DD/MM/AAAA`       |
| Novo script              | `feat(scripts): nome do script`                  |
| Atualização de prompt    | `feat(prompts): atualiza Prompt_X`               |
| Organização de arquivos  | `chore: move/renomeia arquivos`                  |
| Novas imagens Raw        | `feat(raw): captura [mat]-[u]-[c]`               |
| Captura Edros (raw)      | `feat(edros): captura edros-[ano]-[Xav]`         |
| Banco Edros              | `feat(edros): adiciona banco_edros_[ano]_[Xav]`  |
| Bancos de revisão Edros  | `feat(edros): adiciona bancos de revisão [X]ª av`|
| Novo aluno / pipeline    | `feat(marcela): ...` (mesmo padrão, prefixo do aluno) |

Regras:
- Ao commitar um novo prep, sempre incluir no mesmo commit:
  - `[Aluno]/Prep/[Materia]/[mat]-[u]-[c]-prep.md`
  - `[Aluno]/Prep/[Materia]/mindmap_[mat][u][c].html` (se existir)
  - Imagens Raw correspondentes (se houver)
- Transcrições são commitadas separadamente do prep
- Nunca commitar arquivos dentro de `Pietro/temp/`
- Sempre incluir data no commit quando for relatório ou validação
- Um commit por operação — não agrupar coisas não relacionadas

---

## Contexto pedagógico — Pietro

- Aluno: Pietro, 9º ano, escola particular, Rio de Janeiro
- Objetivo: reforço de conteúdo antes de provas
- Tom: próximo, encorajador, didático
- Nunca revelar resposta antes do aluno tentar
- O Professor opera no Claude.ai — o Claude Code é usado apenas
  para manutenção da infraestrutura (scripts, validação, organização)

Para o contexto pedagógico da Marcela, ver `Marcela/CLAUDE.md`.
