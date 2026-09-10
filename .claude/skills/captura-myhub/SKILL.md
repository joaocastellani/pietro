---
name: captura-myhub
description: Automatiza a captura de conteúdo de um capítulo via agentes do MyHub.IA — sobe os screenshots já organizados em lotes de 5, dispara o agente certo, extrai o markdown gerado e monta o .md final em Raw/. Use quando o usuário pedir para "capturar", "gerar o raw" ou "rodar o myhub" de um capítulo já com screenshots organizados.
---

# Captura via MyHub.IA

Uso: `/captura-myhub <slug>` — ex.: `/captura-myhub bio-1-5`

Substitui a etapa manual de: abrir o MyHub, subir prints em lotes de 5, copiar
cada resposta e pedir para o Claude Code concatenar. Esta skill faz isso via
Claude in Chrome, ponta a ponta, e já entrega o `.md` final em `Raw/`.

## Pré-requisitos (checar antes de começar; parar e avisar se algo faltar)

- Extensão Claude in Chrome conectada (`claude --chrome`, ou `/chrome` com
  "Enabled by default"). Chrome precisa estar aberto e logado no
  myhub.ia.br **antes** de a skill começar.
- Autenticação do Claude Code via `/login` com conta Anthropic direta —
  Claude in Chrome não funciona com API key nem Bedrock/Vertex/Foundry.
- Screenshots do capítulo já organizados em
  `Pietro/Raw/[Materia]/imagens/[slug]-NN.png` (etapa de organização já
  feita antes — esta skill não tira nem organiza screenshots).
- Existe um agente `Captura-[Materia]` no MyHub (Agentes → Meus Agentes)
  para a matéria do slug. Mapeamento prefixo → matéria/agente:

  | Prefixo | Matéria    | Agente esperado    |
  |---------|------------|---------------------|
  | bio     | Biologia   | Captura-Biologia    |
  | fis     | Fisica     | Captura-Fisica       |
  | qui     | Quimica    | Captura-Quimica      |
  | geo     | Geografia  | Captura-Geografia    |
  | his     | Historia   | Captura-Historia     |
  | mat     | Matematica | Captura-Matematica   |
  | por     | Portugues  | Captura-Portugues    |
  | ing     | Ingles     | Captura-Ingles       |
  | art     | Artes      | Captura-Artes        |

  Hoje só `Captura-Biologia` existe. Se o agente da matéria pedida não
  existir na lista "Meus agentes", **pare e avise o usuário** — não crie
  o agente automaticamente (o prompt/config de cada agente é decisão dele).

## Passo a passo

1. Derivar a matéria do prefixo do slug e listar
   `Pietro/Raw/[Materia]/imagens/[slug]-*.png`, ordenado numericamente.
   Dividir em lotes de até 5 imagens (nunca mais que 10 — limite do
   input de arquivo do Claude in Chrome).

