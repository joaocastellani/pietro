#!/bin/bash

# Uso: ./concat_screenshots.sh <prefixo> <n> [diretório]
# Exemplo: ./concat_screenshots.sh por-1-1 4

PREFIX=$1
N=$2
DIR=${3:-.}

if [[ -z "$PREFIX" || -z "$N" ]]; then
  echo "Uso: $0 <prefixo> <n_imagens_por_grupo> [diretório]"
  exit 1
fi

# Coleta e ordena os screenshots
mapfile -t FILES < <(ls "$DIR"/Screenshot_*.png 2>/dev/null | sort)

TOTAL=${#FILES[@]}
if [[ $TOTAL -eq 0 ]]; then
  echo "Nenhum Screenshot_*.png encontrado em '$DIR'"
  exit 1
fi

echo "Total de screenshots encontrados: $TOTAL"
echo "Agrupando de $N em $N..."

SEQ=1
for ((i=0; i<TOTAL; i+=N)); do
  GROUP=("${FILES[@]:i:N}")
  OUTPUT=$(printf "%s-%02d.png" "$PREFIX" "$SEQ")

  echo "Gerando $OUTPUT com ${#GROUP[@]} imagem(ns):"
  printf "  %s\n" "${GROUP[@]}"

  convert +append "${GROUP[@]}" "$OUTPUT"

  ((SEQ++))
done

echo "Concluído! $((SEQ-1)) arquivo(s) gerado(s)."
