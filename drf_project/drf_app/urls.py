"""URL configuration for API requests."""

from django.urls import path

from drf_app import views
from drf_app.views import drf_views

urlpatterns = [
    path('math-calc-exercise/', views.MathCalcExerciseAPIView.as_view()),
    path('words/', drf_views.WordListCreateAPIView.as_view()),
    path('words/<int:pk>/', drf_views.DeleteWordAPIView.as_view()),
]
