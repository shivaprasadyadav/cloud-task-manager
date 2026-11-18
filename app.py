from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Store tasks temporarily
tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")

    if task and task.strip():
        tasks.append({
            "id": len(tasks) + 1,
            "name": task.strip(),
            "status": "Pending"
        })

    return redirect(url_for("home"))


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)