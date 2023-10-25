
from django.shortcuts import render
import requests
from django.http import HttpResponseNotFound

def food(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        api_url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}?fields=product_name,brands,nutriments,nutrition_grades,image_front_small_url'
        response = requests.get(api_url)

        if response.status_code == 200:
            product_data = response.json()
            if 'product' in product_data:
                return render(request, 'food/food_info.html', {'product': product_data['product']})
            else:
                return HttpResponseNotFound('Không tìm thấy thông tin sản phẩm')
        else:
            return HttpResponseNotFound('Không tìm thấy thông tin sản phẩm')
    return render(request, 'food/input_barcode.html')
