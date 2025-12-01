from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

task = [
    {"name": "Task 1", "completed": False},
    {"name": "Task 2", "completed": False},
    {"name": "Task 3", "completed": False}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=task)

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('newTask')
    if new_task:
        task.append({"name": new_task, "completed": False})
    return redirect(url_for('index'))

@app.route('/complete', methods=['POST'])
def complete_tasks():
    completed_indexes = request.form.getlist('taskCheckbox')
    for t in task:
        t["completed"] = False
    for idx in completed_indexes:
        index = int(idx)
        task[index]["completed"] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_task(index):
    if 0 <= index < len(task):
        task.pop(index)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)