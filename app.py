from flask import Flask, render_template, request
import pandas as pd
from model import process_data, label_customer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    df = pd.read_csv(file)

    df = process_data(df)

    df["Segment"] = df.apply(label_customer, axis=1)

    segment_counts = df["Segment"].value_counts().to_dict()

    # prepare chart data
    income = df["Annual Income (k$)"].tolist()
    spending = df["Spending Score (1-100)"].tolist()
    clusters = df["Cluster"].tolist()

    return render_template(
        "index.html",
        segments=segment_counts,
        income=income,
        spending=spending,
        clusters=clusters
    )


if __name__ == "__main__":
    app.run(debug=True)