from django.utils import timezone
from time import timezone
import datetime

from django.shortcuts import render
from joblib import load
from django.conf import settings
from django.db import models
from .models import Bodymeasurements
from .models import UserPred
def predict(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        density = float(request.POST.get('Density'))
        age = float(request.POST.get('Age'))
        weight = float(request.POST.get('Weight'))
        height = float(request.POST.get('Height'))
        neck = float(request.POST.get('Neck'))
        chest = float(request.POST.get('Chest'))
        abdomen = float(request.POST.get('Abdomen'))
        hip = float(request.POST.get('Hip'))
        thigh = float(request.POST.get('Thigh'))
        knee = float(request.POST.get('Knee'))
        ankle = float(request.POST.get('Ankle'))
        biceps = float(request.POST.get('Biceps'))
        forearm = float(request.POST.get('Forearm'))
        wrist = float(request.POST.get('Wrist'))
        activity_level = float(request.POST.get('ActivityLevel'))
        model_path = settings.BASE_DIR / 'model' / 'linear_regression_model.joblib'
        loaded_model = load(model_path)
        date = datetime.datetime.now()
        result = loaded_model.predict([[density, age, weight, height, neck, chest, abdomen, hip, thigh, knee, ankle, biceps, forearm, wrist]])
        user_id2 = request.user.id
        new_entry = Bodymeasurements(
            userid=int(user_id2),  # Gán người dùng hiện tại
            density=density,  # Gán các giá trị dự đoán
            age=age,
            weight=weight,
            height=height,
            neck=neck,
            chest=chest,
            abdomen=abdomen,
            hip=hip,
            thigh=thigh,
            knee=knee,
            ankle=ankle,
            biceps=biceps,
            forearm=forearm,
            wrist=wrist,

        )
        print(user_id)
        new_entry.save()
        new_entry_id = new_entry.id
        current_date = date
        bmi = (weight / (height * height)) * 10000
        tdee =activity_level*((9.99*weight)+(6.25*height))
        new_pred_entry = UserPred(
            body_id=new_entry_id,
            bdf=result[0],
            tdee=tdee,
            bmi=bmi
        )
        new_pred_entry.save()  # Lưu bản ghi UserPred
        return render(request, 'result.html', {'result': result[0]})

    return render(request, 'input.html')
