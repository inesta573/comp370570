import pandas as pd

dataset = pd.read_csv("dataset.tsv", sep="\t")

dupes = dataset[dataset["content"].duplicated(keep=False)]
dupes_sorted = dupes.sort_values("content")
print(dupes_sorted[["tweet_id", "content"]].head(20))
