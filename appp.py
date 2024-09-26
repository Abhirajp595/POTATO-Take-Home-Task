from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load data (adjust path if needed)
data = pd.read_csv('correct_twitter_201904.tsv', sep='\t')

# Function to search for a term and generate aggregate results
def search_term_analysis(df, term):
    filtered_df = df[df['text'].str.contains(term, case=False, na=False)]
    if filtered_df.empty:
        return {
            'tweets_per_day': "No tweets found",
            'unique_users': 0,
            'avg_likes': 0,
            'tweet_locations': "No locations found",
            'tweets_per_hour': "No data available",
            'top_user': "No user found"
        }

    filtered_df['date'] = pd.to_datetime(filtered_df['created_at']).dt.date
    tweets_per_day = filtered_df.groupby('date').size()
    unique_users = filtered_df['author_id'].nunique()
    avg_likes = filtered_df['like_count'].mean()
    tweet_locations = filtered_df['place_id'].value_counts()
    filtered_df['hour'] = pd.to_datetime(filtered_df['created_at']).dt.hour
    tweets_per_hour = filtered_df.groupby('hour').size()
    top_user = filtered_df['author_handle'].value_counts().idxmax()

    return {
        'tweets_per_day': tweets_per_day.to_dict(),
        'unique_users': unique_users,
        'avg_likes': avg_likes,
        'tweet_locations': tweet_locations.to_dict(),
        'tweets_per_hour': tweets_per_hour.to_dict(),
        'top_user': top_user
    }

# API endpoint to handle search queries
@app.route('/search', methods=['GET'])
def search():
    term = request.args.get('term', '')
    if not term:
        return jsonify({'error': 'No search term provided'}), 400

    results = search_term_analysis(data, term)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
