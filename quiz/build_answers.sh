#!/usr/bin/env bash

cp chars_with_answers.txt chars.txt
make clean
export SPHINXOPTS="-t answer"
make latexpdf
