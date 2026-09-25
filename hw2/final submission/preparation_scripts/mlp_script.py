import pandas as pd

df = pd.read_csv("clean_dialog.csv", encoding="latin1")
df = df.dropna(subset=["dialog"])

df["content"] = (
    df["dialog"]
    .str.replace(r"<U\+0097>", "\u2014", regex=True)
    .str.replace(r"\[[^\]]*\]", "", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

out = df.rename(columns={"title": "episode", "pony": "speaker"})[
    ["episode", "speaker", "content"]
]
out.to_csv("mlp_dialogue_clean.csv", index=False)
