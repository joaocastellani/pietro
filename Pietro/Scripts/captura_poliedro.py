#!/usr/bin/env python3
"""
captura_poliedro.py — Captura automática do leitor PDF Poliedro
Usa PyAutoGUI: você abre o browser em fullscreen, o script captura.

USO:
  python3 captura_poliedro.py --materia bio --unidade 1 --capitulo 3 \
      --paginas 18 --prefixo bio-1-3

  --paginas  : número de páginas do capítulo a capturar
  --prefixo  : nome base dos arquivos (ex: bio-1-3)

DEPENDÊNCIAS:
  pip install pyautogui pillow
"""

import argparse
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import pyautogui
except ImportError:
    print("❌ PyAutoGUI não instalado.")
    print("   Execute: pip install pyautogui pillow")
    sys.exit(1)

# ──────────────────────────────────────────────
# CONFIGURAÇÃO
# ──────────────────────────────────────────────

PROJECT_ROOT = Path.home() / "Projects" / "Professor"
RAW_DIR      = PROJECT_ROOT / "Pietro" / "Raw"

# Pausa após PageDown antes de capturar (segundos)
# Aumente se a conexão for lenta e a página demorar a renderizar
PAUSA_APOS_PAGEDOWN = 1.5

# Pausa de segurança no início para você colocar o browser em foco
PAUSA_INICIAL = 4

# PyAutoGUI — desativa o failsafe se mover o mouse pro canto
pyautogui.FAILSAFE = True  # mova o mouse pro canto superior esquerdo para parar

# ──────────────────────────────────────────────
# CAPTURA
# ──────────────────────────────────────────────

def capturar(materia, unidade, capitulo, pagina_inicial, total_paginas):
    base    = f"{materia}-{unidade}-{capitulo}"
    out_dir = RAW_DIR / base
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n📚 Capturando: {base}")
    print(f"   Página inicial: {pagina_inicial}")
    print(f"   Total de páginas: {total_paginas}")
    print(f"   Saída: {out_dir}")
    print(f"\n⏳ Você tem {PAUSA_INICIAL} segundos para:")
    print(f"   1. Colocar o Chrome em fullscreen (F11)")
    print(f"   2. Navegar para a página {pagina_inicial} do capítulo")
    print(f"   3. Clicar na janela do Chrome para dar foco")
    print(f"\n   Iniciando em...", end="", flush=True)

    for i in range(PAUSA_INICIAL, 0, -1):
        print(f" {i}", end="", flush=True)
        time.sleep(1)
    print(" 🚀\n")

    pagina_atual = pagina_inicial
    seq = 1
    shots_capturados = 0

    while pagina_atual < pagina_inicial + total_paginas:
        nome = f"{base}-p{pagina_atual:03d}-s{seq:02d}.png"
        png_path = out_dir / nome

        # Captura screenshot da tela inteira
        screenshot = pyautogui.screenshot()
        screenshot.save(str(png_path))
        shots_capturados += 1

        print(f"   📸 [{shots_capturados:3d}] {nome}", flush=True)

        # Verifica se é a última página
        if pagina_atual >= pagina_inicial + total_paginas - 1 and seq >= 2:
            break

        # PageDown
        pyautogui.press('pagedown')
        time.sleep(PAUSA_APOS_PAGEDOWN)

        # Lógica de controle: após 2 pagedowns na mesma página, avança o contador
        # O leitor avança de página automaticamente — o script acompanha
        if seq >= 2:
            pagina_atual += 1
            seq = 1
        else:
            seq += 1

    print(f"\n✅ Concluído: {shots_capturados} screenshots capturados")
    print(f"   Pasta: {out_dir}")
    return out_dir


# ──────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Captura automática do leitor Poliedro via PyAutoGUI"
    )
    parser.add_argument("--materia",  "-m", help="Prefixo da matéria (ex: bio)")
    parser.add_argument("--unidade",  "-u", help="Número da unidade (ex: 1)")
    parser.add_argument("--capitulo", "-c", help="Número do capítulo (ex: 3)")
    parser.add_argument("--de",   dest="de",     type=int, help="Página inicial do leitor")
    parser.add_argument("--paginas",  "-n", dest="paginas", type=int,
                        help="Total de páginas do capítulo a capturar")
    args = parser.parse_args()

    materia  = args.materia  or input("Matéria (ex: bio): ").strip()
    unidade  = args.unidade  or input("Unidade (ex: 1): ").strip()
    capitulo = args.capitulo or input("Capítulo (ex: 3): ").strip()
    de       = args.de       or int(input("Página inicial no leitor: ").strip())
    paginas  = args.paginas  or int(input("Total de páginas do capítulo: ").strip())

    capturar(materia, unidade, capitulo, de, paginas)


if __name__ == "__main__":
    main()
