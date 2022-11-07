from flask import Flask

from routes.empresa_routes import empresa_bp

app = Flask(__name__)
app.register_blueprint(empresa_bp)

 