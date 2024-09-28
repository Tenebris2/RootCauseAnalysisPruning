import pandas as pd
from pprint import pprint

COLUMNS_TO_WRITE = ["Test Case", "Predicates", "SLOC"]
FILE_TO_WRITE = "stats/stats"
METHODS = ["aurora", "loc", "loc with source", "basic block"]
COMBINE_WRITETO_CSV = "stats_sum.csv"


def get_stats():
    for method in METHODS:
        df = pd.read_csv("Avg_res.csv")
        df = df[df["Method"] == method].round()
        columns_to_write = ["Test Case", "Predicates", "SLOC"]
        if method == "basic block":
            df.to_csv(
                FILE_TO_WRITE + f"_basic_block.csv",
                columns=columns_to_write,
                mode="w",
                index=False,
            )
        elif method == "loc with source":
            df.to_csv(
                FILE_TO_WRITE + f"_loc_with_source.csv",
                columns=columns_to_write,
                mode="w",
                index=False,
            )
        else:
            df.to_csv(
                FILE_TO_WRITE + f"_{method}.csv",
                columns=columns_to_write,
                mode="w",
                index=False,
            )


def csv_to_latex(csv_file):
    csv_table = pd.read_csv(csv_file)
    tex = csv_table.to_latex(index=False)
    with open("instructions_traced.tex", "w") as texfile:
        texfile.write(tex)


def combine_csv():
    sum_contents = []
    for method in METHODS:
        if method == "basic block":
            with open(f"{FILE_TO_WRITE}_basic_block.csv") as file:
                contents = file.readlines()[1:]
        elif method == "loc with source":
            with open(f"{FILE_TO_WRITE}_loc_with_source.csv") as file:
                contents = file.readlines()[1:]
        else:
            with open(f"{FILE_TO_WRITE}_{method}.csv") as file:
                if method == "aurora":
                    contents = file.readlines()[1:]
                    sum_contents = contents
                    continue
                else:
                    contents = file.readlines()[1:]
        for i in range(0, len(sum_contents)):
            sum_contents[i] = sum_contents[i].strip() + " " + contents[i].strip()

    pprint(sum_contents)


# csv_to_latex("./instructions_traced_per.csv")
get_stats()
# get_instructions_per()
combine_csv()
