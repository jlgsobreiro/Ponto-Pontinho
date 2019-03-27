import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

client_mongodb = MongoClient('localhost', 2000)
dbPontinho = client_mongodb.pontinho
pontosCollection = dbPontinho['pontos']
usersCollection = dbPontinho['usuarios']


def access(password, user):
    if usersCollection.find_one({"Usuario": user}) is not None:
        user = usersCollection.find_one({"Usuario": user})
        if check_password_hash(user["Senha"], password):
            return True
        else:
            return False
    else:
        return False


def equals_password(password, confirm_password):
    if password == confirm_password:
        return True
    else:
        return False


def verify_login(user):
    if usersCollection.find_one({"Usuario": user}) is not None:
        return True
    else:
        return False


def insert_user(name, last_name, email, user, password):
    if verify_login(user) is True:
        return False
    else:
        usersCollection.insert_one({'Nome': name,
                                    'Sobrenome': last_name,
                                    'Email': email,
                                    'Usuario': user,
                                    'Senha': generate_password_hash(password)})
        return True


def hit_ponto(user,tipo):
    user_id = usersCollection.find_one({"Usuario": user})['_id']
    dia = datetime.datetime.now().day
    mes = datetime.datetime.now().month
    ano = datetime.datetime.now().year
    hora = datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute
    pontosCollection.insert_one({"User_id": user_id,
                                "Dia": dia,
                                "Mes": mes,
                                "Ano": ano,
                                "Hora": hora,
                                "Minuto": minuto,
                                "Tipo": tipo})


def count_ponto(user):
    return pontosCollection.find({"Usuario": user}).count()

def last_ponto_type(user):
    user_id = usersCollection.find_one({"Usuario": user})['_id']
    i = 0
    for registry in pontosCollection.find({"User_id":user_id}):
        if(i == pontosCollection.count({"User_id":user_id})-1):
            return registry["Tipo"]
        i += 1

    return ''