from django.shortcuts import render
from .models import User

def home(request):
    return render(request,'users/home.html')

def users(request):
    #salvar os dadaos no db
    novo_user = User()
    novo_user.nome = request.POST.get('nome')
    novo_user.idade = request.POST.get('idade')
    novo_user.save()
    #duyinaw
    users = {
        'users': User.objects.all()
    }
    #gudwhjk
    return render(request,'users/users.html',users)
