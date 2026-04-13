#!/usr/bin/env python3
"""
validate_preps.py — Validador de arquivos prep.md do Prompt Professor
Uso: python3 validate_preps.py <pasta_com_preps>
     python3 validate_preps.py fis-1-3-prep.md   # arquivo único
"""

import sys
import os
import re
import glob
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

# ─────────────────────────────────────────────
# Configuração das seções obrigatórias
# ─────────────────────────────────────────────

SECOES_OBRIGATORIAS = [
    ("SEÇÃO 0",  "DIAGRAMAS DISPONÍVEIS",    True),   # (padrão, keyword, obrigatória)
    ("SEÇÃO 1",  "PERFIL DO CAPÍTULO",       True),
    ("SEÇÃO 2",  "MAPA DE CONCEITOS",        True),
    ("SEÇÃO 3",  "CIENTISTAS",               False),  # opcional: só se histórico
    ("SEÇÃO 4",  "FÓRMULAS",                 False),  # opcional: só se mat-operacional
    ("SEÇÃO 5",  "GLOSSÁRIO",                True),
    ("SEÇÃO 6",  "TABELAS",                  True),
    ("SEÇÃO 7",  "DICAS DE OURO",            True),
    ("SEÇÃO 8",  "ALERTAS",                  True),
    ("SEÇÃO 9",  "SÍNTESE",                  True),
    ("SEÇÃO 10", "SÍNTESE DO LIVRO",         False),  # opcional: requer imagem
    ("SEÇÃO 11", "QUESTÕES",                 True),
    ("SEÇÃO 12", "DIAGRAMAS SVG",            True),
]

# Regex para detectar cada seção (case-insensitive, aceita variações)
SECAO_PATTERNS = {
    "SEÇÃO 0":  r"#+\s*(SEÇÃO\s*0|DIAGRAMAS\s+DISPON[IÍ]VEIS)",
    "SEÇÃO 1":  r"#+\s*SEÇÃO\s*1",
    "SEÇÃO 2":  r"#+\s*SEÇÃO\s*2",
    "SEÇÃO 3":  r"#+\s*SEÇÃO\s*3",
    "SEÇÃO 4":  r"#+\s*SEÇÃO\s*4",
    "SEÇÃO 5":  r"#+\s*SEÇÃO\s*5",
    "SEÇÃO 6":  r"#+\s*SEÇÃO\s*6",
    "SEÇÃO 7":  r"#+\s*SEÇÃO\s*7",
    "SEÇÃO 8":  r"#+\s*SEÇÃO\s*8",
    "SEÇÃO 9":  r"#+\s*SEÇÃO\s*9",
    "SEÇÃO 10": r"#+\s*SEÇÃO\s*10",
    "SEÇÃO 11": r"#+\s*SEÇÃO\s*11",
    "SEÇÃO 12": r"#+\s*SEÇÃO\s*12",
}

PREFIXOS_VALIDOS = {"fis", "qui", "bio", "geo", "his", "mat", "por", "ing", "art"}

# ─────────────────────────────────────────────
# Estrutura de resultado
# ─────────────────────────────────────────────

@dataclass
class Problema:
    nivel: str        # "ERRO" | "AVISO" | "INFO"
    categoria: str
    mensagem: str
    linha: Optional[int] = None

@dataclass
class ResultadoValidacao:
    arquivo: str
    problemas: List[Problema] = field(default_factory=list)

    @property
    def erros(self):
        return [p for p in self.problemas if p.nivel == "ERRO"]

    @property
    def avisos(self):
        return [p for p in self.problemas if p.nivel == "AVISO"]

    @property
    def valido(self):
        return len(self.erros) == 0

# ─────────────────────────────────────────────
# Funções de validação
# ─────────────────────────────────────────────

