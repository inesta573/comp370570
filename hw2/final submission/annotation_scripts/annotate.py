import pandas as pd

df = pd.read_csv("mlp_dialogue_clean.csv")

df["addressee"] = df.groupby("episode")["speaker"].shift(-1)
df["addressee"] = df["addressee"].fillna("(end of episode)")
df.to_csv("mlp_dialogue_annotated.csv", index=False)

print(df.head(10))
print("\nRows marked end-of-episode:", (df["addressee"] == "(end of episode)").sum())
print("Should equal number of episodes:", df["episode"].nunique())
