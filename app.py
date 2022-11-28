from flask import Flask
from flask_cors import CORS

#, cross_origin
#Caso não ser certo utiliza o @cross_origin() abaixo dos @ , 

from routes.empresa_routes import empresa_bp
from routes.login_routes import login_bp
from routes.calendario_routes import calendario_bp
from routes.agenda_routes import agenda_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(empresa_bp)
app.register_blueprint(login_bp)
app.register_blueprint(calendario_bp)
app.register_blueprint(agenda_bp)
 