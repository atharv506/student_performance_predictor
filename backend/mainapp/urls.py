from django.urls import path
from mainapp import views



urlpatterns = [
    path('', views.predict_final_exam_score, name='predict_final_exam_score'),
    path('api/predict/', views.predict_final_exam_score, name='predict_final_exam_score_api'),
]