from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://elleve:jpbd9765@mysql.elleve.net.br/elleve'
db = SQLAlchemy(app)

#Cria classe da tabela negócios
class negocio_copia_teste(db.Model):
      idNegocio	= db.Column(db.Integer, primary_key = True)
      id_facilita	= db.Column(db.Integer)
      product_id = db.Column(db.Integer)
      id_customer	= db.Column(db.Integer)
      name = db.Column(db.String(255))
      email = db.Column(db.String(255))
      birthday = db.Column(db.String(255))
      rg = db.Column(db.String(255))
      cpf = db.Column(db.String(255))
      mobile = db.Column(db.String(255))
      phone = db.Column(db.String(255))
      sex = db.Column(db.String(255))
      children = db.Column(db.String(255))
      state = db.Column(db.String(255))
      city_id = db.Column(db.String(255))
      profession = db.Column(db.String(255))
      observations = db.Column(db.String(255))
      income = db.Column(db.String(255))
      state_civil = db.Column(db.String(255))
      created_at = db.Column(db.DateTime)
      updated_at = db.Column(db.DateTime)
      last_user_id = db.Column(db.String(255))
      avatar = db.Column(db.String(255))
      favorite = db.Column(db.String(255))
      email_extra = db.Column(db.String(255))
      phone_residential = db.Column(db.String(255))
      phone_commercial = db.Column(db.String(255))
      address = db.Column(db.String(255))
      business = db.Column(db.String(255))
      complement = db.Column(db.String(255))
      neighborhood_id = db.Column(db.String(255))
      origin = db.Column(db.String(255))
      corporate_name = db.Column(db.String(255))
      cnpj = db.Column(db.String(255))
      type = db.Column(db.String(255))
      cep = db.Column(db.String(255))
      ie = db.Column(db.String(255))
      options = db.Column(db.String(255))
      rd_uuid = db.Column(db.String(255))
      dataRegistro = db.Column(db.DateTime)

#Consulta o lead no facilita
def consulta_facilita(id):
    headers = {
    'api-instance': 'elleve',
    'api-key': '1e50de4951dea1c59bee6dd73da67070',
    'token-user': 'eyJpdiI6IjVcL2JmSDM2cTJGWmZwM3hLdU9OdUZ3PT0iLCJ2YWx1ZSI6IlUwXC96ZDE3SlVxeG9cL3RObE55RGFzV3F4SkppRlFoRzZOb1NQU0swKzR4XC83aTBkWDRrbmsrSVNzYjZ3SHNtTGIiLCJtYWMiOiJhZDVkMmJkZWFiMmRlODQ5NWZiNmI2ZDlmMmMwMWUyMTE4MmQ0ZjQ0MGM5OGZkMjQ5NjlkZmViY2Q3MjA4MjdmIn0',
    'Content-Type': 'application/json'
    }
    url="https://api.facilitaapp.com/platform/v1/deal?deal_id="+str(id)
    response = requests.request("GET", url, headers=headers)
    response = response.json()
    return response
    

print(consulta_facilita('24610'))

@app.route('/cadastro', methods=["GET"])
def cadastro():
 #   body = requests.get_json()
    id_facilita_recebido = 24610
    negocio_facilita = consulta_facilita(id_facilita_recebido)
    name_negocio = negocio_facilita['customer']["name"]
    negocio_copia = negocio_copia_teste(id_facilita=id_facilita_recebido, name=name_negocio, dataRegistro="25/08/2021")

    db.session.add(negocio_copia)
    db.session.commit()
    return(200)
  


#Executa a api
app.run(host='0.0.0.0')