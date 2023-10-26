
from django.shortcuts import render
import requests
from django.http import HttpResponseNotFound
from .models import Products, Nutritions

def food(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        try:
            # Kiểm tra xem sản phẩm có trong cơ sở dữ liệu không
            product = Products.objects.get(barcode__nutrition_id=barcode)
            nutrition = product.barcode  # Lấy đối tượng Nutritions từ trường barcode
            # Nếu có trong cơ sở dữ liệu, trả về thông tin từ cơ sở dữ liệu
            return render(request, 'food/food_info.html', {'product': product, 'nutrition': nutrition})
        except Products.DoesNotExist:
            api_url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}?fields=product_name,brands,nutriments,nutrition_grades,image_front_small_url'
            response = requests.get(api_url)

            if response.status_code == 200:
                product_data = response.json()
                if 'product' in product_data:
                    nutrition, created = Nutritions.objects.get_or_create(
                        nutrition_id=barcode,
                        defaults={
                            'carbohydrates_100g': product_data['product']['nutriments']['carbohydrates_100g'],
                            'energy_kcal_100g': product_data['product']['nutriments']['energy-kcal_100g'],
                            'fat_100g': product_data['product']['nutriments']['fat_100g'],
                            'proteins_100g': product_data['product']['nutriments']['proteins_100g'],
                            'sugars_100g': product_data['product']['nutriments']['sugars_100g'],
                            'sodium_100g': product_data['product']['nutriments']['sodium_100g'],
                        }
                    )
                    product, created = Products.objects.get_or_create(
                        barcode=nutrition,
                        defaults={
                            'brand': product_data['product']['brands'],
                            'image_url': product_data['product']['image_front_small_url'],
                        }
                    )
                    # Trả về thông tin sản phẩm
                    return render(request, 'food/food_info.html', {'product': product_data['product'], 'nutrition': nutrition})
                else:
                    return HttpResponseNotFound('Không tìm thấy thông tin sản phẩm')
            else:
                return HttpResponseNotFound('Không tìm thấy thông tin sản phẩm')
    return render(request, 'food/input_barcode.html')
