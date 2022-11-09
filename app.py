from flask import Flask

from routes.empresa_routes import empresa_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)
app.register_blueprint(empresa_bp)
app.register_blueprint(auth_bp)
 