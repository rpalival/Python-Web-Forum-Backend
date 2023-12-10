from flask import Flask, request, jsonify
import secrets 
from datetime import datetime

app = Flask(__name__)

# In-memory storage for posts
posts = {}
post_counter = 0

# Endpoint 1
# Endpoint to create a post
@app.route('/post', methods=['POST'])
def create_post():
    global post_counter
    try:
        # Parse and validate the JSON request
        data = request.get_json()
    except Exception:
        return jsonify({'err': 'Invalid JSON format'}), 400
    
    if 'msg' not in data:
        return jsonify({'err': 'Missing \'msg\' field'}), 400

    # Check if 'msg' field is not a string
    if not isinstance(data['msg'], str):
        return jsonify({'err': '\'msg\' must be a string'}), 400

    # Create a new post
    post_id = post_counter
    post_counter += 1
    key = secrets.token_urlsafe(16)  # Generate a secure random key
    timestamp = datetime.utcnow().isoformat()  # ISO 8601 timestamp in UTC

    # Store the post
    posts[post_id] = {'id': post_id, 'key': key, 'timestamp': timestamp, 'msg': data['msg']}

    # Return the post data
    return jsonify({'id': post_id, 'key': key, 'timestamp': timestamp}), 200

#Endpoint 2
@app.route('/post/<int:post_id>', methods=['GET'])
def read_post(post_id):
    # Check if the post exists
    if post_id not in posts:
        return jsonify({'err': 'Post not found'}), 404

    post = posts[post_id]
    return jsonify({'id': post_id, 'timestamp': post['timestamp'], 'msg': post['msg']}), 200

# Endpoint 3
#@app.route('/post/<int:post_id>/delete/<string:key>', methods=['DELETE'])



if __name__ == '__main__':
    app.run(debug=True)