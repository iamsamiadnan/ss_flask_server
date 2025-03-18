from extensions import db

# task model
class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Task(task_name = {self.task_name}, status = {self.status})"