2. Para cada lote (numerado 01, 02, ...):

   a. **Stage**: copiar os arquivos do lote para a sessão com
      `device_stage_files`. Importante: `file_upload` do Claude in Chrome
      **rejeita** o caminho direto da pasta conectada
      (`/home/.../Raw/...`) — sempre usar o `stagedPath` retornado
      (`/mnt/user-data/uploads/...`).

   b. **Abrir o agente**: `navigate` até `https://myhub.ia.br/agents`,
      usar `find` para localizar o card `Captura-[Materia]`, clicar, e
      clicar em "Iniciar conversa". Cada lote usa uma conversa **nova**
      (não reaproveitar chat entre lotes — evita mistura de contexto).

   c. **Upload**: `find` para localizar o input de arquivo (tipicamente
      um botão oculto tipo "file input" perto do clipe de anexo), chamar
      `file_upload` com os `stagedPath` do lote.

   d. **Prompt**: clicar no campo de mensagem, digitar algo como
      "Capture o conteúdo dessas páginas." e clicar no botão de enviar
      (não dá pra enviar só com imagem e texto vazio — o agente exige
      texto no campo).

   e. **Esperar terminar**: o botão de enviar vira um quadrado (parar)
      durante a geração e volta a ser seta quando termina. Checar a cada
      ~10s via screenshot; timeout de ~90s (capítulos geram bastante
      texto). Se estourar o timeout, avisar o usuário em vez de seguir.

   f. **Extrair o markdown bruto** — não usar `get_page_text`/`read_page`
      para isso: eles achatam a formatação e perdem `##`/`**`. O MyHub
      não tem um botão de "baixar .md" na mensagem, só um ícone de
      copiar — usar o truque validado:
      - Clicar no ícone de copiar abaixo da última resposta do
        assistente (fica junto com like/dislike; localizar via
        screenshot/zoom na área logo abaixo do texto gerado).
      - Clicar no campo de mensagem (vazio) e apertar `ctrl+v`.
      - Rodar via `javascript_tool` (isso baixa o arquivo direto pelo
        navegador do usuário, sem precisar trazer o texto de volta pela
        chamada de ferramenta — evita truncamento):
        ```js
        (() => {
          const ta = document.querySelector('textarea');
          const blob = new Blob([ta.value], {type: 'text/markdown'});
          const url = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = '<slug>-parte-<NN>.md';
          document.body.appendChild(a);
          a.click();
          a.remove();
          const len = ta.value.length;
          ta.value = '';
          ta.dispatchEvent(new Event('input', {bubbles:true}));
          return len;
        })()
        ```
      - Confirmar que `len` bate com um tamanho razoável (não é 0/pequeno
        demais) antes de seguir.

   g. **Recolher o arquivo**: o download cai em `~/Downloads/` no
      dispositivo do usuário. Confirmar com `device_bash`/`device_list_dir`
      (pode pedir `device_request_folder_access` em `~/Downloads` na
      primeira vez) e mover para `Pietro/temp/<slug>-parte-<NN>.md`.

   h. Fechar a aba do chat (`tabs_close_mcp`) antes do próximo lote.

3. **Fusão inteligente** (não é `cat` bruto): ler todas as partes
   `Pietro/temp/<slug>-parte-*.md` em ordem. Cada parte foi gerada como
   se fosse o capítulo inteiro (tem seu próprio METADADOS, FLASHCARDS
   etc.), então concatenar direto duplica cabeçalhos e reinicia a
   numeração dos flashcards. Ler o conteúdo de todas as partes e escrever
   um único documento coerente — um só bloco de METADADOS, conceitos sem
   repetição, flashcards renumerados em sequência (FC-1, FC-2, ...) — e
   salvar como `Pietro/Raw/[Materia]/<slug>.md`.

4. Apagar as partes de `Pietro/temp/` após a fusão (usar
   `device_request_delete_permission` se necessário; se não for possível
   apagar, mover para `Pietro/temp/_to_delete/` e avisar o usuário).

5. Reportar ao usuário: quantos lotes/partes foram processados, o
   caminho final gerado, e qualquer trecho onde as partes pareceram
   inconsistentes entre si (datas, nomes, números diferentes) para
   revisão manual antes de subir ao Knowledge Base.

## Limites conhecidos

- Não roda em segundo plano: precisa do Chrome aberto e de uma sessão do
  Claude Code ativa disparando cada lote — é uma automação sob demanda,
  não um job agendado.
- Depende da estrutura atual de `myhub.ia.br` (é uma SPA sem contrato de
  API). Se o layout mudar e `find`/seletores pararem de achar os
  elementos, tirar um screenshot, reidentificar os elementos e atualizar
  esta skill.
- Upload por chamada tem limite de ~10MB combinados — lotes de 5 prints
  em resolução muito alta podem chegar perto disso; se acontecer, reduzir
  o lote para 3–4 imagens.
- Sem checagem automática de créditos do MyHub — se a conta ficar sem
  créditos, a geração falha silenciosamente ou trava; nesse caso avisar
  o usuário em vez de repetir a tentativa.
