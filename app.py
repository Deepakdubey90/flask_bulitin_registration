from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter

# Use a Class-based config to avoid needing a 2nd file
# os.getenv() enables configuration through OS environment variables

# Setup Flask app and app.config
app = Flask(__name__)
app.config.from_pyfile('env_settings.py')
port= app.config['PORT_NUMBER']
debug_flag= app.config['DEBUG_FLAG']

# Initialize Flask extensions
db = SQLAlchemy(app)                            # Initialize Flask-SQLAlchemy
mail = Mail(app)                                # Initialize Flask-Mail


def create_app():
    """ Flask application """

    from models import User
    # Setup Flask-User
    db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
    user_manager = UserManager(db_adapter, app)     # Initialize Flask-User

    # The Home page is accessible to anyone
    @app.route('/')
    def home_page():
        return render_template("base.html")
    return app

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

# Start development web server on port 5000
if __name__=='__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=port, debug=debug_flag)