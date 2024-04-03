from flask import Flask, jsonify, request
from tasks_module import load_tasks, get_task_by_id, delete_task, create_task, update_task, save_tasks

app = Flask(__name__)

@app.route("/Tasks", methods=['GET'])
def get_tasks():
    all_tasks = load_tasks()
    return jsonify(all_tasks)

@app.route("/Tasks/<int:task_id>", methods=['GET'])
def get_single_task(task_id):
    all_tasks = load_tasks()
    task = get_task_by_id(all_tasks, task_id)
    if task:
        return jsonify(task)
    else:
        return jsonify({"error": "Task not found"}), 404

@app.route("/Tasks/<int:task_id>", methods=['DELETE'])
def delete_task_api(task_id):
    all_tasks = load_tasks()
    delete_task(all_tasks, task_id)
    save_tasks(all_tasks)
    return jsonify({"message": "Task deleted successfully"})

@app.route("/Tasks", methods=['POST'])
def create_task_endpoint():
    data = request.get_json()
    all_tasks = load_tasks()
    new_task = create_task(data, all_tasks)
    all_tasks.append(new_task)
    save_tasks(all_tasks)
    return jsonify(new_task), 201

@app.route("/Tasks/<int:task_id>", methods=['PUT'])
def put_task(task_id):
    data = request.get_json()
    all_tasks = load_tasks()
    task = get_task_by_id(all_tasks, task_id)
    if task:
        updated_task = update_task(task, data)
        save_tasks(all_tasks)
        return jsonify(updated_task)
    else:
        return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)