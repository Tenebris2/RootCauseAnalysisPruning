#!/bin/bash 

rm $EVAL_DIR/*_trace

cp $EVAL_DIR/test_bin/9-mruby_uninitialized_variable/mruby_uninitialized_variable_trace $EVAL_DIR 

python3 fuzzing.py $EVAL_DIR/seed/mruby_uninitialized_variable_seed/  "$EVAL_DIR/test_bin/9-mruby_uninitialized_variable/mruby_uninitialized_variable_fuzz @@"

python3 run.py "$EVAL_DIR/mruby_uninitialized_variable_trace @@" "pack.c:802"

