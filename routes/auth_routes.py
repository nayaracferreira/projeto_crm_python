from flask import Blueprint, request
from config.database import cursor

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    body = request.json
    email = body["email"]
    senha = body["senha"]
    select_sql = """ SELECT senha FROM empresa WHERE email = %s"""
    cursor.execute(select_sql, (email,))
    empresa = cursor.fetchone()
    senha_da_empresa = empresa[0]
      
    if senha_da_empresa == senha :
        return {"Sucesso": True}, 200
        
    return {"sucesso": False, "message": "Login e/ou senha inválido(s). Tente Novamente!"}, 401

    # if "email" not in body or "senha" not in body:
    #  raise Exception("Login e/ou senha inválido(s). Tente Novamente!")