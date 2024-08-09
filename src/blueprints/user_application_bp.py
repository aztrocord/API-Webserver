from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.user_application import ApplicationSchema, Application, School, SchoolSchema
from auth import  authorize_application_owner
from init import db, bcrypt

application_bp = Blueprint('applications', __name__, url_prefix='/applications')

# Create a new application (C)
@application_bp.route('/', methods=['POST'])
@jwt_required()
def create_application():
    """
    Handles the creation of new applications by creating a new application 
    instance and adding it to the database.
    """
    # Validate data from HTTP POST request from client and store it in the params variable.
    params = ApplicationSchema(only=['status', 'school_id', 'major_id', 'user_id']).load(
        request.json,
        unknown='exclude'
    )

    # Register new application by making an application instance from the data in params.
    new_application = Application(
            status=params['status'],
            school_id=params['school_id'],
            major_id=params['major_id'],
            user_id=params['user_id']
        )

    # Add the new application to the database.
    db.session.add(new_application)
    db.session.commit()

    # Return the new application as a JSON reponse to the client.
    return ApplicationSchema(new_application), 201

# Read all applications in the database (R)
@application_bp.route('/<str:school_name>/<str:application_status>', methods=['GET'])
@jwt_required()
def read_all_applications(school_name, application_status):
    """
    Retrieves the details of all applications in the database.
    Requires a valid JWT token for authentication.
    """
    if not application_status or not school_name:
        # Create a query to select all applications in the database and execute it.
        application_queries = db.select(Application)
        applications = db.session.scalars(application_queries).all()

        # Return all applications in the database to the client in JSON.
        return ApplicationSchema(many=True).dump(applications)
    
    elif school_name and application_status == "accepted":
        # Create a query to select all applications with an accepted status for a particular school
        school_query = db.select(School).where(School.name == school_name)
        school_obj = db.session_scalar(school_query)

        if school_obj:
            # Find applications accepted into the chosen school in the URL
            application_queries = db.select(Application).where(Application.school_id == school_obj.id)
            applications = db.session.scalars(application_queries).all()


            # Return all curated applications in the database to the client in JSON.
            return ApplicationSchema(many=True).dump(applications)
        else:
            return {"School not found": "Try changing the school name"}

# Read your own applications (R)
@application_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def read_application(id):
    """
    Retrieves the details of a specific application by their ID.
    Requires a valid JWT token for authentication.
    """
    # Find the application in the application database with the same ID as the URL.
    application_query = db.select(Application).where(Application.id == id)
    application = db.session.scalar(application_query)

    if application:
        # if the application exists, return it as a JSON reponse to the client.
        return ApplicationSchema().dump(application)
    else:
        # if the application doesn't exist, send a JSON reponse to the client that it wasn't found.
        return {"Error": "Application not found"}, 404
    
# Update your application (U)
@application_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_application(id):
    """
    Updates the details of a specific application by their ID.
    Requires a valid JWT token by owner for authentication and authorization.
    """
    # Find the application in the application database with the same ID as the URL.
    application_query = db.select(Application).where(Application.id == id)
    application = db.session.scalar(application_query)

    # Ensure the logged-in user is authorized to update this application.
    authorize_application_owner(application)

    # Load and validate the incoming data.
    application_info = ApplicationSchema().load(
        request.json
    )
    # Update the application details.
    application.status = application_info.get('status', application.status)
    application.school_id = application_info.get('school_id', application.school_id)
    application.major_id = application_info.get('major_id', application.major_id)
    application.user_id = application_info.get('user_id', application.user_id)
    application.degree_id = application_info.get('degree_id', application.degree_id)
    
    # Add the updated application details to the database.
    db.session.commit()

    # Return the updated application as a JSON reponse to the client.
    return ApplicationSchema().dump(application)

# Delete your application (D)
@application_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_application(id):
    """
    Deletes a specific user's application based on their ID.
    Requires a valid JWT token by owner for authentication and authorization.
    """
    # Find the application in the application database with the same ID as the URL
    application_query = db.select(Application).where(Application.id == id)
    application = db.session.scalar(application_query)

    # Ensure the logged-in user is authorized to delete this application
    authorize_application_owner(application)
    
    # Delete the application by committing changes to the database
    db.session.delete(application)
    db.session.commit()
    
    # Return a JSON reponse to the client that the application has been deleted
    return {"message": "Application deleted successfully"}
