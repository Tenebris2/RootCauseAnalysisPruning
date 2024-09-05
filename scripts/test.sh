#!/bin/bash
timeout 50 $AFL_DIR/afl-fuzz -C -d -m none -i $1 -o "$AFL_WORKDIR/afl-workdir-$2/testing" -- $3 $4
