from werkzeug.security import generate_password_hash, check_password_hash
def acesso(senha,usuario,usuariosCollection):
    if usuariosCollection.find_one({"Usuario":usuario}):
        user = usuariosCollection.find_one({"Usuario": usuario})
        if check_password_hash(user["Senha"], senha):
            return True
        else:
            return False
    else:
        return False


def verifica_senha(senha, confirma_senha):
    if senha == confirma_senha:
        return True
    else:
        return False

def verifica_login(usuario, usuariosCollection):
    if usuariosCollection.find_one({"Usuario": usuario}):
        return False
    else:
        return True

def insere_usuario(nome, sobrenome, email, usuario, senha, usuariosCollection):
    if verifica_login:
        return False
    else:
        usuariosCollection.insert_one({'Nome': nome,
                                    'Sobrenome': sobrenome,
                                    'Email': email,
                                    'Usuario': usuario,
                                    'Senha': generate_password_hash(senha)})
        return True