def validar_nome_arquivo(caminho: str) -> List[Problema]:
    """Verifica se o nome segue o padrão [prefixo]-[u]-[c]-prep.md"""
    problemas = []
    nome = os.path.basename(caminho)

    # Deve terminar em -prep.md
    if not nome.endswith("-prep.md"):
        problemas.append(Problema(
            "ERRO", "nomenclatura",
            f"Nome '{nome}' não termina em '-prep.md'"
        ))
        return problemas

    # Extrai partes: prefixo-unidade-capitulo-prep.md
    partes = nome.replace("-prep.md", "").split("-")
    if len(partes) != 3:
        problemas.append(Problema(
            "ERRO", "nomenclatura",
            f"Nome '{nome}' deve seguir padrão [materia]-[unidade]-[capitulo]-prep.md "
            f"(ex: fis-1-3-prep.md). Encontradas {len(partes)} partes."
        ))
        return problemas

    prefixo, unidade, capitulo = partes

    if prefixo not in PREFIXOS_VALIDOS:
        problemas.append(Problema(
            "ERRO", "nomenclatura",
            f"Prefixo '{prefixo}' inválido. Válidos: {', '.join(sorted(PREFIXOS_VALIDOS))}"
        ))

    if not unidade.isdigit():
        problemas.append(Problema(
            "AVISO", "nomenclatura",
            f"Unidade '{unidade}' deveria ser numérica"
        ))

    if not capitulo.isdigit():
        problemas.append(Problema(
            "AVISO", "nomenclatura",
            f"Capítulo '{capitulo}' deveria ser numérico"
        ))

    return problemas


def validar_secoes(conteudo: str, prefixo: str = "") -> List[Problema]:
    """Verifica presença e ordem das seções obrigatórias"""
    problemas = []
    linhas = conteudo.splitlines()

    # Inglês não usa diagramas SVG — SEÇÃO 0 e SEÇÃO 12 são opcionais
    SECOES_INGLES_OPCIONAIS = {"SEÇÃO 0", "SEÇÃO 12"}
    secoes_efetivas = [
        (s, k, (False if (prefixo == "ing" and s in SECOES_INGLES_OPCIONAIS) else o))
        for s, k, o in SECOES_OBRIGATORIAS
    ]

    # Detectar quais seções existem e em que linha
    secoes_encontradas = {}
    for i, linha in enumerate(linhas, 1):
        for secao, pattern in SECAO_PATTERNS.items():
            if re.search(pattern, linha, re.IGNORECASE):
                if secao not in secoes_encontradas:
                    secoes_encontradas[secao] = i

    # Verificar presença das obrigatórias
    for secao, keyword, obrigatoria in secoes_efetivas:
        if secao not in secoes_encontradas:
            if obrigatoria:
                problemas.append(Problema(
                    "ERRO", "estrutura",
                    f"{secao} ({keyword}) ausente — seção obrigatória"
                ))
            else:
                problemas.append(Problema(
                    "INFO", "estrutura",
                    f"{secao} ({keyword}) ausente — seção opcional"
                ))

    # Verificar ordem das seções encontradas
    nums_encontrados = []
    for secao, linha in sorted(secoes_encontradas.items(), key=lambda x: x[1]):
        m = re.search(r"(\d+)$", secao)
        if m:
            nums_encontrados.append((int(m.group(1)), secao, linha))

    for i in range(1, len(nums_encontrados)):
        n_ant, s_ant, l_ant = nums_encontrados[i-1]
        n_cur, s_cur, l_cur = nums_encontrados[i]
        if n_cur < n_ant:
            problemas.append(Problema(
                "ERRO", "ordem",
                f"{s_cur} (linha {l_cur}) aparece antes de {s_ant} (linha {l_ant}) — ordem incorreta",
                linha=l_cur
            ))

    return problemas


def validar_secao9_sintese(conteudo: str) -> List[Problema]:
    """Verifica se a Seção 9 tem lacunas no formato tabela"""
    problemas = []

    # Localiza o bloco da Seção 9
    m = re.search(r"#+\s*SEÇÃO\s*9.*?(?=#+\s*SEÇÃO\s*10|$)", conteudo,
                  re.IGNORECASE | re.DOTALL)
    if not m:
        return problemas  # ausência já reportada em validar_secoes

    bloco = m.group(0)

    # Deve ter tabela markdown
    if "|" not in bloco:
        problemas.append(Problema(
            "ERRO", "seção 9",
            "SEÇÃO 9 não contém tabela markdown (| ... |)"
        ))
        return problemas

    # Contar linhas de lacunas (linhas com | que não são header/separador)
    linhas_tabela = [l for l in bloco.splitlines()
                     if l.strip().startswith("|")
                     and "---" not in l
                     and re.search(r"\w", l)]

    # Desconta header
    lacunas = max(0, len(linhas_tabela) - 1)
    if lacunas < 3:
        problemas.append(Problema(
            "AVISO", "seção 9",
            f"SEÇÃO 9 tem apenas {lacunas} lacuna(s) — recomendado mínimo 3"
        ))

    # Verificar se tem coluna "Lacuna — resposta esperada"
    if "lacuna" not in bloco.lower() and "resposta" not in bloco.lower():
        problemas.append(Problema(
            "AVISO", "seção 9",
            "SEÇÃO 9: coluna 'Lacuna — resposta esperada' não identificada"
        ))

    return problemas


