from flask import Flask, request, jsonify
import secrets
from datetime import datetime

app = Flask(__name__)

# In-memory storage for posts
posts = {}
post_counter = 0

# Endpoint to create a post
@app.route('/post', methods=['POST'])
def create_post():
    global post_counter
    try:
        # Parse and validate the JSON request
        data = request.get_json()
        if not data or 'msg' not in data or not isinstance(data['msg'], str):
            return jsonify({'err': 'Bad request'}), 400

        # Create a new post
        post_id = post_counter
        post_counter += 1
        key = secrets.token_urlsafe(16)  # Generate a secure random key
        timestamp = datetime.utcnow().isoformat()  # ISO 8601 timestamp in UTC

        # Store the post
        posts[post_id] = {'id': post_id, 'key': key, 'timestamp': timestamp, 'msg': data['msg']}

        # Return the post data
        return jsonify({'id': post_id, 'key': key, 'timestamp': timestamp}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'err': f'Unexpected error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)