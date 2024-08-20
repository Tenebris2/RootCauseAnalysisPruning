#!/bin/bash

# Define directories
AFL_WORKDIR="{$PWD}"+ "/afl_workdir"
EVAL_DIR=$PWD

# Define sample sizes
queue_files=($(find "$AFL_WORKDIR/queue" -type f))
total_queue_files=${#queue_files[@]}
sample_size_queue=$((total_queue_files / 2))

non_crash_files=($(find "$AFL_WORKDIR/non_crashes" -type f))
total_non_crash_files=${#non_crash_files[@]}
sample_size_non_crash=$((total_non_crash_files / 2))

QUEUE_SAMPLE_SIZE=$sample_size_queue        # Number of files to sample from queue
NON_CRASH_SAMPLE_SIZE=$sample_size_non_crash    # Number of files to sample from non_crashes

echo $QUEUE_SAMPLE_SIZE
echo $NON_CRASH_SAMPLE_SIZE
# Sample files from queue and move them to the respective directories
find "$AFL_WORKDIR/queue" -type f | shuf | head -n "$QUEUE_SAMPLE_SIZE" | while read -r file; do
    cp "$file" "$EVAL_DIR/inputs/crashes"
done

# Sample files from non_crashes and move them to the respective directories
find "$AFL_WORKDIR/non_crashes" -type f | shuf | head -n "$NON_CRASH_SAMPLE_SIZE" | while read -r file; do
    cp "$file" "$EVAL_DIR/inputs/non_crashes"
done
