import pandas as pd
from sklearn.cluster import KMeans

def process_data(df):
    X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

    kmeans = KMeans(n_clusters=5, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X)

    return df


def label_customer(row):
    income = row["Annual Income (k$)"]
    spending = row["Spending Score (1-100)"]

    if income > 70 and spending > 70:
        return "VIP"
    elif income > 70 and spending < 40:
        return "Potential"
    elif income < 40 and spending < 40:
        return "Low Value"
    elif income < 40 and spending > 60:
        return "Young Spenders"
    else:
        return "Average"