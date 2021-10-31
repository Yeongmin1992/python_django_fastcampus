from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def shop(request):
    if request.method == 'GET':
        # Shop db를 불러오겠다.
        # shop = Shop.objects.all()
        # serializer는 db의 데이터를 보기 쉽게 json 형태로 바꿔주는 역할을 한다.
        # many=True는 shop이라는 데이터가 여러개여도 상관하지 않겠다는 뜻
        # serializer = ShopSerializer(shop, many=True)
        # return JsonResponse(serializer.data, safe=False)

        # 아래 두줄의 코드는 shop에 있는 모든 object들이 shop_list 이름으로 가운데 html상에 들어가게 된다. -> html에서 shop_list를 for 문을 돌며 뿌려주게 됨
        shop = Shop.objects.all()
        return render(request, 'order/shop_list.html', {'shop_list':shop})



    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def menu(request, shop):
    if request.method == 'GET':
        # Shop db를 불러오겠다.
        # menu = Menu.objects.all()
        # url로 들어온 shop id에 속한 메뉴만 호출, Menu.objects.get을 사용하면 한 줄 밖에 불러오지 못하므로 아래와 같이 사용
        menu = Menu.objects.filter(shop=shop)
        # serializer는 db의 데이터를 보기 쉽게 json 형태로 바꿔주는 역할을 한다.
        # serializer = MenuSerializer(menu, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return render(request, 'order/menu_list.html', {'menu_list':menu, 'shop':shop})


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# 아래와 같이 하면 save 함수를 안 써도 저장이 된다!?
from django.utils import timezone
@csrf_exempt
def order(request):
    if request.method == 'POST':
        address = request.POST['address']
        shop = request.POST['shop']
        food_list = request.POST.getlist('menu')
        order_date = timezone.now()

        shop_item = Shop.objects.get(pk=int(shop))

        # shop을 외래키로 가지는 order 행을 만들 때 -> 테이블명(소문자로)_set.create()
        shop_item.order_set.create(address=address, order_date=order_date, shop=int(shop))

        # 주문하는 shop을 외래키로 갖는 order 테이블 상의 id 값의 마지막 id
        order_item = Order.objects.get(pk = shop_item.order_set.latest('id').id)
        for food in food_list:
            order_item.orderfood_set.create(food_name = food)

        return render(request, 'order/success.html')

    elif request.method == "GET":
        order_list = Order.objects.all()
        return render(request, 'order/order_list.html', {'order_list':order_list})
