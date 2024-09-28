import os
import sys

target_rca = "mat5.c:4975"
from extract_ranking import extract_ranking


DIR_PATH = sys.argv[1]


def get_target_rca_rankings(file, target_rca):
    return extract_ranking(file, target_rca)


def replace_content(ranked_predicates_path, path):
    with open(path) as file:
        content = file.readlines()
        target = content[-2:]
        content = content[:-2]

        target = [x.split(" ") for x in target]

        wanted_predicates_ranking, wanted_loc_ranking = get_target_rca_rankings(
            ranked_predicates_path, target_rca
        )
        target[0][2] = str(wanted_predicates_ranking) + "\n"
        target[1][3] = str(wanted_loc_ranking)

        target = [" ".join(x) for x in target]

    with open(path, "w") as file:
        file.writelines(content)
        file.writelines(target)


def main():
    for dirpath, dirnames, filenames in os.walk(DIR_PATH):
        if len(filenames) != 0 and len(dirnames) == 0:
            rca_results_path = ""
            ranked_predicates_path = ""
            for f in filenames:
                if f == "rca_results.txt":
                    rca_results_path = dirpath + "/" + f
                elif f == "ranked_predicates_verbose.txt":
                    ranked_predicates_path = dirpath + "/" + f
                print(dirpath)
            try:
                replace_content(ranked_predicates_path, rca_results_path)
            except:
                print("errored out at", dirpath)


main()
