objdump -dGlS $1 > trace.dump
python3 ./scripts/extract_addresses.py trace.dump

cp addresses $AURORA_GIT_DIR/tracing/scripts/ -r
