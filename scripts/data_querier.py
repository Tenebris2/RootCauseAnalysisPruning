import pandas as pd


def get_aurora_stats():
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


def get_instructions_per():

    methods = ["aurora", "loc", "loc with source", "basic block"]
    first = True
    for method in methods:

        df = pd.read_csv("Avg_res.csv")
        df = df[df["Method"] == method]
        df[["Test Case", "Instructions Traced", "Total Instructions"]] = df[
            ["Test Case", "Instructions Traced", "Total Instructions"]
        ].round()

        columns_to_write = ["Test Case", "Instructions Traced", "Total Instructions"]
        if first == True:
            first = False
            df.to_csv(
                "instructions_traced_per.csv",
                columns=columns_to_write,
                mode="w",
                index=False,
            )
            print(1)
        else:
            df.to_csv(
                "instructions_traced_per.csv",
                columns=columns_to_write,
                mode="a",
                index=False,
                header=False,
            )
            print(0)
        print(
            f"-----------------------------------------{method}------------------------------------------------"
        )
        print(df)


def csv_to_latex(csv_file):
    csv_table = pd.read_csv(csv_file)
    tex = csv_table.to_latex(index=False)
    with open("instructions_traced.tex", "w") as texfile:
        texfile.write(tex)


csv_to_latex("./instructions_traced_per.csv")

# get_instructions_per()
