#!/bin/bash

echo "🧹 Nettoyage..."
myst clean -y

echo "🏗️ Assemblage du site…"
myst build --html

echo "🔄 Correction des URLs locales vers la production…"
sed -i -E 's|http://localhost:3[0-9]{3}|https://raphael.doursenaud.fr|g' \
    "$(grep -REl "http://localhost:3[0-9]{3}" ./_build)"

echo "🚀 Synchronisation…"
rsync -av --delete \
    _build/html/ experiences:sites/raphael.doursenaud.fr/

echo "✅ Prêt : https://raphael.doursenaud.fr"
