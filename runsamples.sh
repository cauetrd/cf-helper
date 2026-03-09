#!/bin/bash

# load config

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

set -a
source "$SCRIPT_DIR/config.txt"
set +a
PROB=$1

if [ -z "$PROB" ]; then
    echo "Usage: ./runsamples.sh <problem>"
    exit 1
fi

# defaults if not in config
MODE=${MODE:-MULTIFILE}
SINGLEFILE=${SINGLEFILE_PATH:-main.cpp}
COMPILER_FLAGS=${COMPILER_FLAGS:-g++ -std=c++17}
INPUT_OUTPUT_DIR=${INPUT_OUTPUT_DIR:-ins_outs}
PROBLEMS_DIR=${PROBLEMS_DIR}

echo "Running problem $PROB"
echo "Mode: $MODE"

# choose source file
if [ "$MODE" = "MULTIFILE" ]; then
    SRC="$PROBLEMS_DIR$PROB.cpp"
else
    SRC="$SINGLEFILE"
fi

if [ ! -f "$SRC" ]; then
    echo "ERROR: source file $SRC not found"
    exit 1
fi

# compile

$COMPILER_FLAGS "$SRC" -o run

if [ $? -ne 0 ]; then
    echo "Compilation failed"
    exit 1
fi

# run sample
./run < "$INPUT_OUTPUT_DIR/in$PROB.txt" > output.txt

# compare
if diff -q output.txt "$INPUT_OUTPUT_DIR/out$PROB.txt" >/dev/null; then
    echo "OK"
else
    echo "Wrong Answer"
    echo "Expected:"
    cat "$INPUT_OUTPUT_DIR/out$PROB.txt"
    echo
    echo "Got:"
    cat output.txt
fi