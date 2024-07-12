from blueprints.user_bp import users_bp
from init import app

app.register_blueprint(users_bp)

@app.route('/')
def index():
    return 'hello world'

if __name__ == "__main__":
    app.run(debug=True)