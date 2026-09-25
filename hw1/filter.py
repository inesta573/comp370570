import pandas as pd
import re

# Read only the first 10,000 rows
df = pd.read_csv("IRAhandle_tweets_1.csv", nrows=10000)

# Filter: English tweets only, and tweets that do NOT contain "?"
filtered = df[
    (df["language"] == "English") &
    (~df["content"].str.contains(r"\?", na=False))
].copy()

# Word-boundary, case-sensitive match for "Trump"
# \b matches a boundary between an alphanumeric char and a non-alphanumeric char (or string start/end)
pattern = re.compile(r"\bTrump\b")

filtered["trump_mention"] = filtered["content"].apply(
    lambda text: "T" if pattern.search(str(text)) else "F"
)

# Keep only the required columns, in the required order
dataset = filtered[["tweet_id", "publish_date", "content", "trump_mention"]]

# Save as TSV
dataset.to_csv("dataset.tsv", sep="\t", index=False)

print(f"Annotated {len(dataset)} tweets")
print(dataset["trump_mention"].value_counts())
