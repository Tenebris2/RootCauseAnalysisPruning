import os
import csv
import pandas as pd

df = pd.read_csv("results.csv")
id_list = df["ID"].tolist() 
method_list = df["Method"].tolist()
pd.set_option('display.max_columns', None)
res = df.groupby(["Method", "Test Case"]).mean().reset_index().sort_values(by="Test Case").reset_index()

res.to_csv("Avg_res.csv")
# print(res["Predicates"], res["SLOC"])
#
# print(res["Trace Analysis Time"], res["Monitoring Time"], res["Ranking Time"], res["Tracing Time"])

