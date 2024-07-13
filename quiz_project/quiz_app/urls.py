# In quiz_app/urls.py

from django.urls import path
from . import views

app_name = 'quiz_app'  # Ensure this matches your app's name in settings.py

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/take/', views.take_quiz, name='take_quiz'),
    path('quiz/<int:quiz_id>/result/<int:quiz_taker_id>/', views.quiz_result, name='quiz_result'),
    path('quiz/<int:quiz_id>/leaderboard/', views.leaderboard, name='leaderboard'),
]
