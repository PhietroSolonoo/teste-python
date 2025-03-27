from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import re

def verificar_senha(senha):
    # Verifica se tem pelo menos uma letra maiúscula
    if not any(char.isupper() for char in senha):
        return False

    # Verifica se tem pelo menos um caractere especial
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False

    return True

def index(request):
    if request.method == 'POST':
        senha = request.POST.get('senha')
        if verificar_senha(senha):
            resultado = "Senha correta!"
        else:
            resultado = "Senha incorreta! A senha deve conter pelo menos uma letra maiúscula e um caractere especial."
        return render(request, 'verificar_senha/index.html', {'resultado': resultado})
    return render(request, 'verificar_senha/index.html')
