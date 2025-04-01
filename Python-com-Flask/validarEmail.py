import re

def validarEmail(email):
    # Expressão para validar apenas e-mails do Gmail
    padrao = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    
    if re.match(padrao, email):
        return "E-mail do Gmail válido!"
    else:
        return "E-mail inválido ou não é do Gmail."