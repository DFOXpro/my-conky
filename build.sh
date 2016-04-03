#!/usr/bin/env bash
python -m compileall src/
mv src/*.pyc build/.conkycolors/
chmod +x build/.conkycolors/*.pyc