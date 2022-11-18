from flask import Blueprint, request
from config.database import cursor, connection

calendario_bp = Blueprint("calendario", __name__)

@calendario_bp.route("/calendario", methods=["GET"])
def read():
    body = request.json
    razao = body["razao"]
    select_sql = """
    SELECT razao FROM empresa WHERE razao = %s
    """
    cursor.execute(select_sql, (razao,))
    razao_id = cursor.fetchone()
    verifica_razao = razao_id[0]
    connection.commit() 

    
    read_day_sql = """
    SELECT empresa_id FROM empresa WHERE empresa_id = %s
    """ 
    cursor.execute(read_day_sql)
    razao_agenda = cursor.fetchall()  
    connection.commit()  

    if verifica_razao != razao :
        return {"Essa empresa não consta em nosso registro": False}, 200        
    else :
        return {razao_agenda}, 200
        
        # {"Empresa Logada": True}, 200 

