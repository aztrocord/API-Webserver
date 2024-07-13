from marshmallow.exceptions import ValidationError
from blueprints.user_bp import users_bp
from blueprints.cli_commands_bp import db_commands
from init import app

app.register_blueprint(users_bp)
app.register_blueprint(db_commands)

@app.route('/')
def index():
    return 'hello world'

@app.errorhandler(405)
@app.errorhandler(404)
def not_found(err):
    return {'error': 'Not found'}

@app.errorhandler(ValidationError)
def invalid_request(err):
    return {'Error': vars(err)['messages']}

@app.errorhandler(KeyError)
def missing_key(err):
    return {'Error': f'Missing Field: {err}'}


if __name__ == "__main__":
    app.run(debug=True)