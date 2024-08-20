#!/bin/bash

export AURORA_GIT_DIR="$(pwd)/aurora"
cd evaluation
export EVAL_DIR=`pwd`
export AFL_DIR=$EVAL_DIR/afl-fuzz
export AFL_WORKDIR=$EVAL_DIR/afl-workdir

export PIN_ROOT="$(pwd)/pin-3.15-98253-gb56e429b1-gcc-linux"

cd ..
