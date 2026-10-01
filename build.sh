#!/bin/bash
myst clean -y
myst build --html
sed -i -e 's|http://localhost:3000|https://raphael.doursenaud.fr|g' $(grep -RIl "http://localhost:3000" ./_build)
