from flask_restful import Api
from app import flaskAppInstance
from .ProjectAPI import ProjectAPI



restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(ProjectAPI,"https://www.ing.nl/api/locator/atms/")