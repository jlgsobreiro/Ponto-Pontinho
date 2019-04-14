from datetime import datetime
import python.mongo_login as Login
from flask import Flask, render_template, url_for, flash, redirect, request, session, jsonify
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3160b2ceb0907af541541fc865bbb1fa'


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('layout.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']

        if Login.access(password, user):
            session["user"] = user
            return jsonify({"Access": "Granted"})
        else:
            return jsonify({"Access": "Denied"})
    return ''


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
        return render_template('ponto.html')
    return render_template('ponto.html')


@app.route("/production", methods=['GET', 'POST'])
def production():
    if request.method == "POST":
        print(datetime.now())
        print(session)
        return render_template('production.html')
    return render_template('production.html')


@app.route("/expedition", methods=['GET', 'POST'])
def expedition():
    if request.method == "POST":
        print(datetime.now())
        print(session)
        return render_template('expedition.html')
    return render_template('espedition.html')


@app.route("/routes", methods=['GET', 'POST'])
def routes():
    if request.method == "POST":
        print(datetime.now())
        print(session)
        return render_template('routes.html')
    return render_template('routes.html')


@app.route("/emplyees", methods=['GET', 'POST'])
def employees():
    if request.method == "POST":
        print(datetime.now())
        print(session)
        return render_template('employees.html')
    return render_template('employees.html')


@app.route("/clients", methods=['GET', 'POST'])
def clients():
    if request.method == "POST":
        print(datetime.now())
        print(session)
        return render_template('clients.html')
    return render_template('clients.html')


@app.route("/panel")
def panel():
    return render_template('layout_panel.html')


@app.route("/consult")
def consult():
    return render_template('consult.html')


@app.route("/inventory")
def inventory():
    return render_template('inventory.html')


@app.route("/session", methods=["GET", "POST"])
def session_user():
    print(session["user"])
    return jsonify(session["user"])


@app.route("/arrive", methods=["GET", "POST"])
def arrive():
    if request.method == "POST":
        Login.hit_ponto(session["user"], request.form['tipo'])
    return ''


@app.route("/last_entry", methods=["GET", "POST"])
def last_entry():
    if request.method == "POST":
        return jsonify(Login.last_ponto_type(session["user"]))
    return ''


@app.route("/last_ponto", methods=["GET", "POST"])
def last_ponto():
    if request.method == "POST":
        print(Login.last_ponto_date(session["user"], request.form['last']))
        return jsonify(Login.last_ponto_date(session["user"], request.form['last']))
    return ''


@app.route("/get_ponto_at", methods=["GET", "POST"])
def get_ponto_at():
    if request.method == "POST" or "GET":
        index = request.args.get("index")
        item = Login.get_ponto_at(session["user"], index)
        return item
    return ''


@app.route("/get_ponto_count", methods=["GET", "POST"])
def get_ponto_count():
    return jsonify(Login.count_ponto(session["user"]))


@app.route("/get_all_pontos", methods=["GET", "POST"])
def get_all_pontos():
    return Login.get_pontos(session["user"])


@app.route("/get_user_name", methods=["GET", "POST"])
def get_user_name():
    return Login.get_user_name(session["user"])




app.run()
