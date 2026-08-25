# Marcela — Física Geral (Ensino Superior, curso de Biologia)

Pipeline próprio, desacoplado do `Pietro/` — ver `CLAUDE.md` na
raiz do repositório para a visão geral do projeto multi-aluno.

---

## Contexto pedagógico

- Aluna: Marcela, Ensino Superior, cursando Biologia
- Disciplina: Física Geral — conteúdo atual: Capítulo 2 (Mecânica)
- Objetivo: reforço de conteúdo do capítulo (vetores, MUV, leis de Newton)
- Tom: próximo, respeitoso, rigor matemático de nível universitário
- Nunca revelar resposta antes da aluna tentar
- O Professor opera no Claude.ai (Project/Knowledge Base **separado**
  do Pietro) — o Claude Code/Cowork é usado apenas para manutenção
  da infraestrutura (organização de arquivos, prompts, validação)

---

## Estrutura de pastas

```
~/Projects/Professor/
└── Marcela/
    ├── CLAUDE.md                  ← este arquivo
    ├── Raw/
    │   └── Fisica/
    │       ├── fis-2-1-mecanica-parte1.pdf   ← capítulo original (PDF nativo)
    │       └── fis-2-2-mecanica-parte2.pdf   ← capítulo original (PDF nativo)
    ├── Prep/
    │   └── Fisica/                ← preps prontos (ainda vazio)
    └── Prompts/
        ├── Prompt_de_Captura_Fis_Marcela_txt.md
        ├── Prompt_de_Preparacao_Fis_Marcela.md
        ├── Prompt_Professor_Fis_Marcela.md
        └── Prompt_Professor_Master_Marcela.md
```

Diferença-chave em relação ao Pietro: o material da Marcela já
chega como **PDF de texto nativo** (apostila digitada), não como
screenshots do leitor Poliedro. Por isso não há pastas `imagens/`
nem etapa de Transcrição — o PDF é anexado diretamente na etapa
de Captura.

---

## Convenção de nomenclatura dos preps

Mesmo padrão do Pietro: `[materia]-[unidade]-[capitulo]-prep.md`,
mas para a Marcela:
- `unidade` = número do capítulo do material dela (ex: 2 = Mecânica)
- `capitulo` (no nome do arquivo) = número da "Parte" dentro do
  capítulo (o material dela é dividido em Partes, não em capítulos
  sequenciais)

Exemplo: `fis-2-1-prep.md` → Física, Capítulo 2 (Mecânica), Parte 1.

Só Física está configurada até o momento (`fis`). Se outra
disciplina for adicionada, seguir os mesmos prefixos da tabela do
`CLAUDE.md` raiz e criar `Raw/[Materia]/` + `Prep/[Materia]/` aqui
dentro.

---

## Pipeline C — PDF de texto nativo direto

Pipeline específico da Marcela (equivalente aos Pipelines A/B do
Pietro, mas sem etapa de captura por screenshot nem transcrição):

```
1. CAPTURA      — Claude.ai (Project da Marcela) com
                  Prompt_de_Captura_Fis_Marcela_txt.md
                  Anexar: PDF do capítulo/parte diretamente
                  Gera: fis-[u]-[c].md

2. PREPARAÇÃO   — Claude.ai com Prompt_de_Preparacao_Fis_Marcela.md
                  Anexar: fis-[u]-[c].md
                  Gera: Marcela/Prep/Fisica/fis-[u]-[c]-prep.md
                        Marcela/Prep/Fisica/mindmap_fis[u][c].html

3. VALIDAÇÃO    — python3 Pietro/Scripts/validate_preps.py [arquivo]
                  (script é agnóstico de aluno — reaproveitado sem cópia)

4. AULA         — Claude.ai (Project da Marcela) com
                  Prompt_Professor_Master_Marcela.md +
                  instrucoes_visuais.md (Professor/) + prep no KB
                  Aluna: Marcela (Ensino Superior — Biologia)
```

Estado atual (2026-08-25): os preps das duas partes do Capítulo 2
já foram gerados e validados (`Marcela/Prep/Fisica/fis-2-1-prep.md`
e `fis-2-2-prep.md`).

**Knowledge Base do Project da Marcela no Claude.ai — 5 arquivos,
não 4:** os 4 prompts desta pasta + `Professor/instrucoes_visuais.md`.
Achado de QA: esse arquivo não estava na lista original de upload
(só os "4 prompts desta pasta"), mesmo sendo referenciado por
`Prompt_Professor_Master_Marcela.md` como fonte única das regras de
SVG, cores, contraste e image_search — sem ele no KB, essas regras
nunca chegam à aula, por mais corretas que estejam no repositório.
Não há sincronização automática entre este repositório e o Project
da Marcela: ao atualizar `instrucoes_visuais.md` ou qualquer um dos
4 prompts aqui, é preciso resubir a versão nova ao Knowledge Base
manualmente.

---

## Script de validação

Reaproveita o script do Pietro (agnóstico de aluno, valida
qualquer `*-prep.md` pelo nome do arquivo e pela estrutura de
seções):

```bash
python3 Pietro/Scripts/validate_preps.py Marcela/Prep/Fisica/fis-2-1-prep.md
python3 Pietro/Scripts/validate_preps.py Marcela/Prep/
```

---

## Git

Mesmo repositório do Pietro (`github.com/joaocastellani/pietro`),
pasta separada. Seguir a mesma convenção de commits do `CLAUDE.md`
raiz, usando `Marcela` no lugar de `Pietro` quando fizer sentido
(ex: `feat(marcela): adiciona prep fis-2-1`).
