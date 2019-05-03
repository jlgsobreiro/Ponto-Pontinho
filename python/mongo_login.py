import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from bson import Binary, Code
from bson.json_util import dumps

client_mongodb = MongoClient('localhost', 2000)
dbPontinho = client_mongodb.pontinho
pontosCollection = dbPontinho['pontos']
usersCollection = dbPontinho['usuarios']
timeBankCollection = dbPontinho['banco_de_horas']


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
                                    'Senha': generate_password_hash(password),
                                    "Data": datetime.datetime.now()})
        return True

def month_ptbr(month):
    months_ptbr = {"Jan": "Janeiro",
                    "Feb": "Fevereiro",
                    "Mar": "Março",
                    "Apr": "Abril",
                    "May": "Maio",
                    "Jun": "Junho",
                    "Jul": "Julho",
                    "Aug": "Agosto",
                    "Sep": "Setembro",
                    "Oct": "Outubro",
                    "Nov": "Novembro",
                    "Dec": "Dezembro"}
    return months_ptbr[month]


def weekday_ptbr(day):
    weekdays_ptbr = {"Sun": "Domingo",
                    "Mon": "Segunda-feira",
                    "Tue": "Terça-feira",
                    "Wed": "Quarta-feira",
                    "Thu": "Quinta-feira",
                    "Fri": "Sexta-feira",
                    "Sat": "Sabado"}
    return weekdays_ptbr[day]


def hit_ponto(user, tipo):
    user_id = usersCollection.find_one({"Usuario": user})['_id']
    data = datetime.datetime.now().ctime()
    dia_semana = data[0:3]
    dia = data[8:10]
    mes = data[4:7]
    ano = data[20:24]
    horario = data[11:19]
    pontosCollection.insert_one({"User_id": user_id,
                                 "Dia_semana": weekday_ptbr(dia_semana),
                                 "Dia": dia,
                                 "Mes": month_ptbr(mes),
                                 "Ano": ano,
                                 "Horario": horario,
                                 "Tipo": tipo})


def count_ponto(user):
    user_id = usersCollection.find_one({"Usuario": user})['_id']
    return pontosCollection.count({"User_id": user_id})


def last_ponto_type(user):
    user_id = usersCollection.find_one({"Usuario": user})['_id']
    i = 0
    for registry in pontosCollection.find({"User_id": user_id}):
        if i == pontosCollection.count({"User_id": user_id}) - 1:
            return registry["Tipo"]
        i += 1

    return ''


def last_ponto_date(user, method):
    user_id = usersCollection.find_one({"Usuario": user})['_id']
    list_registry = []
    i = 0
    for registry in pontosCollection.find({"User_id": user_id, "Tipo": method}):
        list_registry.insert(i, registry)
        i += 1

    if list_registry[-1] is not None:
        return str(list_registry[-1]['Dia_semana']) + " " + \
               str(list_registry[-1]['Dia']) + "/" + \
               str(list_registry[-1]['Mes']) + "/" + \
               str(list_registry[-1]['Ano']) + " " + \
               str(list_registry[-1]['Horario'])
    return ''


def get_pontos(user):
    user_id = usersCollection.find_one({"Usuario": user})['_id']
    list_registry = []
    i = 0
    for registry in pontosCollection.find({"User_id": user_id}):
        list_registry.insert(i, registry)
        i += 1

    if list_registry is not None:
        return dumps(list_registry)

    return ''


def get_ponto_at(user, index):
    user_id = usersCollection.find_one({"Usuario": user})['_id']
    i = 0
    for registry in pontosCollection.find({"User_id": user_id}):
        if i == int(index):
            return dumps(registry)
        i+=1
    return ''


def get_ponto_count (user):
    count = usersCollection.count({"Usuario": user})
    return count


def get_user_name(user):
    print(user)
    return usersCollection.find_one({"Usuario": user})["Nome"]


def get_all_users_name():
    list = []
    i = 0
    for x in usersCollection.find({}):
        list.insert(i, x["Nome"])
        i += 1

    return list
