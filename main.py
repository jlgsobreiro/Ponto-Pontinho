from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import RegistrationForm, LoginForm
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

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
    if (request.method == "POST"):
        usuario = form.username.data
        if (usuariosCollection.find_one({"Usuario":usuario})):
            user = usuariosCollection.find_one({"Usuario": usuario})
            if (check_password_hash(user["Senha"],form.password.data)):
                print("redirecting")
                session['username'] = form.username.data
                return redirect(url_for('ponto'))
            else:
                flash('errado')
        else:
            flash('errado')
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
        senha = generate_password_hash(form.password.data)
        senha_confirma = form.confirm_password.data
        if check_password_hash(senha, senha_confirma):
            usuariosCollection.insert_one({'Nome': nome,
                                           'Sobrenome': sobrenome,
                                           'Email': email,
                                           'Usuario': usuario,
                                           'Senha': senha})
            print("redirecting")
            flash(f'Conta criada para {form.username.data}!')
            return redirect(url_for('login'))
        else:
            flash(f'Senha incorreta!')
    return render_template('cadastro.html', title='Cadastro', form=form)


@app.route("/ponto")
def ponto():
    print(session)
    return render_template('ponto.html', title='Entrar')

@app.route("/panel")
def panel():
    return render_template('panel.html',title='Painel')
app.run()
