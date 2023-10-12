from django.shortcuts import render

from joblib import load
from django.conf import settings

def predict(request):
    if request.method == 'POST':
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
        model_path = settings.BASE_DIR / 'model' / 'linear_regression_model.joblib'
        # Tiến hành dự đoán với các giá trị này
        loaded_model = load(model_path)
        result = loaded_model.predict([[density, age, weight, height, neck, chest, abdomen, hip, thigh, knee, ankle, biceps, forearm, wrist]])

        return render(request, 'result.html', {'result': result[0]})

    return render(request, 'input.html')
