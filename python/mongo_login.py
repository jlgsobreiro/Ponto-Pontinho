import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

client_mongodb = MongoClient('localhost', 27017)
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


def hit_ponto(user):
    user_id = usersCollection.find_one({"Usuario": user})['_id']

    pontosCollection.insert_one({"User_id": user_id,
                                 "Horario": datetime.datetime.now()})


def count_ponto(user):
    return pontosCollection.find({"Usuario": user}).count()