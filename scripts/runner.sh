#!/bin/bash 

rm $EVAL_DIR/*_trace

cp $EVAL_DIR/test_bin/0-matio/matdump_trace $EVAL_DIR 

python3 fuzzing.py $EVAL_DIR/seed/matio_seed/  "$EVAL_DIR/test_bin/0-matio/matdump_fuzz @@"

python3 run.py "$EVAL_DIR/matdump_trace @@" "mat5.c:4975"
