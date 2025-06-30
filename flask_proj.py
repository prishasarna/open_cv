from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

users = [
    {'id': 101, 'name': "Prisha", "email": "radharay@gmail.com"},
    {'id': 102, 'name': "Scott", "email": "scott@gmail.com"}
]

@app.route('/')
def home():
    return jsonify({
        'message': "Welcome to the GET API",
        'timestamp': datetime.now().isoformat(),
        'endpoints': {
            "GET /": "Welcome message",
            "GET /users": "Get all users",
            "GET /users/<id>": "Get user by ID"
        }
    })

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({
        'users': users,
        "count": len(users)
    })

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': "user not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'name' not in data or 'email' not in data:
        return jsonify({'error': "Missing 'name' or 'email'"}), 400
    new_user = {
        'id': max((u['id'] for u in users), default=100) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "user not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "no data provided"}), 400
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": f"User {user_id} deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
