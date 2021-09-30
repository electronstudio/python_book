cp ../richlib/examples/chase_game/*.py chapters/programs/
cp ../richlib/examples/*.py chapters/programs
make latexpdf
make html
rm -rf docs
mv _build/html/ docs
touch docs/.nojekyll
mv _build/latex/learntocodewithpythonandraylib.pdf docs