def validar_svgs(conteudo: str, prefixo: str = "") -> List[Problema]:
    """Verifica SVGs na Seção 12"""
    problemas = []

    # Inglês não usa diagramas SVG — pula validação
    if prefixo == "ing":
        return problemas

    # Localiza bloco da Seção 12
    m = re.search(r"#+\s*SEÇÃO\s*12.*", conteudo, re.IGNORECASE | re.DOTALL)
    if not m:
        return problemas

    bloco = m.group(0)

    # Contar SVGs
    svgs = re.findall(r"<svg\b[^>]*>", bloco, re.IGNORECASE)
    if not svgs:
        problemas.append(Problema(
            "ERRO", "SVG",
            "SEÇÃO 12 não contém nenhum bloco <svg>"
        ))
        return problemas

    # Verificar regras obrigatórias em cada SVG
    blocos_svg = re.findall(r"<svg\b.*?</svg>", bloco, re.IGNORECASE | re.DOTALL)

    for i, svg in enumerate(blocos_svg, 1):
        ref = f"SVG #{i}"

        if 'width="100%"' not in svg:
            problemas.append(Problema(
                "AVISO", "SVG",
                f"{ref}: falta width=\"100%\""
            ))

        if 'viewBox="0 0 680' not in svg:
            problemas.append(Problema(
                "AVISO", "SVG",
                f"{ref}: viewBox não começa com '0 0 680' (largura padrão)"
            ))

        if "<defs>" not in svg or "marker" not in svg:
            problemas.append(Problema(
                "AVISO", "SVG",
                f"{ref}: sem <defs> com marker de seta"
            ))

        # Hardcode de hex para texto (não deve existir)
        hex_no_texto = re.findall(r'fill="#[0-9a-fA-F]{3,6}".*?class="t[sh]?"', svg)
        if hex_no_texto:
            problemas.append(Problema(
                "AVISO", "SVG",
                f"{ref}: possível hardcode de cor em texto — usar classes c-* em vez de fill hex"
            ))

        # Emojis no SVG
        emoji_pattern = re.compile(
            "["
            u"\U0001F600-\U0001F64F"
            u"\U0001F300-\U0001F5FF"
            u"\U0001F680-\U0001F6FF"
            "]+", flags=re.UNICODE
        )
        if emoji_pattern.search(svg):
            problemas.append(Problema(
                "AVISO", "SVG",
                f"{ref}: contém emoji — SVGs não devem usar emojis"
            ))

    # Verificar se Seção 0 lista os diagramas
    sec0 = re.search(r"#+\s*(SEÇÃO\s*0|DIAGRAMAS\s+DISPON[IÍ]VEIS).*?(?=#+\s*SEÇÃO\s*1)",
                     conteudo, re.IGNORECASE | re.DOTALL)
    if sec0:
        nomes_diagrama = re.findall(r"###\s+DIAGRAMA:\s*(\w+)", bloco)
        for nome in nomes_diagrama:
            if nome.lower() not in sec0.group(0).lower():
                problemas.append(Problema(
                    "AVISO", "Seção 0",
                    f"Diagrama '{nome}' da Seção 12 não aparece no índice da Seção 0"
                ))

    return problemas


def validar_secao11_questoes(conteudo: str) -> List[Problema]:
    """Verifica se a Seção 11 tem catálogo (Bloco A) e questões modelo (Bloco B)"""
    problemas = []

    m = re.search(r"#+\s*SEÇÃO\s*11.*?(?=#+\s*SEÇÃO\s*12|$)", conteudo,
                  re.IGNORECASE | re.DOTALL)
    if not m:
        return problemas

    bloco = m.group(0)

    # Caso de seção não gerada (sem questões.md disponível)
    if "não gerada" in bloco.lower():
        problemas.append(Problema(
            "INFO", "seção 11",
            "SEÇÃO 11 marcada como não gerada (arquivo questoes.md ausente no KB)"
        ))
        return problemas

    # Bloco A: deve ter tabela de catálogo
    if "Bloco A" not in bloco and "Q-" not in bloco:
        problemas.append(Problema(
            "AVISO", "seção 11",
            "SEÇÃO 11: Bloco A (catálogo Q-N) não identificado"
        ))

    # Bloco B: deve ter questões modelo QM-
    if "QM-" not in bloco:
        problemas.append(Problema(
            "AVISO", "seção 11",
            "SEÇÃO 11: Bloco B (questões modelo QM-N) não identificado"
        ))

    return problemas


