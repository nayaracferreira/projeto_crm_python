from flask import Blueprint, request
from config.database import cursor
#import bcrypt


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET"])
def login():
    body = request.json
    email = body["email"]
    #hashed = bcrypt.hashpw(body["senha"].encode("utf-8"), bcrypt.gensalt())
    #senha = bcrypt.checkpw(body["senha"].encode("utf-8"), hashed)
    senha = body["senha"]
    select_sql = """ SELECT senha FROM empresa WHERE email = %s"""
    cursor.execute(select_sql, (email,))
    empresa = cursor.fetchone()
    senha_da_empresa = empresa[0]

    if senha_da_empresa == senha :
        return {"Sucesso": True}, 200

    else: 
        return {"Login e/ou senha inválido(s). Tente Novamente!": False}, 401
    