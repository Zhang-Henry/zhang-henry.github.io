#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CV_DIR="$ROOT_DIR/CV"
CV_TEX="CV_Hanrong_Zhang.tex"
CV_PDF="$CV_DIR/CV_Hanrong_Zhang.pdf"
WEB_PDF="$ROOT_DIR/assets/pdf/CV_Hanrong_Zhang.pdf"

command -v latexmk >/dev/null 2>&1 || {
  echo "latexmk is required to build the CV PDF." >&2
  exit 1
}

cd "$CV_DIR"
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error "$CV_TEX"

mkdir -p "$(dirname "$WEB_PDF")"
cp -f "$CV_PDF" "$WEB_PDF"

echo "Updated $WEB_PDF"
