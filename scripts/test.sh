#!/bin/bash
timeout 5 $AFL_DIR/afl-fuzz -C -d -m none -i "$EVAL_DIR/inputs/input-$1" -o "$AFL_WORKDIR/afl-workdir-$2/testing" -- $3
