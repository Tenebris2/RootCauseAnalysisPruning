import csv
import pathlib
import os
import re
# with open("data.csv", "w", newline="") as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

eval_dir = os.environ["EVAL_DIR"]
RESULTS = f"{eval_dir}/results/readelf_trace/aurora"
PREDICATE_INDICATOR = r"Predicate Ranking:"
LOC_INDICATOR = r"LOC Ranking:"
CRASHES_AND_NON_CRASHES_INDICATOR = r"(\d+) crashes"
TRACE_ANALYSIS_INDICATOR = "trace analysis time:"
MONITORING_INDICATOR = "monitoring time:"
RANKING_INDICATOR = "ranking time:"
def extract():
    for file_path in pathlib.Path(RESULTS).rglob("*"):
        if file_path.is_file():
            method, id = (" ".join(file_path.parent.name.split("_")[:-1]), file_path.parent.name.split("_")[-1])
            testcase = file_path.parent.parent.parent.name
            
            print(f"{testcase}: {method} number {id}")
            if file_path.name == "rca_results.txt":
                collect_rca_results(file_path)
            if file_path.name == "stats.txt":
                collect_tracing_results(file_path)
        
def collect_rca_results(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        crashes = ""
        non_crashes = ""
        predicates = ""
        sloc = ""
        trace_analysis_time = ""
        monitoring_time = ""
        ranking_time = ""
        for line in lines:
            match_crashes_and_non_crashes = re.search(CRASHES_AND_NON_CRASHES_INDICATOR, line)
            if match_crashes_and_non_crashes:
                crashes = line.split(" ")[0]
                non_crashes = line.split(" ")[3]
                break
        for line in lines:
            if PREDICATE_INDICATOR in line:
                predicates = line.split(" ")[-1].strip()
            elif LOC_INDICATOR in line:
                sloc = line.split(" ")[-1].strip()
            elif TRACE_ANALYSIS_INDICATOR in line:
                trace_analysis_time = line.split(" ")[-2].strip()
            elif MONITORING_INDICATOR in line:
                monitoring_time = line.split(" ")[-2].strip()
            elif RANKING_INDICATOR in line:
                ranking_time = line.split(" ")[-2].strip()
        print(f"Crashes: {crashes}\nNon Crashes: {non_crashes}\nPredicates: {predicates}\nSLOC: {sloc}\nTrace analysis time: {trace_analysis_time}\nMonitoring time: {monitoring_time}\nRanking time: {ranking_time}")
def collect_tracing_results(file_path):
    with open(file_path, "r") as file:
        tracing_time = file.read().split(" ")[5][:-1]
        print(f"Tracing time: {tracing_time}")
extract()

# collect_rca_results("/media/ssd-partition/Documents/RootCauseAnalysisPruning/evaluation/results/readelf_trace/aurora/aurora_2/rca_results.txt")
# collect_tracing_results("/media/ssd-partition/Documents/RootCauseAnalysisPruning/evaluation/results/readelf_trace/aurora/aurora_0/stats.txt")

