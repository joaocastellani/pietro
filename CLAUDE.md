# Projeto Professor Particular — Pietro

Sistema de tutoria IA para 9º ano. Geração e validação de
material pedagógico para uso no Claude.ai (Knowledge Base).

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
│   │   │   └── imagens/       ← screenshots concatenados prontos para Claude.ai
│   │   ├── Biologia/
│   │   │   └── imagens/
│   │   ├── Fisica/
│   │   │   └── imagens/
│   │   ├── Geografia/
│   │   │   └── imagens/
│   │   ├── Historia/
│   │   │   └── imagens/
│   │   ├── Ingles/
│   │   │   └── imagens/
│   │   ├── Matematica/
│   │   │   └── imagens/
│   │   ├── Portugues/
│   │   │   └── imagens/
│   │   └── Quimica/
│   │       └── imagens/
│   ├── Scripts/               ← scripts de automação
│   │   ├── validate_preps.py  ← validador de preps
│   │   └── concat_screenshots.sh ← concatenador de screenshots
│   └── temp/                  ← arquivos temporários de trabalho
├── Preparacao/                ← prompts de preparação por matéria
│   ├── Prompt_de_Preparacao_Fis.md
│   ├── Prompt_de_Preparacao_Qui.md
│   └── ...
└── Professor/                 ← prompts do professor por matéria
    ├── Prompt_Professor_Master.md
    ├── Prompt_Professor_Fis.md
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

Regras dos SVGs (Seção 12):
- `width="100%"` e `viewBox="0 0 680 H"` obrigatórios
- Classes de cor: `c-purple`, `c-teal`, `c-amber`, `c-coral`, `c-gray`
- `<defs>` com marker de seta em cada SVG
- Sem emojis, sem hardcode de hex para texto, sem texto rotacionado

---

## Script de validação

```bash
# Validar um prep específico
python3 Pietro/Scripts/validate_preps.py Pietro/Prep/Fisica/fis-1-3-prep.md

# Validar todos os preps de todas as matérias
python3 Pietro/Scripts/validate_preps.py Pietro/Prep/

# Validar uma matéria específica
python3 Pietro/Scripts/validate_preps.py Pietro/Prep/Biologia/
```

Exit code 0 = tudo válido. Exit code 1 = há erros.

---

## Pipeline de geração de conteúdo

```
1. CAPTURA   — Print Screen manual no leitor Poliedro (browser)
               Joao tira screenshots página a página
               Screenshots salvos em: ~/Pictures/Screenshots/

2. ORGANIZAÇÃO — Claude Code organiza os screenshots:
               - Concatena N screenshots por imagem usando concat_screenshots.sh
               - Move para: Pietro/Raw/[Materia]/imagens/[mat]-[u]-[c]-NN.png
               - Deleta os screenshots originais de ~/Pictures/Screenshots/
               Script: Pietro/Scripts/concat_screenshots.sh

3. PREPARAÇÃO — Claude.ai com Prompt de Preparação + imagens do KB
               Gera: Pietro/Prep/[Materia]/[mat]-[u]-[c]-prep.md
                     Pietro/Prep/[Materia]/mindmap_[mat][u][c].html

4. VALIDAÇÃO  — python3 Pietro/Scripts/validate_preps.py [arquivo]
               Verificar antes de subir ao Knowledge Base

5. AULA       — Claude.ai com Prompt Professor Master + prep no KB
               Aluno: Pietro (9º ano)
```

---

## Tarefas comuns — como pedir ao Claude Code

**Organizar screenshots após captura manual:**
```
Acabei de tirar screenshots do capítulo 3 de Biologia unidade 1.
Concatena de 4 em 4, move para Pietro/Raw/Biologia/imagens/ com
prefixo bio-1-3 e deleta os originais de ~/Pictures/Screenshots/.
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
3. Separar o último screenshot dos demais:
   - **Último screenshot** → síntese do capítulo (exceto Artes)
   - **Demais screenshots** → conteúdo a concatenar
4. Usar `concat_screenshots.sh` para concatenar os screenshots de conteúdo:
   ```bash
   bash Pietro/Scripts/concat_screenshots.sh [prefixo] [n] ~/Pictures/Screenshots/
   ```
5. Verificar se a pasta `Pietro/Raw/[Materia]/imagens/` existe — criar se não existir
6. Mover os arquivos concatenados para a pasta de imagens:
   `Pietro/Raw/[Materia]/imagens/[mat]-[u]-[c]-NN.png`
7. Copiar o último screenshot como síntese (exceto Artes):
   `Pietro/Raw/[Materia]/[mat]-[u]-[c]-sintese.png`
8. Deletar todos os screenshots originais de `~/Pictures/Screenshots/`
9. Confirmar quantos arquivos foram gerados e onde estão

**Regra da síntese:**
- Todas as matérias EXCETO Artes: último screenshot → `[mat]-[u]-[c]-sintese.png`
- Artes: todos os screenshots vão para imagens, sem síntese separada

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

| Tipo de mudança          | Prefixo                          |
|--------------------------|----------------------------------|
| Novo prep                | `feat(mat): adiciona prep mat-u-c` |
| Correção em prep         | `fix(mat): corrige prep mat-u-c`   |
| Relatório de validação   | `chore: relatório de validação DD/MM/AAAA` |
| Novo script              | `feat(scripts): nome do script`  |
| Atualização de prompt    | `feat(prompts): atualiza Prompt_X` |
| Organização de arquivos  | `chore: move/renomeia arquivos`  |
| Novas imagens Raw        | `feat(raw): captura [mat]-[u]-[c]` |

Regras:
- Ao commitar um novo prep, sempre incluir no mesmo commit:
  - `Pietro/Prep/[Materia]/[mat]-[u]-[c]-prep.md`
  - `Pietro/Prep/[Materia]/mindmap_[mat][u][c].html` (se existir)
  - Imagens Raw correspondentes (se houver)
- Nunca commitar arquivos dentro de `Pietro/temp/`
- Sempre incluir data no commit quando for relatório ou validação
- Um commit por operação — não agrupar coisas não relacionadas

---

## Contexto pedagógico

- Aluno: Pietro, 9º ano, escola particular, Rio de Janeiro
- Objetivo: reforço de conteúdo antes de provas
- Tom: próximo, encorajador, didático
- Nunca revelar resposta antes do aluno tentar
- O Professor opera no Claude.ai — o Claude Code é usado apenas
  para manutenção da infraestrutura (scripts, validação, organização)
