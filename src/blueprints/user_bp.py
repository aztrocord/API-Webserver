from datetime import timedelta
from flask import Blueprint, request
from flask_jwt_extended import create_access_token, jwt_required
from models.user import UserSchema, User
from auth import authorize_owner
from init import db, bcrypt

#Create user
#Read user data
#Update (your own) user
#Delete user data

users_bp = Blueprint('users', __name__, url_prefix='/users')

#Log into an account
@users_bp.route('/login', methods=['POST'])
def login():
    """
    Handles user login by validating email and password, and generating a JWT token.
    """
    # Validate data from HTTP POST request from client and store it in the params variable
    params = UserSchema(only=['email', 'password']).load(request.json, unknown='exclude')

    # Create query statement looking for a user in the db with the same email as the one in params
    stmt = db.select(User).where(User.email == params['email'])

    # Excuete the SQLAlchemy query and check if that user exists, if so, check if the password is correct
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, params['password']):

        # Generate JWT authentication token for client 
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))

        # Return JWT token to client in JSON
        return {"token": token}
    else:
        return {'error': 'invalid email or password.'}, 401

# Create new user by registering an account (C)
@users_bp.route('/', methods=['POST'])
def register_user():
    """
    Handles user registration by creating a new User instance and adding it to the database.
    """
    # Validate data from HTTP POST request from client and store it in the params variable
    params = UserSchema(only=['first_name', 'last_name', 'email', 'password']).load(
        request.json,
        unknown='exclude'
    )

    # Register user account details by making a User instance from the data in params
    registered_account = User(
        first_name=params['first_name'], 
        last_name=params['last_name'], 
        email=params['email'], 
        password=params['password'])
    
    # Add the registered account to the database
    db.session.add(registered_account)
    db.session.commit()

    return UserSchema(registered_account), 201

# Read the data of all accounts in the database (R)
@jwt_required
@users_bp.route('/', methods=['GET'])
def read_users_details():
    """
    Retrieves the details of all user accounts in the database.
    Requires a valid JWT token for authentication.
    """
    account_queries = db.select(User)
    accounts = db.session.scalars(account_queries)
    return UserSchema.dump(accounts)

# Read your account details (R)
@jwt_required
@users_bp.route('/<int:id>', methods=['GET'])
def read_user_details(id):
    """
    Retrieves the details of a specific user account by their ID.
    Requires a valid JWT token for authentication.
    """
    account_query = db.select(User).where(User.id == id)
    account = db.session.scalars(account_query)
    if account:
        return UserSchema.dump(account)
    else:
        return {"Error": "Account not found"}
    
# Update your account details (R)
@jwt_required()
@users_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update_user_details(id):
    """
    Updates the details of a specific user account by their ID.
    Requires a valid JWT token for authentication and authorization.
    """
    user_account = db.get_or_404(User, id)
    # Ensure the logged-in user is authorized to update this account
    authorize_owner(user_account)

    # Load and validate the incoming data
    account_info = UserSchema(unknown="exclude").load(
        request.json
    )
    # Update the user account details
    user_account.first_name = account_info.get('first_name', user_account.first_name)
    user_account.last_name = account_info.get('last_name', user_account.last_name)
    user_account.email = account_info.get('email', user_account.email)
    user_account.undergrad_school_id = account_info.get('undergrad_school_id', user_account.undergrad_school_id)
    user_account.undergrad_major_id = account_info.get('undergrad_major_id', user_account.undergrad_major_id)
    user_account.undergrad_GPA = account_info.get('undergrad_GPA', user_account.undergrad_GPA)
    user_account.top_extracurriculars = account_info.get('top_extracurriculars', user_account.top_extracurriculars)
    user_account.gre_scores = account_info.get('gre_scores', user_account.gre_scores)
    
    # Add the updated  to the database
    db.session.commit()
    return UserSchema.dump(account_info)
