from flask import Blueprint, request, abort
from config.database import cursor
import bcrypt

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    body = request.json
    email = body["email"]    
    select_sql = """ SELECT senha FROM empresas WHERE email = %s """
    cursor.execute(select_sql, (email,))
    empresa = cursor.fetchone()
  
    if bcrypt.checkpw(body["senha"].encode(), empresa[0].encode()) :
        return {"Sucesso": True}, 200

    else: 
        return {"Login e/ou senha inválido(s). Tente Novamente!": False}, 401  
