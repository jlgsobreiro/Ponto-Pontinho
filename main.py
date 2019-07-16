from datetime import datetime
import python.mongo_login as Login
from flask import Flask, render_template, request, session, jsonify

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
            print("Granted")
            return jsonify({"Access": "Granted"})
        else:
            print("Denied")
            return jsonify({"Access": "Denied"})
    return ''


@app.route("/logoff", methods=['GET','POST'])
def logoff():
    if request.method == "POST":
        print("init")
        if session:
            print("saindo")
            session.clear()
            print("Logoff")
            return jsonify({'Session': 'Cleared'})
        else:
            print("Nope")
            return jsonify({"Session": "No session"})

@app.route("/register", methods=['GET', 'POST'])
def register():
    print("cadastrando")
    print(request.method)
    if request.method == 'POST':
        print("getting")
        usuario = request.form['username']
        print(usuario)
        nome = request.form['name']
        print(nome)
        sobrenome = request.form['last_name']
        print(sobrenome)
        email = request.form['email']
        print(email)
        senha = request.form['password']
        print(senha)
        senha_confirma = request.form['confirm_password']
        print(senha_confirma)
        print('got')

        if nome is '':
            return jsonify({"Register": "Name"})
        if sobrenome is '':
            return jsonify({"Register": "Last_name"})
        if usuario is '':
            return jsonify({"Register": "Username"})
        if email is '':
            return jsonify({"Register": "Email"})
        if senha is '':
            return jsonify({"Register": "Password"})
        if senha_confirma is '':
            return jsonify({"Register": "Confirm_password"})
        if not Login.equals_password(senha, senha_confirma):
            return jsonify({"Register": "Not_equal"})

        if Login.insert_user(nome, sobrenome, email, usuario, senha):
            return jsonify({"Register": "Registered"})
        else:
            return jsonify({"Register": "Exists"})
    else:
        return ''


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    return render_template('cadastro.html')


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


@app.route("/historico_ponto")
def historico_ponto():
    return render_template('historico_ponto.html')


@app.route("/session", methods=["GET", "POST"])
def session_user():
    if session:
        print(session["user"])
        return jsonify(session["user"])
    else:
        return 'Off'

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


@app.route("/get_all_pontos_user", methods=["GET", "POST"])
def get_all_pontos_user():
    if request.method == "POST" or "GET":
        user = request.args.get("user")
        return Login.get_pontos(user)
    return ''


@app.route("/get_user_name", methods=["GET", "POST"])
def get_user_name():
    return Login.get_user_name(session["user"])


@app.route("/days_worked", methods=["GET", "POST"])
def days_worked():
    return Login.get_user_name(session["user"])


@app.route("/hours_worked", methods=["GET", "POST"])
def hours_worked():
    return Login.get_user_name(session["user"])


@app.route("/hours_lunch", methods=["GET", "POST"])
def hours_lunch():
    return Login.get_user_name(session["user"])


app.run()
