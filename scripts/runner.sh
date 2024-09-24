#!/bin/bash 

rm $EVAL_DIR/*_trace

cp $EVAL_DIR/test_bin/21-mruby_use_after_free/mruby_use_after_free_trace $EVAL_DIR 

python3 fuzzing.py $EVAL_DIR/seed/mruby_use_after_free_seed/  "$EVAL_DIR/test_bin/21-mruby_use_after_free/mruby_use_after_free_fuzz @@"

python3 run.py "$EVAL_DIR/mruby_use_after_free_trace @@" "object.c:401"

