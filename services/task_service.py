from flask import abort
from flask_restful import Resource, reqparse, fields, marshal_with
from models import TaskModel
from extensions import db
from enums.status_enum import Status

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
        tasks = TaskModel.query.order_by(TaskModel.id.desc()).all()
        return tasks

    # post method
    @marshal_with(taskFields)
    def post(self):
        args = task_args.parse_args()
        task = TaskModel(task_name = args["task_name"], status = args["status"])
        db.session.add(task)
        db.session.commit()
        tasks = TaskModel.query.order_by(TaskModel.id.desc()).all()
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

        tasks = TaskModel.query.order_by(TaskModel.id.desc()).all()
        return tasks, 200
    
    @marshal_with(taskFields)
    def delete(self, id):
        task = TaskModel.query.filter_by(id = id).first()
        if not task:
            abort(404, "Task not found")

        db.session.delete(task)
        db.session.commit()

        tasks = TaskModel.query.order_by(TaskModel.id.desc()).all()
        return tasks, 200