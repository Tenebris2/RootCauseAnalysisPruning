import csv
import pathlib
import os
import re
# with open("data.csv", "w", newline="") as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

eval_dir = os.environ["EVAL_DIR"]
RESULTS = f"{eval_dir}/results/"
PREDICATE_INDICATOR = r"Predicate Ranking:"
LOC_INDICATOR = r"LOC Ranking:"
CRASHES_AND_NON_CRASHES_INDICATOR = r"(\d+) crashes"
def extract():
    for file_path in pathlib.Path(RESULTS).rglob("*"):
        if file_path.is_file():
            method, id = (file_path.parent.name.split("_")[0], file_path.parent.name.split("_")[1])
            testcase = file_path.parent.parent.parent.name
            print(f"{testcase}: {method} number {id}")
        
def collect_rca_results(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        crashes = ""
        non_crashes = ""
        predicates = ""
        sloc = ""
        for line in lines:
            match_crashes_and_non_crashes = re.search(CRASHES_AND_NON_CRASHES_INDICATOR, line)
            if match_crashes_and_non_crashes:
                crashes = line.split(" ")[0]
                non_crashes = line.split(" ")[3]
                break
        for line in lines:
            if PREDICATE_INDICATOR in line:
                print(line.split(" ")[-1])
            if LOC_INDICATOR in line:
                print(line.split(" ")[-1])
        print(crashes, non_crashes)
collect_rca_results("/media/ssd-partition/Documents/RootCauseAnalysisPruning/evaluation/results/matdump_trace/loc/loc_2143940427/rca_results.txt")
