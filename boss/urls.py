from django.urls import path
from boss import views

urlpatterns = [
    # name을 지정해주면 url이 변해도 이름은 바뀌지 않는 장점이 있다.
    path('orders/<int:shop>', views.order_list, name="order_list"),
    path('timeinput/', views.time_input, name="timeinput"),
    # path('menus/<int:shop>', views.menu, name="menu"),
    # path('order/', views.order, name="order")
]