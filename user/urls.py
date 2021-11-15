from django.urls import path
from user import views

urlpatterns = [
    # name을 지정해주면 url이 변해도 이름은 바뀌지 않는 장점이 있다.
    path('user/', views.user, name="user"),
    path('login/', views.login, name="login"),
]