from django.shortcuts import render, redirect

from usuarios.forms import LoginForms,cadastroForms

def login ( request):
    form = LoginForms ()
    return render(request, "usuarios/login.html", {"form":form})

def cadastro(request):
    return render(request, "usuarios/cadastro.html")

def cadastro(request):
    form = cadastroForms()
    if request.method == 'POST':
        form= cadastroForms(request.POST)

        if form["senha_1"].value() != form["senha_2"].value():
            return redirect('cadastro')
        
    
    
    
    
    else:
        return render (request, "usuarios/cadastro.html", {"form":form})