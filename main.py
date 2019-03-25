from datetime import datetime
import python.mongo_login as Login
from flask import Flask, render_template, url_for, flash, redirect, request, session, jsonify
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3160b2ceb0907af541541fc865bbb1fa'


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        password = form.password.data
        username = form.username.data
        if Login.access(password, username):
            print('sucesso')
            session["user"] = username
            return redirect(url_for('panel'))
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
        if Login.equals_password(senha, senha_confirma):
            if Login.insert_user(nome, sobrenome, email, usuario, senha):
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

    if request.method == "POST":
        print(datetime.now())
        print(session)
        return render_template('ponto.html', title='Ponto')
    return render_template('ponto.html', title='Ponto')


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
        Login.hit_ponto(request.form['user'],request.form['tipo'])
    return ''

@app.route("/last_entry", methods=["GET", "POST"])
def last_entry():
    if request.method == "POST":
        print(request.form['user'])
        print(Login.last_ponto_type(request.form['user']))
        return jsonify(Login.last_ponto_type(request.form['user']))
    return ''


app.run()
