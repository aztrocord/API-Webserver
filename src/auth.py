from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort, jsonify, make_response
from models.user import User
from init import db

def admin_only(fn):
    @jwt_required()
    def inner():
        user_id = get_jwt_identity()
        stmt = db.select(User).where(User.id == user_id)
        user = db.session.scalar(stmt)
        if (user and user.is_admin):
            return fn()
        else:
            return {'error': "You must be an admin to access this resource."}, 403
    
    return inner

def authorize_owner(card):
    user_id = get_jwt_identity()
    if user_id != card.user_id:
        abort(make_response(jsonify(error="You must be the card owner to access this resource"), 403))