def validar_arquivo(caminho: str) -> ResultadoValidacao:
    resultado = ResultadoValidacao(arquivo=caminho)

    # Leitura
    try:
        with open(caminho, encoding="utf-8") as f:
            conteudo = f.read()
    except Exception as e:
        resultado.problemas.append(Problema("ERRO", "leitura", str(e)))
        return resultado

    if not conteudo.strip():
        resultado.problemas.append(Problema("ERRO", "conteúdo", "Arquivo vazio"))
        return resultado

    # Extrai prefixo da matéria para validações específicas por disciplina
    nome = os.path.basename(caminho)
    partes = nome.replace("-prep.md", "").split("-")
    prefixo = partes[0] if partes else ""

    # Validações
    resultado.problemas += validar_nome_arquivo(caminho)
    resultado.problemas += validar_secoes(conteudo, prefixo)
    resultado.problemas += validar_secao9_sintese(conteudo)
    resultado.problemas += validar_svgs(conteudo, prefixo)
    resultado.problemas += validar_secao11_questoes(conteudo)

    return resultado


# ─────────────────────────────────────────────
# Relatório
# ─────────────────────────────────────────────

ICONS = {"ERRO": "❌", "AVISO": "⚠️ ", "INFO": "ℹ️ "}
CORES = {"ERRO": "\033[91m", "AVISO": "\033[93m", "INFO": "\033[94m", "OK": "\033[92m"}
RESET = "\033[0m"

def imprimir_resultado(r: ResultadoValidacao):
    nome = os.path.basename(r.arquivo)
    status = f"{CORES['OK']}✅ VÁLIDO{RESET}" if r.valido else f"{CORES['ERRO']}❌ INVÁLIDO{RESET}"
    print(f"\n{'─'*60}")
    print(f"  {nome}  →  {status}")
    print(f"{'─'*60}")

    if not r.problemas:
        print("  Nenhum problema encontrado.")
        return

    for p in r.problemas:
        cor = CORES.get(p.nivel, "")
        icon = ICONS.get(p.nivel, "?")
        linha_info = f" (linha {p.linha})" if p.linha else ""
        print(f"  {cor}{icon} [{p.nivel}] {p.categoria}{linha_info}: {p.mensagem}{RESET}")


def imprimir_resumo(resultados: List[ResultadoValidacao]):
    total = len(resultados)
    validos = sum(1 for r in resultados if r.valido)
    invalidos = total - validos
    total_erros = sum(len(r.erros) for r in resultados)
    total_avisos = sum(len(r.avisos) for r in resultados)

    print(f"\n{'═'*60}")
    print(f"  RESUMO — {total} arquivo(s) analisado(s)")
    print(f"{'═'*60}")
    print(f"  {CORES['OK']}✅ Válidos:  {validos}{RESET}")
    if invalidos:
        print(f"  {CORES['ERRO']}❌ Inválidos: {invalidos}{RESET}")
    print(f"  {CORES['ERRO']}Erros totais: {total_erros}{RESET}  |  "
          f"{CORES['AVISO']}Avisos: {total_avisos}{RESET}")
    print(f"{'═'*60}\n")


# ─────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 validate_preps.py <pasta_ou_arquivo>")
        sys.exit(1)

    alvo = sys.argv[1]

    if os.path.isfile(alvo):
        arquivos = [alvo]
    elif os.path.isdir(alvo):
        arquivos = sorted(glob.glob(os.path.join(alvo, "**/*-prep.md"), recursive=True))
        if not arquivos:
            print(f"Nenhum arquivo *-prep.md encontrado em '{alvo}'")
            sys.exit(0)
    else:
        # Glob direto
        arquivos = sorted(glob.glob(alvo, recursive=True))
        if not arquivos:
            print(f"Nenhum arquivo encontrado para '{alvo}'")
            sys.exit(1)

    print(f"\nPrompt Professor — Validador de preps")
    print(f"Arquivos encontrados: {len(arquivos)}")

    resultados = []
    for arq in arquivos:
        r = validar_arquivo(arq)
        imprimir_resultado(r)
        resultados.append(r)

    imprimir_resumo(resultados)

    # Exit code: 1 se houver qualquer erro
    sys.exit(0 if all(r.valido for r in resultados) else 1)


if __name__ == "__main__":
    main()
