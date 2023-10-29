from flask import Flask
from flask import g
from flask_login import user_loaded_from_request
from flask.sessions import SecureCookieSessionInterface
from flask_migrate import Migrate
from flask_login import LoginManager
import models
from routes import user_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vZK7siKrV8BL46KsyAIPoQ'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/pingu/serviceorientedarchitecture/project/user/database/user.db'
models.init_app(app)
app.register_blueprint(user_blueprint)
login_manager = LoginManager(app)
migrate = Migrate(app, models.db)


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(id=user_id).first()


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        user = models.User.query.filter_by(api_key=api_key).first()
        if user:
            return user
    return None

class CustomSessionInterface(SecureCookieSessionInterface):
    """Prevent creating session from API requests."""

    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args, **kwargs)

app.session_interface = CustomSessionInterface()

@user_loaded_from_request.connect
def user_loaded_from_request(self, user=None):
    g.login_via_request = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)