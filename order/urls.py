from django.urls import path
from order import views

urlpatterns = [
    # name을 지정해주면 url이 변해도 이름은 바뀌지 않는 장점이 있다.
    path('shops/', views.shop, name="shop"),
    path('menus/<int:shop>', views.menu, name="menu"),
    path('order/', views.order, name="order")
]