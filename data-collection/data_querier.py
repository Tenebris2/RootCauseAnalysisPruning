from logging import log
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
        df = pd.read_csv("Avg_res_final.csv")
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
        components = pd.to_timedelta(df[col], unit="s").dt.components
        df[col] = components.apply(
            lambda x: f"{int(x['minutes']) + int(x['hours']) * 60}:{int(x['seconds']):02}",
            axis=1,
        )
    return df


def get_merged_df():
    df_arr = []
    for method in METHODS:
        df = pd.read_csv("Avg_res_final.csv")
        df[Columns.TRACING_TIME_WITH_TIME_TO_PREPARE.value] = (
            df[Columns.TRACING_TIME.value] + df[Columns.TIME_TO_PREPARE.value]
        )
        df[Columns.PREDICATE_ANALYSIS_TIME.value] = (
            df[Columns.TRACING_TIME.value] + df[Columns.MONITORING_TIME.value]
        )
        df[Columns.TOTAL_TIME.value] = (
            df[Columns.TRACING_TIME_WITH_TIME_TO_PREPARE.value]
            + df[Columns.PREDICATE_ANALYSIS_TIME.value]
            + df[Columns.RANKING_TIME.value]
        )
        # df = apply_timedelta(df)
        df_arr.append((df[df["Method"] == method].round(), method))

    merged_df, method = df_arr[0]

    for dfs in df_arr[1:]:
        prev_method = method
        (df, method) = dfs
        merged_df = pd.merge(
            merged_df, df, on="Test Case", suffixes=(f"_{prev_method}", f"_{method}")
        )
    return merged_df


def get_stats(*args):
    merged_df = get_merged_df()
    merged_df = apply_timedelta(merged_df)
    print(merged_df.columns)
    columns = "|".join([x.value for x in list(args)])
    filtered = merged_df.filter(regex=f"^{columns}").columns.tolist()
    filtered = filtered
    pprint(merged_df[filtered])

    return merged_df[filtered]


def to_csv(df, fname: str):
    return df.to_csv(fname)


def to_tex(df):
    print(df.to_latex(index=False))


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


def plot_stats_difference(col: Columns):
    df = get_merged_df()
    df[f"{col.value}_aurora_loc"] = df[f"{col.value}_aurora"] / df[f"{col.value}_loc"]
    df[f"{col.value}_aurora_loc with source"] = (
        df[f"{col.value}_aurora"] / df[f"{col.value}_loc with source"]
    )
    df[f"{col.value}_aurora basic block"] = (
        df[f"{col.value}_aurora"] / df[f"{col.value}_basic block"]
    )
    ax = df.plot(
        x="Test Case",
        y=f"{col.value}_aurora basic block",
        figsize=(10, 4),
        label="Speedup Time of Block-based to AURORA",
    )
    ax.set_yscale("log", base=2)
    ax.set_xticklabels([])
    ax.set_xlabel("Target")
    ax.set_ylabel("Speedup")
    ax.set_yticks([1 / 2, 2, 4, 8])
    plt.savefig("overall_time_aurora_basic_block.pdf", dpi=300, bbox_inches="tight")
    plt.grid(True)
    plt.show()


def summary_stats(col: Columns):
    df = get_merged_df()

    filtered_cols = df.filter(regex=f"^{col.value}")
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    summary_stats = filtered_cols.describe()
    pprint(summary_stats)

    return summary_stats.describe()


def get_mean(col: Columns):
    df = get_merged_df()

    filtered_cols = df.filter(regex=f"^{col.value}")

    print(filtered_cols.mean())


def seconds_to_minute_seconds(time: int):
    return f"{time // 60}:{time % 60}"


def plot_circles():
    df = pd.read_csv("instruction_comparision.csv")
    class_counts = df["Class"].value_counts()

    plt.figure(figsize=(8, 6))  # Set the figure size
    plt.pie(
        class_counts,
        labels=class_counts.index,
        autopct="%1.1f%%",
        shadow=True,
        startangle=140,
    )

    plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Percentage of Classes")
    plt.savefig("percentage_plot.pdf")
    plt.show()


def tracing_time():
    to_tex(
        pd.concat(
            [
                get_stats(Columns.TEST_CASE),
                get_stats(Columns.PREDICATE_ANALYSIS_TIME),
                get_stats(Columns.RANKING_TIME),
            ],
            axis=1,
        )
    )


def predicates():
    to_tex(
        pd.concat(
            [
                get_stats(Columns.TEST_CASE),
                get_stats(Columns.PREDICATES),
                get_stats(Columns.SLOC),
            ],
            axis=1,
        )
    )


def predicates_analysis_time():
    to_tex(
        pd.concat(
            [
                get_stats(
                    Columns.TEST_CASE,
                ),
                get_stats(Columns.PREDICATE_ANALYSIS_TIME),
                get_stats(Columns.RANKING_TIME),
            ],
            axis=1,
        )
    )


# predicates_analysis_time()
# plot_stats_difference(Columns.TOTAL_TIME)
# predicates()
