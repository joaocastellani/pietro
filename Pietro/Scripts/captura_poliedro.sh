#!/bin/bash
# captura_poliedro.sh — Captura automática do leitor Poliedro
# Usa Print Screen nativo do GNOME + xdotool para paginar
#
# USO:
#   ./captura_poliedro.sh bio 1 3 38 18
#   Argumentos: materia unidade capitulo pagina_inicial total_paginas
#
# ANTES DE RODAR:
#   1. Abra o Chrome no monitor 1, navegue até a página inicial do capítulo
#   2. Pressione F11 para fullscreen
#   3. Clique no Chrome para garantir foco
#   4. Rode este script no terminal do monitor 2

MATERIA=${1:-bio}
UNIDADE=${2:-1}
CAPITULO=${3:-3}
PAG_INICIAL=${4:-38}
TOTAL_PAGS=${5:-18}

BASE="${MATERIA}-${UNIDADE}-${CAPITULO}"
OUT_DIR="$HOME/Projects/Professor/Pietro/Raw/${BASE}"
SCREENSHOTS_DIR="$HOME/Pictures/Screenshots"
PAUSA_INICIAL=5
PAUSA_APOS_PRINT=1.2
PAUSA_APOS_PAGEDOWN=1.8
SHOTS_POR_PAGINA=2

mkdir -p "$OUT_DIR"

echo ""
echo "📚 Capturando: $BASE"
echo "   Página inicial: $PAG_INICIAL | Total: $TOTAL_PAGS páginas"
echo "   Saída: $OUT_DIR"
echo ""
echo "⚠️  Certifique-se que o Chrome está:"
echo "   - Em fullscreen (F11)"
echo "   - Na página $PAG_INICIAL do capítulo"
echo "   - Com foco (clicado)"
echo ""
echo -n "⏳ Iniciando em:"
for i in $(seq $PAUSA_INICIAL -1 1); do
    echo -n " $i"
    sleep 1
done
echo " 🚀"
echo ""

pagina_atual=$PAG_INICIAL
pagina_final=$((PAG_INICIAL + TOTAL_PAGS - 1))
total_shots=0

while [ $pagina_atual -le $pagina_final ]; do
    for seq in $(seq 1 $SHOTS_POR_PAGINA); do
        nome="${BASE}-p$(printf '%03d' $pagina_atual)-s$(printf '%02d' $seq).png"
        png_path="${OUT_DIR}/${nome}"

        # Captura via Print Screen nativo do GNOME
        # O GNOME salva automaticamente em ~/Pictures/Screenshots/
        ANTES=$(ls -t "$SCREENSHOTS_DIR"/*.png 2>/dev/null | head -1)
        xdotool key Print
        sleep $PAUSA_APOS_PRINT

        # Aguarda o arquivo aparecer
        TENTATIVAS=0
        while [ $TENTATIVAS -lt 10 ]; do
            DEPOIS=$(ls -t "$SCREENSHOTS_DIR"/*.png 2>/dev/null | head -1)
            if [ "$DEPOIS" != "$ANTES" ] && [ -n "$DEPOIS" ]; then
                break
            fi
            sleep 0.3
            TENTATIVAS=$((TENTATIVAS + 1))
        done

        # Move o arquivo para a pasta do projeto
        if [ -n "$DEPOIS" ] && [ "$DEPOIS" != "$ANTES" ]; then
            mv "$DEPOIS" "$png_path"
            total_shots=$((total_shots + 1))
            echo "   📸 [$total_shots] $nome"
        else
            echo "   ❌ Falha na captura da página $pagina_atual seq $seq"
        fi

        # Não pagina após último shot da última página
        if [ $pagina_atual -eq $pagina_final ] && [ $seq -eq $SHOTS_POR_PAGINA ]; then
            break
        fi

        # PageDown — envia para a janela em foco (Chrome)
        xdotool key Next
        sleep $PAUSA_APOS_PAGEDOWN
    done

    pagina_atual=$((pagina_atual + 1))
done

echo ""
echo "✅ Concluído: $total_shots screenshots"
echo "   Pasta: $OUT_DIR"
