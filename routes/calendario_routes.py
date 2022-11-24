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
    
    if verifica_razao == razao: 
        return {"Empresa Logada": True}, 200

    else:
        return {"Essa empresa não consta em nosso registro": False}, 200











        


#SELECIONA UM DIA ESPECÍFICO
@calendario_bp.route("/agendamento/dia", methods=["GET"])
def read_day():
    body = request.json
    dia = (body["dia_mes_ano"])      
    select_sql = """
    SELECT * FROM testando WHERE dia_mes_ano = %s
    """
    cursor.execute(select_sql, (dia,))
    verifica_dia = cursor.fetchall()
    connection.commit()     
    return {"testando": verifica_dia,}, 200



# def read_day(empresa_id):
#     body = request.json
#     dia_1 = (body["dia_mes_ano"])      
#     select_sql = f"""
#     SELECT * FROM {empresa_id} WHERE {dia_1}
#     """
#     cursor.execute(select_sql, (dia_1,))
#     verifica_dia = cursor.fetchall()
#     connection.commit()     
#     return {"empresa_id": verifica_dia,}, 200













# SELECIONA TODOS OS DIAS  
@calendario_bp.route("/agendamento/all", methods=["GET"])
def read_all():
    select_sql = """
    SELECT * FROM testando
    """
    cursor.execute(select_sql)
    todos_clientes = cursor.fetchall()
    return{"testando": todos_clientes,}, 200   

#Cria uma agenda para testar
@calendario_bp.route("/agendamento", methods=["POST"])
def create_schedule():
    body = request.json  
    insert_schedule_sql = """
    INSERT INTO testando (dia_mes_ano, cliente, hora, servico, empresa_id) VALUES(%s, %s, %s, %s, %s);    """
    insert_schedule_tuple = (body["dia_mes_ano"]), (body["cliente"]), (body["hora"]), (body["servico"]), (body["empresa_id"])
    cursor.execute(insert_schedule_sql, insert_schedule_tuple,)     
    connection.commit()
    return {}, 201