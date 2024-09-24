import os
import csv
import pandas as pd


def write_to_csv():

    df = pd.read_csv("results.csv")
    id_list = df["ID"].tolist()
    method_list = df["Method"].tolist()
    pd.set_option("display.max_columns", None)
    res = (
        df.groupby(["Method", "Test Case"])
        .mean()
        .reset_index()
        .sort_values(by="Test Case")
        .reset_index()
    )

    res.to_csv("Avg_res.csv")


def groupby_method():
    methods = ["aurora", "loc", "loc_with_source", "basic block"]
    for method in methods:
        df = pd.read_csv("Avg_res.csv")
        df = df[df["Method"] == method]
        new_df = df[
            [
                "Test Case",
                "Predicates",
                "SLOC",
                "Trace Analysis Time",
                "Monitoring Time",
                "Ranking Time",
                "Tracing Time",
            ]
        ]

        print(
            f"-----------------------------------------{method}------------------------------------------------"
        )
        print(new_df)


write_to_csv()
# groupby_method()

# print(res["Predicates"], res["SLOC"])
#
# print(res["Trace Analysis Time"], res["Monitoring Time"], res["Ranking Time"], res["Tracing Time"])
