from flask import Blueprint
from services import Task, Tasks
from flask_restful import Api

main = Blueprint('main', __name__)

api = Api(main)

api.add_resource(Tasks, '/api/tasks/')
api.add_resource(Task, '/api/tasks/<int:id>')