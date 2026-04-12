#!/usr/bin/env python3
"""
separar_svgs.py
---------------
Extrai os diagramas SVG da Seção 12 de arquivos prep.md,
salva cada SVG em arquivo separado, remove a Seção 12 do prep
e atualiza a Seção 0 com os novos identificadores de arquivo KB.

Uso:
    python3 separar_svgs.py [--dry-run] <prep.md> [<prep.md> ...]
"""

import re
import sys
from pathlib import Path


def extrair_svgs(conteudo):
    # Aceita: '## SEÇÃO 12 — DIAGRAMAS SVG DO CAPÍTULO'
    #      ou '## SEÇÃO 12 — DIAGRAMAS SVG'
    match_secao = re.search(
        r'(?:^|\n)## SE\u00c7\u00c3O 12 \u2014 DIAGRAMAS SVG',
        conteudo
    )
    if not match_secao:
        return {}, conteudo

    prep_sem_secao12 = conteudo[:match_secao.start()]
    secao12 = conteudo[match_secao.start():]

    padrao_diagrama = re.compile(
        r'### DIAGRAMA:\s*(\S+)[^\n]*\n'
        r'[\s\S]*?'
        r'(<svg[\s\S]*?</svg>)',
        re.IGNORECASE
    )

    svgs = {}
    for m in padrao_diagrama.finditer(secao12):
        nome = m.group(1).strip()
        svg  = m.group(2).strip()
        svgs[nome] = svg

    return svgs, prep_sem_secao12.rstrip() + '\n'


def extrair_declarados_secao0(conteudo):
    """Extrai nomes de diagramas declarados na tabela da Seção 0."""
    declarados = []
    for m in re.finditer(r'DIAGRAMA:\s*(\S+)', conteudo):
        declarados.append(m.group(1).strip())
    return declarados


def atualizar_secao0(conteudo, prefixo, nomes_svg):
    # Normalizar cabeçalho da coluna
    conteudo = re.sub(
        r'Identificador[^|]*',
        'Arquivo no KB ',
        conteudo
    )

    # Substituir identificadores presentes na Seção 12
    for nome in nomes_svg:
        conteudo = re.sub(
            r'DIAGRAMA:\s*' + re.escape(nome),
            '`' + prefixo + '-svg-' + nome + '`',
            conteudo
        )

    # Atualizar nota ao Professor
    padrao_nota = re.compile(
        r'Para cada diagrama:.*?passe ao Visualizer\.\n'
        r'Tabelas da Se\u00e7\u00e3o 6 s\u00e3o apresentadas como markdown no chat\.',
        re.DOTALL
    )
    nota_nova = (
        'Para cada diagrama: busque o arquivo no KB pelo nome da coluna\n'
        '"Arquivo no KB" via project_knowledge_search e passe ao Visualizer.\n'
        'Tabelas da Se\u00e7\u00e3o 6 s\u00e3o apresentadas como markdown no chat.'
    )
    conteudo = padrao_nota.sub(nota_nova, conteudo)

    return conteudo


def processar_arquivo(caminho, dry_run=False):
    if not caminho.exists():
        print(f"  [ERRO] Arquivo não encontrado: {caminho}")
        return

    if not caminho.name.endswith('-prep.md'):
        print(f"  [AVISO] Ignorando {caminho.name} — não termina em -prep.md")
        return

    conteudo = caminho.read_text(encoding='utf-8')

    # Verificar diagramas declarados vs presentes
    declarados = extrair_declarados_secao0(conteudo)
    svgs, prep_limpo = extrair_svgs(conteudo)

    if not svgs:
        print(f"  [INFO] {caminho.name} — Seção 12 não encontrada, nada feito.")
        return

    prefixo   = caminho.stem.replace('-prep', '')
    diretorio = caminho.parent

    print(f"\n  {caminho.name}")
    print(f"   {len(svgs)} diagrama(s) encontrado(s) na Seção 12:")

    for nome, svg in svgs.items():
        nome_arquivo = f"{prefixo}-svg-{nome}.svg"
        destino = diretorio / nome_arquivo
        print(f"   OK  {nome_arquivo}  ({len(svg)} chars)")
        if not dry_run:
            destino.write_text(svg, encoding='utf-8')
            destino.chmod(0o664)

    # Reportar ausentes
    ausentes = [d for d in declarados if d not in svgs]
    if ausentes:
        print(f"   AVISO — declarados na Seção 0 mas ausentes na Seção 12:")
        for a in ausentes:
            print(f"     ⚠️  DIAGRAMA: {a}")

    prep_atualizado = atualizar_secao0(prep_limpo, prefixo, list(svgs.keys()))

    if not dry_run:
        caminho.write_text(prep_atualizado, encoding='utf-8')
        print(f"   Secao 12 removida ({len(conteudo)} -> {len(prep_atualizado)} chars)")
        print(f"   Secao 0 atualizada")
    else:
        print(f"   [DRY RUN] Nenhum arquivo alterado.")


def main():
    args = sys.argv[1:]
    if not args:
        print("Uso: python3 separar_svgs.py [--dry-run] <prep.md> [<prep.md> ...]")
        sys.exit(1)

    dry_run  = '--dry-run' in args
    arquivos = [Path(a) for a in args if not a.startswith('--')]

    if dry_run:
        print("MODO DRY RUN — nenhum arquivo será alterado.\n")

    for caminho in arquivos:
        processar_arquivo(caminho, dry_run=dry_run)

    print("\nConcluído.")


if __name__ == '__main__':
    main()
