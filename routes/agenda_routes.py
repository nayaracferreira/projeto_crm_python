from flask import Blueprint, request, jsonify
from config.database import cursor, connection, psycopg2

agenda_bp = Blueprint("agenda", __name__)

@agenda_bp.route('/adicionardia',methods=["POST"])
def AddDia():
    json_data = request.get_json()
    dia_aser_adicionado = json_data['dia_aser_adicionado']
    email_da_empressa = json_data['email_da_empresa']
    nota_do_dia = json_data['anotacao']

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    script_adicionar_dia = "INSERT INTO agenda_todas_empresas (dia_mes_ano,email_empresa, anotacao)  VALUES (%s,%s,%s)"
    script_adicionar_dia_value = (dia_aser_adicionado,email_da_empressa,nota_do_dia)

    cursor.execute(script_adicionar_dia,script_adicionar_dia_value)

    connection.commit()
    return {}, 201
    
@agenda_bp.route('/deletadia',methods=["DELETE"])
def DeleteDia():
    json_data = request.get_json()

    dia_aser_deletado = json_data['dia_aser_adicionado']
    email_da_empressa = json_data['email_da_empresa']
    nota_do_dia = json_data['anotacao']

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    script_deletar_dia = "DELETE from agenda_todas_empresas WHERE anotacao = %s AND email_empresa = %s AND dia_mes_ano = %s"
    script_deletar_dia_value = (nota_do_dia,email_da_empressa,dia_aser_deletado,) 
    # A virgula no final não é um erro mas sim um forma de converter o json para string 

    cursor.execute(script_deletar_dia,script_deletar_dia_value)
    connection.commit()

    return{},200
    
@agenda_bp.route('/todomes',methods=["POST"])
def allMes():
    json_data = request.get_json()

    email_da_empresa = json_data['email_da_empresa']

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    script_pegar_todo_dia = "SELECT * FROM agenda_todas_empresas WHERE email_empresa = %s"
    script_pegar_todo_dia_valores = (email_da_empresa,)
    # A virgula no final não é um erro mas sim um forma de converter o json para string 

    cursor.execute(script_pegar_todo_dia,script_pegar_todo_dia_valores)
    toda_informacao_email_especifico=cursor.fetchall()
    connection.commit()

    lista_retornar_json = []
    for x in toda_informacao_email_especifico:
        toda_informacao_email_especifico={}
        toda_informacao_email_especifico["Dia"]= x[0]
        toda_informacao_email_especifico["Email"]= x[1]
        toda_informacao_email_especifico["Nota"]= x[2]
        # print(x)
        lista_retornar_json.append(toda_informacao_email_especifico)
    return jsonify(lista_retornar_json),200 

@agenda_bp.route('/todosdias',methods=["GET"])
def AllDia():
    json_data = request.get_json()

    dia_ase_procurar = json_data['dia_aser_adicionado']
    email_da_empressa = json_data['email_da_empresa']

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    script_pegar_todo_dia = "SELECT * FROM agenda_todas_empresas WHERE dia_mes_ano = %s AND email_empresa = %s"
    script_pegar_todo_dia_valores = (dia_ase_procurar,email_da_empressa,)
    # A virgula no final não é um erro mas sim um forma de converter o json para string 

    cursor.execute(script_pegar_todo_dia,script_pegar_todo_dia_valores)
    toda_informacao_dia_especifico=cursor.fetchall()
    connection.commit()

    lista_retornar_json = []
    for x in toda_informacao_dia_especifico:
        informacao_dia_retornadas={}
        informacao_dia_retornadas["Dia"]= x[0]
        informacao_dia_retornadas["Email"]= x[1]
        informacao_dia_retornadas["Nota"]= x[2]
        print(x)
        lista_retornar_json.append(informacao_dia_retornadas)

    return jsonify(lista_retornar_json),200

# PARTE DE TESTE

teste1 =4
teste2='Ronaldo'
teste3='ronaldo@email'
teste4="1234"

@agenda_bp.route('/teste')
def testando(): 

    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute ('DROP TABLE IF EXISTS empressa')

    script_criar = '''CREATE TABLE IF NOT EXISTS empressa (
                    id int PRIMARY KEY,
                    nomeempressa varchar(360) NOT NULL,
                    emailempressa varchar(360) NOT NULL,
                    senha varchar(360) NOT NULL)'''

    script_inserir ='INSERT INTO empressa (id, nomeEmpressa, emailempressa, senha) VALUES (%s,%s,%s,%s)'
    script_valores = (teste1,teste2,teste3,"123456")

    cursor.execute(script_criar)
    cursor.execute(script_inserir,script_valores)


    # cur.execute('SELECT *  FROM EMPRESSA WHERE ID = 4')
    # for record in cur.fetchall():
    #     print(record['emailempressa'],record['senha'])
    
    cursor.execute(f'SELECT *  FROM EMPRESSA WHERE ID = {teste1}') #Verificar email se existe no banco de dados
    x= cursor.fetchone()
    if x == None: 
        print ("Vazio") #Voltar para pagina porque não encontrou algo ou algo está errado
    else:               #SENÃO , vai para verificar se a senha recebida está correta 
        if teste4 == x[3]: 
            print("Tudo Correto") #Vai para proxima pagina 
        else:
            print("Senha Errada") #Volta a pagina anterior// mensagaem para tentar novamente
        
        
    connection.commit()

    return "Teste Completo"

