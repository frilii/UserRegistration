
from django.urls import path
from app_cad_users import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # facebook.com
    path('',views.home,name='home'),
    # users.com/users
    path('users/',views.users,name='listagem_users')
]
