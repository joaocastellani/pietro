#!/usr/bin/env python3
"""
montar_raw.py — Monta o arquivo [mat]-[u]-[c].md a partir dos .txt capturados
pelo captura_poliedro.py

USO:
  python3 montar_raw.py --dir Pietro/Raw/his-1-3/
  python3 montar_raw.py --materia his --unidade 1 --capitulo 3
"""

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path.home() / "Projects" / "Professor"
RAW_DIR = PROJECT_ROOT / "Pietro" / "Raw"


def montar(raw_dir: Path):
    raw_dir = Path(raw_dir)
    if not raw_dir.exists():
        print(f"❌ Pasta não encontrada: {raw_dir}")
        sys.exit(1)

    # Lê metadata se existir
    meta_files = list(raw_dir.glob("*-meta.json"))
    meta = {}
    if meta_files:
        meta = json.loads(meta_files[0].read_text())

    base = raw_dir.name  # ex: his-1-3
    out_file = RAW_DIR / f"{base}.md"

    # Coleta todos os .txt ordenados por número de página
    txt_files = sorted(raw_dir.glob("*-p*.txt"), key=lambda f: int(f.stem.split("-p")[-1]))

    if not txt_files:
        print(f"❌ Nenhum arquivo .txt encontrado em {raw_dir}")
        sys.exit(1)

    lines = []
    lines.append(f"# {base}.md — conteúdo bruto capturado")
    lines.append(f"<!-- gerado por montar_raw.py -->")
    if meta:
        lines.append(f"<!-- matéria: {meta.get('materia','')} | "
                     f"unidade: {meta.get('unidade','')} | "
                     f"capítulo: {meta.get('capitulo','')} -->")
        lines.append(f"<!-- páginas: {meta.get('pagina_inicial','')}–{meta.get('pagina_final','')} -->")
    lines.append("")

    for txt_file in txt_files:
        page_num = int(txt_file.stem.split("-p")[-1])
        text = txt_file.read_text(encoding="utf-8").strip()
        lines.append(f"<!-- pág. {page_num} -->")
        lines.append(text)
        lines.append("")

    out_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ Arquivo montado: {out_file}")
    print(f"   {len(txt_files)} páginas | {out_file.stat().st_size:,} bytes")
    return out_file


def main():
    parser = argparse.ArgumentParser(description="Monta .md a partir dos .txt capturados")
    parser.add_argument("--dir", help="Pasta com os arquivos capturados (ex: Pietro/Raw/his-1-3/)")
    parser.add_argument("--materia", "-m")
    parser.add_argument("--unidade", "-u")
    parser.add_argument("--capitulo", "-c")
    args = parser.parse_args()

    if args.dir:
        raw_dir = Path(args.dir)
        if not raw_dir.is_absolute():
            raw_dir = PROJECT_ROOT / raw_dir
    elif args.materia and args.unidade and args.capitulo:
        raw_dir = RAW_DIR / f"{args.materia}-{args.unidade}-{args.capitulo}"
    else:
        # Interativo
        m = input("Matéria: ").strip()
        u = input("Unidade: ").strip()
        c = input("Capítulo: ").strip()
        raw_dir = RAW_DIR / f"{m}-{u}-{c}"

    montar(raw_dir)


if __name__ == "__main__":
    main()
