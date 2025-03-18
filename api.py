
from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy

from flask_restful import Resource, Api, reqparse, fields, marshal_with

from status_enum import Status

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.priixfefmlsfneulxpna:yJ0aygmzdpNWiOy5@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'



db = SQLAlchemy(app)
api = Api(app)



# task model
class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Task(task_name = {self.task_name}, status = {self.status})"

# will use this to validate when receiving request
task_args = reqparse.RequestParser()
task_args.add_argument('task_name', type=str, required=True, help="Task cannot be blank")
task_args.add_argument('status', type=str, required=True, help="Status cannot be blank")


# prepare format
taskFields = {
    'id': fields.Integer,
    'task_name': fields.String,
    'status': fields.String
}

# making actual api begins here
# tasks service
class Tasks(Resource):

    # get method
    @marshal_with(taskFields)
    def get(self):
        tasks = TaskModel.query.all()
        return tasks

    # post method
    @marshal_with(taskFields)
    def post(self):
        args = task_args.parse_args()
        task = TaskModel(task_name = args["task_name"], status = args["status"])
        db.session.add(task)
        db.session.commit()
        tasks = TaskModel.query.all()
        return tasks, 201
    
class Task(Resource):

    # by id
    @marshal_with(taskFields)
    def get(self, id):
        task = TaskModel.query.filter_by(id = id).first()
        if not task:
            abort(404, "Task not found")
        return task
    
    @marshal_with(taskFields)
    def patch(self, id):
        targs = task_args.copy()
        # removes task_name as arg (say only updating status)
        targs.remove_argument('task_name')
        args = targs.parse_args() # .parse_args() is important before accessing

        task = TaskModel.query.filter_by(id = id).first()
        if not task:
            abort(404, "Task not found")
        
        # only allows 'not started', 'in progress' and 'done'
        if(args["status"].upper() not in Status._value2member_map_):
            abort(400)
            
        task.status = args["status"]

        db.session.commit()

        return task
    
    @marshal_with(taskFields)
    def delete(self, id):
        task = TaskModel.query.filter_by(id = id).first()
        if not task:
            abort(404, "Task not found")

        db.session.delete(task)
        db.session.commit()

        tasks = TaskModel.query.all()
        return tasks, 200
    
# tasks api
api.add_resource(Tasks, '/api/tasks/')
api.add_resource(Task, '/api/tasks/<int:id>')

@app.route('/')
def home():
    return '<h1>Hi</h1>'


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)