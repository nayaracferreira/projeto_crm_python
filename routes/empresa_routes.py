from flask import Blueprint, request
from config.database import cursor, connection
#import bcrypt

empresa_bp = Blueprint("empresa", __name__)

# CREATE
@empresa_bp.route("/empresa", methods=["POST"])
def create():
    body = request.json    
    insert_sql = """
    INSERT INTO empresa (razao, cnpj, telefone, email, cep, endereco, numero, bloco, bairro, cidade, uf, senha) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    #hashed = bcrypt.hashpw(body["senha"].encode("utf-8"), bcrypt.gensalt())
    insert_tuple = (body["razao"]), (body["cnpj"]), (body["telefone"]), (body["email"]), (body["cep"]), (body["endereco"]), (body["numero"]), (body["bloco"]), (body["bairro"]), (body["cidade"]), (body["uf"]), (body["senha"])
    cursor.execute(insert_sql, insert_tuple,)     
    connection.commit()
    razao_empresa = body["razao"]   
    razao_empresa_2 = razao_empresa.replace(' ', '_')
    script_tabela_calendario = f'''CREATE TABLE IF NOT EXISTS {razao_empresa_2}           
                    (dia_mes_ano VARCHAR(8) NOT NULL,
                     email_empressa VARCHAR NOT NULL,
                     nota_Dia VARCHAR NOT NULL)'''
    cursor.execute(script_tabela_calendario)
    connection.commit()
    return {}, 201

# READ
@empresa_bp.route("/empresa/all", methods=["GET"])
def read_all():
    select_sql = """
    SELECT * FROM empresa 
    """
    cursor.execute(select_sql)
    todas_empresas = cursor.fetchall()
    return {"empresa": todas_empresas}, 200

@empresa_bp.route("/empresa/<empresa_id>", methods=["GET"])
def read(empresa_id):
    select_sql = """
    SELECT * FROM empresa WHERE id = %s
    """
    cursor.execute(select_sql, (empresa_id,))
    empresa = cursor.fetchone()
    return {"empresa": empresa}, 200

#UPDATE
@empresa_bp.route("/empresa/<empresa_id>", methods=["PUT"])
def update(empresa_id):
    body = request.json
    update_sql = """
    UPDATE empresa SET razao = %s, cnpj = %s, telefone = %s, email = %s, cep = %s, endereco = %s, numero = %s, bloco = %s, bairro = %s, cidade = %s, uf = %s, senha = %s WHERE id = %s
    """
    #hashed = bcrypt.hashpw(body["senha"].encode("utf-8"), bcrypt.gensalt())
    update_tuple = (body["razao"], body["cnpj"], body["telefone"], body["email"], body["cep"], body["endereco"], body["numero"], body["bloco"], body["bairro"], body["cidade"], body["uf"], 
    (body["senha"]), empresa_id)
    cursor.execute(update_sql, update_tuple)
    connection.commit()
    return {}, 200

#DELETE
@empresa_bp.route("/empresa/<empresa_id>", methods=["DELETE"])
def delete(empresa_id):
    delete_sql = """
    DELETE FROM empresa WHERE id = %s
    """   
    cursor.execute(delete_sql, (empresa_id,))
    connection.commit()
    return {}, 204

