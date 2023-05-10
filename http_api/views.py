import datetime
import json
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from http_api.models import City, Street, Shop


def index(request):
    return HttpResponse("Server is running now...")


def get_cities(request):
    cities = City.objects.all()
    response = {
        'cities': [{'id': city.id, 'name': city.name} for city in cities]
    }
    return JsonResponse(response)


def get_streets(request, city_id):
    streets = Street.objects.filter(city=city_id)
    data = {'streets': [{'id': street.id, 'name': street.name}
                        for street in streets]}
    return JsonResponse(data)


@csrf_exempt
def shop_interface(request):
    if request.method == 'POST':
        # обработка POST запроса
        try:
            data = json.loads(request.body)
            shop = Shop.objects.create(
                name=data['name'],
                city_id=data['city_id'],
                street_id=data['street_id'],
                house_number=data['house_number'],
                opening_time=data['opening_time'],
                closing_time=data['closing_time']
            )
            return JsonResponse({'id': shop.id})
        except (KeyError, json.JSONDecodeError, ValueError, TypeError):
            return JsonResponse({'error': 'there was an error'}, status=400)
    elif request.method == 'GET':
        # обработка GET запроса
        city_id = request.GET.get('city')
        street_id = request.GET.get('street')
        is_open = request.GET.get('open')

        shops = Shop.objects.all()

        # Фильтрация по городу
        if city_id:
            shops = shops.filter(street__city_id=city_id)

        # Фильтрация по улице
        if street_id:
            shops = shops.filter(street_id=street_id)

        # Фильтрация по открытости / закрытости
        if is_open is not None:
            now = datetime.datetime.now().time()
            if is_open == '1':
                shops = shops.filter(
                    Q(opening_time__lte=now) & Q(closing_time__gte=now))
            elif is_open == '0':
                shops = shops.exclude(
                    Q(opening_time__lte=now) & Q(closing_time__gte=now))

        result = []
        for shop in shops:
            result.append({
                'id': shop.id,
                'name': shop.name,
                'city': shop.street.city.name,
                'street': shop.street.name,
                'house_number': shop.house_number,
                'opening_time': str(shop.opening_time),
                'closing_time': str(shop.closing_time),
            })

        return JsonResponse(result, safe=False)

    else:
        return JsonResponse(
            {'Error': 'This method is not allowed'}, status=400)
