from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# =====================================
# Load Saved Files
# =====================================

df = pd.read_pickle("model/df2.pkl")

with open("model/tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

with open("model/tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)

with open("model/indices.pkl", "rb") as f:
    indices = pickle.load(f)

# =====================================
# Convert numeric columns
# =====================================

if "vote_average" in df.columns:
    df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce").fillna(0)

if "popularity" in df.columns:
    df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce").fillna(0)

# =====================================
# Debug Information
# =====================================

print("\n========== DATAFRAME INFO ==========")
print(df.dtypes)

print("\n========== SAMPLE DATA ==========")
print(df.head())

print("\n===================================\n")

# =====================================
# Recommendation Function
# =====================================

def recommend(movie_name, n=10):

    if movie_name not in indices:
        return None

    idx = indices[movie_name]

    similarity = cosine_similarity(
        tfidf_matrix[idx],
        tfidf_matrix
    ).flatten()

    similar_movies = similarity.argsort()[::-1][1:n+1]

    recommendations = []

    for i in similar_movies:

        rating = pd.to_numeric(
            df.iloc[i].get("vote_average", 0),
            errors="coerce"
        )

        popularity = pd.to_numeric(
            df.iloc[i].get("popularity", 0),
            errors="coerce"
        )

        recommendations.append({

            "title": df.iloc[i].get("title", "N/A"),

            "overview": df.iloc[i].get(
                "overview",
                "No overview available."
            ),

            "genres": df.iloc[i].get(
                "genres",
                "Unknown"
            ),

            "rating": round(float(rating), 2)
            if pd.notna(rating) else 0,

            "popularity": round(float(popularity), 2)
            if pd.notna(popularity) else 0

        })

    return recommendations

# =====================================
# Home
# =====================================

@app.route("/")
def home():

    movie_list = sorted(
        df["title"].dropna().unique()
    )

    return render_template(
        "index.html",
        movies=movie_list
    )

# =====================================
# Recommendation
# =====================================

@app.route("/recommend", methods=["POST"])
def recommendation():

    movie = request.form["movie"]

    results = recommend(movie)

    if results is None:

        return render_template(
            "result.html",
            movie=movie,
            error="Movie not found."
        )

    return render_template(
        "result.html",
        movie=movie,
        results=results
    )

# =====================================
# Run App
# =====================================

if __name__ == "__main__":
    app.run(debug=True)