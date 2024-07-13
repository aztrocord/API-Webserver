from blueprints.user_bp import users_bp
from blueprints.cli_commands_bp import db_commands
from init import app

app.register_blueprint(users_bp)
app.register_blueprint(db_commands)

@app.route('/')
def index():
    return 'hello world'

if __name__ == "__main__":
    app.run(debug=True)