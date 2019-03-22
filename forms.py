from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    nome = StringField('Nome',
                           validators=[DataRequired(), Length(min=2, max=50)])
    sobrenome = StringField('Sobrenome',
                           validators=[DataRequired(), Length(min=2, max=50)])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm_password = PasswordField('Confirme Senha',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar')


class LoginForm(FlaskForm):
    username = StringField('Usuario',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Entrar')


class PontoForm(FlaskForm):
    submit = SubmitField('Bater Ponto')


