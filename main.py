from datetime import datetime
import python.mongo_login as Login
<<<<<<< HEAD
from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import RegistrationForm, LoginForm, PontoForm
from pymongo import MongoClient

=======
from flask import Flask, render_template, url_for, flash, redirect, request, session, jsonify
from forms import RegistrationForm, LoginForm, PontoForm
>>>>>>> d4d430355b0b5c6d5ccd2cfdccf8eaa5b6496823

app = Flask(__name__)
app.config['SECRET_KEY'] = '3160b2ceb0907af541541fc865bbb1fa'


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
<<<<<<< HEAD
<<<<<<< HEAD
    if (request.method == "POST"):
        usuario = form.username.data
        if (usuariosCollection.find_one({"Usuario":usuario})):
            user = usuariosCollection.find_one({"Usuario": usuario})
            if (check_password_hash(user["Senha"],form.password.data)):
                print("redirecting")
                return redirect(url_for('ponto'))
            else:
                flash("<script>M.toast({html: 'I am a toast!'});</script>")
        else:
            flash("<script>M.toast({html: 'I am a toast!'});</script>")
=======
    if request.method == "POST":
        password = form.password.data
        username = form.username.data
        if Login.acesso(password,username,usuariosCollection):
            return redirect(url_for('panel'))
            print('sucesso')
=======
    if request.method == "POST":
        password = form.password.data
        username = form.username.data
        if Login.access(password, username):
            print('sucesso')
            session["user"] = username
            return redirect(url_for('panel'))
>>>>>>> d4d430355b0b5c6d5ccd2cfdccf8eaa5b6496823
        else:
            print('falhou')
            flash(f"Login ou senha errados")

<<<<<<< HEAD
>>>>>>> 1f4f45398ef1ecba7a392200cdb5d8e74a81be9b
=======
>>>>>>> d4d430355b0b5c6d5ccd2cfdccf8eaa5b6496823
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
<<<<<<< HEAD
<<<<<<< HEAD
        if check_password_hash(senha, senha_confirma):
            usuariosCollection.insert_one({'Nome': nome,
                                           'Sobrenome': sobrenome,
                                           'Email': email,
                                           'Usuario': usuario,
                                           'Senha': senha})
            print("redirecting")
            flash(f'Conta criada para {form.username.data}!',category="message")
            return redirect(url_for('ponto'))
=======
        if Login.verifica_senha(senha, senha_confirma):
            if Login.insere_usuario(nome, sobrenome, email, usuario, senha, usuariosCollection):
=======
        if Login.equals_password(senha, senha_confirma):
            if Login.insert_user(nome, sobrenome, email, usuario, senha):
>>>>>>> d4d430355b0b5c6d5ccd2cfdccf8eaa5b6496823
                flash(f'Nome de usuario já cadastrado')
            else:
                print("redirecting")
                flash(f'Conta criada para {usuario}!')
                return redirect(url_for('login'))
<<<<<<< HEAD
>>>>>>> 1f4f45398ef1ecba7a392200cdb5d8e74a81be9b
=======
>>>>>>> d4d430355b0b5c6d5ccd2cfdccf8eaa5b6496823
        else:
            flash("<h1>ABABABAB</h1>")
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

<<<<<<< HEAD
@app.route("/panel")
def panel():
    return render_template('panel.html',title='Painel')

@app.route("/consult")
def consult():
    return render_template('consult.html',title='Consulta')

@app.route("/inventory")
def inventory():
    return render_template('inventory.html',title='Inventario')
=======

@app.route("/panel")
def panel():
    return render_template('panel.html', title='Painel')


@app.route("/consult")
def consult():
    return render_template('consult.html', title='Consulta')


@app.route("/inventory")
def inventory():
    return render_template('inventory.html', title='Inventario')


@app.route("/session", methods=["GET", "POST"])
def session_user():
    return jsonify(session["user"])


@app.route("/arrive", methods=["GET", "POST"])
def arrive():
    if request.method == "POST":
        print(request.form['user'])
        print('abaa')
        Login.hit_ponto(request.form['user'])
    return ''
>>>>>>> d4d430355b0b5c6d5ccd2cfdccf8eaa5b6496823


app.run()

