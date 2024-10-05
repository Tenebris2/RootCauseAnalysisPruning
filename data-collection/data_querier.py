import pandas as pd
from enum import Enum
import matplotlib.pyplot as plt
from pprint import pprint

COLUMNS_TO_WRITE = ["Test Case", "Predicates", "SLOC"]
FILE_TO_WRITE = "stats/stats"
METHODS = ["aurora", "loc", "loc with source", "basic block"]
COMBINE_WRITETO_CSV = "stats_sum.csv"


class Columns(Enum):
    TRACING_TIME = "Tracing Time"
    TEST_CASE = "Test Case"
    PREDICATES = "Predicates"
    SLOC = "SLOC"
    TRACE_ANALYSIS_TIME = "Trace Analysis Time"
    RANKING_TIME = "Ranking Time"

    MONITORING_TIME = "Monitoring Time"
    TIME_TO_PREPARE = "Time to Prepare For Tracing"
    STEPS_TO_ROOT_CAUSE = "Steps To Root Cause"
    INSTRUCTIONS_TRACED = "Instructions Traced"
    TRACING_TIME_WITH_TIME_TO_PREPARE = "Tracing Time with Time to Prepare"
    TOTAL_TIME = "Total Time"
    PREDICATE_ANALYSIS_TIME = "PA Time"


class Method(Enum):
    AURORA = "aurora"
    LOC = "loc"
    LOC_WITH_SOURCE = "loc with source"
    BASIC_BLOCK = "basic block"


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


def apply_timedelta(df):
    time_columns = df.filter(like="Time").columns
    for col in time_columns:
        df[col] = pd.to_timedelta(df[col], unit="s").astype(str).str.split().str[-1]

    return df


def get_merged_df():
    df_arr = []
    for method in METHODS:
        df = pd.read_csv("Avg_res.csv")
        df_arr.append((df[df["Method"] == method].round(), method))

    merged_df, method = df_arr[0]

    for dfs in df_arr[1:]:
        prev_method = method
        (df, method) = dfs
        merged_df = pd.merge(
            merged_df, df, on="Test Case", suffixes=(f"_{prev_method}", f"_{method}")
        )
    merged_df = apply_timedelta(merged_df)
    return merged_df


def get_stats(*args):
    merged_df = get_merged_df()
    columns = "|".join([x.value for x in list(args)])
    filtered = merged_df.filter(regex=f"^{columns}").columns.tolist()
    filtered = list(["Test Case"]) + filtered
    pprint(merged_df[filtered])

    return merged_df[filtered]


def to_csv(df, fname: str):
    return df.to_csv(fname)


def to_tex(df, fname: str):
    with open(fname, "w") as f:
        f.write(df.to_latex(index=False))


def csv_to_latex(csv_file, tex_file):
    csv_table = pd.read_csv(csv_file)
    tex = csv_table.to_latex(index=False)
    with open(tex_file, "w") as file:
        file.write(tex)


def plot_stats(plt_name: str, *args):
    df = get_merged_df()

    columns = "|".join([x.value for x in list(args)])
    filtered = df.filter(regex=f"^{columns}").columns.tolist()

    df.plot(x="Test Case", y=filtered, kind="barh", figsize=(20, 8), logx=True)
    # plt.xticks([])  # Hides x-axis ticks
    # plt.xlabel("")  # Optionally hide the x-axis label
    plt.grid(True)
    plt.savefig(plt_name, dpi=300, bbox_inches="tight")
    plt.show()


def summary_stats(col: Columns):
    df = get_merged_df()

    filtered_cols = df.filter(regex=f"^{col.value}")
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    summary_stats = filtered_cols.describe()
    pprint(summary_stats)

    return summary_stats.describe()


summary_stats(Columns.PREDICATES)
