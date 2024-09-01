import enum
import os
import shutil
import subprocess
import sys
from enum import Enum
from extract_ranking import extract_ranking
eval_dir = os.getenv("EVAL_DIR")
aurora_git_dir = os.getenv("AURORA_GIT_DIR")
afl_workdir = os.getenv("AFL_WORKDIR")
afl_dir = os.getenv("AFL_DIR")

pin_root = os.getenv("PIN_ROOT")
method_dir = os.getenv("METHOD_DIR")
args = sys.argv[1]

fpath = args.split("/")

if len(fpath) > 1:
 fpath = f"{eval_dir}/results/{fpath[len(fpath)  - 1]}"

aurora_path = f"{fpath}/aurora/"
loc_path = f"{fpath}/loc/"
loc_with_source_path = f"{fpath}/loc_with_source"
basic_block_path = f"{fpath}/basic_block/"
script_path = f"{aurora_git_dir}/tracing/scripts"
traces_path = f"{eval_dir}/traces"
rca_path = f"{aurora_git_dir}/root_cause_analysis"
paths = [aurora_path, loc_path, loc_with_source_path, basic_block_path]
for path in paths:
    os.makedirs(path, exist_ok=True)
paths = [aurora_path, loc_path, loc_with_source_path, basic_block_path]

class Method(Enum):
    AURORA = "default_tracing/aurora_tracer.cpp"
    LOC = "map_tracing/aurora_tracer.cpp"
    BASIC_BLOCK = "jump_tracing/aurora_tracer.cpp"

# results -> stats from traces, predicate ranking, line ranking, rca time 

# aurora 
def run_aurora():
    trace(aurora_path)
    root_cause_analysis(aurora_path)

def run_loc():

    pass
def run_loc_with_source():
    pass
def run_basic_block():
    pass

def trace(res_path):
    clean_previous_run()

    trace_cmd = f"python3 {script_path}/tracing.py {args} {eval_dir}/inputs {eval_dir}/traces"
    print(trace_cmd)

    get_addr = f"python3 {script_path}/addr_ranges.py --eval_dir {eval_dir} {traces_path}"

    print(get_addr)
    try:
        shutil.move(f"{traces_path}/stats.txt", res_path)
        print(f"File moved from {traces_path} to {res_path}")
    except FileNotFoundError:
        print(f"Error: the file {traces_path} does not exist")

def clean_previous_run():
    try:
        rm_traces_cmd = f"rm -rf {traces_path}/*"
        print(rm_traces_cmd)
        os.remove(f"{eval_dir}/ranked_predicates_verbose.txt")
        print("Cleaned")
    except FileNotFoundError:
        print("File ranked_predicates_verbose.txt not found")
def root_cause_analysis(res_path: str):
    clean_previous_run()
    # run rca
    rca_cmd = f"cargo run --release --bin rca -- --eval-dir {eval_dir} --trace-dir {eval_dir} --monitor --rank-predicates"
    # enrich
    addr2bin_cmd = f"cargo run --release --bin addr2line -- --eval-dir {eval_dir}"
    result = subprocess.run(rca_cmd, shell=True, text=True, capture_output=True, cwd=rca_path)
    subprocess.run(addr2bin_cmd, shell=True, text=True, capture_output=True,cwd=rca_path)
    
    predicate_rank, line_rank = extract_ranking(f"{eval_dir}/ranked_predicates_verbose.txt", "mat5.c:4975")

    with open(f"{res_path}/rca_results.txt", "a") as file:
        file.write(result.stdout)
        file.write(result.stderr)
        file.write(f"Predicate Ranking: {predicate_rank}\n LOC Ranking: {line_rank}")

def set_method(method: Method, with_source: bool):
    setup_method_cmd = f"{method_dir}/setup_method.sh " + method.value
    if method is Method.AURORA:
        print(setup_method_cmd)
    elif method is Method.LOC:
        if with_source is False:
            setup_address_cmd = f"./setup.sh " + args
            print(setup_address_cmd)
        else:
            setup_address_cmd = f"./extract.sh " + args
            print(setup_address_cmd)
            result = subprocess.run(setup_address_cmd, shell=True, text=True, capture_output=True, cwd="./source-code-extractor/")
            print(result.stdout, result.stderr)
set_method(Method.LOC, True)
