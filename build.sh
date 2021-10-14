#!/usr/bin/env bash

cp ../rlzero/examples/chase_game/*.py chapters/programs/
cp ../rlzero/examples/*.py chapters/programs
make latexpdf
make html
rm -rf docs
mv _build/html/ docs
touch docs/.nojekyll
mv _build/latex/learntocodewithpythonandraylib.pdf docs