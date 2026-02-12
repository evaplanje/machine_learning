import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Inladen data
data = pd.read_csv("Werkcolleges/datasets.csv")

# Datasets opvragen
print("Aantal datasets:", data["dataset"].nunique())
print("Namen van datasets:", data["dataset"].unique())

# Per dataset informatie
print(data.groupby("dataset").agg(['count','mean','var','std']))

# Visualiseren X coordinaten dataset
sns.violinplot(x="dataset", y="x", data=data)
plt.title("Verdeling van X-coördinaten per dataset")
plt.xlabel("Dataset")
plt.ylabel("X-coördinaat")
plt.show()

# Visualiseren Y coordinaten dataset
sns.violinplot(x="dataset", y="y", data=data)
plt.title("Verdeling van Y-coördinaten per dataset")
plt.xlabel("Dataset")
plt.ylabel("Y-coördinaat")
plt.show()

# Bepalen correlatie tussen x en y per dataset
for dataset in data["dataset"].unique():
    subset = data[data["dataset"] == dataset]
    correlation = subset["x"].corr(subset["y"])
    print(f"Correlatie tussen x en y voor {dataset}: {correlation:.2f}")