from flask import Flask, render_template
from config import Config
from extensions import db, socketio

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    socketio.init_app(app)

    from routes.auth_routes import auth_bp
    from routes.task_routes import task_bp

    app.register_blueprint(auth_bp)

    app.register_blueprint(task_bp)

    return app


app = create_app()


@app.route("/")
def home():

    return "Task Management System Running Successfully"


@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


if __name__ == "__main__":

    with app.app_context():

        db.create_all()

    socketio.run(app, debug=True)