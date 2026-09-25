import pandas as pd

dataset = pd.read_csv("dataset.tsv", sep="\t")

frac = (dataset["trump_mention"] == "T").mean()
frac_rounded = round(frac, 3)

print(f"Fraction of tweets mentioning Trump: {frac_rounded}")

results = pd.DataFrame({
    "result": ["frac-trump-mentions"],
    "value": [frac_rounded]
})
results.to_csv("results.tsv", sep="\t", index=False)
