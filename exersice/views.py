from django.shortcuts import render
from .models import Exercises
from django.core.paginator import Paginator

# Create your views here.
def exersice(request, page_number):
    exercises = Exercises.objects.all()
    paginator = Paginator(exercises, 10)  # Chia danh sách thành các trang, mỗi trang chứa 10 bài tập
    page = paginator.get_page(page_number)
    return render(request, 'exersice/exersice.html', {'page': page})
def exercise_detail(request, exercise_id, page_number):
    exercise = Exercises.objects.get(exerciseid=exercise_id)
    return render(request, 'exersice/detailsEx.html', {'exercise': exercise, 'page_number': page_number})
