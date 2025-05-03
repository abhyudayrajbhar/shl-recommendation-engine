from flask import Flask, request, jsonify
from recommend import get_recommendations

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "running"})

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    query = data.get('query', '')
    if not query:
        return jsonify({"error": "No query provided"}), 400
    results = get_recommendations(query)
    recommendations = []
    for _, row in results.iterrows():
        recommendations.append({
            "assessment_name": row['Assessment Name'],
            "url": row['URL'],
            "remote_testing_support": row['Remote Testing'],
            "adaptive_support": row['Adaptive Support'],
            "duration": row['Duration'],
            "test_type": row['Test Type']
        })
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
