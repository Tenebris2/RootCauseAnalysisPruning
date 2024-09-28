import csv
import pathlib
import os
import re
from types import prepare_class
# with open("data.csv", "w", newline="") as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

eval_dir = os.environ["EVAL_DIR"]
RESULTS = f"{eval_dir}/results/"
PREDICATE_INDICATOR = r"Predicate Ranking:"
LOC_INDICATOR = r"LOC Ranking:"
CRASHES_AND_NON_CRASHES_INDICATOR = r"(\d+) crashes"
TRACE_ANALYSIS_INDICATOR = "trace analysis time:"
MONITORING_INDICATOR = "monitoring time:"
RANKING_INDICATOR = "ranking time:"
TIME_INDICATOR = "real"
SOURCE_TIME_INDICATOR = "elapsed"
def extract():
    # (crashes, non_crashes, predicates, sloc, trace_analysis_time, monitoring_time, ranking_time)
    total_results_from_running_test_cases = [["Test Case", "Method", "ID", "Crashes", "Non Crashes", "Predicates", "SLOC","Trace Analysis Time", "Monitoring Time", "Ranking Time", "Tracing Time",  "Instructions Traced", "Total Instructions", "Time to Prepare For Tracing"]]

    for dirpath, dirnames, filenames in os.walk(RESULTS):
        if len(filenames) != 0 and len(dirnames) == 0:
            row = []
            method, id = (" ".join(dirpath.split("/")[-1].split("_")[:-1]), dirpath.split("/")[-1].split("_")[-1])
            testcase = dirpath.split("/")[-3]
            rca_res = ""
            tracing_time = ""
            instructions_traced = ""
            total_instructions = ""
            time = ""
            row.append(testcase)
            row.append(method)
            row.append(id)
                       
            for f in filenames:
                if f == "rca_results.txt":
                    rca_results_path = dirpath + "/" +f
                    rca_res = collect_rca_results(rca_results_path)
                elif f == "stats.txt":
                    trace_results_path = dirpath + "/" + f
                    tracing_time = collect_tracing_results(trace_results_path)
                elif f == "hitcount.out":
                    hitcount_results_path = dirpath + "/" + f
                    instructions_traced, total_instructions = collect_hitcount(hitcount_results_path)
                elif f == "decompiling_execution_time.txt":
                    prepare_time_path = dirpath + "/" + f 
                    time = collect_time_to_prepare_address(prepare_time_path)
                elif f == "source_code_extraction_time.txt":
                    prepare_time_path = dirpath + "/" + f 
                    time = collect_time_to_extract_address_from_source(prepare_time_path)
            if method == "aurora" or method == "basic block":
                time = 0
            for dat in rca_res:
                row.append(dat)
            row.append(tracing_time)
            row.append(instructions_traced)
            row.append(total_instructions)
            row.append(time)
            total_results_from_running_test_cases.append(row)
    return total_results_from_running_test_cases
def write_to_csv(data):
    with open("results.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
        
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
                trace_analysis_time = round(float(line.split(" ")[-2].strip()), 2)
            elif MONITORING_INDICATOR in line:
                monitoring_time = round(float(line.split(" ")[-2].strip()), 2)
            elif RANKING_INDICATOR in line:
                ranking_time = round(float(line.split(" ")[-2].strip()), 2)
        return (crashes, non_crashes, predicates, sloc, trace_analysis_time, monitoring_time, ranking_time)
def collect_tracing_results(file_path):
    with open(file_path, "r") as file:
        tracing_time = file.read().split(" ")[5][:-1]
        return round(float(tracing_time), 2)
def collect_hitcount(file_path):
    with open(file_path, "r") as file:
        data = [[y.strip() for y in x.split("/")] for x in file.readlines()]
        sum_x = 0
        sum_y = 0

        size = len(data)
        for dat in data:
            try:
                x = int(dat[0])
                y = int(dat[1])

                sum_x += x
                sum_y += y
            except ValueError:
                continue

        return (sum_x // size, sum_y // size)
def collect_time_to_prepare_address(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        for l in lines:
            if TIME_INDICATOR in l:
                time = l.split("\t")[1].split("m")
                min = time[0]
                seconds = time[1].strip()[:-1]
                total_time = int(min) * 60 + float(seconds)
                return total_time
def collect_time_to_extract_address_from_source(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        line = lines[0].split(" ")
        for l in line:
            if SOURCE_TIME_INDICATOR in l:
                min = int(l[:-7].split(":")[0])
                seconds = float(l[:-7].split(":")[1])
                return min + seconds
write_to_csv(extract())

# collect_time_to_extract_address_from_source("/media/ssd-partition/Documents/RootCauseAnalysisPruning/evaluation/results/readelf_trace/loc_with_source/loc_with_source_0/source_code_extraction_time.txt")

