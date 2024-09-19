#!/bin/bash 

rm $EVAL_DIR/*_trace

cp $EVAL_DIR/test_bin/8-mruby_heap_buffer_overflow/mruby_heap_buffer_overflow_trace $EVAL_DIR 

python3 fuzzing.py $EVAL_DIR/seed/mruby_heap_buffer_overflow_seed/  "$EVAL_DIR/test_bin/8-mruby_heap_buffer_overflow/mruby_heap_buffer_overflow_fuzz @@"

python3 run.py "$EVAL_DIR/mruby_heap_buffer_overflow_trace @@" "fiber.c:208"

