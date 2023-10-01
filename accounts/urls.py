from accounts import views
from django.urls import path, include

urlpatterns = [
    path('register/', views.AccountRegister.as_view(), name="register"),   
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
    
]
