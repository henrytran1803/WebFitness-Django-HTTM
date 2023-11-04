from audioop import reverse
from datetime import date
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
import requests
from django.http import HttpResponseNotFound,HttpResponseRedirect,HttpResponseServerError
from .models import Products, Nutritions, EatTrack, DetailEatTrack, AuthUser
from django.shortcuts import get_object_or_404
def info(request, barcode):
    product = get_object_or_404(Products, barcode=barcode)
    nutrition = Nutritions.objects.get(nutrition_id=product)

    request.session['barcode']=product.barcode
    return render(request, 'food/food_info.html', {'product': product, 'nutrition': nutrition})

def food(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        request.session['barcode'] = barcode
        print(barcode)
        try:
            product = Products.objects.get(barcode=barcode)
            nutrition = Nutritions.objects.get(nutrition_id=product)
            return render(request, 'food/food_info.html', {'product': product, 'nutrition': nutrition})
        except Products.DoesNotExist:
            api_url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}?fields=product_name,brands,nutriments,nutrition_grades,image_front_small_url'
            response = requests.get(api_url)
            if response.status_code == 200:
                product_data = response.json()
                if 'product' in product_data:
                    carbohydrates_100g = product_data['product']['nutriments'].get('carbohydrates_100g', None)
                    energy_kcal_100g = product_data['product']['nutriments'].get('energy-kcal_100g', None)
                    fat_100g = product_data['product']['nutriments'].get('fat_100g', None)
                    proteins_100g = product_data['product']['nutriments'].get('proteins_100g', None)
                    sugars_100g = product_data['product']['nutriments'].get('sugars_100g', None)
                    sodium_100g = product_data['product']['nutriments'].get('sodium_100g', None)
                    if carbohydrates_100g is None:
                        carbohydrates_100g = 0
                    if energy_kcal_100g is None:
                        energy_kcal_100g = 0
                    if fat_100g is None:
                        fat_100g = 0
                    if proteins_100g is None:
                        proteins_100g = 0
                    if sugars_100g is None:
                        sugars_100g = 0
                    if sodium_100g is None:
                        sodium_100g = 0
                    product, created = Products.objects.get_or_create(
                        barcode=barcode,
                        defaults={
                            'product_name': product_data['product']['product_name'],
                            'brand': product_data['product']['product_name'],
                            'image_url': product_data['product']['image_front_small_url'],
                        }
                    )

                    # Lưu trữ khóa chính (barcode) của sản phẩm trong trường nutrition_id
                    nutrition, created = Nutritions.objects.get_or_create(
                        nutrition_id=product.barcode,
                        defaults={
                            'carbohydrates_100g': carbohydrates_100g,
                            'energy_kcal_100g': energy_kcal_100g,
                            'fat_100g': fat_100g,
                            'proteins_100g': proteins_100g,
                            'sugars_100g': sugars_100g,
                            'sodium_100g': sodium_100g,
                        }
                    )

                    return render(request, 'food/food_info.html', {'product': product, 'nutrition': nutrition, 'barcode': barcode})
                else:
                    return HttpResponseNotFound('Không tìm thấy thông tin sản phẩm')
            else:
                return HttpResponseNotFound('Không tìm thấy thông tin sản phẩm')

    # Retrieve all products
    all_products = Products.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(all_products, 5)  # Show 5 products per page
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'food/input_barcode.html', {'products': products})
def tracking(request):
    user_id = request.user.id
    eat_tracks = EatTrack.objects.filter(user_id=user_id)
    return render(request, 'food/tracking.html', {'eat_tracks': eat_tracks})




def eat_track_detail(request, track_id):
    # Lấy một EatTrack cụ thể bằng trường track_id
    eat_track = get_object_or_404(EatTrack, track_id=track_id)

    # Truy vấn tất cả các DetailEatTrack liên quan đến EatTrack
    detail_eat_tracks = DetailEatTrack.objects.filter(id=eat_track)

    return render(request, 'food/eat_track_detail.html',
                  {'eat_track': eat_track, 'detail_eat_tracks': detail_eat_tracks})



def detail(request):
    if request.method == 'POST':
        serving_size = request.POST.get('serving')
        barcode = request.session['barcode']
        user_id = request.session.get('user_id')
        today = date.today()
        user = AuthUser.objects.filter(id=user_id).first()

        try:
            eat_track = EatTrack.objects.get(user=user, date=today)
        except EatTrack.DoesNotExist:
            eat_track = EatTrack(user=user, date=today)
            eat_track.save()

        serving_size = float(serving_size)
        product_instance = get_object_or_404(Products, barcode=barcode)

        try:
            # Kiểm tra tổ hợp khóa (id, product) trong bảng DetailEatTrack
            detail_eat_track = DetailEatTrack.objects.get(id=eat_track, product=product_instance)
            # Bản ghi đã tồn tại, cập nhật serving_size
            detail_eat_track.serving_size = serving_size
            detail_eat_track.save()
        except DetailEatTrack.DoesNotExist:
            # Bản ghi không tồn tại, tạo mới
            detail_eat_track = DetailEatTrack(id=eat_track, product=product_instance, serving_size=serving_size)
            detail_eat_track.save()

        return HttpResponseRedirect(reverse('eat_track_detail', args=[eat_track.track_id]))
    return render(request, 'food/tracking.html')