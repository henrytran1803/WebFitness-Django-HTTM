from django.shortcuts import render
from random import random
from WebSite import settings
from .models import Exercises
from django.core.paginator import Paginator
import joblib
from .models import UserPred, ExerciseSuggestions
import numpy as np
from django.core.paginator import Paginator
from random import randint
# Create your views here.
def exersice(request, page_number):
    exercises = Exercises.objects.all()
    paginator = Paginator(exercises, 10)
    page = paginator.get_page(page_number)
    return render(request, 'exersice/exersice.html', {'page': page})
def exercise_detail(request, exercise_id, page_number):
    exercise = Exercises.objects.get(exerciseid=exercise_id)
    return render(request, 'exersice/detailsEx.html', {'exercise': exercise, 'page_number': page_number})
from django.contrib.auth.decorators import login_required


@login_required
def predict_label(request, page_number):
    model_path = settings.BASE_DIR / 'model' / 'RandomForestRegressor.joblib'
    model = joblib.load(model_path)
    user = request.user
    try:
        latest_user_pred = UserPred.objects.filter(body__userid=user.id).latest('date')
    except UserPred.DoesNotExist:
        bmi = 25.0
        tdee = 2000
        bdf = 20.0
        height = 170.0
        weight = 70.0
    else:
        bmi = latest_user_pred.bmi
        tdee = latest_user_pred.tdee
        bdf = latest_user_pred.bdf
        height = latest_user_pred.body.height
        weight = latest_user_pred.body.weight

    label = None
    exercise_type = None
    exercise_difficulty = None

    try:
        suggestion = ExerciseSuggestions.objects.get(user_pred=latest_user_pred)
        label = suggestion.label
        exercise_type = suggestion.exercise_type
        exercise_difficulty = suggestion.exercise_difficulty
    except ExerciseSuggestions.DoesNotExist:
        features = np.array([[bmi, tdee, bdf, height, weight]])
        predicted_label = model.predict(features)
        predicted_label_rounded = np.round(predicted_label).astype(int)
        rounded_label = predicted_label_rounded[0]
        result = f"Predicted Label: {rounded_label}"

        # Tạo một bản ghi mới trong ExerciseSuggestions
        suggestion = ExerciseSuggestions(
            user_pred=latest_user_pred,
            label=rounded_label,
        )
        suggestion.save()

    exercises = Exercises.objects.filter(exercisetype=exercise_type, difficultylevel=exercise_difficulty)

    total_exercises = exercises.count()

    page = None  # Đặt page thành None ngay từ đầu

    # Ensure that there are enough exercises to paginate
    if total_exercises > 0:
        exercises_per_page = 10  # Xác định exercises_per_page

        total_pages = (total_exercises + exercises_per_page - 1) // exercises_per_page

        # Validate the page number
        page_number = int(page_number)
        if page_number < 1:
            page_number = 1
        elif page_number > total_pages:
            page_number = total_pages

        start_index = (page_number - 1) * exercises_per_page
        end_index = start_index + exercises_per_page

        # Get the exercises for the current page
        page_exercises = exercises[start_index:end_index]

        paginator = Paginator(page_exercises, exercises_per_page)
        page = paginator.get_page(page_number)

    return render(request, 'exersice/exersice.html', {'page': page})


