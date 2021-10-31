from django.urls import path
from delivery import views

urlpatterns = [
    # name을 지정해주면 url이 변해도 이름은 바뀌지 않는 장점이 있다.
    path('orders/', views.order_list, name="order_list"),
    # path('menus/<int:shop>', views.menu, name="menu"),
    # path('order/', views.order, name="order")
]