import pandas as pd
from sklearn.cluster import KMeans

def process_data(df):
    X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

    kmeans = KMeans(n_clusters=5, random_state=42)
    df["Cluster"] = kmeans.fit_predict(X)

    return df


def label_customer(cluster):
    if cluster == 2:
        return "VIP"
    elif cluster == 1:
        return "Potential"
    elif cluster == 0:
        return "Average"
    elif cluster == 3:
        return "Low Value"
    elif cluster == 4:
        return "Young Spenders"