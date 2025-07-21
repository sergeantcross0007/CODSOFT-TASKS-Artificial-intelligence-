import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("=== Content-Based Filtering ===")

# ---------------------------
# CONTENT-BASED FILTERING
# ---------------------------
# Step 1: Sample movie data
movies = {
    'title': ['Inception', 'Interstellar', 'The Dark Knight', 'The Prestige', 'Avengers', 'The Lion King'],
    'genres': ['Action Sci-Fi', 'Adventure Drama Sci-Fi', 'Action Crime Drama',
               'Drama Mystery Sci-Fi', 'Action Adventure Sci-Fi', 'Animation Adventure Drama']
}
movie_df = pd.DataFrame(movies)

# Step 2: TF-IDF Vectorization of genres
vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(movie_df['genres'])

# Step 3: Compute cosine similarity
cosine_sim = cosine_similarity(genre_matrix)

# Step 4: Content-based recommend function
def content_based_recommend(title, top_n=3):
    if title not in movie_df['title'].values:
        return f"Movie '{title}' not found."
    idx = movie_df[movie_df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    return [movie_df.iloc[i[0]]['title'] for i in sim_scores]

# Step 5: Try it
user_movie = 'Inception'
print(f"\nBecause you liked '{user_movie}', you might also like (Content-Based):")
for m in content_based_recommend(user_movie):
    print("✔️", m)

# ---------------------------
# COLLABORATIVE FILTERING
# ---------------------------
print("\n=== Collaborative Filtering ===")

# Step 6: User-item ratings matrix
ratings_data = {
    'User1': [5, 3, 0, 1, 0, 0],
    'User2': [4, 0, 0, 1, 0, 0],
    'User3': [1, 1, 0, 5, 0, 0],
    'User4': [1, 0, 0, 4, 0, 0],
    'User5': [0, 1, 5, 4, 4, 4],
}
items = movie_df['title'].tolist()
ratings_df = pd.DataFrame(ratings_data, index=items)

# Step 7: Cosine similarity between users
user_similarity = cosine_similarity(ratings_df.T)
user_sim_df = pd.DataFrame(user_similarity, index=ratings_df.columns, columns=ratings_df.columns)

# Step 8: Collaborative filtering function
def collaborative_recommend(user, top_n=2):
    if user not in ratings_df.columns:
        return f"User '{user}' not found."
    similar_users = user_sim_df[user].sort_values(ascending=False)[1:]
    top_sim_users = similar_users.index[:top_n]
    recommendation_scores = ratings_df[top_sim_users].mean(axis=1)
    unrated = ratings_df[user] == 0
    recommendations = recommendation_scores[unrated].sort_values(ascending=False)
    return recommendations

# Step 9: Try it
user_name = 'User1'
print(f"\nRecommendations for {user_name} (Collaborative Filtering):")
for title, score in collaborative_recommend(user_name).items():
    print(f"✔️ {title} (predicted rating: {score:.2f})")