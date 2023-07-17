from django.shortcuts import render, redirect

from apps.usuarios.forms import LoginForms,cadastroForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login ( request):
    form = LoginForms()
    
    if request.method == 'POST':
        form =LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login']. value()
            senha = form['senha']. value()
    
        usuario = auth.authenticate(
            request,
            username = nome,
            password= senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, "Usuario foi conectado")
            return redirect('index')

        else:
            messages.error(request, "senha ou usuario incorreto")
            return redirect('login')

    return render(request, "usuarios/login.html", {"form":form})

def cadastro(request):

    form = cadastroForms()
    if request.method == 'POST':
        form= cadastroForms(request.POST)

        
    
        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect('cadastro')

            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha= form["senha_1"].value()

            if User.objects.filter(username= nome).exists():
                messages.error(request, "usuario ja existe")
                return redirect('cadastro')
            
            usuario= User.objects.create_user(
                username = nome,
                email= email,
                password= senha
            )
            usuario.save()
            messages.success(request, "parabens voçe nao tem alzheimer")
            return redirect('login')
    
    return render (request, "usuarios/cadastro.html", {"form":form})    

def logout (request):
    messages.success(request,"saiu da sua conta ja lindo")
    auth.logout(request)
    return redirect('login')


