from datetime import datetime
import python.mongo_login as Login
from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import RegistrationForm, LoginForm, PontoForm
from pymongo import MongoClient


app = Flask(__name__)
app.config['SECRET_KEY'] = '3160b2ceb0907af541541fc865bbb1fa'

client_mongo = MongoClient('localhost', 27017)
dbPontinho = client_mongo.pontinho
pontosCollection = dbPontinho['pontos']
usuariosCollection = dbPontinho['usuarios']

@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        password = form.password.data
        username = form.username.data
        if Login.acesso(password,username,usuariosCollection):
            return redirect(url_for('panel'))
            print('sucesso')
        else:
            print('falhou')
            flash(f"Login ou senha errados")

    return render_template('login.html', title='Entrar', form=form)


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    print("acesso cadastro")
    form = RegistrationForm()
    if request.method == "POST":
        usuario = form.username.data
        nome = form.nome.data
        sobrenome = form.sobrenome.data
        email = form.email.data
        senha = form.password.data
        senha_confirma = form.confirm_password.data
        if Login.verifica_senha(senha, senha_confirma):
            if Login.insere_usuario(nome, sobrenome, email, usuario, senha, usuariosCollection):
                flash(f'Nome de usuario já cadastrado')
            else:
                print("redirecting")
                flash(f'Conta criada para {usuario}!')
                return redirect(url_for('login'))
        else:
            flash(f'Senha incorreta!')
    return render_template('cadastro.html', title='Cadastro', form=form)


@app.route("/ponto", methods=['GET', 'POST'])
def ponto():
    form = PontoForm()
    print(datetime.now())
    print(session)
    if request.method == "POST":
        print(datetime.now())
        print(session)
        return render_template('ponto.html', title='Ponto', form=form)
    return render_template('ponto.html', title='Ponto', form=form)

@app.route("/panel")
def panel():
    return render_template('panel.html',title='Painel')

@app.route("/consult")
def consult():
    return render_template('consult.html',title='Consulta')

@app.route("/inventory")
def inventory():
    return render_template('inventory.html',title='Inventario')


app.run()

