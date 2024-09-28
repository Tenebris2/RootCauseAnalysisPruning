import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

COLUMNS_TO_WRITE = ["Test Case", "Predicates", "SLOC"]
FILE_TO_WRITE = "stats/stats"
METHODS = ["aurora", "loc", "loc with source", "basic block"]
COMBINE_WRITETO_CSV = "stats_sum.csv"


def write_to_stats():
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


def get_predicates_and_loc():
    df_arr = []
    for method in METHODS:
        df = pd.read_csv("Avg_res.csv")
        df_arr.append((df[df["Method"] == method].round(), method))

    merged_df, method = df_arr[0]

    count = 0
    for dfs in df_arr[1:]:
        prev_method = method
        (df, method) = dfs
        merged_df = pd.merge(
            merged_df, df, on="Test Case", suffixes=(f"_{prev_method}", f"_{method}")
        )
        count += 1
    filtered = merged_df.filter(regex="^(Predicates|SLOC)").columns.tolist()
    filtered = list(["Test Case"]) + filtered
    pprint(merged_df[filtered])

    return merged_df[filtered]


def to_csv(df, fname: str):
    return df.to_csv(fname)


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
    with open(COMBINE_WRITETO_CSV, "w") as f:
        f.writelines(sum_contents)
    pprint(sum_contents)


def plot_stats(method):
    df = pd.read_csv("Avg_res.csv")
    df["Total_Time"] = (
        df["Trace Analysis Time"]
        + df["Monitoring Time"]
        + df["Ranking Time"]
        + df["Tracing Time"]
        + df["Time to Prepare For Tracing"]
    )
    aur_df = df[df["Method"] == "aurora"].round()
    loc_df = df[df["Method"] == "loc"].round()

    df_compare = pd.merge(aur_df, loc_df, on="Test Case", suffixes=("_aurora", "_loc"))
    #
    # df_compare["Time_Diff"] = (
    #     df_compare["Predicates_aurora"] - df_compare["Predicates_loc"]
    # )
    #
    # print(df_compare[["Test Case", "Predicates_Diff"]])

    df_compare.plot(
        x="Test Case",
        y=["Total_Time_aurora", "Total_Time_loc"],
        kind="line",
        marker="o",
    )

    plt.grid(True)

    plt.show()
    # ax = df.plot(x="Predicates", y="aurora", kind="line", marker="o")
    # ax.set_title("AURORA vs LOC")
    # ax.set_xlabel("Predicates")
    # ax.set_ylabel("SLOC")
    # ax.grid(True)
    #
    # plt.show()


# plot_stats("aurora")
to_csv(get_predicates_and_loc(), "predicates_and_loc.csv")
