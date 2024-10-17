from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = "secret"
todos = []

@app.before_request
def auth_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "Unauthed"}), 401
    
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def create_todo():
    title = request.json.get("title")
    if not title:
        return jsonify({"error": "No Title"}), 400
    
    todo = {
        "id": len(todos) + 1,
        "title": request.json.get("title", ""), 
        "completed": request.json.get("completed", False),
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route("/todos/<int:id>", methods=["POST"])
def update_todo(id):
    todo = next((t for t in todos if t["id"] == id), None)
    if todo is None: return jsonify({"error": "Todo not found"}), 404
    todo["title"] = request.json.get("title", todo["title"])
    todo["completed"] = request.json.get("completed", todo["completed"])  # Fixed typo here
    
    return jsonify(todo)

@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    global todos
    todos = [t for t in todos if t["id"] != id]
    return '', 204

@app.errorhandler(404)
def not_found(e): return jsonify({"error": "not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
