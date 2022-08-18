from sqlite3 import Cursor
from flask import Flask
import pyodbc


def conexacao(): #conexacao com o banco de dados
    server = 'localhost'
    database = 'Concessionaria' 
    username = 'sa'
    password = 'alves'
    conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password) 
    
    cursor = conexao.cursor()
    
    return cursor
  
app = Flask(__name__)
@app.route("/<ID_Cliente>", methods=['GET']) #passa o id pela url, e especifica o metodo que será usado
def home(ID_Cliente): 
    
    cursor = conexacao() # o curso permite que faça alteração no banco (o cursor esta trazendo o acesso ao banco)
    cursor.execute("SELECT * FROM Cliente WHERE ID_Cliente = ? " , ID_Cliente ) #busca o id
    return {'clientes':
            [dict(zip([column[0] for column in cursor.description], row)) #tranforma o cursor em um dicio
             for row in cursor.fetchall()]} #zip função retorna um iterador de tuplas com base nos objetos iteráveis.
                                            #zip relaciona as colunas
                                            #row são as linhas column a coluna
                                            #trás o resultado da query como um dicionario


class paginado():
    @app.route("/", methods=['GET'])
    def paginado():
        cursor = conexacao()
        cursor.execute("SELECT * FROM Cliente" )
        return {'clientes':
            [dict(zip([column[0] for column in cursor.description], row))
             for row in cursor.fetchall()]}
   
if __name__ == "__main__":
    app.run(debug=True)
    
    
