from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3160b2ceb0907af541541fc865bbb1fa'


@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Entrar', form=form)


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    print("acesso cadastro")
    form = RegistrationForm()
    if request.method == "POST":
        print("redirecting")
        flash(f'Conta criada para {form.username.data}!')
        return redirect(url_for('ponto'))
    return render_template('cadastro.html', title='Cadastro', form=form)


@app.route("/ponto")
def ponto():
    return render_template('ponto.html', title='Entrar')


app.run()
