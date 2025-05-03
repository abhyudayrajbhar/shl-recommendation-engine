import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('data.csv')
df['description'] = df['Assessment Name'] + " " + df['Test Type']

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df['description'].tolist())

def get_recommendations(query, top_k=10):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    indices = similarities.argsort()[-top_k:][::-1]
    return df.iloc[indices]
