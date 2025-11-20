from django.http import HttpResponse
from .models import cars_brand, cars_info


def install(request):
    output = []

    brands = [
        {"BRAND_NAME": "Toyota", "BRAND_COUNTRY": "Japan", "BRAND_RATING": 9},
        {"BRAND_NAME": "Ford", "BRAND_COUNTRY": "USA", "BRAND_RATING": 8},
        {"BRAND_NAME": "BMW", "BRAND_COUNTRY": "Germany", "BRAND_RATING": 9},
    ]

    cars = [
        {"CAR_NAME": "Corolla", "CAR_MODEL": "2023", "CAR_PRICE": 20000, "CAR_BRAND": "Toyota"},
        {"CAR_NAME": "Mustang", "CAR_MODEL": "2022", "CAR_PRICE": 35000, "CAR_BRAND": "Ford"},
        {"CAR_NAME": "X5", "CAR_MODEL": "2023", "CAR_PRICE": 60000, "CAR_BRAND": "BMW"},
    ]



    return HttpResponse("<br>".join(output))
