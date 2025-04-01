import re

def validarSenha(senha):
    if len(senha) < 8:
        return "Senha muito curta. Deve ter pelo menos 8 caracteres."

    if not re.search(r"[A-Z]", senha):
        return "A senha deve conter pelo menos 1 letra maiúscula."

    if not re.search(r"[a-z]", senha):
        return "A senha deve conter pelo menos 1 letra minúscula."

    if not re.search(r"[0-9]", senha):
        return "A senha deve conter pelo menos 1 número."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return "A senha deve conter pelo menos 1 caractere especial."

    return "Senha válida!"

