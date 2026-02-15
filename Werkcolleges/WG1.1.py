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

# Bepalen covariantie tussen x en y per dataset
for dataset in data["dataset"].unique():
    subset = data[data["dataset"] == dataset]
    covariance = subset["x"].cov(subset["y"])
    print(f"Covariantie tussen x en y voor {dataset}: {covariance:.2f}")


# Bepalen lineair regression tussen x en y per dataset scipy
from scipy import stats

for dataset in data["dataset"].unique():
    subset = data[data["dataset"] == dataset]
    slope, intercept, r_value, p_value, std_err = stats.linregress(subset["x"], subset["y"])
    print(f"Lineaire regressie tussen x en y voor {dataset}:")
    print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}, R-squared: {r_value**2:.2f}, P-value: {p_value:.4f}, Std Err: {std_err:.2f}")

# Maken van scatterplots
g = sns.FacetGrid(data, col="dataset", col_wrap=2, height=4)
g.map_dataframe(sns.scatterplot, "x", "y")
g.set_axis_labels("X-coördinaat", "Y-coördinaat")
g.set_titles("Dataset: {col_name}")
plt.show()


# Bepalen regression line tussen x en y per dataset
g = sns.lmplot(x="x", y="y", col="dataset", data=data, height=4, aspect=1, col_wrap=2)
g.set_axis_labels("X-coördinaat", "Y-coördinaat")
g.set_titles("Dataset: {col_name}")
plt.show()


    


    


