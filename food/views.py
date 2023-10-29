from audioop import reverse
from datetime import date
from django.urls import reverse

from django.shortcuts import render
import requests
from django.http import HttpResponseNotFound,HttpResponseRedirect,HttpResponseServerError
from .models import Products, Nutritions, EatTrack, DetailEatTrack, AuthUser
from django.shortcuts import get_object_or_404

def food(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        request.session['barcode'] = barcode
        print(barcode)
        try:
            product = Products.objects.get(barcode__nutrition_id=barcode)
            nutrition = product.barcode  # Lấy đối tượng Nutritions từ trường barcode
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
                    return render(request, 'food/food_info.html', {'product': product, 'nutrition': nutrition, 'barcode': barcode})
                else:
                    return HttpResponseNotFound('Không tìm thấy thông tin sản phẩm')
            else:
                return HttpResponseNotFound('Không tìm thấy thông tin sản phẩm')
    return render(request, 'food/input_barcode.html')
def tracking(request):
    user_id = request.user.id
    eat_tracks = EatTrack.objects.filter(user_id=user_id)
    return render(request, 'food/tracking.html', {'eat_tracks': eat_tracks})
def eat_track_detail(request, track_id):
    eat_track = get_object_or_404(EatTrack, track_id=track_id)
    detail_eat_tracks = DetailEatTrack.objects.filter(id=eat_track.track_id)
    if not detail_eat_tracks:
        no_detail_eat_tracks = True
    else:
        no_detail_eat_tracks = False
    return render(request, 'food/eat_track_detail.html', {'eat_track': eat_track, 'detail_eat_tracks': detail_eat_tracks, 'no_detail_eat_tracks': no_detail_eat_tracks})
def detail(request):
    if request.method == 'POST':
        serving_sizes = request.POST.get('serving')
        barcode = request.session['barcode']  # Assuming it's a single barcode
        print(barcode)
        user_id = request.session.get('user_id')
        print(serving_sizes, barcode, user_id)
        try:
            today = date.today()
            user = AuthUser.objects.filter(id=user_id).first()
            try:
                eat_track = EatTrack.objects.get(user=user, date=today)
            except EatTrack.DoesNotExist:
                eat_track = EatTrack(user=user, date=today)
                eat_track.save()
            serving_size =float(serving_sizes)

            try:
                product_instance = Products.objects.get(barcode=barcode)
            except Products.DoesNotExist:
                print(f"Product with barcode {barcode} does not exist.")
                return HttpResponseServerError(f"Product with barcode {barcode} does not exist.")

            detail_eat_track, created = DetailEatTrack.objects.get_or_create(id=eat_track, product=product_instance)
            detail_eat_track.serving_size = serving_size
            detail_eat_track.save()

            return HttpResponseRedirect(reverse('eat_track_detail', args=[eat_track.track_id]))
        except Exception as e:
            return HttpResponseServerError('Có lỗi xảy ra: ' + str(e))
    return render(request, 'food/tracking.html')
