import pandas as pd

df = pd.read_csv("mlp_dialogue_clean.csv")

sample = df.sample(n=100, random_state=42)

sample.to_csv("sample_check.csv", index=False)
print(sample.head(10))
