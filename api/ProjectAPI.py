from flask_restful import Resource
import logging as logger

class ProjectAPI(Resource):

    def get(self):

        logger.debug("Inside the get method")

        projectDetails = {
                "version" : "1.0.0.0",
                "owner" : "Selftuts",
                "projectName" : "Python Flask Docker Container"
        }


        return projectDetails,200