from flask import Blueprint, request,jsonify
from config.database import cursor, connection
import bcrypt

empresa_bp = Blueprint("empresa", __name__)

# CREATE
@empresa_bp.route("/empresa", methods=["POST"])
def create():
    body = request.json  
    insert_sql = """
    INSERT INTO empresas (razao, cnpj, telefone, email, cep, endereco, numero, bloco, bairro, cidade, uf, senha) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);    """
    hashed = bcrypt.hashpw(body["senha"].encode("utf-8"), bcrypt.gensalt())
    insert_tuple = (body["razao"]), (body["cnpj"]), (body["telefone"]), (body["email"]), (body["cep"]), (body["endereco"]), (body["numero"]), (body["bloco"]), (body["bairro"]), (body["cidade"]), (body["uf"]), hashed.decode("utf-8")
    cursor.execute(insert_sql, insert_tuple,)     
    connection.commit()
    # razao_empresa = body["razao"]   
    # # razao_cliente = razao_empresa.replace(' ', '_')
    # script_tabela_calendario = f'''CREATE TABLE IF NOT EXISTS agenda_todas_empresas           
    #                 (dia_mes_ano VARCHAR(8) NOT NULL,
    #                  email_empresa VARCHAR(255) NOT NULL, anotacao VARCHAR NOT NULL)'''
    # cursor.execute(script_tabela_calendario)
    # connection.commit()
    return {}, 201

# READ
@empresa_bp.route("/empresa/all", methods=["GET"])
def read_all():
    select_sql = """
    SELECT * FROM empresas
    """
    cursor.execute(select_sql)
    todas_empresas = cursor.fetchall()
    connection.commit()
    return (todas_empresas), 200

    # lista_retornar_json = []
    # for x in todas_empresas:
    #     informacao_dia_retornadas={}
    #     informacao_dia_retornadas["id"]= x[0]
    #     informacao_dia_retornadas["razao"]= x[1]
    #     informacao_dia_retornadas["cnpj"]= x[2]
    #     informacao_dia_retornadas["telefone"]= x[3]
    #     informacao_dia_retornadas["email"]= x[4]
    #     informacao_dia_retornadas["cep"]= x[5]
    #     informacao_dia_retornadas["endereco"]= x[6]
    #     informacao_dia_retornadas["numero"]= x[7]
    #     informacao_dia_retornadas["bloco"]= x[8]
    #     informacao_dia_retornadas["bairro"]= x[9]
    #     informacao_dia_retornadas["cidade"]= x[10]
    #     informacao_dia_retornadas["uf"]= x[11]
    #     informacao_dia_retornadas["senha"]= x[12]
    #     lista_retornar_json.append(informacao_dia_retornadas)
    # return jsonify(lista_retornar_json), 200
    

@empresa_bp.route("/empresa/<empresa_id>", methods=["GET"])
def read(empresa_id):
    select_sql = """
    SELECT * FROM empresas WHERE id = %s
    """
    cursor.execute(select_sql, (empresa_id,))
    empresa = cursor.fetchone()
    return {"empresa": empresa}, 200

#UPDATE
@empresa_bp.route("/empresa/<empresa_id>", methods=["PUT"])
def update(empresa_id):
    body = request.json
    update_sql = """
    UPDATE empresas SET razao = %s, cnpj = %s, telefone = %s, email = %s, cep = %s, endereco = %s, numero = %s, bloco = %s, bairro = %s, cidade = %s, uf = %s, senha = %s WHERE id = %s
    """
    hashed = bcrypt.hashpw(body["senha"].encode("utf-8"), bcrypt.gensalt())
    update_tuple = (body["razao"], body["cnpj"], body["telefone"], body["email"], body["cep"], body["endereco"], body["numero"], body["bloco"], body["bairro"], body["cidade"], body["uf"], hashed.decode("utf-8"), empresa_id)
    cursor.execute(update_sql, update_tuple)
    connection.commit()
    return {}, 200

#DELETE
@empresa_bp.route("/empresa/<empresa_id>", methods=["DELETE"])
def delete(empresa_id):
    delete_sql = """
    DELETE FROM empresas WHERE id = %s
    """   
    cursor.execute(delete_sql, (empresa_id,))
    connection.commit()
    return {}, 204

