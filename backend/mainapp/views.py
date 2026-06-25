import json
import re

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .ml_model import predict_final_exam_score as predict_exam_score_from_model

# Create your views here
@csrf_exempt
def predict_final_exam_score(request):
    prediction = None

    if request.method == 'POST':
        if request.content_type and 'application/json' in request.content_type:
            payload = json.loads(request.body.decode('utf-8'))
        else:
            payload = request.POST

        # Get the input values from the form which are required in ml model\
##        X = df[[
##    "study_hours_per_day",
##    "deep_work_sessions",
##    "assignment_completion_rate",
##    "attendance_percentage",
##    "social_media_hours",    
##    "gaming_hours",
##    "stress_level",
##    "motivation_level",
##    "focus_score",
##    "procrastination_index",
##    "mental_state",    
##    "sleep_hours",
##    "financial_stress",    
##    "revision_efficiency",
##    "burnout_risk",
##    "consistency_score"
##]]
## we input each value of X from the form and then we will use the model to predict the final exam score

        study_hours_per_day = float(payload.get('study_hours_per_day'))
        deep_work_sessions = int(payload.get('deep_work_sessions'))
        assignment_completion_rate = float(payload.get('assignment_completion_rate'))
        attendance_percentage = float(payload.get('attendance_percentage'))
        social_media_hours = float(payload.get('social_media_hours'))
        gaming_hours = float(payload.get('gaming_hours'))
        stress_level = float(payload.get('stress_level'))
        motivation_level = float(payload.get('motivation_level'))
        focus_score = float(payload.get('focus_score'))
        procrastination_index = float(payload.get('procrastination_index'))
        #mental state is a string value which can be "Focused", "Distracted", "Burnout", "Balanced" which we will convert to numerical value using one hot encoding
        mental_state = payload.get('mental_state')
        sleep_hours = float(payload.get('sleep_hours'))
        financial_stress = float(payload.get('financial_stress'))
        revision_efficiency = float(payload.get('revision_efficiency'))
        burnout_risk = float(payload.get('burnout_risk'))
        consistency_score = float(payload.get('consistency_score'))

        student_data = {
            "study_hours_per_day": study_hours_per_day,
            "deep_work_sessions": deep_work_sessions,
            "assignment_completion_rate": assignment_completion_rate,
            "attendance_percentage": attendance_percentage,
            "social_media_hours": social_media_hours,
            "gaming_hours": gaming_hours,
            "stress_level": stress_level,
            "motivation_level": motivation_level,
            "focus_score": focus_score,
            "procrastination_index": procrastination_index,
            "mental_state": mental_state,
            "sleep_hours": sleep_hours,
            "financial_stress": financial_stress,
            "revision_efficiency": revision_efficiency,
            "burnout_risk": burnout_risk,
            "consistency_score": consistency_score,
        }

        prediction = predict_exam_score_from_model(student_data)

        return JsonResponse({"prediction": prediction})

    # now 

    # Render the input form template for GET requests
    return render(request, 'predict.html', {'prediction': prediction})